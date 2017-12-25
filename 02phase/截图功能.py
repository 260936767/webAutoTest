#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/30 17:26
# @Author  : yc
# @Site    : 
# @File    : 截图功能.py
# @Software: PyCharm

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

# 截图功能 使用装饰器功能
class Screen(object):

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


class test_baidu(unittest.TestCase):
    chrome_path = r"E:/studyMenu/PycharmProjects/webAutoTest/drivers/chromedriver.exe"
    driver = webdriver.Chrome(chrome_path)

    def setUp(self):
        self.driver.get("http://www.baidu.com/")

    @Screen(driver)
    def test_01(self):
        self.driver.find_element(By.XPATH,"asdasd")


if __name__=='__main__':
    unittest.main()