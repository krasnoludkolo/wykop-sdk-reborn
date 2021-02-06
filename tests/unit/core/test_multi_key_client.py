from wykop import MultiKeyWykopAPI
from wykop.api.exceptions import DailyRequestLimitError
from wykop.core.credentials import Credentials
from wykop.core.requestor import Requestor
import pytest

RESULT = 'result'


class TestKeyLoader(object):

    def test_reload_current_credentials_if_used(self):
        used_key = 'used_key'
        used_secret = 'used_secret'
        new_key = 'new_key'
        new_secret = 'new_secret'

        api = MultiKeyWykopAPI([(used_key, used_secret), (new_key, new_secret)])
        api.__requestor = FakeRequestor(allowed_keys=([(new_key, new_secret)]), appkey=used_key, secretkey=used_secret)

        assert api.tag('test') == RESULT

    def test_reuse_used_credentials_if_available_again(self):
        used_key = 'used_key'
        used_secret = 'used_secret'
        new_key = 'new_key'
        new_secret = 'new_secret'
        fake_requestor = FakeRequestor(allowed_keys=[(new_key, new_secret)], appkey=used_key, secretkey=used_secret)

        api = MultiKeyWykopAPI([(used_key, used_secret), (new_key, new_secret)])
        api.__requestor = fake_requestor

        assert api.tag('test') == RESULT

        fake_requestor.allowed_keys = [(used_key, used_secret)]

        assert api.tag('test') == RESULT

    def test_raise_error_if_all_are_used(self):
        used_key = 'used_key'
        used_secret = 'used_secret'

        api = MultiKeyWykopAPI([(used_key, used_secret)])
        api.__requestor = FakeRequestor(allowed_keys=(), appkey=used_key, secretkey=used_secret)

        with pytest.raises(DailyRequestLimitError):
            api.tag('test')


class FakeRequestor(Requestor):

    def __init__(self, allowed_keys, appkey, secretkey):
        super().__init__(Credentials(appkey, secretkey))
        self.allowed_keys = allowed_keys

    def request(self, rtype, rmethod=None,
                named_params=None, api_params=None, post_params=None, file_params=None):
        if (self.credentials.appkey, self.credentials.secretkey) in self.allowed_keys:
            return RESULT
        else:
            raise DailyRequestLimitError
