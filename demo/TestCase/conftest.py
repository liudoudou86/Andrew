# -*- coding:utf-8 -*-

import pytest
from Andrew.Common.LogUtil import log


@pytest.fixture(scope="function")
def start():
    log.info('------------------------ Test Start ------------------------')
    yield
    log.info('------------------------ Test End ------------------------')