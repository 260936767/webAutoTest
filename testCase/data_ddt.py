#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/30 13:28
# @Author  : yc
# @Site    : 
# @File    : data_ddt.py
# @Software: PyCharm


'''数据驱动'''

import ddt
import unittest

testdata = [{"username":"admin","password":"123456"},
            {"username":"xxx","password":"sdfsf"},
            {"username":"dasad","password":"3453ddd"},]

@ddt.ddt
class Test(unittest.TestCase):

    def setUp(self):
        print("setup")

    def tearDown(self):
        print("tearDown")

    @ddt.data(*testdata)
    def test_ddt(self,data):
        print(data)

if __name__ == "__main__":
    unittest.main()