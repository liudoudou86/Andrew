# Andrew

#### 项目介绍

接口测试自动化框架，使用POM设计模式基于schema规约接口自动化框架

#### 安装方式

```
# 需要安装python环境
> pip install Andrew-1.0.0-py3-none-any.whl
```

#### 命令说明

| 命令               | 说明                                                         
| ----------------- | ---------------------------
| -h,--help         | 查看帮助信息
| -v                | 查看框架版本号
| -api              | 执行框架脚本
| -server           | 打开拓展平台

#### 项目结构

```
Andrew -- 父工程
├── common -- 公共工具类
├── config -- 配置文件
├── database -- 读取数据库
├── log -- 日志输出
├── report -- 报告输出
├── testcase -- 测试用例
├── testdata -- 测试数据
└── run -- 框架入口
```

#### 技术选型

| 技术                 | 说明                                                         
| -------------------- | ---------------------------
| Python 3.7.9         | 编程语言
| Visual Studio Code   | 开发工具
| Loguru               | 日志框架
| Requests             | 接口请求工具
| JsonPath             | json解析工具
| PyHamcrest           | 基于java语言断言工具
| Jsonschema           | 基于schema规约断言工具
| Pytest               | 测试框架
| Allure               | 测试报告
| PyMysql              | 数据库处理工具
| PyYaml               | yaml文件处理工具
| Web服务              | Flask
| 部署方式              | Jenkins

### 项目安装&打包

* pip install -r requirements.txt
* python setup.py bdist_wheel
* uvicorn main:app --reload