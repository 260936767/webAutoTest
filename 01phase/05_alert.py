from  selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time

''''
主要操作方法：
    text
    accept()
    dismiss()
    send_keys()

alert ->只有确定
confirm ->有确定和取消
prompt ->确定，取消，输入框
   
使用：
    1.先switch_to_alert()
    2.再操作
'''
driver = webdriver.Chrome("../drivers/chromedriver.exe")

driver.implicitly_wait(20)

driver.get("http://www.baidu.com")

set =  driver.find_element_by_partial_link_text(u"设置")

ActionChains(driver).move_to_element(set).perform()

searchSet = driver.find_element_by_partial_link_text(u"搜索设置")
ActionChains(driver).move_to_element(searchSet).perform()
searchSet.click()

s = driver.find_element_by_name("NR")

# Select(s).select_by_value("20")
Select(s).select_by_index(1)

driver.find_element_by_class_name("prefpanelgo").click()
time.sleep(3)
alert = driver.switch_to.alert

# alert.send_keys(u"输入的内容")
print(alert.text)
# 点击“X”按钮
# alert.dismiss()
# 点击“确定”按钮
alert.accept()


driver.quit()