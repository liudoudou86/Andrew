# -*- coding: utf-8 -*-

import os
from threading import Thread

import pytest

from Andrew.Config.Conf import cm
from Andrew.TestCase.test_01 import Test01


def main():
    Thread(
        target=Test01.test_01,
        name="TestThread",
        args=("python3 {}".format(cm.testcase_dir, "test_01.py"),),
        daemon=False
    ).start()
    pytest.main(["-sq", "--alluredir", cm.report_dir])


# 自动化测试启动器
if __name__ == '__main__':
    main()