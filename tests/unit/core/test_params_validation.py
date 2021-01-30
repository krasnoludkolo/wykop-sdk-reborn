import pytest

from wykop.api.exceptions.client_exceptions import NamedParameterNone, ApiParameterNone
from wykop.core.credentials import EMPTY_CREDENTIALS
from wykop.core.requestor import Requestor


class TestParamsValidation(object):

    def test_should_raise_exception_if_named_parameter_is_none(self):
        requestor = Requestor(EMPTY_CREDENTIALS)
        named_params = {
            'key': None
        }

        with pytest.raises(NamedParameterNone):
            assert requestor.request('test', named_params=named_params)

    def test_should_raise_exception_if_api_parameter_is_none(self):
        requestor = Requestor(EMPTY_CREDENTIALS)
        api_params = ['value', None]

        with pytest.raises(ApiParameterNone):
            assert requestor.request('test', api_params=api_params)
