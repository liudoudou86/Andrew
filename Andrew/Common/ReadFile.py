# -*- coding:utf-8 -*-

import json

import yaml
from Andrew.Config.Conf import cm

from Andrew.Common.LogUtil import log


class ReadFile(object):

    def read_yaml(self, file_name):
        """
        读取yaml文件
        :return:
        """
        try:
            with open(cm.testdata_file + '\\' + file_name, 'r', encoding='utf-8') as f:
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
            with open(cm.testdata_file + '\\' + file_name, 'r', encoding='utf-8-sig') as f:
                data = json.load(f)
            return data
        except FileExistsError as e:
            log.error("文件不存在: {}".format(e))

File = ReadFile()