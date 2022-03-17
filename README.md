# Andrew

#### 项目介绍

接口测试自动化框架，使用POM设计模式对业务逻辑、测试方法等进行分离封装
- [x] 数据驱动
- [x] 关键字驱动
- [x] 全局配置文件封装
- [x] 日志监控
- [x] selenium、requests的二次封装
- [x] 断言
- [x] 报告

#### 项目结构

```
Andrew -- 父工程
├── common -- 通用模块
├── logs -- 日志模块
├── testcase -- 用例模块
└── report -- 报告模块
```

#### 技术选型

| 技术                 | 说明                                                         
| -------------------- | ---------------------------
| Python               | 编程语言     
| Requests             | 接口的http内置库
| Pytest               | 单元测试框架
| Loguru               | 日志框架

#### 开发工具

Visual Studio Code - 代码编辑器

### 备注

* 接口自动化测试框架
* pip install -r requirements.txt - 一次性安装所有需求的三方库

### 开发进度

- [x] 封装日志的方法
- [x] 封装读取配置文件的方法
- [ ] 封装request的方法