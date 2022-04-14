# -*- coding:utf-8 -*-

import jsonpath

json = {
  "data": {
    "amountAvailable": 0,
    "enterpriseAvailableRebateAmount": "",
    "modularRebateInfoList": [
      {
        "availableRebateAmount": 0,
        "data": "",
        "exceptCauseApp": "",
        "exceptCauseIp": "",
        "exceptClass": "",
        "extFields": {},
        "moduleCode": "KM01",
        "moduleName": "商务",
        "rebateAmountWithInPast180Days": 0,
        "rebateAmountWithoutPast180Days": 0,
        "result": "",
        "resultCode": "0",
        "resultMsg": "success"
      },
      {
        "availableRebateAmount": 0,
        "data": "",
        "exceptCauseApp": "",
        "exceptCauseIp": "",
        "exceptClass": "",
        "extFields": {},
        "moduleCode": "KM03",
        "moduleName": "OTC",
        "rebateAmountWithInPast180Days": 0,
        "rebateAmountWithoutPast180Days": 0,
        "result": "",
        "resultCode": "0",
        "resultMsg": "success"
      },
      {
        "availableRebateAmount": 0,
        "data": "",
        "exceptCauseApp": "",
        "exceptCauseIp": "",
        "exceptClass": "",
        "extFields": {},
        "moduleCode": "KM04",
        "moduleName": "商销",
        "rebateAmountWithInPast180Days": 0,
        "rebateAmountWithoutPast180Days": 0,
        "result": "",
        "resultCode": "0",
        "resultMsg": "success"
      }
    ],
    "regionAvailableRebateAmount": "",
    "regionLimitRebateAmount": 0.0,
    "saleOrgAvailableRebateAmount": ""
  },
  "exceptCauseApp": "",
  "exceptCauseIp": "",
  "exceptClass": "",
  "extFields": {},
  "resultCode": "0",
  "resultMsg": "success"
}

class JsonAnalysis():

    """
    解析JSON工具类
    """
    def json_value(data, keyword, number):
        """
        提取json中的某一个关键字对应的值
        :param data: 传入的json数据
        :param keyword: 提取的关键字
        :param number: 关键字的排序
        :return:
        """
        return jsonpath.jsonpath(data, f'$..{keyword}')[number]

    def json_values(data, keyword):
        """
        提取json中的某一个关键字对应的值
        :param data: 传入的json数据
        :param keyword: 提取的关键字
        :return:
        """
        return jsonpath.jsonpath(data, f'$..{keyword}')


js = JsonAnalysis()