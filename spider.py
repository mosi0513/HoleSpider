import requests
from lxml import etree
from multiprocessing.pool import Pool
import pymysql
import time







#  mysql配置信息
HOST = 'localhost'
MSQLPORT = 3306
MSQLUSER = 'root'
MSQLPASSWORD = '******'
DB = 'JINSHILI'# 数据库名



class MysqlClient():
    #定义初始化信息
    def __init__(self, host=HOST, port=MSQLPORT, user=MSQLUSER, password=MSQLPASSWORD, db=DB):

        self.db = pymysql.connect(host=host, user=user, password=password, port=port, db=db, charset='utf8')
        self.cursor = self.db.cursor()


    #  查询标题是否存在
    def query_name(self,table, name):
        sql = "select * from %s where NAME='%s'"%(table, name)
        if self.cursor.execute(sql):
            return True
        else:
            return False


    #  插入数据
    def insert(self,table, data):
        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table,keys=keys,values=values)
        if self.cursor.execute(sql, tuple(data.values())):
            self.db.commit()
            print('标题添加到数据库成功')
        else:
            print('标题添加到数据库失败')







class Spider():

    def parse(self,page):
        url = 'http://dk.zhongxinwanka.com/product/show-' + str(page) + '.html'
        response = requests.get(url)
        if response.status_code == 200:
            html = etree.HTML(response.text)
            name = html.xpath('/html/body/div[1]/dl/dd[1]/p[1]/text()')# app名
            img = html.xpath('/html/body/div[1]/dl/dt/img/@src')# 图片
            secc = html.xpath('/html/body/div[1]/dl/dd[1]/p[2]/i/text()')#成功率
            title = html.xpath('/html/body/div[1]/dl/dd[1]/p[3]/text()')#标题
            price = html.xpath('/html/body/div[3]/ul/li[1]/p/text()')# 额度
            limit = html.xpath('/html/body/div[3]/ul/li[2]/p/text()')#期限
            fy = html.xpath('/html/body/div[3]/ul/li[3]/p/text()')# 月利率
            time = html.xpath('/html/body/div[3]/ul/li[4]/p/text()')# 放款时间
            method = html.xpath('/html/body/div[3]/ul/li[5]/p/text()')# 审核方式
            dz = html.xpath('/html/body/div[3]/ul/li[6]/p/text()')# 到帐方式
            if name and img and secc and title and price and limit and fy and method and dz:
                infos = {
                    'URL':str(url),
                    'NAME' : str(name[0]),
                    'IMG':str(img[0]),
                    'SECC':str(secc[0]),
                    'TITLE':str(title[0]),
                    'PRICE':str(price[0]),
                    'LIM':str(limit[0]),
                    'FY':str(fy[0]),
                    'TIMESS':str(time[0]),
                    'METHOD':str(method[0]),
                    'DZ':str(dz[0])

                }

                table = 'APPS'
                conn = MysqlClient()

                if conn.query_name(table, infos.get('NAME')):
                    print('数据已存在数据库')
                else:

                    conn.insert(table, infos)

                print(infos)
        else:
            print('状态码不合法')


    def main(self):
        for x in range(1,736):
            self.parse(x)
          #  time.sleep(1)


#    多线程抓取， 容易封ip 
#    def run(self):
    #    pool = Pool()
    #    groups = ([x*1 for x in range(1,736)])
    #    pool.map(self.main,groups)
    #    pool.close()
    #    pool.join




spider = Spider()
spider.main()
