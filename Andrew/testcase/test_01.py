# -*- coding:utf-8 -*-

import pytest
from Andrew.Common.AssertTool import Assert
from Andrew.Common.LogTool import log
from Andrew.Common.RequestTool import Request


class Test01():

    @pytest.mark.run(order=1)
    def test_01(self):
        log.info("第一条用例")
        url = 'v1/rebate/query/availableRebateSummary?regionCode=340000&saleOrgCode=1017&firstLevelReceivingEnterpriseCode=1000009899'
        Request.get(url)
        s = Request.status_code
        # body = Request.response
        # expected_code = {"resultMsg": "success"}
        Assert.assert_code(s, 200)

    @pytest.mark.run(order=2)
    def test_02(self):
        log.info("第二条用例")
