

import requests
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from lxml import etree
import random
from db import MysqlClient




#  填写类
class HotCuteInput():

    def __init__(self):
        self.url = 'http://xxxx.xxxxx.xxxxx'# 后台网址
        self.username = 'a*******'
        self.password = 'a*******'# 后台账号密码

        # 有界面浏览器
        # self.browser = webdriver.Chrome()
        # self.wait = WebDriverWait(self.browser, 10)

        # 无界面浏览器
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--headless')
        self.browser = webdriver.Chrome(chrome_options=self.chrome_options)
        self.wait = WebDriverWait(self.browser, 10)



    #  登入
    def login(self):


        self.browser.set_window_size(1300,1000)#注意: 浏览器的窗口需要根据实际情况进行调试， 窗口要调试到能看到提交两个字
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
        self.add_detail_infos()



    #  标题 → 封面图片 → 优势 → 放款时间 → 借款额度 → 月利率 → 申请人数 →
    #  额度筛选（faction）→ 借款分类筛选(faction) →  文章内容链接 → 产品内容 → 点击提交 → 点击确定
    def add_detail_infos(self):
        conn = MysqlClient()
        results = conn.random()

        nums = 0
        for result in results:
            response = requests.get(result[2])
            if response.status_code == 200:
                with open('1'+'.'+'jpg','wb') as f:
                    print('下载封面图片%s'%result[2])
                    f.write(response.content)


            self.fill_infos(result)
            nums +=1
            print('*'*50)
            print('*'*50)
            print('添加热门口子%s'%nums)
            print('*'*50)
            print('*'*50)




    #  填写详细信息
    def fill_infos(self, result):
        #self.browser.current_window_handle  #定位到当前页面
        self.browser.implicitly_wait(10)
        click_infos = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#main-container > div.header > div.nav.fl > ul > li:nth-child(2) > a')))
        click_infos.click()
        click_homepage = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#main-container > div.main > div.sidebar2 > ul > li:nth-child(32) > a')))
        click_homepage.click()
        click_addinfos = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#main-container > div.main > div.content_box > a:nth-child(3)')))
        click_addinfos.click()

        title = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#tiqutitle')))
        title.send_keys(str(result[1]))
        print('标题:%s'%str(result[1]))


        cover = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#upload-image')))
        cover.send_keys('C:/Users/jsl/Desktop/JSL/1.jpg') # 根据个人电脑文件夹名称修改路径
        print('添加封面图片')


        advantage = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#formrec > div:nth-child(21) > div > input')))
        advantage.send_keys(str(result[4]))
        print('优势信息:%s'%str(result[4]))


        sendtime = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#formrec > div:nth-child(22) > div > input')))
        sendtime.send_keys(str(result[10]))
        print('放款时间:%s'%str(result[10]))



        limit = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#formrec > div:nth-child(23) > div > input')))
        limit.send_keys(str(result[5]))
        print('借款额度:%s'%str(result[5]))


        rate = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#formrec > div:nth-child(24) > div > input')))
        rate.send_keys(str(result[7]))
        print('月利率:%s'%str(result[7]))


        peoples = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#formrec > div:nth-child(25) > div > input')))
        peoples.send_keys(random.randint(100,13670))# random.randint(10000,250000)添加随机人数
        print('申请人数:%s'%random.randint(100,10456))

        connect_url = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#formrec > div:nth-child(28) > div > input')))
        connect_url.send_keys(str(result[0]))
        print('文章连接:%s'%str(result[0]))


        content = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#ueditor_1')))
        content.click()
        content.send_keys('ddd')
        print('产品内容添加ddd')


        submit = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#formrec > div:nth-child(31) > div > button')))
        submit.click()
        print('提交成功')


        determine = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#layui-layer1 > div.layui-layer-btn.layui-layer-btn- > a')))
        determine.click()
        print('确定提交')
        print('进行分类操作...')  
        time.sleep(1)
        self.classification()



        #  分类操作
    def classification(self):
        self.browser.implicitly_wait(10)
        #  点击首页
        hmpage = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#main-container > div.main > div.sidebar2 > ul > li:nth-child(32) > a')))
        hmpage.click()
       # print('进入口子首页')

        #  勾选刚刚添加的口子
        addcuted = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#article_list > tr:nth-child(1) > td:nth-child(1) > div')))
        addcuted.click()
        #print('勾选添加的新口子')

        #  点击选择分类
        click_type = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#formrec > div:nth-child(1) > div > div > input')))
        click_type.click()
      #  print('点击分类')


        #  选择口子类型
        choice_cute = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#formrec > div:nth-child(1) > div > dl > dd:nth-child(31)')))
        choice_cute.click()
        print('添加到:热门口子')

        #  点击批量移动
        movie = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#formrec > div:nth-child(2) > a')))
        movie.click()
       # print('点击批量移动')

        #  点击确定
        sure = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#layui-layer1 > div.layui-layer-btn.layui-layer-btn- > a')))
        sure.click()
       # print('点击确定')


        time.sleep(1)


    #  关闭浏览器，退出程序
    def close(self):
        self.browser.close()






# # 填入数据       
# newcute = HotCuteInput()
# newcute.login()
# newcute.close()










