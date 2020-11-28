from collections import OrderedDict

import base64
import hashlib
import logging

from six.moves.urllib.parse import urlunparse, quote_plus

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

    def __init__(self, appkey, secretkey, login=None, accountkey=None,
                 password=None, output='', response_format='json'):
        self.appkey = appkey
        self.secretkey = secretkey
        self.login = login
        self.accountkey = accountkey
        self.password = password
        self.output = output
        self.format = response_format
        self.userkey = ''

    def __getstate__(self):
        return {
            'appkey': self.appkey,
            'secretkey': self.secretkey,
            'login': self.login,
            'accountkey': self.accountkey,
            'password': self.password,
            'output': self.output,
            'format': self.format,
            'userkey': self.userkey,
        }

    def __setstate__(self, state):
        self.appkey = state['appkey']
        self.secretkey = state['secretkey']
        self.login = state['login']
        self.accountkey = state['accountkey']
        self.password = state['password']
        self.output = state['output']
        self.format = state['format']
        self.userkey = state['userkey']

    def get_default_named_params(self):
        """
        Gets default api parameters.
        """
        return {
            'appkey': self.appkey,
            'format': self.format,
            'output': self.output,
            'userkey': self.userkey,
        }

    def get_api_sign(self, url, **post_params):
        """
        Gets request api sign.
        """
        post_params_values = self.get_post_params_values(**post_params)
        post_params_values_str = ",".join(post_params_values)
        post_params_values_bytes = force_bytes(post_params_values_str)
        url_bytes = force_bytes(url)
        secretkey_bytes = force_bytes(self.secretkey)
        return hashlib.md5(
            secretkey_bytes + url_bytes + post_params_values_bytes).hexdigest()

    def get_post_params_values(self, **post_params):
        """
        Gets post parameters values list. Required to api sign.
        """
        return [force_text(post_params[key])
                for key in sorted(post_params.keys())]

    def get_user_agent(self):
        """
        Gets User-Agent header.
        """
        client_version = get_version()
        return '/'.join([self._client_name, client_version])

    def get_headers(self, url, **post_params):
        """
        Gets request headers.
        """
        apisign = self.get_api_sign(url, **post_params)
        user_agent = self.get_user_agent()

        return {
            'apisign': apisign,
            'User-Agent': user_agent,
        }

    def get_connect_named_params(self, redirect_url=None):
        """
        Gets request api parameters for wykop connect.
        """
        apisign = self.get_api_sign(redirect_url)

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

    def get_connect_data(self, data, parser=default_parser):
        """
        Gets decoded data from wykop connect.
        """
        data_bytes = force_bytes(data)
        decoded = base64.decodestring(data_bytes)
        decoded_str = force_text(decoded)
        parsed = parser.parse(decoded_str)
        return parsed['appkey'], parsed['login'], parsed['token']


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
        headers = self.get_headers(url, **post_params)

        response = requester.make_request(
            url, post_params, headers, file_params)

        if parser is None:
            return response

        return parser.parse(response)

    def construct_url(self, rtype, api_params, named_params, rmethod=None):
        """
        Constructs request url.
        """
        path = self.get_path(rtype, api_params=api_params, rmethod=rmethod, named_params=named_params)

        urlparts = (self._protocol, self._domain, path, '', '', '')
        return str(urlunparse(urlparts))

    def get_path(self, rtype, api_params, rmethod=None, **named_params):
        """
        Gets request path.
        """
        pathparts = (rtype,)

        if rmethod is not None:
            pathparts += (rmethod,)

        if api_params is not None:
            pathparts += tuple(api_params)

        named_params = self.get_named_params(**named_params)

        if named_params:
            pathparts += tuple(named_params)

        return '/'.join(pathparts)

    def get_named_params(self, named_params):
        """
        Gets request method parameters.
        """
        params = self.get_default_named_params()
        params.update(named_params)
        # sort
        params_ordered = OrderedDict(sorted(params.items()))
        # map all params to string
        for key, value in params_ordered.items():
            if not value:
                continue
            yield str(key)
            yield str(value)


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

    def get_connect_url(self, redirect_url=None):
        """
        Gets url for wykop connect.
        """
        named_params = self.get_connect_named_params(redirect_url)

        return self.construct_url('login', 'connect', **named_params)

    # entries

    def get_entry(self, entry_id):
        named_params = {
            'entry': entry_id,
        }
        return self.request('entries', named_params=named_params)

    def get_stream_entries(self, page=1):
        named_params = {
            'page': page,
        }
        return self.request('entries', 'stream', named_params=named_params)

    def get_hot_entries(self, period=12, page=1):
        assert period in [6, 12, 24]
        named_params = {
            'period': period,
            'page': page,
        }
        return self.request('entries', 'hot', named_params=named_params)

    # links

    def get_links_promoted(self, page=1):
        named_params = {
            'page': page,
        }
        return self.request('links', 'promoted', named_params=named_params)

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

    def get_hits_month(self, year, month, page=1):
        named_params = {
            str(year): month,
            'page': page,
        }
        return self.request('hits', 'month', named_params=named_params)

    def get_hits_popular(self):
        return self.request('hits', 'popular')

    # pm

    @login_required
    def get_conversations_list(self):
        return self.request('pm', 'conversationsList')

    @login_required
    def get_conversation(self, receiver):
        api_params = [receiver]
        return self.request('pm', 'Conversation', api_params=api_params)

    @login_required
    def send_message(self, receiver, message):
        api_params = [receiver]
        post_params = {
            'body': message
        }
        return self.request('pm', 'SendMessage', post_params=post_params, api_params=api_params)

    # notifications

    @login_required
    def get_direct_notifications(self, page=1):
        named_params = {
            'page': page
        }
        return self.request('notifications', named_params=named_params)

    @login_required
    def get_direct_notifications_count(self):
        return self.request('notifications', 'Count')

    @login_required
    def get_hashtags_notifications(self, page=1):
        named_params = {
            'page': page
        }
        return self.request('notifications', 'hashtags', named_params=named_params)

    @login_required
    def get_hashtags_notifications_count(self):
        return self.request('notifications', 'hashtagscount')

    @login_required
    def get_all_notifications(self, page=1):
        named_params = {
            'page': page
        }
        return self.request('notifications', 'total', named_params=named_params)

    @login_required
    def get_all_notifications_count(self):
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
        api_params = [notification_id]
        return self.request('Notifications', 'MarkAsRead', api_params=api_params)

    # search

    # tags

    def get_tag(self, tag, page=1):
        named_params = {
            'page': page
        }
        api_params = [tag]
        return self.request('Tags', 'Index', named_params=named_params, api_params=api_params)

    def get_tag_links(self, tag, page=1):
        named_params = {
            'page': page
        }
        api_params = [tag]
        return self.request('Tags', 'Links', named_params=named_params, api_params=api_params)

    def get_tag_entries(self, tag, page=1):
        named_params = {
            'page': page
        }
        api_params = [tag]
        return self.request('Tags', 'Entries', named_params=named_params, api_params=api_params)

    @login_required
    def observe_tag(self, tag):
        api_params = [tag]
        return self.request('Tags', 'Observe', api_params=api_params)

    @login_required
    def unobserve_tag(self, tag):
        api_params = [tag]
        return self.request('Tags', 'Unobserve', api_params=api_params)

    @login_required
    def enable_tags_notifications(self, tag):
        api_params = [tag]
        return self.request('Tags', 'Notify', api_params=api_params)

    @login_required
    def disable_tags_notifications(self, tag):
        api_params = [tag]
        return self.request('Tags', 'Dontnotify', api_params=api_params)

    @login_required
    def block_tag(self, tag):
        api_params = [tag]
        return self.request('Tags', 'Block', api_params=api_params)

    @login_required
    def unblock_tag(self, tag):
        api_params = [tag]
        return self.request('Tags', 'Unblock', api_params=api_params)

