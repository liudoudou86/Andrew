# -*- coding:utf-8 -*-

import yaml
from Andrew.Config.Conf import cm
from Andrew.Common.LogTool import log


class ReadYaml(object):

    def read_yaml(self):
        """
        读取yaml文件
        """
        try:
            with open(cm.testdata_file, 'r', encoding='utf-8') as f:
                data = yaml.load(stream=f, Loader=yaml.FullLoader)
            return data
        except FileExistsError as e:
            log.error("文件不存在: {}".format(e)) 


Yaml = ReadYaml()