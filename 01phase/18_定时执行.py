#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/14 10:30
# @Author  : yc
# @Site    : 
# @File    : 18_定时执行.py
# @Software: PyCharm

import os,time


#切换到目录 cd
# os.chdir(r"E:/studyMenu/PycharmProjects/webAutoTest/01phase/")
#system 可执行任意的shell和DOS命令
# os.system("python 17_threading.py")

k=1
while k<2:
    now_time = time.strftime("%H_%M",time.localtime())

    if now_time == "10_45":
        print(u"-----开始运行-----")
        os.chdir(r"E:/studyMenu/PycharmProjects/webAutoTest/01phase/")
        os.system("python 17_threading.py")
        print(u"-----运行结束-----")
        # break  #每天都执行的话 不要break
    else:
        time.sleep(10)
        print(now_time)