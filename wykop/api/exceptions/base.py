"""Wykop API base exceptions module."""
__all__ = [
    'InvalidAPIKeyError', 'InvalidParamsError', 'NotEnoughParamsError',
    'AppWritePermissionsError', 'DailyRequestLimitError',
    'InvalidAPISignError', 'AppPermissionsError', 'SessionAppPermissionError',
    'InvalidUserKeyError', 'InvalidSessionKeyError', 'UserDoesNotExistError',
    'InvalidCredentialsError', 'CredentialsMissingError', 'IPBannedError',
    'UserBannedError', 'OwnVoteError', 'InvalidLinkIDError', 'OwnObserveError',
    'CommentEditError', 'EntryEditError', 'RemovedLinkError',
    'PrivateLinkError', 'EntryDoesNotExistError', 'EntryLimitExceededError',
    'QueryTooShortError', 'CommentDoesNotExistError', 'NiceTryError',
    'UnreachableAPIError', 'NoIndexError', 'WykopAPIError', 'ReceiverHasBlockedDMError',
    'ReceiverProbablyDoesNotExist'
]


class WykopAPIError(Exception):
    """Base Wykop API exception."""
    pass


class InvalidAPIKeyError(WykopAPIError):
    pass


class InvalidParamsError(WykopAPIError):
    pass


class NotEnoughParamsError(WykopAPIError):
    pass


class AppWritePermissionsError(WykopAPIError):
    pass


class DailyRequestLimitError(WykopAPIError):
    pass


class InvalidAPISignError(WykopAPIError):
    pass


class AppPermissionsError(WykopAPIError):
    pass


class SessionAppPermissionError(WykopAPIError):
    pass


class NotSupportedAPIKeyError(WykopAPIError):
    pass


class InvalidUserKeyError(WykopAPIError):
    pass


class InvalidSessionKeyError(WykopAPIError):
    pass


class UserDoesNotExistError(WykopAPIError):
    pass


class InvalidCredentialsError(WykopAPIError):
    pass


class CredentialsMissingError(WykopAPIError):
    pass


class IPBannedError(WykopAPIError):
    pass


class UserBannedError(WykopAPIError):
    pass


class OwnVoteError(WykopAPIError):
    pass


class InvalidLinkIDError(WykopAPIError):
    pass


class OwnObserveError(WykopAPIError):
    pass


class CommentEditError(WykopAPIError):
    pass


class EntryEditError(WykopAPIError):
    pass


class RemovedLinkError(WykopAPIError):
    pass


class PrivateLinkError(WykopAPIError):
    pass


class EntryDoesNotExistError(WykopAPIError):
    pass


class EntryLimitExceededError(WykopAPIError):
    pass


class QueryTooShortError(WykopAPIError):
    pass


class CommentDoesNotExistError(WykopAPIError):
    pass


class ReceiverHasBlockedDMError(WykopAPIError):
    pass


class NiceTryError(WykopAPIError):
    pass


class UnreachableAPIError(WykopAPIError):
    pass


class NoIndexError(WykopAPIError):
    pass


class No2FAError(WykopAPIError):
    pass


class Invalid2FACodeError(WykopAPIError):
    pass


class ReceiverProbablyDoesNotExist(WykopAPIError):
    pass


__all_exceptions__ = {
    1: InvalidAPIKeyError,
    2: InvalidParamsError,
    3: NotEnoughParamsError,
    4: AppWritePermissionsError,
    5: DailyRequestLimitError,
    6: InvalidAPISignError,
    7: AppPermissionsError,
    8: SessionAppPermissionError,
    9: NotSupportedAPIKeyError,
    11: InvalidUserKeyError,
    12: InvalidSessionKeyError,
    13: UserDoesNotExistError,
    14: InvalidCredentialsError,
    15: CredentialsMissingError,
    17: IPBannedError,
    18: UserBannedError,
    31: OwnVoteError,
    32: InvalidLinkIDError,
    33: OwnObserveError,
    34: CommentEditError,
    35: EntryEditError,
    41: RemovedLinkError,
    42: PrivateLinkError,
    61: EntryDoesNotExistError,
    62: EntryLimitExceededError,
    71: QueryTooShortError,
    81: CommentDoesNotExistError,
    102: ReceiverHasBlockedDMError,
    999: NiceTryError,
    1001: UnreachableAPIError,
    1002: NoIndexError,
    1101: No2FAError,
    1102: Invalid2FACodeError,
}
