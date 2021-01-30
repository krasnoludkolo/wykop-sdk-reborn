class WykopAPIClientError(Exception):
    """Base Wykop client API exception."""
    pass


class NamedParameterNone(WykopAPIClientError):
    pass


class ApiParameterNone(WykopAPIClientError):
    pass
