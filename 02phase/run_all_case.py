#coding:utf-8
import unittest
import os
import HTMLTestRunner
import time


# class mainTest(unittest.TestCase):
#
#     #类装饰器  只执行一次
#     @classmethod
#     def setUpClass(cls):
#         print("setUpClass")
#
#     @classmethod
#     def tearDownClass(cls):
#         print("tearDownClass")


# print(os.getcwd()) #当前文件路径 E:/studyMenu/PycharmProjects/webAutoTest/02phase

# case_path = os.path.join(os.getcwd(),'badidu')   #添加路径 E:/studyMenu/PycharmProjects/webAutoTest/02phase/badidu

case_path = os.path.join(os.getcwd())

# report_path = os.path.join(os.getcwd(),"report/report.html")

#文件名不能含有空格和： 换用_
nowTime = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime())

#报告路径
report_path = r"E:/studyMenu/PycharmProjects/webAutoTest/02phase/report/report"+nowTime+".html"


# 定义方法，返回含有test关键字的文件名称list，即所有测试用例
def all_testCase():

    #discover加载测试用例为list集合 待执行用例目录，匹配脚本名称规则，顶层目录
    discover = unittest.defaultTestLoader.discover(case_path,
                                               pattern="test*.py",
                                               top_level_dir=None)
    print(discover)

    return discover

if __name__ == "__main__":

    #返回运行实例
    runner = unittest.TextTestRunner()

    #运行实例
    # runner.run(all_testCase())
    # 文件操作 写入
    fp = open(report_path,"wb")

    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='<Demo Test>',
        description='This demonstrates the report output by HTMLTestRunner.'
    )
    runner.run(all_testCase())

    # 关闭文件流
    fp.close()