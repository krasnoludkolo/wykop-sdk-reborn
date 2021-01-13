import os
from wykop import WykopAPI, MultiKeyWykopAPI
from wykop.api.api_const import ANDROID_APPKEY


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

    def test_connection_with_login_and_password(self):
        login = os.environ.get('WYKOP_TAKTYK_BOT_LOGIN')
        password = os.environ.get('WYKOP_TAKTYK_BOT_PASSWORD')
        api = WykopAPI(ANDROID_APPKEY)

        api.authenticate(login=login, password=password)
        conversations = api.conversations_list()

        assert isinstance(conversations, list)
