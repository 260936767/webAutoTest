#coding:utf-8
import unittest
import os,sys

sys.path.append(r"E:\studyMenu\PycharmProjects\webAutoTest")


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def test01(self):
        print(u"执行测试用例01")
    def test02(self):
        print(u"执行测试用例02")
    def test03(self):
        print(u"执行测试用例03")
        self.assertEqual(u"学院",u'执行')
    def test04(self):
        print(u"执行测试用例04")
    def test05(self):
        print(u"执行测试用例05")

if __name__ == "__main__":
    unittest.main()