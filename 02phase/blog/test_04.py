#coding:utf-8
import unittest


class Test(unittest.TestCase):
    def setUp(self):
        print("start!")

    def tearDown(self):
        print("end!")

    def test01(self):
        print(u"执行测试用例01")
    def test02(self):
        print(u"执行测试用例02")
    def test03(self):
        print(u"执行测试用例03")
    def test04(self):
        print(u"执行测试用例04")
    def test05(self):
        print(u"执行测试用例05")