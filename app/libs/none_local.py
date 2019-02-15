"""
进程管理对象 Local LocalStack
被进程管理对对象 AppContext RequestContext
Flask(app) -> AppContext  request -> RequestContext
每次请求都是全新的 AppContext RequestContext
cureent_app 是全局唯一的对象 

进程隔离 与 进程安全
"""

class NoneLocal:
    def __init__(self, v):
        self.v = v
    
n = NoneLocal(1)