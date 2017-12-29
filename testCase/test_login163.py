#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/22 13:45
# @Author  : yc
# @Site    : 
# @File    : test_login163.py
# @Software: PyCharm

from PageObject.login_page163 import Login_page_163
from PageObject.Home.home_page import HomePage
from PageObject.Send.send_page import SendPage
from Util.SeleniumUtil import browser
from Util.ScreenUtil import Screen
import unittest,time,HTMLTestRunner,os
from Util.Logging import MyLog as Log
import configRead
import unittest
from Util import Logging

# 日志和浏览器驱动
log = Log.get_log()
driver = browser()

configAction = configRead.configFileAction()
url = configAction.get("163","url")

class Login163(unittest.TestCase):



    def setUp(self):
        self.driver = driver
        self.loginpage163 = Login_page_163(self.driver)
        self.homePage = HomePage(self.driver)
        self.sendPage = SendPage(self.driver)
        self.title = r'163网易免费邮--中文邮箱第一品牌'
        log.info("setUp")

    def tearDown(self):
        log.info("tearDown")
        pass

        # driver.quit()


    @Screen(driver)
    def test_login163_001(self):
        u'''163登录测试 '''
        self.loginpage163.open(url,self.title,20)
        self.loginpage163.login('XXXXXXXXX','XXXXXXXXXX')
        self.assertIn("185",self.homePage.get_text(self.homePage.userinfo_loc))

        log.info("test_login163_001")

    @Screen(driver)
    def test_login163_002(self):
        log.info("test_login163_002")
        self.sendPage.send_email("999")

    @Screen(driver)
    def test_login163_003(self):
        log.info("test_login163_003")
        self.homePage.click_logout()

    @Screen(driver)
    def test_login163_004(self):
        log.info("test_login163_004")
        log.info("driver 退出")
        self.driver.quit()

# if __name__ == "__main__":
    # unittest.main()
    #
    # suite = unittest.TestSuite()
    # suite.addTest(Login163("test_login163_001"))
    # report_path = Logging.logPath
    # now_time = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime())
    # report_file = report_path + "\\result" + now_time + ".html"
    #
    # log.info(report_file)
    #
    # fp = open(report_file, "wb")
    #
    # runner = HTMLTestRunner.HTMLTestRunner(fp,
    #                                        verbosity=2,
    #                                        title=u"ssss",
    #                                        description=u"ttttt")
    # runner.run(suite)
    #
    # fp.close()