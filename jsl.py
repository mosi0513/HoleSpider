import requests
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import requests
import json
from lxml import etree
import random
import pymysql
from PIL import Image
import os


#  mysql配置信息
HOST = 'localhost'
MSQLPORT = 3306
MSQLUSER = 'root'
MSQLPASSWORD = '******'
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






# 定义一个输入的类

class Input():

    def __init__(self, cute):
        self.cute = cute

        self.url = '*******************'
        self.username = '*******'
        self.password = '*******'
        # self.browser = webdriver.Chrome()
        # self.wait = WebDriverWait(self.browser, 10)

            #    无界面浏览器
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--headless')
        self.browser = webdriver.Chrome(chrome_options=self.chrome_options)
        self.wait = WebDriverWait(self.browser, 10)






    #  登入
    def login(self):
        self.browser.set_window_size(1300,1000)
        # self.browser.maximize_window()# 浏览器窗口全屏， 否则容易出错
        self.browser.get(self.url)
        input_username = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#username')))
        input_username.send_keys(self.username)
        input_password = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#password')))
        input_password.send_keys(self.password)
        print('正在登陆到主页面...')
        login_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#doLogin > button')))
        login_button.click()
        print('登陆成功，等待页面加载...')
        self.browser.implicitly_wait(10)
        self.login_detail_page()



    # 点击内容管理 → 口子首页 → 添加内容
    def login_detail_page(self):

        #self.browser.current_window_handle  #定位到当前页面
        print('页面加载中，请稍等...')
        print('正在进入内容管理页面...')
        click_infos = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#main-container > div.header > div.nav.fl > ul > li:nth-child(2) > a')))
        click_infos.click()
        print('正在进入文章首页...')
        click_homepage = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#main-container > div.main > div.sidebar2 > ul > li:nth-child(37) > a')))
        click_homepage.click()
        print('正在进入详细内容添加页面...')
        click_addinfos = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#main-container > div.main > div.content_box > a:nth-child(3)')))
        click_addinfos.click()
        self.add_detail_infos()



    #  标题 → 封面图片 → 预发时间 → 副标题（浏览人数） → 文章内容
    def add_detail_infos(self):
        response = requests.get(self.cute)
        html = etree.HTML(response.text)
        link_url = html.xpath('//*/tr/th/a[2]/@href')

        for url in link_url:
            surl = 'https://www.kashen.com/' + url
        #    print(url)
            #  请求详细页
            res = requests.get(surl)
            html = etree.HTML(res.text)
            titles = html.xpath('//*[@id="thread_subject"]/text()') #标题
        #    print(title)
            infos= html.xpath('//*[@class="t_f"]')# 整个内容节点
            infoslist = infos[0].xpath('*//text()')# 内容列表
            iamgelist = infos[0].xpath('*//div[1]/p[2]/a[1]/@href')# 图片列表浏览器
            data1 = '申请图片：'
            data2 = '卡神网解析：'

            """
            这里做一个数据库查询

            1. 如果标题不存在，则将数据库插入到数据库，同时添加到金时利后台
            2. 如果存在，则提示无更新，且关闭浏览器

            """
            title = {'TITLE':titles[0]}
            xxxx = str(title.get('TITLE'))
            table = 'NEWINFO'
            conn = MysqlClient()
            if conn.query_title(table, xxxx):
                print('此数据已存在, 无需更新，正在判断下一条')






            else:
                print('数据不存在，正在插入数据')
                conn.insert(table, title)
                if iamgelist[0] and data1 in infoslist and  data2 in infoslist:#  如果图片为真， 和申请图片：与卡神网解析的字样存在

                    iamge = 'https://www.kashen.com/'  + iamgelist[0]#  图片url 可进行清洗
                    response = requests.get(iamge)
                    if response.status_code == 200:
                        with open('1' + '.' + 'jpg', 'wb') as f:
                            print('下载图片%s' % iamge)
                            f.write(response.content)

                            #  压缩图片
                            im= Image.open('1.jpg').convert('RGB')
                            w,h = im.size
                            print(w,h)
                            gim = im.resize((w//5,h//5),Image.ANTIALIAS)#  原有尺寸，除以6倍
                            gim.save('2.jpg')


                            time.sleep(2)
                            imgd = Image.open('2.jpg')



                            print(imgd.size[0])# 获取宽度尺寸
                            ints = int(imgd.size[0])


                            img2=imgd.crop((0,0,ints,ints))
                            img2.save("3.jpg")



                    #  清洗规则， 有图片的则根据图片  申请图片：   卡神网解析： 查找，根据内容进行解析删掉申请图片 和卡神网解析等字样


                        titles =self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#tiqutitle')))
                        titles.clear()
                        titles.send_keys(xxxx)
                        print('添加标题***%s***成功'%xxxx)

                        #  添加封面图片
                        cover = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#upload-image')))
                        #cover.clear()
                        cover.send_keys('C:/Users/jsl/Desktop/JSL/3.jpg') #  此处需要修改路径
                        print('封面图片添加成功')

                        sub_title = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#formrec > div:nth-child(21) > div > input')))
                        sub_title.click()
                        sub_title.clear()
                        sub_title.send_keys(random.randint(100,15000))
                        print('添加阅读数量***%s***成功'%random.randint(100,15000))

                        content = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#ueditor_1')))
                        content.click()
                        #content.clear()浏览器
                        #content.click()

                        print('添加详细内容')
                        nums = infoslist.index(data1)
                        newinfos = infoslist[0:nums]

                        for info in newinfos:# 遍历输入内容


                            if info == '卡神网解析：':
                                continue

                            content.send_keys(info)
                            print(info)

                        submit = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#formrec > div:nth-child(26) > div > button')))
                        submit.click()
                        print('提交成功')
                        determine = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#layui-layer1 > div.layui-layer-btn.layui-layer-btn- > a')))
                        determine.click()
                        print('准备下一条数据输入')
                    else:
                        print('不满足筛选条件，跳过')


    def close(self):
        self.browser.close()



