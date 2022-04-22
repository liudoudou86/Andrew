# -*- coding:utf-8 -*-

import allure
import pytest
from Common.ReadYaml import Yaml
from Common.AssertUtil import Assert
from Common.JsonPathUtil import Json
from Common.RequestUtil import Request


@allure.feature("接口测试")
class TestSelect:

    @allure.story("读取yaml文件")
    @pytest.mark.parametrize("args",Yaml("\data.yaml").read_yaml())
    def test_request(self, args, start):
        url = args["data"]["url"]
        method = args["data"]["method"]
        expected_msg = args["data"]["expected_msg"]
        Request.get(url=url)
        body = Json.get_value(Request.response, "resultMsg", 0)
        Assert.assert_string(body, expected_msg)