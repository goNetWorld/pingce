from controller.init import *
from model.init import *
import time
import tornado.web
from configure.session import Session
class LoginHandler(MainController):
    def get(self, *args, **kwargs):
        self.render("login.html")
    def post(self, *args, **kwargs):
        account=self.get_argument("id",None)
        pwd=self.get_argument("password",None)
        method=self.get_argument("loginMethod","0")
        if method=="0":
            if (account and pwd):
                m = MainModel()
                sql = '''select * from user where account=%s and pwd=%s;'''
                r = m.fetchOneData(sql,(account,pwd,))
                print(sql,(account, pwd))
                print(r)
                if r:
                    # 普通用户登录
                    sess = Session(self)
                    sess["userInfo"] = r
                    self.redirect("/index")
                    return
        else:
            # 尝试是不是管理员
            m = MainModel()
            sql = '''select * from manage where account=%s and pwd=%s;'''
            r = m.fetchOneData(sql,(account, pwd,))
            if r:
                # 如果是管理员登录则返回2
                sess = Session(self)
                sess["adminInfo"] = r
                self.redirect("/admin/index")
                return
        self.redirect("/login")

class RegisterHandler(MainController):
    def get(self, *args, **kwargs):
        self.render("login.html")
    def post(self, *args, **kwargs):
        account=self.get_argument("id")
        pwd=self.get_argument("password")
        name=self.get_argument("name")
        phone=self.get_argument("phone")
        idCode=self.get_argument("identification")
        department=self.get_argument("department")
        try:
            if(len(idCode)!=18):
                self.toJson(1, "未正确填写身份证!")
                return
            idCode=int(idCode)
        except Exception as e:
            print(e)
            self.toJson(1, "未正确填写身份证!")
            return
        idCode=str(idCode)
        sex="男"
        if int(idCode[17])/2==0:
            sex="女"
        age=(time.localtime().tm_year)-(int(idCode[6:10]))
        sql='''insert into user(account,pwd,name,age,sex,phone,department,idCode,createTime)
                value(%s,%s,%s,%s,%s,%s,%s,%s,%s);'''
        data=(
            account,
            pwd,
            name,
            age,
            sex,
            phone,
            department,
            idCode,
            int(time.time()),
        )
        m=MainModel()
        r=m.insertData(sql,data)
        if r:
            sess=Session(self)
            sess["userInfo"]=r
            self.toJson(0,"注册成功!")
            return
        self.toJson(1,"登录失败,请重试!")

class AlterPasswordHandler(MainController):
    def get(self, *args, **kwargs):
        pass
    def post(self, *args, **kwargs):
        old=self.get_argument("old",'0')
        new=self.get_argument("new","0")
        sess = Session(self)
        uid=sess['userInfo'][0]
        if (new and old):
            m = MainModel()
            sql = '''select * from user where id=%s and pwd=%s;'''
            r = m.fetchOneData(sql,(uid,old,))
            if r:
                sql = '''update user set pwd=%s where id=%s and pwd=%s;'''
                d = m.fetchOneData(sql, (new,uid, old,))
                # 普通用户登录
                if d:
                    self.toJson("0", "修改密码成功,请牢记新密码!")
                    return
        self.toJson("1","修改密码失败,请重新输入!")
class ForgetCode(MainController):
    def get(self, *args, **kwargs):
        pass
    def post(self, *args, **kwargs):
        pass