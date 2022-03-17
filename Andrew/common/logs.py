# -*- coding:utf-8 -*-

import os
import sys

sys.path.append(os.path.realpath('./Andrew/Andrew/'))
from config.conf import cm
from loguru import logger

from config.readconfig import ini
from common.times import dt_strftime


class Log():
  
    """
    日志方法封装，异步打印
    :return:
    """

    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Log, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    log_path = cm.log_file
    time = dt_strftime()
    logger.add(sink = log_path + f"/Log_{time}.log", # 日志路径
                level = ini._get('Log', 'level'), # 输出级别
                rotation = ini._get('Log', 'rotation'),  # 最大保存大小
                retention = ini._get('Log', 'retention'),  # 保存期限7天
                encoding = "utf-8",  # 支持中文格式
                enqueue = True,  # 支持异步存储
                format = ini._get('Log', 'format') # 输出格式
    )

    def info(self, msg):
        return logger.info(msg)

    def debug(self, msg):
        return logger.debug(msg)
    
    def error(self, msg):
        return logger.error(msg)

    def warning(self, msg):
        return logger.warning(msg)

log = Log()

if __name__ == '__main__':
    log.debug('where are you?')
