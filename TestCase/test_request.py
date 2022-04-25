# -*- coding:utf-8 -*-

import allure
import pytest
from Common.AssertUtil import Assert
from Common.JsonPathUtil import Parsing
from Common.LogUtil import log
from Common.ReadFile import File
from Common.RequestUtil import Requestor
from Common.TimeUtil import sleep


@allure.feature("接口测试")
class TestRequest:

    @allure.story("断言字符串")
    @pytest.mark.parametrize("args",File.read_yaml("data.yaml"))
    def test_string(self, args, start):
        name = args["case"]["name"]
        url = args["case"]["url"]
        method = args["case"]["method"]
        expected_msg = args["case"]["expected_msg"]
        log.info(name)
        Requestor.request(method=method, url=url)
        body = Parsing.get_value(Requestor.response, "resultMsg", 0)
        Assert.assert_string(body, expected_msg)
        sleep(0.1)
