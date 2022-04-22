# -*- coding:utf-8 -*-

import yaml
from Config.Conf import cm
from Common.LogUtil import log


class Yaml(object):

    def __init__(self, file_name):
        self.file_name = file_name

    def read_yaml(self):
        """
        读取yaml文件
        """
        try:
            with open(cm.testdata_file + self.file_name, 'r', encoding='utf-8') as f:
                data = yaml.load(stream=f, Loader=yaml.FullLoader)
            return data
        except FileExistsError as e:
            log.error("文件不存在: {}".format(e)) 