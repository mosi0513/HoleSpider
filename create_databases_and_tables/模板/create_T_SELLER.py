import pymysql

db = pymysql.connect(host="localhost", user="root", password='1991513', port=3306, db='T_STUFF',charset='utf8')
cursor=db.cursor()
#cursor.execute("DROP TABLE IF EXISTS T_CONFIG")

sql = """
  CREATE TABLE T_SELLER(
STUFFID varchar(256) default NULL,
ADDRESS varchar(256) default NULL,
SELLERNAME varchar(256) default NULL,
SELLERICON varchar(256) default NULL,
SELLERWW varchar(256) default NULL,
SELLERSHOPURL varchar(256) default NULL,
SELLERVIP varchar(256) default NULL,
SELLERTYPE varchar(256) default NULL,
SELLERTYPEREASON varchar(256) default NULL,
CUST1 varchar(256) default NULL,
CUST2 varchar(256) default NULL,
CUST3 varchar(256) default NULL,
CUST4 varchar(256) default NULL,
CUST5 varchar(256) default NULL,
CUST6 varchar(256) default NULL,
CUST7 varchar(256) default NULL,
CUST8 varchar(256) default NULL,
CUST9 varchar(256) default NULL,
CUST10 varchar(256) default NULL,
ID varchar(64) not NULL,
CREATE_BY varchar(64) default NULL,
CREATE_DATE DATE default NULL,
UPDATE_BY varchar(64) default NULL,
UPDATE_DATE DATE default NULL,
REMARKS Nvarchar(255) default NULL,
DEL_FLAG varchar(64) default NULL,
CONSTRAINT PK_T_SELLER_ID PRIMARY KEY (ID)

)"""

#  CONSTRAINT PK_T_SELLER_ID PRIMARY KEY (ID)相当于在主键索引上又建了个二级索引。


cursor.execute(sql)
db.close()
print('Create T_seller Tbale Success ')


#  sql数据库的基本操作
#  查询所有的数据库名 show databases;
#  进入某个数据库  use 数据库名
#  查看数据库里面的表名 show tables;
#  查看表中的内容 select * from 表名
#  删除一个表 DROP TABLE 表名;
#
