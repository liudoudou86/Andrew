# -*- coding:utf-8 -*-

import pytest
from Andrew.Common.LogTool import log


@pytest.fixture()
def start():
    log.info("------------------------测试开始------------------------")
    yield
    log.info("------------------------测试结束------------------------")