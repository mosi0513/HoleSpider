from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Login():

        def __init__(self):
            self.url = '*******************'
            self.username = '*************'
            self.password = '*************'
            self.browser = webdriver.Chrome()
            self.wait = WebDriverWait(self.browser, 10)


        def login(self):
            self.browser.maximize_window()# 浏览器窗口全屏
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


login = Login()
login.login()
