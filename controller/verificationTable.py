from controller.init import *
from model.init import MainModel

class VerificationTableOne(MainController):
    # @tornado.web.authenticated
    def get(self, *args, **kwargs):
        sess = Session(self)
        m = MainModel()
        sql = 'select education,moral,workload,reward,research from teachwork where userId=%s and id=%s and status=0 order by id desc limit 1'
        # data=(sess['userInfo'][0],)
        data = (10,1)
        result = m.fetchOneData(sql, data)
        if result:
            edu = json.loads(result[0])
            moral = json.loads(result[1])
            workload = json.loads(result[2])
            reward = json.loads(result[3])
            research = json.loads(result[4])
            self.render("verificationTable1.html",edu=edu,moral=moral,workload=workload,reward=reward,research=research)
            return
        self.redirect("index")
    @tornado.web.authenticated
    def post(self, *args, **kwargs):
        pass

class VerificationTableTwo(MainController):
    # @tornado.web.authenticated
    def get(self, *args, **kwargs):
        sess = Session(self)
        m = MainModel()
        sql='select setProject,conclude,result,artistic,transform,other from scientistlevel where userId=%s and id=%s and status=0 order by id desc limit 1'
        data=(10,5)
        result = m.fetchOneData(sql, data)
        if result:
            setProject=json.loads(result[0])
            conclude=json.loads(result[1])
            results=json.loads(result[2])
            artistic=json.loads(result[3])
            transform=json.loads(result[4])
            other=json.loads(result[5])
            self.render("verificationTable2.html",setProject=setProject,conclude=conclude,results=results,artistic=artistic,transform=transform,other=other)
            return
        self.redirect("index")
    @tornado.web.authenticated
    def post(self, *args, **kwargs):
        pass

class VerificationTableThree(MainController):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render("printTable3.html")
    @tornado.web.authenticated
    def post(self, *args, **kwargs):
        pass
