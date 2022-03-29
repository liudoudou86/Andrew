# -*- coding:utf-8 -*-

import requests
from Andrew.common.log import log
from Andrew.config.readconfig import ini


IMG = ["jpg", "jpeg", "gif", "bmp", "webp"]


class ResponseResult:
    status_code = 200
    response = None

def request(func):
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        print("\n")
        log.info('-------------- Request -----------------[🚀]')
        try:
            url = list(args)[1]
        except IndexError:
            url = kwargs.get("url", "")
        if (ini._get('Host', 'Host') is not None) and ("http" not in url):
            url = ini._get('Host', 'Host') + list(args)[1]

        img_file = False
        file_type = url.split(".")[-1]
        if file_type in IMG:
            img_file = True

        log.debug("[method]: {m}      [url]: {u} \n".format(m=func_name.upper(), u=url))
        auth = kwargs.get("auth", "")
        headers = kwargs.get("headers", "")
        cookies = kwargs.get("cookies", "")
        params = kwargs.get("params", "")
        data = kwargs.get("data", "")
        json = kwargs.get("json", "")
        if auth != "":
            log.debug(f"[auth]:\n {auth} \n")
        if headers != "":
            log.debug(f"[headers]:\n {headers} \n")
        if cookies != "":
            log.debug(f"[cookies]:\n {cookies} \n")
        if params != "":
            log.debug(f"[params]:\n {params} \n")
        if data != "":
            log.debug(f"[data]:\n {data} \n")
        if json != "":
            log.debug(f"[json]:\n {json} \n")

        # running function
        r = func(*args, **kwargs)

        ResponseResult.status_code = r.status_code
        log.info("-------------- Response ----------------[🛬️]")
        try:
            resp = r.json()
            log.debug(f"[type]: json \n")
            log.debug(f"[response]:\n {resp} \n")
            ResponseResult.response = resp
        except BaseException as msg:
            log.debug("[warning]: {} \n".format(msg))
            if img_file is True:
                log.debug("[type]: {}".format(file_type))
                ResponseResult.response = r.content
            else:
                log.debug("[type]: text \n")
                log.debug(f"[response]:\n {r.text} \n")
                ResponseResult.response = r.text

    return wrapper

class HttpRequest():
  
    """
    请求工具类封装
    :return:
    """

    def __init__(self):
        self.log = log
        self.cookies = 'SESSION=68bd6e98-4d01-4177-ba3d-544a67aa2d9d' # TODO 需要后期维护为动态获取
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
        }

    @request
    def get(self, url, params=None, **kwargs):
        if (ini._get('Host', 'Host') is not None) and ("http" not in url):
            url = ini._get('Host', 'Host') + url
        return requests.get(url, self.headers, params=params, **kwargs)

    @request
    def post(self, url, data=None, json=None, **kwargs):
        if (ini._get('Host', 'Host') is not None) and ("http" not in url):
            url = ini._get('Host', 'Host') + url
        return requests.post(url, data=data, json=json, **kwargs)

    @request
    def put(self, url, data=None, **kwargs):
        if (ini._get('Host', 'Host') is not None) and ("http" not in url):
            url = ini._get('Host', 'Host') + url
        return requests.put(url, data=data, **kwargs)

    @request
    def delete(self, url, **kwargs):
        if (ini._get('Host', 'Host') is not None) and ("http" not in url):
            url = ini._get('Host', 'Host') + url
        return requests.delete(url, **kwargs)

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
    
    @staticmethod
    def request(method=None, url=None, headers=None, files=None, data=None,
                params=None, auth=None, cookies=None, hooks=None, json=None):
        """
        预留用户创建的请求方法
        """
        req = requests.Request(method, url, headers, files, data,
                               params, auth, cookies, hooks, json)
        return req
    


if __name__ == '__main__':
    url = 'v1/rebate/queryRebateIsToSelect/B2B2022031610335949514_1017_1'
    result = HttpRequest().get(url)
