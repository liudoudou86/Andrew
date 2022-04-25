# -*- coding:utf-8 -*-

import pytest
from Common.LogUtil import log


@pytest.fixture(scope="function")
def start():
    print("\n")
    log.info('------------------------ Test Start ------------------------')
    yield
    print("\n")
    log.info('------------------------ Test End ------------------------')