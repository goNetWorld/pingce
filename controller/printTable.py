from controller.init import *
from model.init import *
class PrintTableOne(MainController):
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
            self.render("printTable1.html",edu=edu,moral=moral,workload=workload,reward=reward,research=research)
            return
        self.redirect("index")
    @tornado.web.authenticated
    def post(self, *args, **kwargs):
        pass

class PrintTableTwo(MainController):
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
            self.render("printTable2.html",setProject=setProject,conclude=conclude,results=results,artistic=artistic,transform=transform,other=other)
            return
        self.redirect("index")
    @tornado.web.authenticated
    def post(self, *args, **kwargs):
        pass

class PrintTableThree(MainController):
    # @tornado.web.authenticated
    def get(self, *args, **kwargs):
        tableOne=self.getTableOne()
        tableTwo=self.getTableTwo()
        tableThree=self.getTableThree()
        userInfo=self.getUserInformation()
        print(tableOne)
        print(tableTwo)
        print(tableThree)
        print(userInfo)
        self.render("printTable3.html",tableOne=tableOne,tableTwo=tableTwo,tableThree=tableThree,userInfo=userInfo)
    @tornado.web.authenticated
    def post(self, *args, **kwargs):
        self.redirect("index")
    def getTableOne(self):
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
            return result
    def getTableOne(self):
        sess = Session(self)
        m = MainModel()
        sql = 'select education,moral,workload,reward,research from teachwork where userId=%s and id=%s and status=0 order by id desc limit 1'
        # data=(sess['userInfo'][0],)
        data = (10,1)
        result = m.fetchOneData(sql, data)
        total=dict()
        if result:
            total['edu'] = json.loads(result[0])
            total['moral'] = json.loads(result[1])
            total['workload'] = json.loads(result[2])
            total['reward'] = json.loads(result[3])
            total['research'] = json.loads(result[4])
        return total
    def getTableTwo(self):
        sess = Session(self)
        m = MainModel()
        sql='select setProject,conclude,result,artistic,transform,other from scientistlevel where userId=%s and id=%s and status=0 order by id desc limit 1'
        data=(10,5)
        total=dict()
        result = m.fetchOneData(sql, data)
        if result:
            total['setProject']=json.loads(result[0])
            total['conclude']=json.loads(result[1])
            total['results']=json.loads(result[2])
            total['artistic']=json.loads(result[3])
            total['transform']=json.loads(result[4])
            total['other']=json.loads(result[5])
        return total
    def getTableThree(self):
        m = MainModel()
        sql = 'select detail from moreDetail where userId=%s and status=0 order by id desc limit 1'
        # data=(sess['userInfo'][0],)
        data = (10,)
        result = m.fetchOneData(sql, data)
        detail=dict()
        if result:
            detail = json.loads(result[0])
        return detail
    def getUserInformation(self):
        m = MainModel()
        # 这个状态应该是改变的,而不是0
        sql = 'select sex,name,idCode from user where id=%s order by id desc limit 1'
        # data=(sess['userInfo'][0],)
        data = (10,)
        result = m.fetchOneData(sql, data)
        total=dict()
        if result:
            total['sex']=result[0]
            total['name']=result[1]
            total['born']=result[2][6:14]
        return total
