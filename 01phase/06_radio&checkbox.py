
#coding:utf-8
from selenium import webdriver
import time

'''
radio:单选框
    找到元素直接点击
checkbox:复选框
    找到元素直接点击
    全部勾选：
        1.xpath：找到元素组 .//*[@type='checkbox']
        2.遍历list，取出复选框，查看状态，false的勾选即可
    
状态：
    is_selected(): 选中->True 未选中->False
'''

driver = webdriver.Chrome("../drivers/chromedriver.exe")

driver.implicitly_wait(20)