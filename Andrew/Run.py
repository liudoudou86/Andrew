# -*- coding: utf-8 -*-

import os
from threading import Thread

import pytest

from Andrew.Config.Conf import cm
from Andrew.TestCase.test_select import TestSelect
from Andrew.Common.LogTool import log


def main():

    Thread(
        target=TestSelect,
        name="TestThread",
        args=("python3 {}".format(cm.testcase_dir, "test_01.py"),),
        daemon=False
    ).start()
    pytest.main()
    report = os.system("allure generate --clean %s -o %s" % (cm.result_dir, cm.allure_dir))
    if report == 0:
        log.info("生成报告成功")
        os.system('allure open {}'.format(cm.allure_dir))
    else:
        log.info("生成报告失败")

# 自动化测试启动器
if __name__ == '__main__':
    main()