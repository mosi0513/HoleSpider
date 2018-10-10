import pymysql
db = pymysql.connect(host='localhost', user='root', password='1991513', port=3306, db='JINSHILI')
cursor=db.cursor()
sql = """CREATE TABLE NEWINFO(
TITLE VARCHAR(256) DEFAULT NULL,
CUST1 VARCHAR(256) DEFAULT NULL,
CUST2 VARCHAR(256) DEFAULT NULL,
CUST3 VARCHAR(256) DEFAULT NULL,
CUST4 VARCHAR(256) DEFAULT NULL,
CUST5 VARCHAR(256) DEFAULT NULL,
CUST6 VARCHAR(256) DEFAULT NULL,
CUST7 VARCHAR(256) DEFAULT NULL,
CUST8 VARCHAR(256) DEFAULT NULL,
CUST9 VARCHAR(256) DEFAULT NULL,
CUST10 VARCHAR(256) DEFAULT NULL,
CREATE_DATE VARCHAR(256) DEFAULT NULL,
UPDATE_DATE VARCHAR(256) DEFAULT NULL
)"""

cursor.execute(sql)
db.close()
print('创建表成功,表名为NEWINFO')



#  sql数据库的基本操作
#  查询所有的数据库名 show databases;
#  进入某个数据库  use 数据库名
#  查看数据库里面的表名 show tables;
#  查看表中的内容 select * from 表名
#  删除一个表 DROP TABLE 表名;
