from enum import Enum


class PROFILE_SETTINGS:
    REAL_NAME = 'realname'
    HOME_SITE = 'homesite'
    CITY = 'city'
    EMAIL = 'email'
    SKYPE = 'skype'
    ABOUT = 'about'
    FACEBOOK = 'facebook'
    TWITTER = 'twitter'
    INSTAGRAM = 'instagram'


class DirectNotificationType(Enum):
    ENTRY_MENTIONED = 'entry_comment_directed'
    DIRECT_MESSAGE = 'pm'


class NotificationType(Enum):
    TAG_NOTIFICATION = 'entry_directed'
    ENTRY_MENTIONED = 'entry_comment_directed'
    DIRECT_MESSAGE = 'pm'
