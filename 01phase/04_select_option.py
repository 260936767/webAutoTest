#coding:utf-8

from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

'''
方法一：
    二次定位方式
        1.先定位select
        2.再定位option
    直接定位：
        直接xpath定位option值点击
方法二：Select
    1.导入Select： from selenium.webdriver.support.select import Select
    2.通过select的index，value值，text等来操作 
'''

driver = webdriver.Chrome("../drivers/chromedriver.exe")

driver.implicitly_wait(20)

driver.get("http://www.baidu.com")

set =  driver.find_element_by_partial_link_text(u"设置")

ActionChains(driver).move_to_element(set).perform()

searchSet = driver.find_element_by_partial_link_text(u"搜索设置")
ActionChains(driver).move_to_element(searchSet).perform()
searchSet.click()


time.sleep(2)
# # 方法1 二次定位方式
# s = driver.find_element_by_id("nr")
# s.find_element_by_xpath("//option[@value = '20']").click()
# # 合起来写
# driver.find_element_by_id("nr").find_element_by_xpath("//option[@value = '20']").click()

# # 方法1 直接xpath定位option值点击
# driver.find_element_by_xpath(".//*[@id='nr']/option[2]").click()


# 方法二 index  从0 开始
s = driver.find_element_by_id("nr")

# Select(s).select_by_index(2)
# Select(s).select_by_value('20')
Select(s).select_by_visible_text(u'每页显示50条')
# 取消选中 index value text   所有选项  选项
# Select(s).deselect_by_index()
# 第一个  所有等
# Select(s).first_selected_option
# Select(s).all_selected_options
# Select(s).deselect_all()




time.sleep(2)

driver.quit()