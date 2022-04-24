# -*- coding:utf-8 -*-

import requests

from Common.LogUtil import log
from Common.ReadConfig import ini


class ResponseResult:
    status_code = None
    response = None

def request_log(func):
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        print("\n")
        log.info('------------------------ Request ------------------------[🚀]')
        try:
            url = list(args)[1]
        except IndexError:
            url = kwargs.get("url", "")
        # 读取配置文件中的url或者传入url
        if (ini._get('Host', 'host') is not None) and ('http' not in url):
            url = ini._get('Host', 'host') + url

        log.debug("[method]: {m}".format(m=func_name.upper()))
        log.debug("[url]: {u}".format(u=url))
        headers = kwargs.get("headers", "")
        cookies = kwargs.get("cookies", "")
        params = kwargs.get("params", "")
        data = kwargs.get("data", "")
        json = kwargs.get("json", "")
        if headers != "":
            log.debug(f"[headers]: \n {headers}")
        if cookies != "":
            log.debug(f"[cookies]: \n {cookies}")
        if params != "":
            log.debug(f"[params]: \n {params}")
        if data != "":
            log.debug(f"[data]: \n {data}")
        if json != "":
            log.debug(f"[json]: \n {json}")

        # 传入可变参数以字典形式展示
        r = func(*args, **kwargs)

        log.info("------------------------ Response ------------------------[🛬️]")
        # 判断是否为json格式，排除其他格式的响应数据
        try:
            res = r.json()
            log.debug(f"[status_code]: {r.status_code}")
            log.debug(f"[type]: json")
            log.debug(f"[response]: \n {res}")
            ResponseResult.status_code = r.status_code
            ResponseResult.response = r.json()
        # 在返回的数据中没有json格式，则认为是文本格式
        except BaseException as msg:
            log.debug("[warning]: {}".format(msg))
            log.debug(f"[status_code]: {r.status_code}")
            log.debug("[type]: text")
            log.debug(f"[response]: \n {r.text}")
            ResponseResult.status_code = r.status_code
            ResponseResult.response = r.text

    return wrapper

class HttpRequest(object):
  
    """
    请求工具类封装
    """

    @request_log
    def get(self, url, params=None, **kwargs):
        if (ini._get('Host', 'host') is not None) and ('http' not in url):
            url = ini._get('Host', 'host') + url
        return requests.get(url, params=params, **kwargs)

    @request_log
    def post(self, url, data=None, json=None, **kwargs):
        if (ini._get('Host', 'host') is not None) and ('http' not in url):
            url = ini._get('Host', 'host') + url
        return requests.post(url, data=data, json=json, **kwargs)

    @request_log
    def put(self, url, data=None, **kwargs):
        if (ini._get('Host', 'host') is not None) and ('http' not in url):
            url = ini._get('Host', 'host') + url
        return requests.put(url, data=data, **kwargs)

    @request_log
    def delete(self, url, **kwargs):
        if (ini._get('Host', 'host') is not None) and ('http' not in url):
            url = ini._get('Host', 'host') + url
        return requests.delete(url, **kwargs)

    @property
    def status_code(self):
        """
        返回状态码
        :return: status_code
        """
        return ResponseResult.status_code

    @property
    def response(self):
        """
        返回响应结果
        :return: response
        """
        return ResponseResult.response

    @property
    def session(self):
        """
        请求session
        """
        s = requests.Session()
        return s
    
    @request_log
    def request(self, method, url, **kwargs):
        """
        预留自动化调用方法
        """
        if (ini._get('Host', 'host') is not None) and ('http' not in url):
            url = ini._get('Host', 'host') + url
        return requests.request(method, url, **kwargs)

Requests = HttpRequest()