from wykop.api.models.model_utils import auto_str, auto_repr


@auto_str
@auto_repr
class WykopConnectLoginInfo:

    def __init__(self, appkey, login, token, sign):
        self.app_key = appkey
        self.login = login
        self.token = token
        self.api_sign = sign

    def __iter__(self):
        return iter(
            (self.app_key,
             self.login,
             self.token,
             self.api_sign))

