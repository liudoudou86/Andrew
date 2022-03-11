# -*- coding:utf-8 -*-

from loguru import logger
import os
import sys

sys.path.append(os.path.realpath('./Andrew'))
logger.add('test_{time}.log', format="{time} {level} {message}", filter="my_module", level="INFO")

def test(a, b):
    logger.info("a + b = {}".format(a + b))

test(1, 2)