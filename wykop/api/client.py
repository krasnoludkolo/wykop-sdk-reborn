import logging

from typing import Dict, List

from wykop.api.api_const import PAGE_NAMED_ARG, BODY_NAMED_ARG, FILE_POST_NAME
from wykop.core.credentials import Credentials
from wykop.core.requestor import Requestor

log = logging.getLogger(__name__)


class WykopAPI:
    """Wykop API version 2."""

    def __init__(self, appkey, secretkey=None, account_key=None,
                 login=None, password=None,
                 output='', response_format='json'):
        self.requestor = Requestor(
            credentials=Credentials(appkey, secretkey, account_key),
            output=output,
            response_format=response_format
        )

    def request(self, rtype, rmethod=None,
                named_params=None, api_params=None, post_params=None, file_params=None):
        return self.requestor.request(rtype, rmethod=rmethod,
                                      named_params=named_params,
                                      api_params=api_params,
                                      post_params=post_params,
                                      file_params=file_params)

    def authenticate(self, account_key=None, login=None, password=None):
        self.requestor.authenticate(account_key=account_key, login=login, password=password)

    def authenticate_2fa(self, tfa_code):
        self.requestor.user_login_2fa(tfa_code)

    # entries

    def entries_stream(self, page=1, first_id=None):
        named_params = self \
            .__with_page(page)
        if first_id:
            named_params.update(dict(firstId=first_id))
        return self.request('Entries', 'Stream', named_params=named_params)

    def entries_hot(self, page=1, period=12):
        assert period in [6, 12, 24]
        named_params = self \
            .__with_page(page)
        named_params.update(dict(period=period))
        return self.request('Entries', 'Hot',
                            named_params=named_params)

    def entries_active(self, page=1):
        return self.request('Entries', 'Active',
                            named_params=self.__with_page(page))

    def entries_observed(self, page=1):
        return self.request('Entries', 'Observed',
                            named_params=self.__with_page(page))

    def entry(self, entry_id):
        return self.request('Entries', 'Entry',
                            api_params=self.__api_param(entry_id))

    def entry_add(self, body: str, file=None, file_url: str = None, is_adult_media: bool = False):
        return self.request('Entries', 'Add',
                            post_params=self.content_post_params(
                                body, file_url, is_adult_media),
                            file_params=self.__with_file(file))

    def entry_edit(self, entry_id: str, body: str, file=None, file_url: str = None, is_adult_media: bool = False):
        return self.request('Entries', 'Edit',
                            post_params=self.content_post_params(
                                body, file_url, is_adult_media),
                            api_params=self.__api_param(entry_id),
                            file_params=self.__with_file(file))

    def entry_vote_up(self, entry_id: str):
        return self.request('Entries', 'VoteUp',
                            api_params=self.__api_param(entry_id))

    def entry_vote_remove(self, entry_id: str):
        return self.request('Entries', 'VoteRemove',
                            api_params=self.__api_param(entry_id))

    def entry_upvoters(self, entry_id: str):
        return self.request('Entries', 'Upvoters',
                            api_params=self.__api_param(entry_id))

    def entry_delete(self, entry_id: str):
        return self.request('Entries', 'Delete',
                            api_params=self.__api_param(entry_id))

    def entry_favorite_toggle(self, entry_id: str):
        return self.request('Entries', 'Favorite',
                            api_params=self.__api_param(entry_id))

    def entry_survey_vote(self, entry_id: str, answer_id: str):
        return self.request('Entries', 'SurveyVote',
                            api_params=[entry_id, answer_id])

    # comments

    def entry_comment(self, comment_id: str):
        return self.request('Entries', 'Comment',
                            api_params=self.__api_param(comment_id))

    def entry_comment_add(self, entry_id: str, body: str, file=None, file_url: str = None,
                          is_adult_media: bool = False):
        return self.request('Entries', 'CommentAdd',
                            post_params=self.content_post_params(
                                body, file_url, is_adult_media),
                            api_params=self.__api_param(entry_id),
                            file_params=self.__with_file(file))

    def entry_comment_edit(self, comment_id: str, body: str, file=None, file_url: str = None,
                           is_adult_media: bool = False):
        return self.request('Entries', 'CommentEdit',
                            post_params=self.content_post_params(
                                body, file_url, is_adult_media),
                            api_params=self.__api_param(comment_id),
                            file_params=self.__with_file(file))

    def entry_comment_delete(self, comment_id: str):
        return self.request('Entries', 'CommentDelete',
                            api_params=self.__api_param(comment_id))

    def entry_comment_vote_up(self, comment_id: str):
        return self.request('Entries', 'CommentVoteUp',
                            api_params=self.__api_param(comment_id))

    def entry_comment_vote_remote(self, comment_id: str):
        return self.request('Entries', 'CommentVoteRemove',
                            api_params=self.__api_param(comment_id))

    def entry_comment_observed(self, page: int = 1):
        return self.request('Entries', 'ObservedComments',
                            named_params=self.__with_page(page))

    def entry_comment_favorite_toggle(self, entry_id: str):
        return self.request('Entries', 'CommentFavorite',
                            api_params=self.__api_param(entry_id))

    # links

    def links_promoted(self, page=1):
        return self.request('links', 'promoted',
                            named_params=self.__with_page(page))

    # mywykop

    # profiles

    def profile(self, login):
        return self.request('profiles', 'index', api_params=self.__api_param(login))

    def profile_observe(self, username):
        named_params = {
            'observe': username,
        }
        return self.request('profiles', named_params=named_params)

    def profile_unobserve(self, username):
        named_params = {
            'unobserve': username,
        }
        return self.request('profiles', named_params=named_params)

    def profile_block(self, username):
        named_params = {
            'block': username,
        }
        return self.request('profiles', named_params=named_params)

    def profile_unblock(self, username):
        named_params = {
            'unblock': username,
        }
        return self.request('profiles', named_params=named_params)

    # hits

    def hits_popular(self):
        return self.request('hits', 'popular')

    # pm

    def conversations_list(self):
        return self.request('pm', 'conversationsList')

    def conversation(self, receiver: str):
        return self.request('pm', 'Conversation',
                            api_params=self.__api_param(receiver))

    def message_send(self, receiver: str, message: str):
        return self.request('pm', 'SendMessage',
                            post_params=self.__with_body(message),
                            api_params=self.__api_param(receiver))

    def conversation_delete(self, receiver: str):
        return self.request('pm', 'DeleteConversation',
                            api_params=self.__api_param(receiver))

    # notifications

    def notifications_direct(self, page=1):
        return self.request('notifications',
                            named_params=self.__with_page(page))

    def notifications_direct_count(self):
        return self.request('notifications', 'Count')

    def notifications_hashtags_notifications(self, page=1):
        return self.request('notifications', 'hashtags',
                            named_params=self.__with_page(page))

    def notifications_hashtags_count(self):
        return self.request('notifications', 'hashtagscount')

    def notifications_all(self, page=1):
        return self.request('notifications', 'total',
                            named_params=self.__with_page(page))

    def notifications_all_count(self):
        return self.request('notifications', 'totalcount')

    def notification_mark_all_as_read(self):
        return self.request('Notifications', 'ReadAllNotifications')

    def notifications_mark_all_direct_as_read(self):
        return self.request('Notifications', 'ReadDirectedNotifications')

    def notifications_mark_all_hashtag_as_read(self):
        return self.request('Notifications', 'ReadHashTagsNotifications')

    def notification_mark_as_read(self, notification_id):
        return self.request('Notifications', 'MarkAsRead',
                            api_params=self.__api_param(notification_id))

    # search

    def search_links(self, page=1, query=None, when=None, votes=None, from_date=None, to_date=None, what=None,
                     sort=None):
        assert len(query) > 2 if query else True
        assert when in ["all", "today", "yesterday",
                        "week", "month", "range"] if when else True
        assert what in ["all", "promoted", "archived",
                        "duplicates"] if when else True
        assert sort in ["best", "diggs", "comments", "new"] if when else True
        post_params = {
            'q': query,
            'when': when,
            'votes': votes,
            'from': from_date,
            'to': to_date,
            'what': what,
            'sort': sort
        }
        return self.request('Search', 'Links',
                            post_params=post_params,
                            named_params=self.__with_page(page))

    def search_entries(self, page=1, query=None, when=None, votes=None, from_date=None, to_date=None):
        assert len(query) > 2 if query else True
        assert when in ["all", "today", "yesterday",
                        "week", "month", "range"] if when else True
        post_params = {
            'q': query,
            'when': when,
            'votes': votes,
            'from': from_date,
            'to': to_date
        }
        return self.request('Search', 'Entries',
                            post_params=post_params,
                            named_params=self.__with_page(page))

    def search_profiles(self, query):
        assert len(query) > 2 if query else True
        post_params = {
            'q': query,
        }
        return self.request('Search', 'Profiles',
                            post_params=post_params)

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

    def tag_observe(self, tag):
        return self.request('Tags', 'Observe',
                            api_params=self.__api_param(tag))

    def tag_unobserve(self, tag):
        return self.request('Tags', 'Unobserve',
                            api_params=self.__api_param(tag))

    def tag_enable_notifications(self, tag):
        return self.request('Tags', 'Notify',
                            api_params=self.__api_param(tag))

    def tag_disable_notifications(self, tag):
        return self.request('Tags', 'Dontnotify',
                            api_params=self.__api_param(tag))

    def tag_block(self, tag):
        return self.request('Tags', 'Block',
                            api_params=self.__api_param(tag))

    def tag_unblock(self, tag):
        return self.request('Tags', 'Unblock',
                            api_params=self.__api_param(tag))

    # settings

    def settings_profile_update(self, profile_settings: Dict[str, str]):
        return self.request('Settings', 'Profile',
                            post_params=profile_settings)

    def settings_avatar_update(self, avatar_file):
        return self.request('Settings', 'Avatar',
                            file_params=self.__with_file(avatar_file))

    def settings_background_update(self, background_file):
        return self.request('Settings', 'Background',
                            file_params=self.__with_file(background_file))

    def settings_password_update(self, old_password: str, new_password: str):
        post_params = {
            'old_password': old_password,
            'password': new_password
        }
        return self.request('Settings', 'Password',
                            post_params=post_params)

    def settings_password_reset(self, email: str):
        post_params = {
            'email': email
        }
        return self.request('Settings', 'ResetPassword',
                            post_params=post_params)

    @staticmethod
    def __api_param(param: str) -> List[str]:
        return [str(param)] if param else None

    @staticmethod
    def __with_page(page: int) -> Dict[str, int]:
        return {PAGE_NAMED_ARG: page} if page else {}

    @staticmethod
    def __with_body(body: str) -> Dict[str, str]:
        return {BODY_NAMED_ARG: body} if body else {}

    @staticmethod
    def __with_file(file: str) -> Dict[str, str]:
        return {FILE_POST_NAME: file} if file else {}

    @staticmethod
    def content_post_params(body: str, file_url: str, is_adult_media: bool):
        post_params = {
            'adultmedia': is_adult_media,
            'body': body,
            'embed': file_url
        }
        return post_params
