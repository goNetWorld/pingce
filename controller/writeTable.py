from controller.init import *
from model.init import *
import json
class WriteTableOne(MainController):
    # @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render("writeTable1.html")
    # @tornado.web.authenticated
    def post(self, *args, **kwargs):
        education=self.get_argument("education",None)
        moral=self.get_argument("moral",None)
        workload=self.get_argument("workload",None)
        reward=self.get_argument("reward",None)
        research=self.get_argument("research",None)
        sql="""insert into teachwork(userId,education,moral,workload,reward,research,createTime,status)values(
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s);"""
        sess=Session(self)
        data=(
            # sess["userInfo"][0],
            10,
            education,
            moral,
            workload,
            reward,
            research,
            int(time.time()),
            0,      #表明是新插入的数据
            )
        m=MainModel()
        result=m.insertData(sql,data)
        if(result):
            self.toJson(0,"数据保存成功!")
        else:
            self.toJson(1, "请重试!")

class WriteTableTwo(MainController):
    # @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render("writeTable2.html")
    # @tornado.web.authenticated
    def post(self, *args, **kwargs):
        setProject=self.get_argument("setProject",'')
        conclude=self.get_argument("conclude",'')
        result=self.get_argument("result",'')
        artistic=self.get_argument("artistic",'')
        transform=self.get_argument("transform",'')
        other=self.get_argument("other",'')
        sql="""insert into scientistlevel(userId,setProject,conclude,result,artistic,transform,other,createTime,status)values(
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s);"""
        sess=Session(self)
        data=(
            # sess["userInfo"][0],
            10,
            setProject,
            conclude,
            result,
            artistic,
            transform,
            other,
            int(time.time()),
            '已填写',      #表明是新插入的数据
            )
        m=MainModel()
        result=m.insertData(sql,data)
        if(result):
            self.toJson(0,"数据保存成功!")
        else:
            self.toJson(1, "请重试!")

class WriteTableThree(MainController):
    # @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render("writeTable3.html")
    # @tornado.web.authenticated
    def post(self, *args, **kwargs):
        detail=self.get_argument("Detail",None)
        sql="""insert into moreDetail(userId,detail,createTime,status)values(
                %s,
                %s,
                %s,
                %s);"""
        if(detail):
            sess=Session(self)
            data=(
                # sess["userInfo"][0],
                10,
                detail,
                int(time.time()),
                '已填写',      #表明是新插入的数据
                )
            m=MainModel()
            result=m.insertData(sql,data)
            if(result):
                self.toJson(0,"数据保存成功!")
                return
        else:
            self.toJson(1, "请重试!")