from wykop import MultiKeyWykopAPI
from wykop.api.exceptions import DailtyRequestLimitError
from wykop.core.requestor import Requestor
import pytest


class TestKeyLoader(object):

    def test_raise_error_if_all_are_used(self):
        used_key = 'used_key'
        used_secret = 'used_secret'
        appkeys = [used_key]
        secretkeys = [used_secret]

        api = MultiKeyWykopAPI(appkeys, secretkeys)
        api.requestor = FakeRequestor((), used_key, used_secret)

        with pytest.raises(DailtyRequestLimitError):
            api.tag('test')


class FakeRequestor(Requestor):

    def __init__(self, allowed_keys, appkey, secretkey):
        super().__init__(appkey, secretkey)
        self.allowed_keys = allowed_keys

    def request(self, rtype, rmethod=None,
                named_params=None, api_params=None, post_params=None, file_params=None):
        if (self.appkey, self.secretkey) in self.allowed_keys:
            return ''
        else:
            raise DailtyRequestLimitError
