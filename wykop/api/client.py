import base64
import hashlib
import logging
import itertools

from typing import Dict, List

from six.moves.urllib.parse import urlunparse, quote_plus

from wykop.api.api_const import PAGE_NAMED_ARG, BODY_NAMED_ARG
from wykop.api.decorators import login_required
from wykop.api.exceptions import WykopAPIError
from wykop.api.parsers import default_parser
from wykop.api.requesters import default_requester
from wykop.utils import (
    get_version,
    dictmap,
    force_bytes,
    force_text,
)

log = logging.getLogger(__name__)


class WykopAPI:
    """Base Wykop API version 2."""

    _protocol = 'https'
    _domain = 'a2.wykop.pl'

    _client_name = 'wykop-sdk-reborn'

    def __init__(self, appkey, secretkey, accountkey=None,
                 password=None, output='', response_format='json'):
        self.appkey = appkey
        self.secretkey = secretkey
        self.accountkey = accountkey
        self.password = password
        self.output = output
        self.format = response_format
        self.userkey = ''

    def __getstate__(self):
        return {
            'appkey': self.appkey,
            'secretkey': self.secretkey,
            'accountkey': self.accountkey,
            'password': self.password,
            'output': self.output,
            'format': self.format,
            'userkey': self.userkey,
        }

    def __setstate__(self, state):
        self.appkey = state['appkey']
        self.secretkey = state['secretkey']
        self.accountkey = state['accountkey']
        self.password = state['password']
        self.output = state['output']
        self.format = state['format']
        self.userkey = state['userkey']

    def default_named_params(self):
        """
        Gets default named parameters.
        """
        return {
            'appkey': self.appkey,
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
        secretkey_bytes = force_bytes(self.secretkey)
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
        return '/'.join([self._client_name, client_version])

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

    def request(self, rtype, rmethod=None,
                named_params=None, api_params=None, post_params=None, file_params=None,
                parser=default_parser, requester=default_requester):
        """
        Makes request.
        """
        log.debug('Making request')

        named_params = named_params or {}
        api_params = api_params or []
        post_params = post_params or {}
        file_params = file_params or {}

        # sanitize data
        rtype = force_text(rtype)
        rmethod = rmethod and force_text(rmethod)
        post_params = dictmap(force_bytes, post_params)
        named_params = dictmap(force_text, named_params)

        url = self.construct_url(rtype=rtype, rmethod=rmethod, api_params=api_params, named_params=named_params)
        headers = self.headers(url, **post_params)

        response = requester.make_request(
            url, post_params, headers, file_params)

        if parser is None:
            return response

        return parser.parse(response)

    def construct_url(self, rtype, api_params, named_params, rmethod=None):
        """
        Constructs request url.
        """
        path = self.path(rtype, api_params=api_params, rmethod=rmethod, named_params=named_params)

        urlparts = (self._protocol, self._domain, path, '', '', '')
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

    def authenticate(self, accountkey=None):
        self.accountkey = accountkey or self.accountkey

        if not self.accountkey:
            raise WykopAPIError(
                0, 'account key not set')

        res = self.user_login(self.accountkey)
        self.userkey = res['data']['userkey']

    def user_login(self, account_key):
        post_params = {'accountkey': account_key}

        return self.request('login', post_params=post_params)

    # Connect

    def connect_url(self, redirect_url=None):
        """
        Gets url for wykop connect.
        """
        named_params = self.connect_named_params(redirect_url)

        return self.construct_url('login', 'connect', **named_params)

    # entries

    def entry(self, entry_id):
        named_params = {
            'entry': entry_id,
        }
        return self.request('entries', named_params=named_params)

    def stream_entries(self, page=1):
        return self.request('entries', 'stream',
                            named_params=self.__with_page(page))

    def hot_entries(self, period=12, page=1):
        assert period in [6, 12, 24]
        named_params = {
            'period': period,
            'page': page,
        }
        return self.request('entries', 'hot', named_params=named_params)

    # links

    def links_promoted(self, page=1):
        return self.request('links', 'promoted',
                            named_params=self.__with_page(page))

    # mywykop

    # profiles

    @login_required
    def observe_profile(self, username):
        named_params = {
            'observe': username,
        }
        return self.request('profiles', named_params=named_params)

    @login_required
    def unobserve_profile(self, username):
        named_params = {
            'unobserve': username,
        }
        return self.request('profiles', named_params=named_params)

    @login_required
    def block_profile(self, username):
        named_params = {
            'block': username,
        }
        return self.request('profiles', named_params=named_params)

    @login_required
    def unblock_profile(self, username):
        named_params = {
            'unblock': username,
        }
        return self.request('profiles', named_params=named_params)

    # hits

    def hits_popular(self):
        return self.request('hits', 'popular')

    # pm

    @login_required
    def conversations_list(self):
        return self.request('pm', 'conversationsList')

    @login_required
    def conversation(self, receiver):
        return self.request('pm', 'Conversation',
                            api_params=self.__api_param(receiver))

    @login_required
    def send_message(self, receiver, message):
        return self.request('pm', 'SendMessage',
                            post_params=self.__with_body(message),
                            api_params=self.__api_param(receiver))

    # notifications

    @login_required
    def direct_notifications(self, page=1):
        return self.request('notifications',
                            named_params=self.__with_page(page))

    @login_required
    def direct_notifications_count(self):
        return self.request('notifications', 'Count')

    @login_required
    def hashtags_notifications(self, page=1):
        return self.request('notifications', 'hashtags',
                            named_params=self.__with_page(page))

    @login_required
    def hashtags_notifications_count(self):
        return self.request('notifications', 'hashtagscount')

    @login_required
    def all_notifications(self, page=1):
        return self.request('notifications', 'total',
                            named_params=self.__with_page(page))

    @login_required
    def all_notifications_count(self):
        return self.request('notifications', 'totalcount')

    @login_required
    def mark_all_notification_as_read(self):
        return self.request('Notifications', 'ReadAllNotifications')

    @login_required
    def mark_all_direct_notification_as_read(self):
        return self.request('Notifications', 'ReadDirectedNotifications')

    @login_required
    def mark_all_hashtag_notification_as_read(self):
        return self.request('Notifications', 'ReadHashTagsNotifications')

    @login_required
    def mark_notification_as_read(self, notification_id):
        return self.request('Notifications', 'MarkAsRead',
                            api_params=self.__api_param(notification_id))

    # search

    # tags

    def tag(self, tag, page=1):
        return self.request('Tags', 'Index',
                            named_params=dict(page=page),
                            api_params=self.__api_param(tag))

    def tag_links(self, tag, page=1):
        return self.request('Tags', 'Links',
                            named_params=self.__with_page(page),
                            api_params=self.__api_param(tag))

    def tag_entries(self, tag, page=1):
        return self.request('Tags', 'Entries',
                            named_params=self.__with_page(page),
                            api_params=self.__api_param(tag))

    @login_required
    def observe_tag(self, tag):
        return self.request('Tags', 'Observe',
                            api_params=self.__api_param(tag))

    @login_required
    def unobserve_tag(self, tag):
        return self.request('Tags', 'Unobserve',
                            api_params=self.__api_param(tag))

    @login_required
    def enable_tags_notifications(self, tag):
        return self.request('Tags', 'Notify',
                            api_params=self.__api_param(tag))

    @login_required
    def disable_tags_notifications(self, tag):
        return self.request('Tags', 'Dontnotify',
                            api_params=self.__api_param(tag))

    @login_required
    def block_tag(self, tag):
        return self.request('Tags', 'Block',
                            api_params=self.__api_param(tag))

    @login_required
    def unblock_tag(self, tag):
        return self.request('Tags', 'Unblock',
                            api_params=self.__api_param(tag))

    @staticmethod
    def __api_param(param: str) -> List[str]:
        return list(param)

    @staticmethod
    def __with_page(page: int) -> Dict[str, int]:
        return {PAGE_NAMED_ARG: page}

    @staticmethod
    def __with_body(body: str) -> Dict[str, str]:
        return {BODY_NAMED_ARG: body}
