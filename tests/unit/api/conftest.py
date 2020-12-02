import pytest
try:
    from unittest import mock
except ImportError:
    import mock


from wykop.api.client import WykopAPI
from wykop.api.exceptions.resolvers import ExceptionResolver


class Test1Exception(Exception):
    pass


class Test2Exception(Exception):
    pass


@pytest.fixture
def base_wykop_api():
    return WykopAPI(
        mock.sentinel.appkey,
        mock.sentinel.secretkey,
        accountkey=mock.sentinel.account_key,
        password=mock.sentinel.password,
        output=mock.sentinel.output,
        response_format=mock.sentinel.format,
    )


@pytest.fixture
def key_pairs():
    return [
        (mock.sentinel.appkey1, mock.sentinel.secretkey1),
        (mock.sentinel.appkey2, mock.sentinel.secretkey2),
    ]


@pytest.fixture
def exception_resolver():
    exceptions = {
        1: Test1Exception,
        2: Test2Exception,
    }
    return ExceptionResolver(exceptions)
