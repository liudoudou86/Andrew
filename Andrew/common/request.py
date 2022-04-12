# -*- coding:utf-8 -*-

import json

import requests
from Andrew.common.log import log
from Andrew.config.readconfig import ini


def request(func):
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        print("\n")
        log.info('------------------------ Request ------------------------[🚀]')
        try:
            url = list(args)[1]
        except IndexError:
            url = kwargs.get("url", "")
        # 读取配置文件中的url或者传入url
        if (ini._get('Host', 'Host') is not None) and ('http' not in url):
            url = ini._get('Host', 'Host') + list(args)[1]

        log.debug("[method]: {m}".format(m=func_name.upper()))
        log.debug("[url]: {u}".format(u=url))
        headers = kwargs.get("headers", "")
        cookies = kwargs.get("cookies", "")
        params = kwargs.get("params", "")
        data = kwargs.get("data", "")
        jsons = json.dumps(kwargs.get("json", ""), indent=2, ensure_ascii=False)
        if headers != "":
            log.debug(f"[headers]: \n {headers}")
        if cookies != "":
            log.debug(f"[cookies]: \n {cookies}")
        if params != "":
            log.debug(f"[params]: \n {params}")
        if data != "":
            log.debug(f"[data]: \n {data}")
        if jsons != "":
            log.debug(f"[json]: \n {jsons}")

        # 传入可变参数以字典形式展示
        r = func(*args, **kwargs)

        log.info("------------------------ Response ------------------------[🛬️]")
        # 判断是否为json格式，排除其他格式的响应数据
        try:
            res = json.dumps(r.json(), indent=2, ensure_ascii=False)
            log.debug(f"[status_code]: {r.status_code}")
            log.debug(f"[type]: json")
            log.debug(f"[response]: \n {res}")
        # 在返回的数据中没有json格式，则认为是文本格式
        except BaseException as msg:
            log.debug("[warning]: {}".format(msg))
            log.debug(f"[status_code]: {r.status_code}")
            log.debug("[type]: text")
            log.debug(f"[response]: \n {r.text}")

    return wrapper

class HttpRequest(object):
  
    """
    请求工具类封装
    """

    @request
    def get(self, url, params=None, **kwargs):
        if (ini._get('Host', 'Host') is not None) and ('http' not in url):
            url = ini._get('Host', 'Host') + url
        return requests.get(url, params=params, **kwargs)

    @request
    def post(self, url, data=None, json=None, **kwargs):
        if (ini._get('Host', 'Host') is not None) and ('http' not in url):
            url = ini._get('Host', 'Host') + url
        return requests.post(url, data=data, json=json, **kwargs)

    @request
    def put(self, url, data=None, **kwargs):
        if (ini._get('Host', 'Host') is not None) and ('http' not in url):
            url = ini._get('Host', 'Host') + url
        return requests.put(url, data=data, **kwargs)

    @request
    def delete(self, url, **kwargs):
        if (ini._get('Host', 'Host') is not None) and ('http' not in url):
            url = ini._get('Host', 'Host') + url
        return requests.delete(url, **kwargs)

    @property
    def response(self):
        """
        返回响应结果
        :return: response
        """
        response = None
        return response

    @property
    def session(self):
        """
        请求session
        """
        s = requests.Session()
        return s


if __name__ == '__main__':
    # url = 'v1/rebate/query/availableRebateSummary?regionCode=340000&saleOrgCode=1017&firstLevelReceivingEnterpriseCode=1000009899'
    # result = HttpRequest().get(url)
    url = 'https://strategyppm-stg.tasly.com/EHRTF/background/login/loginCheck.do'
    jsons = {
        "userName" : "hanbo",
        "userPassword" : "1",
        "remember" : "true"
    }
    result = HttpRequest().post(url, json=jsons)
