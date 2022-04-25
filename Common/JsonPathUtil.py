# -*- coding:utf-8 -*-

import jsonpath


class JsonAnalysis(object):

    """
    解析JSON工具类
    """
    def get_value(self, data, keyword, number):
        """
        提取json中的关键字对应的一个值
        :param data: 传入的json数据
        :param keyword: 提取的关键字
        :param number: 关键字的排序
        :return:
        """
        return jsonpath.jsonpath(data, f'$..{keyword}')[number]

    def get_pair(self, data, keyword):
        """
        提取json中的关键字对应的一组值
        :param data: 传入的json数据
        :param keyword: 提取的关键字
        :return:
        """
        return jsonpath.jsonpath(data, f'$..{keyword}')

Parsing = JsonAnalysis()