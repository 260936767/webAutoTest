#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/22 10:30
# @Author  : yc
# @Site    : 
# @File    : login_page163.py
# @Software: PyCharm

from Util.SeleniumUtil import CommonAction
from selenium.webdriver.common.by import  By

url = "http://mail.163.com/"

class Login_page_163(CommonAction):

    email_login_link_loc = (By.XPATH,"//*[@id='lbNormal']")

    iframe_loc = 'x-URS-iframe'
    username_loc = (By.XPATH,"//input[@name='email']")
    password_loc = (By.XPATH,"//input[@name='password']")
    loginBtn_loc = (By.XPATH,"//a[@id='dologin']")




    def click_email_login_link(self):
        self.click(self.email_login_link_loc)

    def type_username(self,username):
        self.send_keys(self.username_loc,username)

    def type_password(self,password):
        self.send_keys(self.password_loc,password)

    def click_loginBtn(self):
        self.click(self.loginBtn_loc)



    def login(self,username,password):
        self.click_email_login_link()
        self.switch_to_iframe(self.iframe_loc)
        self.type_username(username)
        self.type_password(password)
        self.click_loginBtn()

