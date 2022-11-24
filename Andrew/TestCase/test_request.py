# -*- coding:utf-8 -*-

import allure
import pytest
from Andrew.Common.AssertUtil import Assert
from Andrew.Common.JsonPathUtil import Parsing
from Andrew.Common.ReadConfig import ini
from Andrew.Common.ReadFile import File
from Andrew.Common.RequestUtil import Requestor
from Andrew.Common.TimeUtil import sleep


class TestAdjuestment:

    def get_token(self):
        """
        捕获token
        :return:
        """
        url = 'http://10.6.3.13:28083/api/identity/v2/user/token'
        params = {"userName":"wangrx","password":"VEBzbHk3ODkj","code":"","loginType":0,"uniqueid":"image389c9902-5013-4b7a-b95a-417b39560f70","loginSource":"1020517159","checkCodeUniqueId":"image389c9902-5013-4b7a-b95a-417b39560f70","instanceId":1,"tenantId":1}
        Requestor.request('post', url, params)
        # Assert.assert_code(Requestor.status_code, 200)
        tokencode = Parsing.get_value(Requestor.response, "token", 0)
        ini._set("Host", "token", tokencode)


    @pytest.mark.parametrize("args",File.read_yaml("data.yaml"))
    def test_string(self, args):
        feature = args["case"]["feature"]
        story = args["case"]["story"]
        title = args["case"]["title"]
        url = args["case"]["url"]
        method = args["case"]["method"]
        headers = { 
            "Accept": "application/json, text/plain, */*", 
            "Access-Token": ini._get("Host", "token"),
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50",
        }
        json = args["case"]["json"]
        string = args["case"]["string"]
        number = args["case"]["number"]
        expected_msg = args["case"]["expected_msg"]
        allure.dynamic.feature(feature)
        allure.dynamic.story(story)
        allure.dynamic.title(title)
        Requestor.request(method=method, url=url, headers=headers, json=json)
        body = Parsing.get_value(Requestor.response, string, number)
        Assert.assert_is_string(body, expected_msg)
        sleep(0.1)
