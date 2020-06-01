from admin.init import *
from model.init import *
from configure.session import *
class AdminIndexHandler(MainController):
    def get(self, *args, **kwargs):
        self.render("adminIndex.html")
    def post(self, *args, **kwargs):
        pass
class ResetHandler(MainController):
    def get(self, *args, **kwargs):
        pass
    def post(self, *args, **kwargs):
        uid=self.get_argument("uid",'0')
        old=self.get_argument("old",'0')
        new=self.get_argument("new","0")
        if (new and old):
            m = MainModel()
            sql = '''select * from manage where id=%s and pwd=%s;'''
            r = m.fetchOneData(sql,(uid,old,))
            if r:
                sql = '''update manage set pwd=%s where id=%s and pwd=%s;'''
                d = m.fetchOneData(sql, (new,uid, old,))
                # 普通用户登录
                if d:
                    self.toJson("0", "修改密码成功,请牢记新密码!")
                    return
        self.toJson("1","修改密码失败,请重新输入!")