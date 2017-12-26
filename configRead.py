#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/26 11:29
# @Author  : yc
# @Site    : 
# @File    : configRead.py
# @Software: PyCharm

import configparser
import os
file = os.path.split(os.path.realpath(__file__))
sysPath = file[0]
fileName = "config.ini"
filePath = os.path.join(sysPath,fileName)

class configFileAction:
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(filePath,encoding='utf-8')

    def get(self,section,name):
        value = self.cf.get(section,name)
        return value
    def set(self,section,name,value):
        if section in self.cf.sections():
            pass
        else:
            self.cf.add_section(section)
        self.cf.set(section,name,value)
        with open(filePath,"w+") as f:
            self.cf.write(f)




