# -*- coding:utf-8 -*-

import os
import sys
sys.path.append(os.path.realpath('./Andrew'))
from config.conf import cm
from common.times import dt_strftime
from loguru import logger
import configparser

class Log():
  
    """
    对loguru进行二次封装
    :return:
    """

    __instance = None

    config = configparser.ConfigParser()
    log_path = cm.log_file
    config.read(cm.ini_file, encoding="UTF-8")
    time = dt_strftime()
    logger.add(log_path + f"/Log_{time}.log",
                rotation=config.get('Log', 'rotation'),  # 最大保存大小
                encoding="utf-8",  # 支持中文格式
                enqueue=True,  # 支持异步存储
                retention=config.get('Log', 'retention'),  # 保存期限10天
                format="{time:YYYY-MM-DD HH:mm:ss} | {level:<8} [ {file}:{line} ] - {message}"
    )

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Log, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

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