import pymysql
class MainModel(object):
    # 数据库密码为sjkmm123
    def __init__(self):
        self.conn=pymysql.Connection(host='127.0.0.1', database='teachSystem', user='root', password='sjkmm123',charset='utf8')
        self.cursor = self.conn.cursor()
    def fetchOneData(self,sql,data):
        try:
            self.cursor.execute(sql,data)
            self.conn.commit()
            result=self.cursor.fetchone()
            return result
        except Exception as e:
            print(e)
            return False
    def fetchMultyData(self,sql,data):
        try:
            self.cursor.execute(sql,data)
            result = self.cursor.fetchall()
            self.conn.commit()
            return result
        except Exception as e:
            print(e)
            return False
    def insertData(self,sql,data):
        try:
            self.cursor.execute(sql,data)
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False
    def __delete__(self, instance):
        self.cursor.close()
        self.conn.close()