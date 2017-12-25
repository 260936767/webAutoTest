#coding:utf-8
import unittest,time,HTMLTestRunner
import os

class assertTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print(u"初始化方法！")

    @classmethod
    def tearDownClass(cls):
        print(u"类结束方法!")

    def test_01(self):
        '''测试用例——01 a=b  assertEqual'''
        a = u"测试"
        b = u"测试"
        self.assertEqual(a,b,msg=u"a=b")
        print("test_01")

    def test_02(self):
        '''测试用例——02 a！=b  assertNotEqual'''
        a = u"测试01"
        b = u"测试02"
        self.assertNotEqual(a, b, msg=u"a！=b")
        print("test_02")

    def test_03(self):
        '''测试用例——03 a = False  assertFalse'''
        a = False
        self.assertFalse(a,msg=u"a是False")
        print("test_03")

    def test_04(self):
        '''测试用例——04 assertIn'''
        a = "abc"
        b = "b"
        self.assertIn(a,b,msg=u"b包含a")
        print("test_04")

    def test_05(self):
        '''测试用例——01 assertNotIn'''
        a = "abc"
        b = "b"
        self.assertNotIn(a, b, msg=u"b不包含a")
        print("test_05")


if __name__ == "__main__":


    #添加测试集
    suite = unittest.TestSuite()
    #添加测试套件 类名(用例名)
    suite.addTest(assertTest("test_01"))
    suite.addTest(assertTest("test_02"))
    suite.addTest(assertTest("test_03"))
    suite.addTest(assertTest("test_04"))
    suite.addTest(assertTest("test_05"))
    #
    # # runner = unittest.TextTestRunner()
    # # runner.run(suite)

    # # test_dir = "E:\\studyMenu\\PycharmProjects\webAutoTest\\02phase"
    # test_dir = os.path.join(os.getcwd())
    #
    # suite = unittest.defaultTestLoader.discover(test_dir,
    #                                            pattern='test*.py', #测试类必须以test开头 不然找不到文件
    #                                            top_level_dir=None)



    print(suite)

    nowTime = time.strftime("%Y-%m-%d_%H_%M_%S",time.localtime())
    filePath = r"E:/studyMenu/PycharmProjects/webAutoTest/02phase/report"+nowTime+".html"
    fp = open(filePath,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           verbosity=1,  #冗长
                                           title=u"测试标题",
                                           description=u"测试描述")
    runner.run(suite)
    fp.close()