import os
from wykop import WykopAPI


def create_client():
    key = os.environ.get('WYKOP_TAKTYK_KEY')
    secret = os.environ.get('WYKOP_TAKTYK_SECRET')
    account_key = os.environ.get('WYKOP_TAKTYK_ACCOUNTKEY')
    return WykopAPI(key, secret, output='clear', account_key=account_key)


class TestApiIntegration(object):

    def test_api_connection(self):
        api = create_client()

        api.authenticate()
        entries = api.entries_hot()

        assert isinstance(entries, dict)

    def test_api_connection_with_method_related_to_account(self):
        api = create_client()

        api.authenticate()
        conversations = api.conversations_list()

        assert isinstance(conversations, dict)
