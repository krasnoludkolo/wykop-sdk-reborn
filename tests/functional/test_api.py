import json
import mock
import responses

from wykop.api.api_const import PROTOCOL, DOMAIN


class FileMock(object):

    def __init__(self, name):
        self.name = name

    def read(self):
        return self.name

    def close(self):
        return


class TestWykopAPI(object):

    @responses.activate
    def test_simple(self, wykop_api):
        rtype = 'rtype'
        body_dict = {
            'data': 'data'
        }
        body = json.dumps(body_dict)

        named_params = 'appkey/123456app/format/json'
        url = '{protocol}://{domain}/{rtype}/{named_params}'.format(
            protocol=PROTOCOL,
            domain=DOMAIN,
            rtype=rtype,
            named_params=named_params,
        )
        responses.add(
            responses.GET,
            url,
            body=body,
            status=200,
            content_type='application/json',
        )

        response = wykop_api.request(rtype)

        assert response == body_dict

    @responses.activate
    def test_rmethod(self, wykop_api):
        rtype = 'rtype'
        rmethod = 'rmethod'
        body_dict = {
            'data': 'data'
        }
        body = json.dumps(body_dict)

        named_params = 'appkey/123456app/format/json'
        url = '{protocol}://{domain}/{rtype}/{rmethod}/{named_params}'.format(
            protocol=PROTOCOL,
            domain=DOMAIN,
            rtype=rtype,
            rmethod=rmethod,
            named_params=named_params,
        )
        responses.add(
            responses.GET,
            url,
            body=body,
            status=200,
            content_type='application/json',
        )

        response = wykop_api.request(rtype, rmethod)

        assert response == body_dict

    @responses.activate
    def test_named_params(self, wykop_api):
        rtype = 'rtype'
        rmethod = 'rmethod'
        named_params_dict = {
            'page': '2',
        }
        body_dict = {
            'data': 'data'
        }
        body = json.dumps(body_dict)

        named_params = 'appkey/123456app/format/json/page/2'
        url = '{protocol}://{domain}/{rtype}/{rmethod}/{named_params}'.format(
            protocol=PROTOCOL,
            domain=DOMAIN,
            rtype=rtype,
            rmethod=rmethod,
            named_params=named_params,
        )
        responses.add(
            responses.GET,
            url,
            body=body,
            status=200,
            content_type='application/json',
        )

        response = wykop_api.request(
            rtype, rmethod, named_params=named_params_dict)

        assert response == body_dict

    @responses.activate
    def test_post_params(self, wykop_api):
        rtype = 'rtype'
        rmethod = 'rmethod'
        post_param_name = 'post_param_name'
        post_param_value = 'post_param_value'
        post_params = {
            post_param_name: post_param_value,
        }
        body_dict = {
            'data': 'data'
        }
        body = json.dumps(body_dict)

        named_params = 'appkey/123456app/format/json'
        url = '{protocol}://{domain}/{rtype}/{rmethod}/{named_params}'.format(
            protocol=PROTOCOL,
            domain=DOMAIN,
            rtype=rtype,
            rmethod=rmethod,
            named_params=named_params,
        )
        responses.add(
            responses.POST,
            url,
            body=body,
            status=200,
            content_type='application/json',
        )

        response = wykop_api.request(
            rtype, rmethod, post_params=post_params)

        assert response == body_dict

    @responses.activate
    def test_file_params(self, wykop_api):
        rtype = 'rtype'
        rmethod = 'rmethod'
        file_param_name = 'file_param_name'
        file_params = {
            file_param_name: FileMock(file_param_name),
        }
        body_dict = {
            'data': 'data'
        }
        body = json.dumps(body_dict)

        named_params = 'appkey/123456app/format/json'
        url = '{protocol}://{domain}/{rtype}/{rmethod}/{named_params}'.format(
            protocol=PROTOCOL,
            domain=DOMAIN,
            rtype=rtype,
            rmethod=rmethod,
            named_params=named_params,
        )
        responses.add(
            responses.POST,
            url,
            body=body,
            status=200,
            content_type='application/json',
        )

        response = wykop_api.request(
            rtype, rmethod, file_params=file_params)

        assert response == body_dict

