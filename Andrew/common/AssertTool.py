# -*- coding:utf-8 -*-

from Andrew.Common.LogTool import log
from hamcrest import *


class Assertions():
    """
    断言工具类封装
    """
    def __init__(self):
        self.log = log

    def assert_code(self, code, expected_code):
        """
        验证response状态码
        :param code:
        :param expected_code:
        :return:
        """
        try:
            assert_that(code, equal_to(expected_code))
            return True
        except:
            self.log.error("状态码错误, 预期为 %s, 实际为 %s " % (expected_code, code))
            raise

    def assert_string(self, body_msg, expected_msg):
        """
        验证response 相等字符串
        :param body_msg:
        :param expected_msg:
        :return:
        """
        try:
            assert_that(body_msg, has_string(expected_msg))
            return True

        except:
            self.log.error("字符串不等于预期结果, 预期为 %s, 实际为 %s " % (expected_msg, body_msg))
            raise

    def assert_value(self, body, expected_msg):
        """
        验证response 对象是否包含预期值
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            assert_that(body, has_value(expected_msg))
            return True

        except:
            self.log.error("对象未包含预期值, 预期值为 %s" % expected_msg)
            raise

    def assert_key(self, body, expected_msg):
        """
        验证response 对象是否包含预期属性
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            assert_that(body, has_key(expected_msg))
            return True

        except:
            self.log.error("对象未包含预期属性, 预期属性为 %s" % expected_msg)
            raise

    def assert_obj(self, body, expected_msg):
        """
        验证response 对象是否包含预期键值对
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            assert_that(body, has_entries(expected_msg))
            return True

        except:
            self.log.error("对象未包含预期键值对, 预期键值对为 %s" % expected_msg)
            raise

    def assert_time(self, time, expected_time):
        """
        验证response 响应时间小于预期最大响应时间, 单位：毫秒
        :param body:
        :param expected_time:
        :return:
        """
        try:
            assert_that(time, less_than_or_equal_to(expected_time))
            return True

        except:
            self.log.error("响应时间大于预期结果, 预期为 %s, 实际为 %s " % (expected_time, time))
            raise

Assert = Assertions()
