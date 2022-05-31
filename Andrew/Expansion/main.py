# -*- coding:utf-8 -*-

from Andrew.Common.RequestUtil import Requestor
from fastapi import FastAPI
from pydantic import BaseModel


# 实例化Flask
app = FastAPI()

class Data(BaseModel):
    methods: str = None
    url: str  = None

# 配置路由
@app.get("/")
def index():
    return {"message": "success"}

@app.post("/request")
def get_interface(data: Data):
    method = data.methods
    url = data.url
    print(method, url)
    Requestor.request(method, url)
    return Requestor.response