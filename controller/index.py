from controller.init import *
from model.init import *
class IndexHandler(MainController):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        m = MainModel()
        # 这个状态应该是改变的,而不是0
        sql = 'select name,sex,phone,department from user where id=%s order by id desc limit 1;'
        data = (10,)
        result = m.fetchOneData(sql, data)
        if result:
            item=[
                    self.getTableOne(),
                    self.getTableTwo(),
                    self.getTableThree()
                  ]
            minLen=0
            self.render("index.html",result=result,item=item,minLen=minLen)
            return
        self.redirect("/login")

    # @tornado.web.authenticated
    def post(self, *args, **kwargs):
        print(self.get_argument("account","none"))
        print(self.get_argument("pwd","none"))
        # pass
    def getTableOne(self):
        sess = Session(self)
        # 暂时使用0状态,到时候改
        m = MainModel()
        sql = 'select id,status from teachwork where userId=%s and status=0 order by id desc;'
        # data=(sess['userInfo'][0],)
        data = (10,)
        result = m.fetchOneData(sql, data)
        return result
    def getTableTwo(self):
        sess = Session(self)
        # 暂时使用0状态,到时候改
        m = MainModel()
        sql='select id,status from scientistlevel where userId=%s and status=0 order by id desc'
        data=(10,)
        result = m.fetchOneData(sql, data)
        return result
    def getTableThree(self):
        m = MainModel()
        # 暂时使用0状态,到时候改
        sql = 'select id,status from moreDetail where userId=%s and status='' order by id desc limit 1'
        # data=(sess['userInfo'][0],)
        data = (10,)
        result = m.fetchOneData(sql, data)
        return result
