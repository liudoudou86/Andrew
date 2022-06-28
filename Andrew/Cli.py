# -*- coding: utf-8 -*-

import argparse
import os
import sys

from Andrew import __description__, __version__
from Andrew.Common.ReadConfig import ini
from Andrew.Expansion.main import app


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
    parser.add_argument('-server', dest='server', action='store_true', help='start web server.')
    # 解析参数
    args = parser.parse_args()
    # 读取命令行指令
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)
    elif len(sys.argv) == 2:
        # 查看框架版本
        if sys.argv[1] in ["-v", "-V", "--version"]:
            print("Andrew {}".format(__version__))
        elif sys.argv[1] == "-init":
            parser.print_help()
        elif sys.argv[1] == "-run":
            parser.print_help()
        # 启动web服务
        elif sys.argv[1] == "-server":
            command = 'uvicorn main:app --reload'
            os.system(command)
        sys.exit(0)
    # 创建脚手架
    project_name = args.init
    if sys.argv[1] == "-init":
        create_scaffold(project_name)
        return 0
    # 运行测试用例
    test_file = args.run
    if sys.argv[1] == "-run":
        command = 'python -m pytest ' + test_file
        os.system(command)
        return 0

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

    conftest_file = """
# -*- coding:utf-8 -*-

import pytest
from Andrew.Common.LogUtil import log


@pytest.fixture(autouse=True)
def start():
    log.info('[🎈] ------------------------ Test Start ------------------------')
    yield
    log.info('[🎈] ------------------------ Test End ------------------------')

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport():
    '''
    获取每个用例状态的钩子函数
    :return:
    '''
    # 获取钩子方法的调用结果
    out = yield
    # 从钩子方法的调用结果中获取测试报告
    result = out.get_result()
    log.info(('测试步骤: %s' % result.when))
    log.info(('测试结果: %s' % result.outcome))
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

    # 创建项目骨架
    create_folder(project_name)
    create_folder(os.path.join(project_name, "Log"))
    log_dir = os.getcwd() + os.sep + project_name + os.sep + "Log"
    create_folder(os.path.join(project_name, "TestCase"))
    create_file(os.path.join(project_name, "TestCase", "__init__.py"))
    create_file(os.path.join(project_name, "TestCase", "test_request.py"), testcase_file)
    create_folder(os.path.join(project_name, "TestData"))
    testdata_dir = os.getcwd() + os.sep + project_name + os.sep + "TestData"
    create_file(os.path.join(project_name, "TestData", "data.yaml"), testdata_file)
    create_file(os.path.join(project_name, "conftest.py"), conftest_file)
    ini._set("Log", "log_path", log_dir)
    ini._set("TestData", "testdata_path", testdata_dir)
    return 0