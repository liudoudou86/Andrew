# -*- coding:utf-8 -*-

from Andrew.Common.LogUtil import log
from Andrew.Common.RequestUtil import Requestor
from flask import Flask, render_template, request

# json转换中文不使用unicode
JSON_AS_ASCII = False

# 实例化Flask
app = Flask(__name__)
app.config.from_object(__name__)

# 配置路由
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/request', methods=['GET'])
def get_request():
    get_data = request.args.to_dict() # 获取传入的参数
    log.debug(get_data)
    METHOD = get_data.get('METHOD')
    URL = get_data.get('URL')

    Requestor.request(METHOD, URL)
    return Requestor.response

# threaded=True为开启多线程