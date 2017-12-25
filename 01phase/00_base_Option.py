#coding:utf-8

from selenium import webdriver
import time

path = '../drivers/chromedriver.exe'

driver = webdriver.Chrome(path)

#最大化浏览器
driver.maximize_window()

driver.get('http://www.baidu.com')

#获取页面源码
page_source = driver.page_source

# print(str(page_source))

time.sleep(2)

driver.set_window_size(560,960)

driver.get('http://www.360.cn')

#页面刷新
driver.refresh()

#返回上一页
driver.back()

time.sleep(2)
driver.maximize_window()
#切换到下一页
driver.forward()

#截屏
driver.get_screenshot_as_file('./testJPG2.jpg')

time.sleep(2)

#退出driver
driver.quit()