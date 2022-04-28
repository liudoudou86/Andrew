# -*- coding: utf-8 -*-

import argparse
import os

from Andrew import __description__, __version__


def main():
    """
    定义初始化项目命令
    :return:
    """
    # 创建解析器
    parser = argparse.ArgumentParser(description=__description__)
    # 创建命令行指令
    parser.add_argument('-v', '--version', dest='version', action='store_true', help="Show version")
    parser.add_argument('-init', help='Create a new project.')
    parser.add_argument('-run', help='Run test case.')
    # 解析参数
    args = parser.parse_args()
    # 读取版本号
    if args.version:
        print("Andrew {}".format(__version__))
        return 0
    # 创建脚手架
    project_name = args.init
    if project_name:
        create_scaffold(project_name)
        return 0
    # 运行测试用例
    test_case = args.run
    if test_case:
        command = "python3 " + test_case
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

    config_file = """
    [Tester]
    name = douer

    [Host]
    host = http://10.6.3.13:28083/api/rebate/
    token = eyJhbGciOiJIUzI1NiJ9.eyJpbnN0YW5jZUlkIjoxLCJsb2dpbk5hbWUiOiJXQU5HUlgiLCJ0ZW5hbnRJZCI6MSwiaWQiOjQ4MiwibG9naW5Tb3VyY2UiOiIxMDIwNTE3MTU5IiwianRpIjoiYzRmMTUzNmQtNzlhZC00NWUxLWFhOGYtNzAzODNiMDYxM2E0IiwibmJmIjoxNjUxMDIwNTA3LCJleHAiOjE2NTYyMDQ1MDd9.e29c4NuEAca4qY6GMcBeX1ei-tv8O8vbqntWj-iyifk

    [Log]
    level = DEBUG
    rotation = 100MB
    format = {time:YYYY-MM-DD HH:mm:ss} | {level:<8} [ {file}:{line} ] - {message}

    [Mysql]
    host = 10.6.3.13
    user = root
    port = 12000
    password = root
    db_name = dev
    """

    create_folder(project_name)
    create_folder(os.path.join(project_name, "Config"))
    create_file(os.path.join(project_name, "Config", "Config.ini"), config_file)
    create_folder(os.path.join(project_name, "TestCase"))
    create_folder(os.path.join(project_name, "TestData"))