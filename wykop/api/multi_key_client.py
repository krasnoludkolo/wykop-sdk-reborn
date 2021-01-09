import logging

from wykop import WykopAPI
from wykop.api.exceptions import DailyRequestLimitError
from wykop.core.credentials import Credentials, EMPTY_CREDENTIALS

logging = logging.getLogger(__name__)


def create_credentials(keys) -> Credentials:
    if len(keys) == 2:
        return Credentials(keys[0], keys[1])
    else:
        return Credentials(keys[0], keys[1], keys[2])


class MultiKeyWykopAPI(WykopAPI):

    def __init__(self, credentials_list, output='', response_format='json'):
        super().__init__('', '', None, output, response_format)
        self.output = output,
        self.response_format = response_format

        self.credentials = [create_credentials(c) for c in credentials_list]
        logging.debug(f'Loaded {len(self.credentials)} credentials')
        self.available_credentials = []

        self.reset_available_credentials()

        self.requestor.credentials = self.next_credentials()
        self.authenticate_if_needed()
        self.has_credentials_with_exceeded_limit = False

    def request(self, rtype, rmethod=None, named_params=None, api_params=None, post_params=None, file_params=None):
        try:
            response = super(MultiKeyWykopAPI, self).request(rtype, rmethod=rmethod, named_params=named_params,
                                                             api_params=api_params,
                                                             post_params=post_params, file_params=file_params)
            if self.has_credentials_with_exceeded_limit:
                logging.debug('Successful request with current credentials. Request reset available credentials')
                self.reset_available_credentials()
            return response

        except DailyRequestLimitError:
            logging.debug('Daily request limit for current used credentials')
            self.load_next_credentials()
            return self.request(rtype, rmethod, named_params, api_params, post_params, file_params)

    def load_next_credentials(self):
        logging.debug('Loading next credentials')
        self.requestor.credentials = self.next_credentials()
        self.authenticate_if_needed()
        self.has_credentials_with_exceeded_limit = True

    def reset_available_credentials(self):
        logging.debug('Resetting available credentials')
        self.available_credentials = list(self.credentials)
        self.available_credentials.reverse()
        if self.requestor.credentials != EMPTY_CREDENTIALS:
            self.available_credentials.remove(self.requestor.credentials)
        self.has_credentials_with_exceeded_limit = False

    def authenticate_if_needed(self):
        if self.requestor.credentials.account_key:
            logging.debug('Authenticating with new credentials')
            self.authenticate()

    def next_credentials(self) -> Credentials:
        logging.debug('New credentials requested')

        if not self.available_credentials:
            logging.debug('No more keys')
            raise DailyRequestLimitError

        return self.available_credentials.pop()
