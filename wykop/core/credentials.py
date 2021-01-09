class Credentials:

    def __init__(self, appkey, secretkey, accountkey=None):
        self.appkey = appkey
        self.secretkey = secretkey
        self.account_key = accountkey

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Credentials):
            return self.appkey == other.appkey \
                   and self.secretkey == other.secretkey \
                   and self.account_key == other.account_key
        return False


EMPTY_CREDENTIALS = Credentials('', '')
