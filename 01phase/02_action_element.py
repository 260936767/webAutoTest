#coding:utf-8
from selenium import webdriver
import time
import random

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome('../drivers/chromedriver.exe')


'''
操作元素 鼠标键盘
'''

'''
click() clear() send_keys() 中文前面加u  u'中文'
submit()  提交表单  模拟回车
'''

#隐式等待 作用全局  加载没有出来才会等待

# driver.get('http://www.baidu.com')
# driver.implicitly_wait(10)
# driver.find_element_by_css_selector('#kw').clear()
#
# driver.find_element_by_css_selector('#kw').send_keys(u'python')
#
# # driver.find_element_by_css_selector('#su').click()
#
# driver.find_element_by_css_selector('#su').submit()
#
# time.sleep(3)
# driver.implicitly_wait(10)
#
# driver.quit()


'''
模拟键盘
1.导入Keys from selenium.webdriver.common.keys import Keys
2.send_keys()
'''

# driver.get("http://www.hordehome.com")
# driver.find_element_by_xpath("//*[@id='search-button']/i").click()
# driver.find_element_by_id('search-term').clear()
# driver.find_element_by_id('search-term').send_keys('selenium python')
# driver.find_element_by_id('search-term').send_keys(Keys.ENTER)

'''
F1~F12: send_keys(Keys.F1)~send_keys(Keys.F12)
ctrl+a: send_keys(Keys.CONTROL,'a')  c x v 一样
tab: send_keys(Keys.TAB)
'''

# driver.implicitly_wait(10)
#
# time.sleep(10)
#
# driver.quit()

'''
模拟鼠标：
0.导入操作链  from selenium.webdriver.common.action_chains import ActionChains
1.悬停
2.右击
3.按住鼠标拖到某个位置
'''
#
# driver.get("http://www.baidu.com")
# driver.implicitly_wait(5)
#
# mouse = driver.find_element_by_link_text(u'设置')
# # mouse1 = driver.find_element_by_link_text(u'搜索历史')
#
# ActionChains(driver).move_to_element(mouse).perform()  #鼠标移动到元素 perform() 执行ActionChains的动作
# mouse1 = driver.find_element_by_link_text(u'搜索历史')
# ActionChains(driver).move_to_element(mouse1).perform()  #鼠标移动到元素 perform() 执行ActionChains的动作
# mouse1.click()
# # ActionChains(driver).move_by_offset()
# # ActionChains(driver).move_to_element_with_offset()
#
# username = driver.find_element_by_name('userName')
# password = driver.find_element_by_name('password')
# loginBtn = driver.find_element_by_id("TANGRAM__PSP_10__submit")
#
# print(loginBtn)
#
# # ActionChains(driver).context_click(username).perform()
# # time.sleep(2)
# #
# # ActionChains(driver).context_click(password).perform()
# # time.sleep(2)
# ActionChains(driver).double_click(loginBtn).perform()
# # loginBtn.click()
# time.sleep(2)

'''
句柄操作
0.获取当前窗口句柄
1.打开新窗口，获取全部句柄
2.切换窗口操作 
    方法1 遍历所有句柄 判断不等第一个句柄，切换至第二个句柄（窗口）
    方法2 直接切换至第二个句柄操作
'''
#
# driver.implicitly_wait(10)
# driver.get("http://www.baidu.com")
# driver.find_element_by_name("wd").send_keys(u"赶集网")
# driver.find_element_by_id("su")
#
# # 获取当前窗口句柄
# h1 = driver.current_window_handle
#
# print(h1)
#
#
# driver.find_element_by_xpath("//*[@id='1']/h3/a[1]").click()
# # 获取所有窗口的句柄
# h_all = driver.window_handles
#
# print(h_all)
# #方法1
# # for i in h_all:
# #     if i !=h1:
# #         driver.switch_to.window(i)
#
# # 方法2
#
# driver.switch_to.window(h_all[1])
#
# driver.find_element_by_name("search_keyword").send_keys("python")
#
# driver.switch_to.window(h1)
#
# driver.find_element_by_name("wd").clear()
# driver.find_element_by_name("wd").send_keys("selenium python")
# driver.find_element_by_id("su").click()


'''
关闭窗口
1.close()   关闭当前窗口
2.quit()    退出整个进程
'''
# driver.close()
# driver.quit()

'''
获取一组元素
'''

driver.get("http://www.baidu.com/")
driver.find_element_by_id("kw").send_keys(u"测试部落")
driver.find_element_by_id("kw").submit()

time.sleep(2)

s = driver.find_elements_by_css_selector("h3.t>a")
# for i in range(1,3):
a = random.randint(0,9)
print("------------>")
print(s[a].get_attribute('href'))
# driver.get(str(s[a].get_attribute('href')))
s[a].click()

#
# for i in s:
#     print(i.get_attribute("href"))

driver.quit()





















