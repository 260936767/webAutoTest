
#coding:utf-8

from selenium import webdriver

driver = webdriver.Chrome("../drivers/chromedriver.exe")

driver.get("http://www.126.com")

'''
iframe操作
1.找到iframe 的id 、name
    1.没有name,id 找到tag_name
2.切换到iframe switch_to.frame(elementObject)

3.释放iframe driver.switch_to.default_content()

如何判断元素是否在iframe上  firebug 工具左上角显示元素是否在iframe内 ，Top window 说明没有

'''

# i = driver.find_element_by_tag_name("iframe")
#
# driver.switch_to_frame(i)

#直接切换到iframe
driver.switch_to.frame("x-URS-iframe")

driver.find_element_by_name("email").send_keys("ceshi")

# for iframe in iframelist:

# print(element.tag_name)

# driver.switch_to.frame()

#释放
driver.switch_to_default_content()

driver.close()