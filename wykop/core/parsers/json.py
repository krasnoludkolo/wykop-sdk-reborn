"""Wykop API JSON praser module."""
from __future__ import absolute_import

import base64

from wykop.api.models.wykop_connect import WykopConnectLoginInfo
from wykop.utils import force_bytes

try:
    import simplejson as json
except ImportError:
    import json

from wykop.core.parsers.base import BaseParser, Error


class JSONParser(BaseParser):

    def __init__(self, exception_resolver, **json_kwargs):
        super(JSONParser, self).__init__(exception_resolver)
        self.json_kwargs = json_kwargs

    def _get_response(self, data):
        return json.loads(data, **self.json_kwargs)

    def _get_error(self, response):
        if not isinstance(response, dict):
            return

        error_data = response.get('error')

        if error_data is None:
            return

        code = error_data.get('code')
        message = error_data.get('message')

        if message is None:
            # try english message
            message = error_data.get('message_en')

        return Error(code, message)

    def parse_wykop_connect_response(self, response) -> WykopConnectLoginInfo:
        decoded_response = base64.b64decode(force_bytes(response)).decode('utf-8')
        field_dict = json.loads(decoded_response)
        return WykopConnectLoginInfo(**field_dict)
