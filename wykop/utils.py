"""Wykop utils module."""
import mimetypes
from collections import OrderedDict
from typing import Dict, Any, List

from pkg_resources import get_distribution, DistributionNotFound

from six import b, u, PY3, text_type, string_types
from six.moves.urllib.request import pathname2url

from wykop.api.exceptions.client_exceptions import NamedParameterNone, ApiParameterNone


def paramsencode(d):
    return ','.join(['%s,%s' % (k, d[k]) for k in sorted(d)])


def dictmap(f, d):
    return dict([(k_v[0], f(k_v[1])) for k_v in iter(d.items())])


def mimetype(filename):
    return mimetypes.guess_type(pathname2url(filename))[0]


def force_bytes(s, encoding='utf-8', errors='strict'):
    if isinstance(s, bytes):
        if encoding == 'utf-8':
            return s
        else:
            return s.decode('utf-8', errors).encode(encoding, errors)
    if not isinstance(s, string_types):
        try:
            if PY3:
                return text_type(s).encode(encoding)
            else:
                return bytes(s)
        except UnicodeEncodeError:
            if isinstance(s, Exception):
                return b(' ').join(force_bytes(arg, encoding, errors)
                                   for arg in s)
            return text_type(s).encode(encoding, errors)
    else:
        return s.encode(encoding, errors)


def force_text(s, encoding='utf-8', errors='strict'):
    if issubclass(type(s), text_type):
        return s
    try:
        if not issubclass(type(s), string_types):
            if PY3:
                if isinstance(s, bytes):
                    s = text_type(s, encoding, errors)
                else:
                    s = text_type(s)
            elif hasattr(s, '__unicode__'):
                s = text_type(s)
            else:
                s = text_type(bytes(s), encoding, errors)
        else:
            s = s.decode(encoding, errors)
    except UnicodeDecodeError:
        s = u(' ').join(force_text(arg, encoding, errors) for arg in s)
    return s


def get_version():
    try:
        return get_distribution('wykop').version
    except DistributionNotFound:
        return 'dev'


def sort_and_remove_none_values(post_params: Dict[str, str]) -> Dict[str, str]:
    return OrderedDict({k: v for k, v in sorted(
        post_params.items()) if v} if post_params else {})


def validate_named_parameters(named_params: Dict[str, str]) -> Dict[str, str]:
    if not named_params:
        return {}
    for key, value in named_params.items():
        if key is None or value is None:
            raise NamedParameterNone(key, value)
    return named_params


def validate_api_parameters(api_params: List[Any]) -> List[Any]:
    if not api_params:
        return []
    for value in api_params:
        if value is None:
            raise ApiParameterNone(value)
    return api_params
