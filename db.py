
import pymysql



#  mysql配置信息
HOST = 'localhost'
MSQLPORT = 3306
MSQLUSER = 'root'
MSQLPASSWORD = '*******'
DB = 'JINSHILI'# 数据库名




class MysqlClient(object):
    #定义初始化信息
    def __init__(self, host=HOST, port=MSQLPORT, user=MSQLUSER, password=MSQLPASSWORD, db=DB):

        self.db = pymysql.connect(host=host, user=user, password=password, port=port, db=db, charset='utf8')
        self.cursor = self.db.cursor()


    #  查询标题是否存在
    def query_title(self, table, title):
        sql = "select * from %s where TITLE='%s'"%(table, title)
        if self.cursor.execute(sql):
            return True
        else:
            return False


    #  插入数据
    def insert(self, table, data):
        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table,keys=keys,values=values)
        if self.cursor.execute(sql, tuple(data.values())):
            self.db.commit()
            print('标题添加到数据库成功')
        else:
            print('标题添加到数据库失败')



    #  查询 以某个字符串开头的数据
    def querysome(slef):
        sql = "select *  from APPS where IMG like '/upload/%'"


    # 删除以某个字符串开头的数据
    def delectsome(self):
        sql = "delete  from APPS where IMG like '/upload/%'"



    def querybigmoney(self):
        sql = "select * from APPS where LIM like '1%'"
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results


    #  随机抽取满足条件的数据
    def randombigmoney(self):
        sql = "select * from APPS where LIM like '1%' order by rand() limit 15"
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results





    # 随机取值， 最后一个参数调整随机数量
    def random(self):
        sql = "select * from APPS order by rand() limit 15"

        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        # for result in results:
        #     print(result)
        return results# 返回查找的随机100条列表







conn = MysqlClient()
conn.querysome()
