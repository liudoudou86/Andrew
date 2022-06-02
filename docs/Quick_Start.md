### 安装使用

- 使用方式共分两种：
  - 通过git直接拉取框架代码进行使用
  ```
  pip install -r requirements.txt
  ```
  - 通过pip安装到windows设备进行使用
  ```
  pip install Andrew-1.0.0-py3-none-any.whl
  ```
- 框架windows命令解释
```
# 通过help查看所有命令
> api -help
# 查看框架版本
> api -v
# 在当前目录创建脚手架
> api -init [your project name]
# 在当前目录运行框架
> api -run
# 启动web服务
> api -server
```

---

### 断言解析

- 基础断言
  - json：可针对json断言状态码、响应中某个值
  ```
  [
    {
      "case" : {
        "name" : "testcase_01",
        "url" : "www.baidu.com",
        "method" : "get",
        "expected_code" : 200,
        "expected_msg" : "success"
      }
    }
  ]
  ```
  - yaml：可针对yaml断言状态码、响应中某个值
  ```
  # 用例1
  -
    case : 
      feature : 接口测试
      story : 页面展示
      title : 字符串断言
      url : www.baidu.com
      method : get
      expected_code : 200
      expected_msg : success
  ```
- 高级断言
  - schema：可针对响应中值的类型进行断言
  ```
  schema = {
    "data": [
      {
        "code": "string",
        "name": "string"
      }
    ]
  }
  ```