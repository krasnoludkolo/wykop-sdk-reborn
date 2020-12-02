import pytest

from wykop.core.parsers.base import BaseParser
from wykop.core.parsers.json import JSONParser


@pytest.fixture
def base_parser(exception_resolver):
    return BaseParser(exception_resolver)


@pytest.fixture
def json_parser(exception_resolver):
    json_param_name = 'json_param_name'
    json_param_value = 'json_param_value'
    json_params = {
        json_param_name: json_param_value,
    }
    return JSONParser(exception_resolver, **json_params)
