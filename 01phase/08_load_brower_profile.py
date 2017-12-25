#coding:utf-8
from selenium import webdriver
import time
#
# '''
# Firefox:
#     # 字符串前面加“r”不会被转义
#
#     #配置文件地址
#     profile_directory = r"C:\Users\YC\AppData\Roaming\Mozilla\Firefox\Profiles\xy1eiozs.default"
#
#     #配置文件
#     profile = webdriver.FirefoxProfile(profile_directory)
#
#     #加载配置文件
#     driver = webdriver.Firefox(profile)
#
# chrome:
#     option  = webdriver.ChromeOptions()
#      option.add_argument('--user-data-dir=C:\Users\YC\AppData\Local\Google\Chrome\User Data')
#     driver = webdriver.Chrome(chrome_options=option)
# '''

option  = webdriver.ChromeOptions()
option.add_argument('--user-agent = iphone 6 Plus')
driver = webdriver.Chrome('../drivers/chromedriver.exe',0,chrome_options=option)

driver.get("http://wwww.taobao.com/")