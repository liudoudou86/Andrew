# -*- coding:utf-8 -*-

import json
import os

import yaml
from Andrew.Common.LogUtil import log
from Andrew.Common.ReadConfig import ini
from Andrew.Config.Conf import cm


class ReadFile(object):

    def __init__(self):
        """
        初始化测试数据路径
        """
        if (ini._get('TestData', 'testdata_path') == ""):
            self.file_path = cm.TESTDATA_DIR
        else:
            self.file_path = ini._get('TestData', 'testdata_path')

    def read_yaml(self, file_name):
        """
        读取yaml文件
        :return:
        """
        try:
            with open(self.file_path + os.sep + file_name, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(stream=f)
            return data
        except FileExistsError as e:
            log.error("文件不存在: {}".format(e))

    def read_json(self, file_name):
        """
        读取json文件
        :return:
        """
        try:
            with open(self.file_path + os.sep + file_name, 'r', encoding='utf-8-sig') as f:
                data = json.load(f)
            return data
        except FileExistsError as e:
            log.error("文件不存在: {}".format(e))

File = ReadFile()
