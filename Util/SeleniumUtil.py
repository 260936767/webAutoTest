#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC   #场景判断
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement
import time
from Util.Logging import MyLog as Log

global_timeout = 30

log = Log.get_log()


def browser(brower = "chrome"):
    '''
    浏览器
    :param brower:
    :return:
    '''

    try:
        if brower == "chrome":
            chrome_path = r"E:/studyMenu/PycharmProjects/webAutoTest/drivers/chromedriver.exe"
            driver = webdriver.Chrome(executable_path = chrome_path)
            return driver
        elif brower == "firefox":
            driver = webdriver.Firefox()
            return driver
        elif brower == "ie":
            driver = webdriver.Ie()
            return driver
        elif brower == "phantomjs":
            phantomjs_path = r"E:/studyMenu/PycharmProjects/webAutoTest/drivers/phantomjs.exe"
            driver = webdriver.PhantomJS(executable_path=phantomjs_path)
            return driver
        else:
            log.error(u"未找到浏览器驱动，你可以选择'chrome','firefox','ie'浏览器驱动。")
    except Exception as msg:
        log.error("%s" %msg)


class CommonAction(object):
    '''
    封装selenium
    '''
    def __init__(self,driver):
        self.driver = driver

    def open(self,url,title = '',timeout = global_timeout):

        # driver = testUtil()
        # driver.open(url,t='')
        self.driver.get(url)
        self.driver.maximize_window()
        log.info(u"打开url:[%s]" %url)

        try:
            #加载判断标题
            WebDriverWait(self.driver,timeout,1).until(EC.title_contains(title))

        except TimeoutException as msg:
            log.error(u"超时：[%s]" %msg)
        except Exception as msg:
            log.error(u"错误：[%s]" % msg)

    def find_element(self,locator,timeout = global_timeout):

        #参数说明：驱动，超时时间，轮循查询时间
        element = WebDriverWait(self.driver,timeout,1).until(EC.presence_of_element_located(locator))
        # element = WebDriverWait(self.driver,timeout,1).until(lambda x:x.find_element_by_id('').is_displayed())
        if element is None:
            log.warning(u"未能定位到元素，locator:[%s]" %str(locator))
            # print(u"未能定位到元素，locator:%s" %locator)
        return element

    def find_elements(self,locator,timeout = global_timeout):
        element = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_all_elements_located(locator))
        return element

    def click(self,locator):

        element = WebDriverWait(self.driver,global_timeout,1).until(EC.presence_of_element_located(locator))
        element.click()
        log.info(u"点击元素：[%s]" %str(locator))


    def submit(self, locator):

        # log.info(u"表单提交：[%s]" %(locator))
        element = WebDriverWait(self.driver,global_timeout,1).until(EC.presence_of_element_located(locator))
        element.submit()

    def send_keys(self,locator,text):
        element = WebDriverWait(self.driver,global_timeout,1).until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)
        log.info(u"元素：[%s] 输入内容：[%s]" %(locator,text))

    def is_text_in_element(self,locator,text,timeout=global_timeout):
        '''元素中的文本断言'''

        try:
            result = WebDriverWait(self.driver,timeout,1).until(EC.text_to_be_present_in_element(locator,text))

        except TimeoutException as msg:
            log.error(u"超时：[%s]" % msg)
            return  False
        else:
            return result

    def is_value_in_element(self,locator,value,timeout=global_timeout):
        '''元素中的value断言'''
        try:
            result = WebDriverWait(self.driver,timeout,1).until(EC.text_to_be_present_in_element_value(locator,value))

        except TimeoutException as msg:
            log.error(u"超时：[%s]" % msg)
            return  False
        else:
            return result

    '''元素相关'''
    def is_title(self,title,timeout = global_timeout):
        '''标题等于'''
        return WebDriverWait(self.driver,timeout,1).until(EC.title_is(title))

    def is_title_contains(self, title, timeout=global_timeout):
        '''标题包含'''
        return WebDriverWait(self.driver, timeout, 1).until(EC.title_contains(title))


    def is_selected(self,locator,timeout = global_timeout):
        '''元素是否被选中'''
        return WebDriverWait(self.driver,timeout,1).until(EC.element_located_to_be_selected(locator))


    def is_selected_to_be(self,locator,timeout = global_timeout,selected=True):
        '''
        判断元素的选中状态
        :param locator: 定位信息
        :param timeout: 超时时间
        :param selected: 默认True
        :return:
        '''

        return WebDriverWait(self.driver,timeout,1).until(EC.element_selection_state_to_be(locator))


    def is_alert_present(self,timeout = 10):
        '''alert是否弹出'''
        return WebDriverWait(self.driver,timeout,1).until(EC.alert_is_present())

    def is_visibility(self,locator,timeout =global_timeout):
        '''
        元素是否可见：可见返回元素，不可见，返回False
        '''
        return WebDriverWait(self.driver,timeout,1).until(EC.visibility_of_element_located(locator))

    def is_clickable(self,locator,timeout = global_timeout):
        '''
        元素是否可点击：可点击返回本身，不可点击，返回False
        '''
        return WebDriverWait(self.driver,timeout,1).until(EC.element_to_be_clickable(locator))


    def is_located(self,locator,timeout = global_timeout):
        '''
        元素是否被定位到(有可能不可见)：返回本身/False
        '''
        return WebDriverWait(self.driver,timeout,1).until(EC.presence_of_element_located(locator))

    def move_to_element(self,locator,timeout = global_timeout):
        '''
        鼠标悬停
        '''
        element = WebDriverWait(self.driver,global_timeout,1).until(EC.presence_of_element_located(locator))
        ActionChains(self.driver).move_to_element(element).perform()
        log.error(u"鼠标移动到元素：[%s]" %locator)

    '''浏览器操作'''
    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    def get_title(self):
        return self.driver.title

    def get_text(self,locator,timeout = global_timeout):
        '''获取元素文本值'''
        element = WebDriverWait(self.driver,timeout,1).until(EC.presence_of_element_located(locator))
        log.info(u"获取元素[ "+str(locator)+" ]文本值")
        return element.text

    def get_attribute(self,name,locator,timeout = global_timeout):
        '''获取属性name的值'''
        element = WebDriverWait(self.driver,global_timeout,1).until(EC.presence_of_element_located(locator))
        log.info(u"获取元素["+str(locator)+"]的["+str(name)+"]属性值")
        return element.get_attribute(name)

    '''js操作'''

    def js_execute(self,js):
        log.info(u"执行js操作：[%s]" %js)
        return self.driver.execute_script(js)

    def js_focus_element(self,locator):
        '''焦点在某元素'''
        target = WebDriverWait(self.driver,global_timeout,1).until(EC.presence_of_element_located(locator))
        log.info(u"焦点元素:[%s]" %locator)
        self.driver.execute_script("arguments[0].scrollIntoView();",target)

    def js_scroll_top(self):
        '''滚动到顶部'''
        js = "windows.scrollTo(0,0)"

        self.driver.execute_script(js)
        log.info(u"滚动到顶部")

    def js_scroll_end(self):
        '''滚动到底部'''
        js = "windows.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)
        log.info(u"滚动到底部")

    '''选中/取消选中'''
    def select_by_index(self,locator,index):

        element = WebDriverWait(self.driver,global_timeout,1).until(EC.presence_of_element_located(locator))

        Select(element).select_by_index(index)
        log.info(u"选中[%s]元素" %index)

    def select_by_value(self,locator,value):

        element = WebDriverWait(self.driver,global_timeout,1).until(EC.presence_of_element_located(locator))

        Select(element).select_by_value(value)
        log.info(u"选中[%s]元素" % value)

    def select_by_text(self,locator,text):

        element = WebDriverWait(self.driver,global_timeout,1).until(EC.presence_of_element_located(locator))

        Select(element).select_by_visible_text(text)
        log.info(u"选中[%s]元素" % text)

    def deselect_by_index(self,locator,index):

        element = WebDriverWait(self.driver,global_timeout,1).until(EC.presence_of_element_located(locator))

        Select(element).deselect_by_index(index)
        log.info(u"取消选中[%s]元素" % index)

    def deselect_by_value(self,locator,value):

        element = WebDriverWait(self.driver,global_timeout,1).until(EC.presence_of_element_located(locator))

        Select(element).deselect_by_value(value)
        log.info(u"取消选中[%s]元素" % value)

    def deselect_by_text(self,locator,text):

        element = WebDriverWait(self.driver,global_timeout,1).until(EC.presence_of_element_located(locator))

        Select(element).deselect_by_visible_text(text)
        log.info(u"取消选中[%s]元素" % text)

    def switch_to_alert(self):
        '''跳转到alert'''
        log.info(u"跳转到alert")
        return self.driver.switch_to.alert
    def switch_to_iframe(self,locator):
        '''跳转frame'''
        # driver.switch_to.frame(0)  # 1.用frame的index来定位，第一个是0
        # driver.switch_to.frame("frame1")  # 2.用id来定位
        # driver.switch_to.frame("myframe")  # 3.用name来定位
        # driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))  # 4.用WebElement对象来定位
        log.info(u"跳转frame：[ "+str(locator)+" ]")
        return self.driver.switch_to.frame(locator)

    def alert_accept(self):
        '''alert确定'''
        time.sleep(10)
        alert =  self.switch_to_alert()
        alert.accept()
        log.info(u"点击alert确定")

    def alert_dismiss(self):
        '''alert取消'''
        alert =  self.switch_to_alert()
        alert.dismiss()
        log.info(u"alert取消")

# if __name__ == "__main__":
#     driver = browser()
#
#     yc = BaseDriver(driver)
#
#     yc.open("http://192.168.1.117:8082/action/login/login.jsp")
#
#     username_loc = ("name","j_username")
#     password_loc = ("name","j_password")
#
#     yc.send_keys(username_loc,"ceshizd")
#     yc.send_keys(password_loc,"123456a")
#
#     yc.submit(password_loc)
#
#     yc.is_title("运维流程管理系统")
#
#     gzgl_loc = (By.XPATH,"//*[@id='sysmanger_0']")
#
#     yc.move_to_element(gzgl_loc)
#
#     time.sleep(5)
#
#     yc.quit()




