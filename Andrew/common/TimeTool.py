# -*- coding:utf-8 -*-

import datetime
import time
from functools import wraps


def timestamp():
    """时间戳"""
    return time.time()


def dt_strftime():
    """
    datetime格式化时间
    :return:
    """
    return datetime.datetime.now().strftime("%Y-%m-%d-%H_%M_%S")


def sleep(seconds=1.0):
    """
    睡眠时间
    """
    time.sleep(seconds)


def running_time(func):
    """函数运行时间"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = timestamp()
        res = func(*args, **kwargs)
        print("校验元素完成! 用时%.3f秒！" % (timestamp() - start))
        return res

    return wrapper