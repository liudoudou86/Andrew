# Andrew

#### 项目介绍

接口测试自动化框架，使用POM设计模式基于schema规约接口自动化框架

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
| Jsonschema           | 预计schema规约断言工具
| Pytest               | 测试框架
| Allure               | 测试报告
| PyMysql              | 数据库处理工具
| PyYaml               | yaml文件处理工具
| Web服务              | Flask
| 部署方式              | Jenkins

### 备忘录

* pip install -r requirements.txt
* python setup.py bdist_wheel
* 打包当前只能使用：python setup.py install安装，.whl文件暂时不能使用，需要研究

### 项目开发进度管理

  - [x] 日志工具类封装
  - [x] 读取配置文件
  - [x] 请求工具类封装
  - [x] 断言工具类封装
  - [x] json解析工具类封装
  - [x] 第一次联调完成
  - [x] 读取数据库
  - [x] 读取ymal文件
  - [x] pytset结合yaml做数据驱动
  - [x] 第二次联调完成
  - [x] 读取json文件
  - [x] 扩展在线postman简版
  - [x] 脚手架
  - [x] 工程打包
  - [ ] 读取sql脚本
  - [ ] schema规约高级断言
  - [ ] docs文件产出