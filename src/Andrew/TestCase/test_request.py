# -*- coding:utf-8 -*-

import allure
import pytest
from Common.AssertUtil import Assert
from Common.JsonPathUtil import Parsing
from Common.ReadFile import File
from Common.RequestUtil import Requestor
from Common.TimeUtil import sleep


class TestAdjuestment:

    @pytest.mark.parametrize("args",File.read_yaml("data.yaml"))
    def test_string(self, args, start):
        feature = args["case"]["feature"]
        story = args["case"]["story"]
        title = args["case"]["title"]
        url = args["case"]["url"]
        method = args["case"]["method"]
        headers = args["case"]["headers"]
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
