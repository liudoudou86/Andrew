# -*- coding:utf-8 -*-

import requests
from Andrew.common.log import log


class HttpRequest():
  
    """
    请求工具类封装
    :return:
    """

    def __init__(self):
        self.log = log
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Content-Type': 'application/json;charset=UTF-8',
            'Cookie': 'SESSION=fa0e0f1d-7948-4f57-8cbf-4add533683c5', # TODO 需要后期维护为动态获取
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
        }
    
    def send_get(self, url, data=None, headers=None):
        if headers:
            self.headers.update(headers)
        res = requests.get(url=url, data=data, headers=self.headers)
        return res
    
    def send_post(self, url, data=None, headers=None):
        if headers:
            self.headers.update(headers)
        res = requests.post(url=url, data=data, headers=self.headers)
        return res


if __name__ == '__main__':
    url = 'http://10.8.8.145:8082/taslyb2bbms/v1/rebate/queryRebateIsToSelect/B2B2022031610335949514_1017_1'
    result = HttpRequest().send_get(url)
    log.debug(result.json)
