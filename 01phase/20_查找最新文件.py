#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/14 16:16
# @Author  : yc
# @Site    : 
# @File    : 20_查找最新文件.py
# @Software: PyCharm

import os

result_dir = r'E:/studyMenu/PycharmProjects/webAutoTest/report/'

lists = os.listdir(result_dir)

lists.sort(key=lambda fn:os.path.getmtime(result_dir+"\\"+fn))

print(lists)

print('最新文件为：'+lists[-1])

file = os.path.join(result_dir,lists[-1])

print(file)