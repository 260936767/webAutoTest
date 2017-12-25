#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/30 14:17
# @Author  : yc
# @Site    : 
# @File    : 装饰器.py
# @Software: PyCharm
import time
from selenium import webdriver
# def add(x,y):
#     return x+y
# def bbb(x,y):
#     return x-y
#
# def cc(fuc,x,y):
#     return fuc(x,y)
#
# #fuc 为一个函数作为参数
#
# print(cc(add,7,3))
# print(cc(bbb,7,3))

#万能参数装饰器

# def test_result(function):
#     # 内部方法
#     def inner(*args,**kwargs):
#         try:
#             function(*args,*kwargs)
#             print("程序正常")
#         except:
#             print("程序异常")
#         return function(*args,*kwargs)
#
#     return inner
#
#
# @test_result #调用上面的装饰器
# def aaaa(a,b):
#     return a + b
#
# print(aaaa(1,4))
#
# print(aaaa(34.23,232,456))  # TypeError: aaaa() takes 2 positional arguments but 3 were given


global driver

class A(object):
    def __init__(self,driver):
        self.driver = driver

    def __call__(self, function):

        def inner(*args):
            try:
                return function(*args)
            except:
                nowTime = time.strftime("%Y-%m-%d_%H_%M_%S")
                self.driver.get_screenshot_as_file("%s.jpg" %nowTime)
                raise
        return inner


class B(object):

    chrome_path = r"E:/studyMenu/PycharmProjects/webAutoTest/drivers/chromedriver.exe"
    driver = webdriver.Chrome(chrome_path)

    @A(driver)
    def yyyy(driver):
        print(driver)

if __name__== '__main__':
    b = B
    b.yyyy(b.driver)
