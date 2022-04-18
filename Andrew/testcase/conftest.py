# -*- coding:utf-8 -*-

import pytest
from Andrew.Common.LogTool import log


@pytest.fixture(scope="session")
def start():
    log.info("------------------------测试开始------------------------")
    yield
    log.info("------------------------测试结束------------------------")