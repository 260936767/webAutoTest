#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/12 22:20
# @Author  : yc
# @Site    : 
# @File    : test_login.py
# @Software: PyCharm

import unittest

from PageObject.login_page import login_url, LoginPage
from Util.SeleniumUtil import browser
from Util.ExcelUtil import ExcelUtil
import ddt

driver = ""

data = ExcelUtil('E:/test.xlsx','Sheet1')
testdata = data.dict_data()

print(testdata[0]["password"])
@ddt.ddt
class LoginTest(unittest.TestCase):


    u'''登录测试的case'''

    @classmethod
    def setUpClass(cls):

        print("setUpClass")

        cls.driver = browser()

        cls.loginPage = LoginPage(cls.driver)

        # self.loginPage.open(login_url,title=u"用户登录 - 博客园")

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


    @ddt.data(*testdata)
    def test_login_001(self,*userinfo):
        '''sucess'''
        print(userinfo)
        self.login_case(userinfo[0]["username"],userinfo[0]["password"])
        result = self.loginPage.is_text_in_element(("id", "lnk_current_user"), u"老杨-tester")
        self.assertTrue(result)
        self.loginPage.click_loginOut()
        self.loginPage.click_accept()

    @ddt.data(*testdata)
    def test_login_002(self,*userinfo):
        '''fail'''
        print(userinfo)
        self.login_case(userinfo[1]["username"],userinfo[1]["password"])
        result = self.loginPage.is_text_in_element(("id", "tip_btn"), u"用户名或密码错误")
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
