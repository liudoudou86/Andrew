# -*- coding:utf-8 -*-

import allure
import pytest
from Common.AssertUtil import Assert
from Common.JsonPathUtil import Json
from Common.ReadYaml import Yaml
from Common.RequestUtil import Requests
from Common.TimeUtil import sleep


@allure.feature("接口测试")
class TestRequest:

    @allure.story("断言字符串")
    @pytest.mark.parametrize("args",Yaml("\data.yaml").read_yaml())
    def test_string(self, args, start):
        url = args["data"]["url"]
        method = args["data"]["method"]
        expected_msg = args["data"]["expected_msg"]
        Requests.request(method=method, url=url)
        body = Json.get_value(Requests.response, "resultMsg", 0)
        Assert.assert_string(body, expected_msg)
        sleep(0.5)
        