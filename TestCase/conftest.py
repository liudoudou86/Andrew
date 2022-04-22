# -*- coding:utf-8 -*-

import pytest
from Common.LogUtil import log


@pytest.fixture(scope="function")
def start():
    log.info("------------------------测试开始------------------------")
    yield
    log.info("------------------------测试结束------------------------")