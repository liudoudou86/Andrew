# -*- coding:utf-8 -*-

import yaml
from Andrew.Common.ReadConfig import cm
from Andrew.Common.LogTool import log


class YamlTool:

    def read_yaml(self, file):
        """
        读取yaml文件
        """
        try:
            with open(file, 'r', encoding='utf-8') as f:
                data = yaml.load(stream=f, Loader=yaml.FullLoader)
            return data
        except FileExistsError as e:
            log.error('文件不存在')
            raise e


yaml = YamlTool()

if __name__ == 'main':
    file = yaml.read_yaml(cm.testdata_dir)
    print(file)