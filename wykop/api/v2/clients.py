import logging
from collections import OrderedDict

from six.moves.urllib.parse import urlunparse

from wykop.api.clients import BaseWykopAPI
from wykop.api.decorators import login_required
from wykop.api.exceptions import WykopAPIError
from wykop.api.parsers import default_parser
from wykop.api.requesters import default_requester
from wykop.utils import (
    dictmap,
    force_bytes,
    force_text,
)

log = logging.getLogger(__name__)


class BaseWykopAPIv2(BaseWykopAPI):
    """Base Wykop API version 2."""

    _protocol = 'https'
    _domain = 'a2.wykop.pl'

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


class WykopAPIv2(BaseWykopAPIv2):
    """Wykop API version 2."""

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

    def get_links_upcoming(self, sort='active', page=1):
        assert sort in ['active', 'date', 'votes', 'comments']
        named_params = {
            'sort': sort,
            'page': page,
        }
        return self.request('links', 'upcoming', named_params=named_params)

    def get_link_comments(self, link_id, sort='old'):
        assert sort in ['old', 'new', 'best']
        named_params = {
            'comments': link_id,
            'sort': sort,
        }
        return self.request('links', named_params=named_params)

    def get_link_related(self, link_id):
        named_params = {
            'related': link_id,
        }
        return self.request('links', named_params=named_params)

    def get_link_upvoters(self, link_id):
        named_params = {
            'upvoters': link_id,
        }
        return self.request('links', named_params=named_params)

    def get_link_downvoters(self, link_id):
        named_params = {
            'downvoters': link_id,
        }
        return self.request('links', named_params=named_params)

    # mywykop

    @login_required
    def get_mywykop(self, page=1):
        named_params = {
            'page': page,
        }
        return self.request('mywykop', named_params=named_params)

    @login_required
    def get_mywykop_tags(self, page=1):
        named_params = {
            'page': page,
        }
        return self.request('mywykop', 'tags', named_params=named_params)

    @login_required
    def get_mywykop_users(self, page=1):
        named_params = {
            'page': page,
        }
        return self.request('mywykop', 'users', named_params=named_params)

    @login_required
    def get_moj(self, page=1):
        named_params = {
            'page': page,
        }
        return self.request('moj', named_params=named_params)

    @login_required
    def get_moj_tagi(self, page=1):
        named_params = {
            'page': page,
        }
        return self.request('moj', 'tagi', named_params=named_params)

    # profiles

    def get_profile(self, username):
        return self.request('profiles', username)

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

    def get_notifications(self, page=1):
        named_params = {
            'page': page
        }
        return self.request('notifications', named_params=named_params)

    def get_hashtags_notifications(self, page=1):
        named_params = {
            'page': page
        }
        return self.request('notifications', 'hashtags', named_params=named_params)

    @login_required
    def get_notifications_count(self):
        return self.request('notifications', 'totalcount')

    def get_hashtags_notifications_count(self):
        return self.request('notifications', 'hashtagscount')

    # search

    def search_entries(self, query, page=1):
        post_params = {
            'q': query,
            'page': page,
        }
        return self.request('search', 'entries', post_params=post_params)

    def search_links(self, query, page=1):
        post_params = {
            'q': query,
            'page': page,
        }
        return self.request('search', 'links', post_params=post_params)

    def search_profiles(self, query):
        post_params = {
            'q': query,
        }
        return self.request('search', 'profiles', post_params=post_params)

    # tags

    def get_tag(self, name, page=1):
        named_params = {
            'page': page,
        }
        return self.request('tags', name, named_params=named_params)

    @login_required
    def get_tags_observed(self):
        return self.request('tags', 'observed')

    def get_tag_entries(self, name, page=1):
        named_params = {
            'entries': name,
            'page': page,
        }
        return self.request('tags', named_params=named_params)

    def get_tag_links(self, name, page=1):
        named_params = {
            'links': name,
            'page': page,
        }
        return self.request('tags', named_params=named_params)

    # tagi

    def get_tagi(self, name, page=1):
        named_params = {
            'page': page,
        }
        return self.request('tags', name, named_params=named_params)
