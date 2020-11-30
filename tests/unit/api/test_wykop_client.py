from wykop import WykopAPI


class TestWykopApi(object):

    def test_should_named_parameters_be_string(self):
        api = self.default_api_client()

        params = api.get_named_params(named_params={})

        for key, value in params.items():
            assert isinstance(key, str)
            assert isinstance(value, str)

    def test_should_take_only_named_parameters_with_value(self):
        api = self.default_api_client()
        params_with_no_value = 'params_with_no_value'
        params_with_value = 'params_with_value'
        named_params = {
            params_with_no_value: None,
            params_with_value: "value"
        }

        params = api.get_named_params(named_params=named_params)

        assert params_with_no_value not in params
        assert params_with_value in params

    def test_should_not_take_named_parameters_with_empty_value(self):
        api = self.default_api_client()
        params_with_empty_value = 'params_with_value'
        named_params = {
            params_with_empty_value: ""
        }

        params = api.get_named_params(named_params=named_params)

        assert params_with_empty_value not in params

    def default_api_client(self):
        return WykopAPI(appkey="appkey", secretkey="secretkey")
