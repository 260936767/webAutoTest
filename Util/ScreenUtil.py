#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/22 16:40
# @Author  : yc
# @Site    : 
# @File    : ScreenUtil.py
# @Software: PyCharm

import time,os
from Util import Logging as Log

logPath = Log.logPath

screenShotPath = os.path.join(logPath,"screenShot")
if not os.path.exists(screenShotPath):
    os.mkdir(screenShotPath)

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
                fileName = os.path.join(screenShotPath,"%s.jpg" %nowTime)
                self.driver.get_screenshot_as_file(fileName)

                raise
        return inner

