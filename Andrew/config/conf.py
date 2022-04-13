# -*- coding:utf-8 -*-

import os


class ConfigManager():

    # 项目目录
    BASE_DIR = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]

    # 报告目录
    report_dir = os.path.join(BASE_DIR, 'Report')

    # 日志目录
    log_dir = os.path.join(BASE_DIR, 'Logs')

    # 用例目录
    testcase_dir = os.path.join(BASE_DIR, 'TestCase')

    @property
    def ini_file(self):
        """配置文件"""
        ini_file = os.path.join(self.BASE_DIR, 'Config', 'Config.ini')
        if not os.path.exists(ini_file):
            raise FileNotFoundError("配置文件%s不存在!" % ini_file)
        return ini_file

cm = ConfigManager()