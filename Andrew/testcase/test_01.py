# -*- coding:utf-8 -*-

import allure
import pytest
from Andrew.Common.AssertTool import Assert
from Andrew.Common.JsonPathTool import json
from Andrew.Common.LogTool import log
from Andrew.Common.RequestTool import Request


class Test01():

    @allure.testcase("第一条用例")
    @pytest.mark.run(order=1)
    def test_01(self, start):
        log.info("第一条用例")
        url = 'v1/rebate/query/availableRebateSummary?regionCode=340000&saleOrgCode=1017&firstLevelReceivingEnterpriseCode=1000009899'
        Request.get(url)
        body = json.get_value(Request.response, "resultMsg", 0)
        expected_code = "success"
        Assert.assert_string(body, expected_code)
