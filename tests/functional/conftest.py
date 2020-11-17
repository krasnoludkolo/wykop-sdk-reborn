import pytest

from wykop.api.v2.clients import WykopAPIv2
from wykop.api.requesters.requests import RequestsRequester
from wykop.api.requesters.urllib import UrllibRequester


@pytest.fixture
def requests_requester():
    return RequestsRequester()


@pytest.fixture
def urllib_requester():
    return UrllibRequester()


@pytest.fixture
def wykop_api_v2():
    appkey = '123456app'
    secretkey = '654321secret'
    api = WykopAPIv2(appkey, secretkey)
    api._domain = 'api.test.com'
    return api
