import logging

from wykop import WykopAPI
from wykop.api.exceptions import DailtyRequestLimitError
from wykop.core.requestor import Requestor


class MultiKeyWykopAPI(WykopAPI):

    def __init__(self, appkeys, secretkeys, account_keys=None, output='', response_format='json'):
        super().__init__(appkeys[0], secretkeys[0], output, response_format)
        self.output = output,
        self.response_format = response_format

        if account_keys:
            self.keys = zip(appkeys, secretkeys, account_keys)
        else:
            empty_account_keys = [None for _ in appkeys]
            self.keys = zip(appkeys, secretkeys, empty_account_keys)

        self.available_keys = set(self.keys)
        self.requestor = self.next_requestor()

    def request(self, rtype, rmethod=None, named_params=None, api_params=None, post_params=None, file_params=None):
        try:
            return self.requestor.request(rtype, rmethod=rmethod,
                                          named_params=named_params,
                                          api_params=api_params,
                                          post_params=post_params,
                                          file_params=file_params)
        except DailtyRequestLimitError:
            self.requestor = self.next_requestor()
            if self.requestor.account_key:
                self.authenticate()
            return self.request(rtype, rmethod, named_params, api_params, post_params, file_params)

    def next_requestor(self) -> Requestor:
        logging.debug('new requestor requested')
        if len(self.available_keys) == 0:
            logging.debug('no more keys')
            raise DailtyRequestLimitError
        appkey, secretkey, account_key = self.available_keys.pop()
        logging.debug('creating new requestor')
        return Requestor(
            appkey=appkey,
            secretkey=secretkey,
            accountkey=account_key,
            output=self.output,
            response_format=self.response_format
        )
