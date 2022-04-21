# -*- coding:utf-8 -*-

import allure
import pytest
from Andrew.Common.AssertTool import Assert
from Andrew.Common.JsonPathTool import Json
from Andrew.Common.RequestTool import Request
from Andrew.Common.LogTool import log

@allure.feature("测试项目")
class TestSelect:

    @allure.title("第一条用例")
    @pytest.mark.run(order=1)
    def test_01(self, start):
        log.info("第一条用例")
        url = 'v1/rebate/query/availableRebateSummary?regionCode=340000&saleOrgCode=1017&firstLevelReceivingEnterpriseCode=1000009899'
        Request.get(url)
        body = Json.get_value(Request.response, "resultMsg", 0)
        expected_msg = "success"
        Assert.assert_string(body, expected_msg)

    @allure.title("第二条用例")
    @pytest.mark.run(order=2)
    def test_02(self, start):
        log.info("第二条用例")
        url = 'v1/rebate/query/availableRebateSummary?regionCode=340000&saleOrgCode=1017&firstLevelReceivingEnterpriseCode=1000009899'
        Request.get(url)
        body = Json.get_value(Request.response, "resultMsg", 0)
        expected_msg = "aaa"
        Assert.assert_string(body, expected_msg)
