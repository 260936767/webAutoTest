#coding:utf-8

from selenium import webdriver
import time

driver = webdriver.Chrome('../drivers/chromedriver.exe')

driver.get('http://www.baidu.com/')

'''
#id
'''
# driver.find_element_by_id('kw').send_keys('selenium python')

'''
#name
'''
# driver.find_element_by_name('wd').send_keys('selenium python')

'''
#class_name
'''
# driver.find_element_by_class_name('s_ipt').send_keys('selenium python')

'''
#tag_name  不推荐 页面中相同的标签比较多
'''

'''
#link_text  含有超链接的  href="http://news.baidu.com"  可以取链接的text值
'''
# driver.find_element_by_link_text('新闻').click()

'''
#partial_link_text 模糊text值
'''
# driver.find_element_by_partial_link_text('闻').click()


'''
#xpath

用法：         //元素[@属性 = '属性值']
 *任意元素     //*[@属性 = '属性值'] 
 层级：        //父元素[@属性 = '属性值']/子元素[@属性 = '属性值'] ...
 索引：        //父元素[@属性 = '属性值']/子元素[@属性 = '属性值'][0]
 逻辑运算：    //元素[@属性1 = '属性值' and @属性2 = '属性值']  and/or/not  与或非
 模糊匹配：    //*[contains(text(),'文本值')]   包含文本
 模糊匹配：    //*[contains(@id,'kw')]         包含属性
 模糊匹配：    //*[starts-with(@id,'k')]       属性以什么开始
 模糊匹配：    //*[ends-with(@id,'w')]         属性以什么结束
 模糊匹配：    //*[matchs(text(),'新闻')]       正则表达式
      
'''
# driver.find_element_by_xpath("//input[@id = 'kw']").send_keys('xpath')

'''
css定位 和xpath类似
. 为class属性
# 为id属性
其他属性  [属性 = '属性值']
层级 索引 模糊匹配

'''
driver.find_element_by_css_selector('#kw').send_keys('python')

'''
其他神器  selenium Builder 
'''

time.sleep(2)
driver.quit()