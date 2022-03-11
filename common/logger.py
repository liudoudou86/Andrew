# -*- coding:utf-8 -*-

import os
import sys
sys.path.append(os.path.realpath('./Andrew'))
from loguru import logger
from config.conf import cm


path = cm.log_file
logger.debug(path)
logger.add(path + '/testlog_{time}.log')
logger.debug('where are you??')