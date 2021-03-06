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
from Util import Logging as Log
from Util import SuiteUtil

from testCase import test_login163


case_path = os.path.join(os.getcwd(),"testCase")

report_path = Log.logPath

def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,
                                        pattern="test*.py",
                                        top_level_dir=None)
    print(discover)

    return discover

if __name__ =="__main__":

    suite = SuiteUtil.Suite()
    suite.addTest(test_login163.Login163("test_login163_001"))
    suite.addTest(test_login163.Login163("test_login163_002"))
    suite.addTest(test_login163.Login163("test_login163_003"))
    suite.addTest(test_login163.Login163("test_login163_004"))

    now_time = time.strftime("%Y-%m-%d_%H_%M_%S",time.localtime())
    report_file_name = report_path+"/report "+now_time+".html"
    fp = open(report_file_name,"wb")

    runner = HTMLTestRunner.HTMLTestRunner(fp,
                                               verbosity=2,
                                               title="title",
                                               description="description")

    runner.run(suite)
    fp.close()