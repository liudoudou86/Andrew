# -*- coding:utf-8 -*-

from Andrew.Common.LogUtil import log
from Andrew.Common.TimeUtil import sleep
from hamcrest import *
from jsonschema import validate


class Assertions():
    """
    断言工具类封装
    """
    def __init__(self):
        self.log = log

    def assert_code(self, code:int, expected_code):
        """
        验证response状态码
        :param code:
        :param expected_code:
        :return:
        """
        try:
            assert_that(code, equal_to(expected_code))
            self.log.info("👀 状态码等于预期结果")
            return True
        except:
            self.log.error("❌ 状态码错误, 预期为 %s, 实际为 %s " % (expected_code, code))
            raise AssertionError("❌ 状态码错误, 预期为 %s, 实际为 %s " % (expected_code, code))

    def assert_is_string(self, body_msg, expected_msg):
        """
        验证response 字符串相同
        :param body_msg:
        :param expected_msg:
        :return:
        """
        try:
            assert_that(body_msg, has_string(expected_msg))
            self.log.info("👀 字符串与预期结果相同")
            return True

        except:
            self.log.error("❌ 字符串与预期结果不同, 预期为 %s, 实际为 %s " % (expected_msg, body_msg))
            raise AssertionError("❌ 字符串与预期结果不同, 预期为 %s, 实际为 %s " % (expected_msg, body_msg))

    def assert_isnot_string(self, body_msg, expected_msg):
        """
        验证response 字符串不同
        :param body_msg:
        :param expected_msg:
        :return:
        """
        try:
            assert_that(body_msg, is_not(has_string(expected_msg)))
            self.log.info("👀 字符串于预期结果不同")
            return True

        except:
            self.log.error("❌ 字符串与预期结果相同, 预期为 %s, 实际为 %s " % (expected_msg, body_msg))
            raise AssertionError("❌ 字符串与预期结果相同, 预期为 %s, 实际为 %s " % (expected_msg, body_msg))
    
    def assert_schema(self, body, expected_schema):
        """
        验证response 是否符合schema规约
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            validate(body, expected_schema)
            return True

        except:
            self.log.error("不符合预期schema规约, 预期规约为 %s" % expected_schema)
            raise AssertionError("不符合预期schema规约, 预期规约为 %s" % expected_schema)

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
            raise AssertionError("对象未包含预期值, 预期值为 %s" % expected_msg)

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
            raise AssertionError("对象未包含预期属性, 预期属性为 %s" % expected_msg)

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
            raise AssertionError("对象未包含预期键值对, 预期键值对为 %s" % expected_msg)

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
            raise AssertionError("响应时间大于预期结果, 预期为 %s, 实际为 %s " % (expected_time, time))

Assert = Assertions()