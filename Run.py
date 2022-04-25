# -*- coding: utf-8 -*-

import os

import pytest

from Common.LogUtil import log
from Config.Conf import cm


def main():

    pytest.main()
    report = os.system("allure generate --clean %s -o %s" % (cm.result_dir, cm.allure_dir))
    if report == 0:
        log.info("生成报告成功")
        # os.system('allure open {}'.format(cm.allure_dir))
    else:
        log.error("生成报告失败")

# 自动化测试启动器
if __name__ == '__main__':
    main()