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
from Util.Logging import Log


log = Log()

class LoginTest(unittest.TestCase):

    u'''登录测试的case'''

    @classmethod
    def setUpClass(cls):

        log.info("setUpClass")
        cls.driver = browser()
        cls.loginPage = LoginPage(cls.driver)

        # cls.loginPage.open(login_url,title=u"用户登录 - 博客园")


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("tearDownClass")


    def login_case(self,username,password):
        self.loginPage.open(login_url, title=u"用户登录 - 博客园")
        self.loginPage.type_username(username)
        self.loginPage.type_password(password)
        self.loginPage.click_submit()
        # self.loginPage.login(username,password)


    def test_login_001(self):
        '''sucess'''

        log.info(u"-----开始测试-test_login_001-----")
        # self.login_case("sieyc","Yangchao@520")
        self.login_case("sieyc","Yangchao@520")
        # result = self.loginPage.is_text_in_element(("id", "lnk_current_user"), u"老杨-tester")
        # self.assertTrue(result)
        self.loginPage.click_loginOut()
        self.loginPage.click_accept()
        log.info(u"-----结束测试-test_login_001-----")

    def test_login_002(self):
        '''fail'''
        log.info(u"-----开始测试-test_login_002-----")
        self.login_case('sieyc','Yangchao@521')
        result = self.loginPage.is_text_in_element(("id", "tip_btn"), u"用户名或密码错误")
        self.assertTrue(result)
        log.info(u"-----结束测试-test_login_002-----")

# if __name__ == "__main__":
#     suite = unittest.TestSuite()
#     suite.addTest(LoginTest('test_login_001'))
#     suite.addTest(LoginTest('test_login_002'))
#
#     runner = unittest.TextTestRunner()
#     runner.run(suite)
