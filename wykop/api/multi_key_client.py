import logging

from wykop import WykopAPI
from wykop.api.exceptions import DailtyRequestLimitError
from wykop.core.credentials import Credentials
from wykop.core.requestor import Requestor


def create_credentials(keys) -> Credentials:
    if len(keys) == 2:
        return Credentials(keys[0], keys[1])
    else:
        return Credentials(keys[0], keys[1], keys[2])


class MultiKeyWykopAPI(WykopAPI):

    def __init__(self, credentials_list, output='', response_format='json'):
        self.output = output,
        self.response_format = response_format

        self.credentials = [create_credentials(c) for c in credentials_list]

        self.available_credentials = set(self.credentials)
        self.requestor = self.next_requestor()
        self.authenticate_if_needed()
        self.has_credentials_with_exceeded_limit = False

    def request(self, rtype, rmethod=None, named_params=None, api_params=None, post_params=None, file_params=None):
        try:
            response = self.requestor.request(rtype, rmethod=rmethod, named_params=named_params, api_params=api_params,
                                              post_params=post_params, file_params=file_params)
            if self.has_credentials_with_exceeded_limit:
                self.reset_available_credentials()
            return response
        except DailtyRequestLimitError:
            logging.info('daily request limit')
            self.requestor = self.next_requestor()
            self.authenticate_if_needed()
            self.has_credentials_with_exceeded_limit = True
            return self.request(rtype, rmethod, named_params, api_params, post_params, file_params)

    def reset_available_credentials(self):
        logging.info('Resetting available credentials')
        self.available_credentials = set(self.credentials)
        self.available_credentials.remove(self.requestor.credentials)
        self.has_credentials_with_exceeded_limit = False

    def authenticate_if_needed(self):
        if self.requestor.credentials.account_key:
            logging.info('Authenticating new requester')
            self.authenticate()

    def next_requestor(self) -> Requestor:
        logging.info('New requestor requested')

        if not self.available_credentials:
            logging.info('no more keys')
            raise DailtyRequestLimitError

        next_credentials = self.available_credentials.pop()

        logging.info('Creating new requestor')
        return Requestor(
            next_credentials,
            output=self.output,
            response_format=self.response_format
        )
