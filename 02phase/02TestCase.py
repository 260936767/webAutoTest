
#coding:utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC  #期望包含
import unittest

class baiduTitleTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("../drivers/chromedriver.exe")
        self.driver.get("http://www.baidu.com")

    def tearDown(self):
        self.driver.quit()

    def test_title(self):
        result = EC.title_contains(u'百度一下')(self.driver)

        print(result)
        self.assertTrue(result)
if __name__ == '__main__':
    unittest.main()