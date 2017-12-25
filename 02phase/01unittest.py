
#coding:utf-8

from selenium import webdriver
import unittest


class Test(unittest.TestCase):

    #前置
    def setUp(self):
        pass

    #后置
    def tearDown(self):
        pass


    def testAdd(self):  # test method names begin with 'test'
        self.assertEqual((1 + 2), 3)
        self.assertEqual(0 + 1, 1)

    def testMultiply(self):
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)

    def testMinus(self):
        u'''测试减法'''
        result = 98-32
        hope = 66
        self.assertEqual(result,hope)


    def testDivide(self):
        u'''测试除法'''
        result = 10/3
        hope = 3.3333333333333335
        self.assertEqual(result,hope)

if __name__ == '__main__':
    unittest.main()
