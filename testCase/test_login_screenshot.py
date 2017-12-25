#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/12 22:20
# @Author  : yc
# @Site    : 
# @File    : test_login.py
# @Software: PyCharm

import unittest
import time

from PageObject.login_page import login_url, LoginPage
from Util.SeleniumUtil import browser


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



class LoginTest(unittest.TestCase):

    u'''登录测试的case'''

    # @classmethod
    # def setUpClass(cls):
    #
    #     print("setUpClass")
    #     cls.driver = browser()
    #     cls.loginPage = LoginPage(cls.driver)

        # cls.loginPage.open(login_url,title=u"用户登录 - 博客园")

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()
    #     print("tearDownClass")
    global driver
    driver = browser()

    def setUp(self):
        self.driver = driver
        self.loginPage = LoginPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def login_case(self,username,password):
        self.loginPage.open(login_url, title=u"用户登录 - 博客园")
        self.loginPage.type_username(username)
        self.loginPage.type_password(password)
        self.loginPage.click_submit()
        # self.loginPage.login(username,password)

    @Screen(driver)
    def test_login_001(self):
        '''sucess'''
        self.login_case('sieyc','Yangchao@520')
        result = self.loginPage.is_text_in_element(("id", "lnk_current_user1"), u"老杨-tester")
        self.assertTrue(result)
        self.loginPage.click_loginOut()
        self.loginPage.click_accept()

    # @Screen(driver)
    # def test_login_002(self):
    #     '''fail'''
    #     self.login_case('sieyc','Yangchao@521')
    #     result = self.loginPage.is_text_in_element(("id", "tip_btn"), u"用户名或密码错误")
    #     self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
