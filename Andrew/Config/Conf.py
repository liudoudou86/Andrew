# -*- coding:utf-8 -*-

import os


class ConfigManager():

    # 项目目录
    BASE_DIR = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]

    # 日志目录
    LOG_DIR = os.path.join(BASE_DIR, 'Log')

    # 报告目录
    REPORT_DIR = os.path.join(BASE_DIR, 'Report')
    ALLURE_DIR = os.path.join(REPORT_DIR, 'Allure')
    RESULT_DIR = os.path.join(REPORT_DIR, 'Result')

    # 测试用例目录
    TESTCASE_DIR = os.path.join(BASE_DIR, 'TestCase')

    # 测试数据目录
    TESTDATA_DIR = os.path.join(BASE_DIR, 'TestData')

    # 配置文件目录
    @property
    def ini_file(self):
        """配置文件"""
        ini_file = os.path.join(self.BASE_DIR, 'Config', 'Config.ini')
        if not os.path.exists(ini_file):
            raise FileNotFoundError("配置文件%s不存在!" % ini_file)
        return ini_file

cm = ConfigManager()