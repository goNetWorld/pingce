from tornado.web import RequestHandler
import json
import tornado.web
from configure.session import *
class MainController(RequestHandler):
    def toJson(self,code,msg=None,content=None):
        d=dict()
        d["code"]=str(code)
        d["msg"]=msg
        d["data"]=content
        self.write(json.dumps(d,ensure_ascii=False))
        # 用于将数据进行json序列号
    def get_current_user(self):
        return Session(self)["userInfo"]
    # def finish(self, chunk=None):
    #     pass
        # print("设置请求头")
        # self.set_header("Access-Control-Allow-Origin", "*")
        # self.set_header("Access-Control-Allow-Headers", "x-requested-with,authorization")
        # self.set_header('Access-Control-Allow-Methods', 'POST,GET,PUT,DELETE,OPTIONS')
