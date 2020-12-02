import pytest

from wykop.core.requesters.base import BaseRequester
from wykop.core.requesters.requests import RequestsRequester
from wykop.core.requesters.urllib import UrllibRequester


@pytest.fixture
def base_requester():
    return BaseRequester()


@pytest.fixture
def requests_requester():
    return RequestsRequester()


@pytest.fixture
def urllib_requester():
    return UrllibRequester()
