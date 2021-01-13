import base64
import hashlib
import itertools
import logging
from collections import OrderedDict

from typing import Dict
from urllib.parse import quote_plus, urlunparse

from wykop.api.exceptions import WykopAPIError
from wykop.api.api_const import CLIENT_NAME, DOMAIN, PROTOCOL
from wykop.core.credentials import Credentials
from wykop.core.parsers import default_parser
from wykop.core.requesters import default_requester
from wykop.utils import force_bytes, force_text, get_version, dictmap

log = logging.getLogger(__name__)


class Requestor:

    def __init__(self, credentials: Credentials,
                 output='', response_format='json'):
        self.credentials = credentials
        self.output = output
        self.format = response_format
        self.userkey = ''
        self.requester = default_requester
        self.parser = default_parser

    def request(self, rtype, rmethod=None,
                named_params=None, api_params=None, post_params=None, file_params=None):
        log.debug('Making request')

        named_params = named_params or {}
        api_params = api_params or []
        post_params = OrderedDict({k: v for k, v in sorted(
            post_params.items()) if v} if post_params else {})

        file_params = file_params or {}

        rtype = force_text(rtype)
        rmethod = rmethod and force_text(rmethod)
        post_params = dictmap(force_bytes, post_params)
        named_params = dictmap(force_text, named_params)

        url = self.construct_url(
            rtype=rtype, rmethod=rmethod, api_params=api_params, named_params=named_params)
        headers = self.headers(url, **post_params)

        response = self.requester.make_request(
            url, post_params, headers, file_params)

        if self.parser is None:
            return response

        return self.parser.parse(response)

    def authenticate(self, account_key=None, login=None, password=None):
        self.credentials.account_key = account_key or self.credentials.account_key
        self.credentials.login = login or self.credentials.login
        self.credentials.password = password or self.credentials.password

        if self.credentials.account_key:
            res = self.user_login_with_accountkey(self.credentials.account_key)
        elif self.credentials.login and self.credentials.password:
            appkey_type = self.credentials.appkey_type()
            if appkey_type['official']:
                res = self.user_login_with_password(self.credentials.login, self.credentials.password)
            else:
                # TODO: implement login/connect polyfill
                raise WykopAPIError(
                    0, 'login and password provided on unofficial appkey')
        else:
            raise WykopAPIError(
                0, 'neither accountkey nor login and password are set')

        self.userkey = res['userkey']

    def user_login_with_accountkey(self, account_key):
        post_params = {'accountkey': account_key}
        return self.request('login', post_params=post_params)

    def user_login_with_password(self, login, password):
        post_params = {'login': login, 'password': password}
        return self.request('login', post_params=post_params)

    def user_login_2fa(self, tfa_token):
        post_params = {'code': tfa_token}
        return self.request('login', '2fa', post_params=post_params)

    def default_named_params(self):
        """
        Gets default named parameters.
        """
        return {
            'appkey': self.credentials.appkey,
            'format': self.format,
            'output': self.output,
            'userkey': self.userkey,
        }

    def api_sign(self, url, **post_params):
        """
        Gets request api sign.
        """
        post_params_values = self.post_params_values(**post_params)
        post_params_values_str = ",".join(post_params_values)
        post_params_values_bytes = force_bytes(post_params_values_str)
        url_bytes = force_bytes(url)
        secretkey_bytes = force_bytes(self.credentials.secretkey)
        return hashlib.md5(
            secretkey_bytes + url_bytes + post_params_values_bytes).hexdigest()

    def post_params_values(self, **post_params):
        """
        Gets post parameters values list. Required to api sign.
        """
        return [force_text(post_params[key])
                for key in sorted(post_params.keys())]

    def user_agent(self):
        """
        Gets User-Agent header.
        """
        client_version = get_version()
        return '/'.join([CLIENT_NAME, client_version])

    def headers(self, url, **post_params):
        """
        Gets request headers.
        """
        apisign = self.api_sign(url, **post_params)
        user_agent = self.user_agent()

        return {
            'apisign': apisign,
            'User-Agent': user_agent,
        }

    def connect_named_params(self, redirect_url=None):
        """
        Gets request api parameters for wykop connect.
        """
        apisign = self.api_sign(redirect_url)

        named_params = {
            'secure': apisign,
        }

        if redirect_url is not None:
            redirect_url_bytes = force_bytes(redirect_url)
            redirect_url_encoded = quote_plus(
                base64.b64encode(redirect_url_bytes))
            named_params.update({
                'redirect': redirect_url_encoded,
            })

        return named_params

    def construct_url(self, rtype, api_params, named_params, rmethod=None):
        """
        Constructs request url.
        """
        path = self.path(rtype, api_params=api_params,
                         rmethod=rmethod, named_params=named_params)

        urlparts = (PROTOCOL, DOMAIN, path, '', '', '')
        return str(urlunparse(urlparts))

    def path(self, rtype, api_params, rmethod=None, **named_params):
        """
        Gets request path.
        """
        pathparts = [rtype]

        if rmethod is not None:
            pathparts += [rmethod]

        if api_params is not None:
            pathparts += tuple(api_params)

        named_params = self.named_params(**named_params)

        if named_params:
            pathparts += list(itertools.chain(*named_params.items()))

        return '/'.join(pathparts)

    def named_params(self, named_params) -> Dict[str, str]:
        """
        Gets request method parameters.
        """
        params = self.default_named_params()
        params.update(named_params)
        return {
            str(key): str(value)
            for key, value in params.items()
            if value
        }
