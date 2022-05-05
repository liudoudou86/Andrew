# -*- coding: utf-8 -*-

import argparse
import os
import sys
from Andrew.Run import main

from Andrew import __description__, __version__


def main():
    """
    定义项目命令行
    :return:
    """
    # 创建解析器
    parser = argparse.ArgumentParser(description=__description__)
    # 创建命令行指令
    parser.add_argument('-v', '--version', dest='version', action='store_true', help="show the version")
    parser.add_argument('-init', help='create a new project.')
    parser.add_argument('-run', help='run test case.')
    # 解析参数
    args = parser.parse_args()
    # 读取命令行指令
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)
    elif len(sys.argv) == 2:
        if sys.argv[1] in ["-v", "-V", "--version"]:
            print("Andrew {}".format(__version__))
        elif sys.argv[1] == "-init":
            parser.print_help()
        elif sys.argv[1] == "-run":
            parser.print_help()
        sys.exit(0)
    # 创建脚手架
    project_name = args.init
    if sys.argv[1] == "-init":
        create_scaffold(project_name)
    # 运行测试用例
    if sys.argv[1] == "-run":
        main()

def create_scaffold(project_name):
    """
    脚手架生成目录结构
    :param project_name: 项目名称
    :return:
    """
    def create_folder(path):
        os.makedirs(path)

    def create_file(path, file_content=""):
        with open(path, "w", encoding="utf-8") as f:
            f.write(file_content)

    config_file = """
[Host]
host = http://10.6.3.13:28083/api/rebate/
token = eyJhbGciOiJIUzI1NiJ9.eyJpbnN0YW5jZUlkIjoxLCJsb2dpbk5hbWUiOiJXQU5HUlgiLCJ0ZW5hbnRJZCI6MSwiaWQiOjQ4MiwibG9naW5Tb3VyY2UiOiIxMDIwNTE3MTU5IiwianRpIjoiYzRmMTUzNmQtNzlhZC00NWUxLWFhOGYtNzAzODNiMDYxM2E0IiwibmJmIjoxNjUxMDIwNTA3LCJleHAiOjE2NTYyMDQ1MDd9.e29c4NuEAca4qY6GMcBeX1ei-tv8O8vbqntWj-iyifk

[Log]
log_path = ./Log
level = DEBUG
rotation = 100MB
format = {time:YYYY-MM-DD HH:mm:ss} | {level:<8} [ {file}:{line} ] - {message}

[Mysql]
host = 10.6.3.13
user = root
port = 23306
password = root
db_name = tasly-center-channel

[Report]
report_path = ./Report
result_path = ./Report/Result
allure_path = ./Report/Allure

[TestData]
testdata_path = ./TestData
"""

    conftest_file = """
# -*- coding:utf-8 -*-

import pytest
from Andrew.Common.LogUtil import log


@pytest.fixture(scope="function")
def start():
    log.info('------------------------ Test Start ------------------------')
    yield
    log.info('------------------------ Test End ------------------------')
"""

    testcase_file = """
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
        url = 'http://10.6.3.13:28083/api/identity/v2/user/token'
        params = {"userName":"wangrx","password":"VEBzbHk3ODkj","code":"","loginType":0,"uniqueid":"image389c9902-5013-4b7a-b95a-417b39560f70","loginSource":"1020517159","checkCodeUniqueId":"image389c9902-5013-4b7a-b95a-417b39560f70","instanceId":1,"tenantId":1}
        Requestor.request('post', url, params)
        # Assert.assert_code(Requestor.status_code, 200)
        tokencode = Parsing.get_value(Requestor.response, "token", 0)
        ini._set("Host", "token", tokencode)


    @pytest.mark.parametrize("args",File.read_yaml("data.yaml"))
    def test_string(self, args, start):
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
    """

    testdata_file = """
# 用例1
-
  case : 
    feature : 接口测试
    story : 列表展示 - 操作人
    title : 字符串断言
    url : v1/rebate/adjustment/pageByPostFilter?withDetail=true&pageSize=10&pageNum=1
    method : post
    json : 
        code: null
        instructions: null
        remark: null
        operatePerson: null
        operateTimeStart: null
        operateTimeEnd: null
        status: null
        type: freeze_adjustment
    expected_code : 200
    string : operatePerson
    number : 0
    expected_msg : 王瑞香

# 用例2
-
  case : 
    feature : 接口测试
    story : 调整 - 返回状态
    title : 字符串断言
    url : v1/rebate/query/availableRebateSummary?regionCode=340000&saleOrgCode=1017&firstLevelReceivingEnterpriseCode=1000009899
    method : get
    json : 
    expected_code : 200
    string : resultMsg
    number : 0
    expected_msg : text
"""
    pytest_file = """
[pytest]
addopts = -vs --alluredir=./Report/Result --clean-alluredir --disable-warnings
testpaths = ./TestCase
python_files = test_*.py
python_classes = Test*
python_functions = test_*

log_level = INFO
log_format = %(asctime)s [%(levelname)s] ~ %(message)s
log_date_format = %Y-%m-%d %H:%M:%S

log_cli = 0
log_cli_level = DEBUG
log_cli_format = %(asctime)s [%(levelname)s] (%(filename)s:%(lineno)s) ~ %(message)s
log_cli_date_format = %Y-%m-%d %H:%M:%S
"""

    # 创建项目骨架
    create_folder(project_name)
    create_folder(os.path.join(project_name, "Config"))
    create_file(os.path.join(project_name, "Config", "Config.ini"), config_file)
    create_folder(os.path.join(project_name, "Log"))
    create_folder(os.path.join(project_name, "Report"))
    create_folder(os.path.join(project_name, "Report", "Allure"))
    create_folder(os.path.join(project_name, "Report", "Result"))
    create_folder(os.path.join(project_name, "TestCase"))
    create_file(os.path.join(project_name, "TestCase", "conftest.py"), conftest_file)
    create_file(os.path.join(project_name, "TestCase", "test_request.py"), testcase_file)
    create_folder(os.path.join(project_name, "TestData"))
    create_file(os.path.join(project_name, "TestData", "data.yaml"), testdata_file)
    create_file(project_name, "data.yaml"), pytest_file