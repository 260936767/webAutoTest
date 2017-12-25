#coding:utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC  #期望包含
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test01(self):
        print("test01")

    def test03(self):
        print("test03")

    def test04(self):
        print("test04")

    def test02(self):
        print("test02")

    def ttyyy(self):
        print("ttyyy")

if __name__ == "__main__":
    unittest.main()

'''
1.根据方法名来执行
2.根据顺序标号执行
3.方法名不含test的方法不执行
3.每个方法调用均会调用 setUp和tearDown方法
...
setUp
test01
tearDown
setUp
test02
tearDown
setUp
test03
tearDown
setUp
test04
tearDown
....
'''