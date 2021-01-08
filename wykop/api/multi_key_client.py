import logging

from wykop import WykopAPI
from wykop.api.exceptions import DailtyRequestLimitError
from wykop.core.requestor import Requestor


class MultiKeyWykopAPI(WykopAPI):

    def __init__(self, credentials, output='', response_format='json'):
        self.output = output,
        self.response_format = response_format

        self.credentials = credentials

        self.credentials = set([tuple(pair) for pair in self.credentials])
        self.requestor = self.next_requestor()
        self.authenticate_if_needed()

    def request(self, rtype, rmethod=None, named_params=None, api_params=None, post_params=None, file_params=None):
        try:
            return self.requestor.request(rtype, rmethod=rmethod,
                                          named_params=named_params,
                                          api_params=api_params,
                                          post_params=post_params,
                                          file_params=file_params)
        except DailtyRequestLimitError:
            logging.info('daily request limit')
            self.requestor = self.next_requestor()
            self.authenticate_if_needed()
            return self.request(rtype, rmethod, named_params, api_params, post_params, file_params)

    def authenticate_if_needed(self):
        if self.requestor.account_key:
            logging.info('Authenticating new requester')
            self.authenticate()

    def next_requestor(self) -> Requestor:
        logging.info('New requestor requested')

        if not self.credentials:
            logging.info('no more keys')
            raise DailtyRequestLimitError

        appkey, secretkey, account_key = self.get_next_credentials()

        logging.info('Creating new requestor')
        return Requestor(
            appkey=appkey,
            secretkey=secretkey,
            accountkey=account_key,
            output=self.output,
            response_format=self.response_format
        )

    def get_next_credentials(self):
        next_credentials = self.credentials.pop()
        if len(next_credentials) == 2:
            return next_credentials[0], next_credentials[1], None
        else:
            return next_credentials
