# -*- coding:utf-8 -*-

from Andrew.Common.ReadConfig import ini
from Andrew.Common.TimeUtil import dt_strftime
from loguru import logger


class Log():
  
    """
    日志工具类封装，异步打印
    :return:
    """

    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Log, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    log_path = ini._get('Log', 'log_path')
    time = dt_strftime()
    logger.add(sink = log_path + f"/Log_{time}.log", # 日志路径
                level = ini._get('Log', 'level'), # 输出级别
                rotation = ini._get('Log', 'rotation'),  # 最大保存大小
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
