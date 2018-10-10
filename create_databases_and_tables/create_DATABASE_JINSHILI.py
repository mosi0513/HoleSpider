
###### 1. unix开启sql服务  ######
# 在客户端启动mysql服务,输入命令
#  sudo mysql.server start
#  启动会报错
#  mysql.server start 还是会报错
# sudo mysql 可以进入



##### linux进入mysql#######
# mysql -uroot -p


import pymysql
db = pymysql.connect(host='localhost', user='root', password='1991513', port=3306)
cursor = db.cursor()
cursor.execute("CREATE DATABASE JINSHILI DEFAULT CHARACTER SET UTF8MB4")
db.close()
print('金时利数据库创建成功，数据库名为JINSHILI')
