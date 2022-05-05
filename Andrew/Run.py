# -*- coding: utf-8 -*-

import os

import pytest

from Andrew.Common.LogUtil import log
from Andrew.Common.ReadConfig import ini


def main():

    result_dir = ini._get('Report', 'result_path')
    allure_dir = ini._get('Report', 'allure_path')
    pytest.main()
    report = os.system("allure generate --clean %s -o %s" % (result_dir, allure_dir))
    if report == 0:
        log.info("生成报告成功")
        os.system('allure open {}'.format(allure_dir))
    else:
        log.error("生成报告失败")

# 工程入口
if __name__ == '__main__':
    main()