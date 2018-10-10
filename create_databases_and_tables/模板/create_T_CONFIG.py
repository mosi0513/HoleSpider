
import pymysql


db = pymysql.connect(host="localhost", user="root", password='1991513', port=3306, db='T_STUFF',charset='utf8')
cursor=db.cursor()
#cursor.execute("DROP TABLE IF EXISTS T_CONFIG")

sql = """CREATE TABLE T_CONFIG (
NAME varchar(256) DEFAULT NULL,
STARTPRICE varchar(256) DEFAULT NULL,
ENDPRICE varchar(256) DEFAULT NULL,
ADDRESS varchar(256) DEFAULT NULL,
MSGCOUNT varchar(256) DEFAULT NULL,
STATUS varchar(256) DEFAULT NULL,
DISKPATH varchar(256) DEFAULT NULL,
INTERVALTIME varchar(256) DEFAULT NULL,
STUFFCOUNT varchar(256) DEFAULT NULL,
CUST1 varchar(256) DEFAULT NULL,
CUST2 varchar(256) DEFAULT NULL,
CUST3 varchar(256) DEFAULT NULL,
CUST4 varchar(256) DEFAULT NULL,
CUST5 varchar(256) DEFAULT NULL,
CUST6 varchar(256) DEFAULT NULL,
CUST7 varchar(256) DEFAULT NULL,
CUST8 varchar(256) DEFAULT NULL,
CUST9 varchar(256) DEFAULT NULL,
CUST10 varchar(256) DEFAULT NULL,
ID varchar(64) NOT NULL,
CREATE_BY varchar(64) DEFAULT NULL,
CREATE_DATE DATE DEFAULT NULL,
UPDATE_BY varchar(64) DEFAULT NULL,
UPDATE_DATE DATE DEFAULT NULL,
REMARKS Nvarchar(255) DEFAULT NULL,
DEL_FLAG varchar(64) DEFAULT NULL,
CONSTRAINT PK_T_CONFIG_ID PRIMARY KEY(ID)
)"""

cursor.execute(sql)
db.close()
print('创建数据库成功')


#  sql数据库的基本操作
#  查询所有的数据库名 show databases;
#  进入某个数据库  use 数据库名
#  查看数据库里面的表名 show tables;
#  查看表中的内容 select * from 表名
#  删除一个表 DROP TABLE 表名;
