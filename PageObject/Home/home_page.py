#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/22 15:49
# @Author  : yc
# @Site    : 
# @File    : home_page.py
# @Software: PyCharm

from Util.SeleniumUtil import CommonAction
from selenium.webdriver.common.by import  By
from Util.Logging import MyLog as Log


log = Log.get_log()

class HomePage(CommonAction):

    userinfo_loc = (By.XPATH,"//*[@id = 'spnUid']")

    logout_loc = (By.XPATH,"//*[@id = '_mail_component_41_41']/a[1]")
    # logout_loc = (By.XPATH,"//*[@id = '_like")
    #
    # def get_userinfo(self):
    #     userinfo = self.get_text(self.userinfo_loc)
    #     log.info(userinfo)
    #     return userinfo

    def click_logout(self):
        self.click(self.logout_loc)

