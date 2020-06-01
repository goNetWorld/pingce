from controller.init import *
from model.init import *
class AlterTableOne(MainController):
    # @tornado.web.authenticated
    def get(self, *args, **kwargs):
        sess = Session(self)
        m = MainModel()
        sql='select education,moral,workload,reward,research from teachwork where userId=%s and status=0 order by id desc limit 1'
        # data=(sess['userInfo'][0],)
        data=(10,)
        result = m.fetchOneData(sql, data)
        if result:
            edu=json.loads(result[0])
            moral=json.loads(result[1])
            workload=json.loads(result[2])
            reward=json.loads(result[3])
            research=json.loads(result[4])
            self.render("alterTable1.html",edu=edu,moral=moral,workload=workload,reward=reward,research=research)
            return
        self.redirect("/index")
    # @tornado.web.authenticated
    def post(self, *args, **kwargs):
        education = self.get_argument("education", None)
        moral = self.get_argument("moral", None)
        workload = self.get_argument("workload", None)
        reward = self.get_argument("reward", None)
        research = self.get_argument("research", None)
        sql = """update teachwork set education=%s,moral=%s,workload=%s,reward=%s,research=%s where id=%s and userId=%s;;"""
        sess = Session(self)
        data = (
            # sess["userInfo"][0],
            education,
            moral,
            workload,
            reward,
            research,
            1,
            10,  # 表明是新插入的数据
        )
        m = MainModel()
        result = m.insertData(sql, data)
        if (result):
            self.toJson(0, "数据保存成功!")
        else:
            self.toJson(1, "请重试!")

class AlterTableTwo(MainController):
    # @tornado.web.authenticated
    def get(self, *args, **kwargs):
        sess = Session(self)
        m = MainModel()
        sql='select setProject,conclude,result,artistic,transform,other from scientistlevel where userId=%s and status=0 order by id desc limit 1'
        # data=(sess['userInfo'][0],)
        data=(10,)
        result = m.fetchOneData(sql, data)
        if result:
            setProject=json.loads(result[0])
            conclude=json.loads(result[1])
            results=json.loads(result[2])
            artistic=json.loads(result[3])
            transform=json.loads(result[4])
            other=json.loads(result[5])
            self.render("alterTable2.html",setProject=setProject,conclude=conclude,results=results,artistic=artistic,transform=transform,other=other)
            return
        self.redirect("/index")
    # @tornado.web.authenticated
    def post(self, *args, **kwargs):
        setProject=self.get_argument("setProject",'')
        conclude=self.get_argument("conclude",'')
        result=self.get_argument("result",'')
        artistic=self.get_argument("artistic",'')
        transform=self.get_argument("transform",'')
        other=self.get_argument("other",'')
        sql="""update scientistlevel set setProject=%s,conclude=%s,result=%s,artistic=%s,transform=%s,other=%s where id=%s and userId=%s;;"""
        sess=Session(self)
        data=(
            setProject,
            conclude,
            result,
            artistic,
            transform,
            other,
            # sess["userInfo"][0],
            5,
            10,
            )
        m=MainModel()
        result=m.insertData(sql,data)
        if(result):
            self.toJson(0,"数据保存成功!")
        else:
            self.toJson(1, "请重试!")

class AlterTableThree(MainController):
    # @tornado.web.authenticated
    def get(self, *args, **kwargs):
        sess = Session(self)
        m = MainModel()
        sql = 'select detail from moreDetail where userId=%s and status=0 order by id desc limit 1'
        # data=(sess['userInfo'][0],)
        data = (10,)
        result = m.fetchOneData(sql, data)
        if result:
            detail = json.loads(result[0])
            self.render("alterTable3.html", detail=detail)
            return
        self.redirect("/index")
    @tornado.web.authenticated
    def post(self, *args, **kwargs):
        pass
