# -*- coding:utf-8 -*-

import os
import sys

sys.path.append(os.path.realpath('./Andrew'))
from config.conf import cm
from loguru import logger
"""
path = cm.log_file
logger.debug(path)
logger.add(path + '/testlog_{time}.log')
logger.debug('where are you??')
"""
class Log:
  
    """
    logurr进行二次封装
    """
    def info(self, msg):
        return logger.info(msg)

    def debug(self, msg):
        return logger.debug(msg)
    
    def error(self, msg):
        return logger.error(msg)
    
    def warning(self, msg):
        return logger.warning(msg)
    