# -*- coding:utf-8 -*-

import pytest
from Andrew.Common.LogUtil import log


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    '''
    获取每个用例状态的钩子函数
    :param item:
    :param call:
    :return:
    '''
    log.info('------------------------ Test Start ------------------------')
    yield

    # 获取钩子方法的调用结果
    out = yield
    log.info('用例执行结果', out)

    # 3. 从钩子方法的调用结果中获取测试报告
    result = out.get_result()

    log.info('测试报告：%s' % result)
    log.info('步骤：%s' % result.when)
    log.info('nodeid：%s' % result.nodeid)
    log.info('description:%s' % str(item.function.__doc__))
    log.info(('运行结果: %s' % result.outcome))