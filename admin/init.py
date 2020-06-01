from tornado.web import RequestHandler
import json
class MainController(RequestHandler):
    def toJson(self,code,msg=None,content=None):
        d=dict()
        d["code"]=str(code)
        d["msg"]=msg
        d["data"]=content
        self.write(json.dumps(d,ensure_ascii=False))
        # 用于将数据进行json序列号