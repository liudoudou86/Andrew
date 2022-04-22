# Andrew

#### 项目介绍

接口测试自动化框架，使用POM设计模式基于schema规约接口自动化框架
* 框架开发进度管理：
  - [x] 日志工具类封装
  - [x] 读取配置文件
  - [x] 请求工具类封装
  - [x] 断言工具类封装
  - [x] json解析工具类封装
  - [x] 第一阶段联调完成
  - [x] 读取数据库
  - [x] 读取ymal文件
  - [x] pytset结合yaml做数据驱动
  - [ ] 脚手架
  - [ ] dockerfile脚本
  - [ ] jenkins脚本
  - [ ] demo文件产出
  - [ ] docs文件产出
  - [ ] schema规约高级断言

#### 项目结构

```
Andrew -- 父工程
├── common -- 公共工具类
├── config -- 配置文件
├── logs -- 日志输出
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
| Web服务               | Flask、FastAPI
| 部署方式              | Docker、Jenkins

### 备注

* 接口自动化测试框架
* pip install -r requirements.txt