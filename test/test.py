from flask import Flask, current_app, request

app = Flask(__name__)

# 应用上下文 对象 Flask
# 请求上下文 对象 Request
# Flask AppContext
# Request RequestContext
# 离线应用 单元测试
# ctx = app.app_context()
# ctx.push()
# a = current_app
# d = current_app.config['DEBUG']
# ctx.pop()

with app.app_context():
    a = current_app
    d = current_app.config['DEBUG']

class MyResource:
    def __enter__(self):
        print('connect to resource')
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if tb:
            print('process exception')
        else:
            print('no exception')
        print('close resource connection')
        # 如果返回False 外部Try except可以捕捉到错误信息  反之 不可以捕捉到 
        # 不写返回值 默认为False
        return True

    def query(self):
        print('query data')

try:
    with MyResource() as resource:
        1/0
        resource.query()
except Exception as ex:
    pass