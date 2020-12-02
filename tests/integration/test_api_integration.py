import os
from wykop import WykopAPI


class TestApiIntegration(object):

    def test_api_connection(self):
        key = os.environ.get('WYKOP_TAKTYK_KEY')
        secret = os.environ.get('WYKOP_TAKTYK_SECRET')
        account_key = os.environ.get('WYKOP_TAKTYK_ACCOUNTKEY')
        api = WykopAPI(key, secret, output='clear')

        api.authenticate(account_key=account_key)
        entries = api.hot_entries()

        assert isinstance(entries, dict)
