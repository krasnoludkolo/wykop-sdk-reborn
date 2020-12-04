import logging

from typing import Dict, List

from wykop.api.api_const import PAGE_NAMED_ARG, BODY_NAMED_ARG
from wykop.core.requestor import Requestor

log = logging.getLogger(__name__)


class WykopAPI:
    """Wykop API version 2."""

    def __init__(self, appkey, secretkey, accountkey=None,
                 password=None, output='', response_format='json'):
        self.requestor = Requestor(
            appkey=appkey,
            secretkey=secretkey,
            accountkey=accountkey,
            password=password,
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

    def authenticate(self, account_key=None):
        self.requestor.authenticate(account_key)

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

    def observe_profile(self, username):
        named_params = {
            'observe': username,
        }
        return self.request('profiles', named_params=named_params)

    def unobserve_profile(self, username):
        named_params = {
            'unobserve': username,
        }
        return self.request('profiles', named_params=named_params)

    def block_profile(self, username):
        named_params = {
            'block': username,
        }
        return self.request('profiles', named_params=named_params)

    def unblock_profile(self, username):
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

    def send_message(self, receiver: str, message: str):
        return self.request('pm', 'SendMessage',
                            post_params=self.__with_body(message),
                            api_params=self.__api_param(receiver))

    def delete_conversation(self, receiver: str):
        return self.request('pm', 'DeleteConversation',
                            api_params=self.__api_param(receiver))

    # notifications

    def direct_notifications(self, page=1):
        return self.request('notifications',
                            named_params=self.__with_page(page))

    def direct_notifications_count(self):
        return self.request('notifications', 'Count')

    def hashtags_notifications(self, page=1):
        return self.request('notifications', 'hashtags',
                            named_params=self.__with_page(page))

    def hashtags_notifications_count(self):
        return self.request('notifications', 'hashtagscount')

    def all_notifications(self, page=1):
        return self.request('notifications', 'total',
                            named_params=self.__with_page(page))

    def all_notifications_count(self):
        return self.request('notifications', 'totalcount')

    def mark_all_notification_as_read(self):
        return self.request('Notifications', 'ReadAllNotifications')

    def mark_all_direct_notification_as_read(self):
        return self.request('Notifications', 'ReadDirectedNotifications')

    def mark_all_hashtag_notification_as_read(self):
        return self.request('Notifications', 'ReadHashTagsNotifications')

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

    def observe_tag(self, tag):
        return self.request('Tags', 'Observe',
                            api_params=self.__api_param(tag))

    def unobserve_tag(self, tag):
        return self.request('Tags', 'Unobserve',
                            api_params=self.__api_param(tag))

    def enable_tags_notifications(self, tag):
        return self.request('Tags', 'Notify',
                            api_params=self.__api_param(tag))

    def disable_tags_notifications(self, tag):
        return self.request('Tags', 'Dontnotify',
                            api_params=self.__api_param(tag))

    def block_tag(self, tag):
        return self.request('Tags', 'Block',
                            api_params=self.__api_param(tag))

    def unblock_tag(self, tag):
        return self.request('Tags', 'Unblock',
                            api_params=self.__api_param(tag))

    @staticmethod
    def __api_param(param: str) -> List[str]:
        return [param]

    @staticmethod
    def __with_page(page: int) -> Dict[str, int]:
        return {PAGE_NAMED_ARG: page}

    @staticmethod
    def __with_body(body: str) -> Dict[str, str]:
        return {BODY_NAMED_ARG: body}
