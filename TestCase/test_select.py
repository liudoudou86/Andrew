# -*- coding:utf-8 -*-

import allure
import pytest
from Common.ReadYaml import Yaml
from Common.AssertUtil import Assertions
from Common.JsonPathUtil import JsonAnalysis
from Common.RequestUtil import HttpRequest


@allure.feature("接口测试")
class TestSelect:

    @allure.story("读取yaml文件")
    @pytest.mark.parametrize("args",Yaml("/data.yaml").read_yaml())
    def test_01(self, args, start):
        url = args["test"]["url"]
        method = args["test"]["method"]
        HttpRequest.request(method, url)
        expected_msg = args["test"]["expected_msg"]
        body = JsonAnalysis.get_value(HttpRequest.response, "resultMsg", 0)
        Assertions.assert_string(body, expected_msg)
