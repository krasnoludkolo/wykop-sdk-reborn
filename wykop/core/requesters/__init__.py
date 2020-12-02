# try requests module
try:
    import requests

    from wykop.core.requesters.requests import RequestsRequester as Requester
except ImportError:
    from wykop.core.requesters.urllib import UrllibRequester as Requester

default_requester = Requester()
