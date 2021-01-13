from ..api.api_const import ANDROID_APPKEY, ANDROID_MIKROBLOG_PLUS_APPKEY


class Credentials:

    def __init__(self, appkey, secretkey, accountkey=None, login=None, password=None):
        self.appkey = appkey
        self.secretkey = secretkey
        self.account_key = accountkey
        self.login = login
        self.password = password

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Credentials):
            return self.appkey == other.appkey \
                and self.secretkey == other.secretkey \
                and self.account_key == other.account_key \
                and self.login == other.login \
                and self.password == other.password
        return False

    def appkey_type(self):
        # welcome to the wykop zone
        if self.appkey == ANDROID_APPKEY:
            return {'official': True, '2fa_required': False}
        if self.appkey == ANDROID_MIKROBLOG_PLUS_APPKEY:
            return {'official': True, '2fa_required': True}
        # 2fa requirement depends on whether you log in with accountkey or via login/connect
        return {'official': False, '2fa_required': None}


EMPTY_CREDENTIALS = Credentials('', '')
