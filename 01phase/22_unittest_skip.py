#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/15 17:38
# @Author  : yc
# @Site    : 
# @File    : 22_unittest_skip.py
# @Software: PyCharm

import unittest

# @unittest.skip(reason=u"无条件跳过")
class test(unittest.TestCase):

    @unittest.skip(reason=u"无条件跳过")
    def test_01(self):

        print("test_01")
    @unittest.skipIf(condition=True,reason=u"条件为True时跳过")
    def test_02(self):

        print("test_02")

    @unittest.skipUnless(condition=False,reason=u"条件为False时跳过")
    def test_03(self):

        print("test_03")

    #断言失败时跳过
    @unittest.expectedFailure
    def test_04(self):


        self.assertTrue(Trueasd)
        print("test_04")

if __name__ == "__main__":
    unittest.main()