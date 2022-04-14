# -*- coding:utf-8 -*-

import pytest
from Andrew.Common.AssertTool import Assert
from Andrew.Common.LogTool import log
from Andrew.Common.RequestTool import Request
from Andrew.Common.JsonPathTool import js


class Test01():

    @pytest.mark.run(order=1)
    def test_01(self, start):
        log.info("第一条用例")
        url = 'v1/rebate/query/availableRebateSummary?regionCode=340000&saleOrgCode=1017&firstLevelReceivingEnterpriseCode=1000009899'
        Request.get(url)
        s = Request.status_code
        res = Request.response
        print(res)
        body = js.json_value(res, "resultMsg", 0)
        expected_code = {"resultMsg": "success"}
        Assert.assert_obj(body, expected_code)

    @pytest.mark.run(order=2)
    def test_02(self, start):
        log.info("第二条用例")

    @pytest.mark.run(order=3)
    def test_03(self, start):
        log.info("第三条用例")
