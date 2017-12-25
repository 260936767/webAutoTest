#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/12 22:06
# @Author  : yc
# @Site    : 
# @File    : login_page.py
# @Software: PyCharm


from selenium.webdriver.common.by import By

from Util.SeleniumUtil import CommonAction

login_url ="https://passport.cnblogs.com/user/signin"

class LoginPage(CommonAction):
    '''登录页'''

    username_loc = (By.XPATH,"//*[@id='input1']")
    password_loc = (By.XPATH,"//*[@id='input2']")
    submit_loc = (By.XPATH,"//*[@id='signin']")
    #自动登录
    remember_me_loc = (By.NAME,"remember_me")
    register_loc = (By.LINK_TEXT,"立即注册")
    quest_loc = (By.LINK_TEXT,"反馈问题")
    retrieve_loc = (By.LINK_TEXT,"找回")
    reset_loc = (By.LINK_TEXT,"重置")
    loginOut_loc = (By.XPATH,"//*[@id='header_user_right']/a[5]")

    def type_username(self,username):
        '''输入账号'''
        self.send_keys(self.username_loc,username)

    def type_password(self,password):
        self.send_keys(self.password_loc,password)

    def click_submit(self):
        self.click(self.submit_loc)

    def click_remember_me(self):
        if self.is_selected_to_be(self.remember_me_loc):
            return
        self.click(self.remember_me_loc)

    def click_register(self):
        self.click(self.remember_me_loc)

    def click_quest(self):
        self.click(self.quest_loc)

    def click_retrieve(self):
        self.click(self.retrieve_loc)

    def click_reset(self):
        self.click(self.reset_loc)

    def click_loginOut(self):
        self.click(self.loginOut_loc)
    def click_accept(self):
        self.alert_accept()

    def login(self,username,password):

        self.type_username(username)
        self.type_password(password)
        self.click_submit()
        self.click_loginOut()








