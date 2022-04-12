# Andrew

#### 项目介绍

接口测试自动化框架，使用POM设计模式对业务逻辑、测试方法等进行分离封装
- [x] 日志处理
- [x] 读取配置文件
- [x] request封装
- [x] 响应断言
- [] json提取

#### 项目结构

```
Andrew -- 父工程
├── common -- 通用模块
├── config -- 配置文件
├── logs -- 日志模块
├── testcase -- 用例模块
└── report -- 报告模块
```

#### 技术选型

| 技术                 | 说明                                                         
| -------------------- | ---------------------------
| Python               | 编程语言
| Visual Studio Code   | 开发工具
| Loguru               | 日志框架
| Requests             | 接口请求工具
| JsonPath             | 响应获取
| Hamcrest             | 断言工具
| Pytest               | 测试框架
| Allure               | 测试报告
| Web服务              | Flask、FastAPI
| 部署方式              | Docker、Jenkins

### 备注

* 接口自动化测试框架
* pip install -r requirements.txt - 一次性安装所有需求的三方库