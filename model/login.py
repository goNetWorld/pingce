from model.init import *

class LoginModel(MainModel):
    def fetchOneData(self):
        cur = self.cursor()
        cur.execute()
        result=cur.fetchone()
        self.conn.commit()
    def fetchMultyData(self):
        cur = self.cursor()
        cur.execute()
        result=cur.fetchall()
        self.conn.commit()
        return result
    def insertData(self,sql):
        cur = self.cursor()
        cur.execute(sql)
        self.conn.commit()