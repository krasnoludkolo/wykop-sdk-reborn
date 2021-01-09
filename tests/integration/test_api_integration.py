import os
from wykop import WykopAPI, MultiKeyWykopAPI


def create_base_client():
    key = os.environ.get('WYKOP_TAKTYK_KEY')
    secret = os.environ.get('WYKOP_TAKTYK_SECRET')
    account_key = os.environ.get('WYKOP_TAKTYK_ACCOUNTKEY')
    return WykopAPI(key, secret, output='clear', account_key=account_key)


def create_multi_key_client():
    key = os.environ.get('WYKOP_TAKTYK_KEY')
    secret = os.environ.get('WYKOP_TAKTYK_SECRET')
    account_key = os.environ.get('WYKOP_TAKTYK_ACCOUNTKEY')
    return MultiKeyWykopAPI([(key, secret, account_key)], output='clear')


def all_api_clients():
    return [create_base_client(), create_multi_key_client()]


class TestApiIntegration(object):

    def test_all_api_clients_connection(self):
        for api in all_api_clients():
            entries = api.entries_hot()

            assert isinstance(entries, list)

    def test_all_api_clients_connection_with_method_related_to_account(self):
        for api in all_api_clients():

            api.authenticate()
            conversations = api.conversations_list()

            assert isinstance(conversations, list)
