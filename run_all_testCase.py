#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/12 23:27
# @Author  : yc
# @Site    : 
# @File    : run_all_testCase.py
# @Software: PyCharm

import HTMLTestRunner
import time
import unittest
import os

from testCase import test_login163

case_path = os.path.join(os.getcwd(),"testCase")

report_path = os.path.join(os.getcwd(),"report")

def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,
                                        pattern="test*.py",
                                        top_level_dir=None)
    print(discover)

    return discover

if __name__ =="__main__":

    suite = unittest.TestSuite()
    suite.addTest(test_login163.Login163("test_login163_001"))

    now_time = time.strftime("%Y-%m-%d_%H_%M_%S",time.localtime())
    report_file = report_path+"/report"+now_time+".html"
    fp = open(report_file,"wb")

    runner = HTMLTestRunner.HTMLTestRunner(fp,
                                  verbosity=2,
                                  title=u"首页登录测试",
                                  description=u"登录成功，登录失败测试")

    runner.run(suite)

    fp.close()