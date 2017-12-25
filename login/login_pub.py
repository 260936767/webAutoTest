#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
'''登录公共方法'''

class Page(object):
    '''
    page基类,用于所有页面继承
    '''

    url = "http://192.168.1.117:8082/action/login/login.jsp"

    def __init__(self,selenium_driver,base_url=url,parent = None):

        self.driver = selenium_driver
        self.base_url = base_url
        self.timeout = 30
        self.parent = parent
        self.tabs = {}

    def _open(self,url):
        url = self.base_url+url
        self.driver.get(url)
        assert self.on_page(),'did not load url : %s' %url

    def find_element(self,*loc):
        return  self.driver.find_element(*loc)

    def open(self):
        self._open(self.url)
    def on_page(self):
        return self.driver.current_url ==(self.base_url+self.url)
    def script(self,src):
        return self.driver.execute_script(src)
    def send_keys(self,loc,value,clear_first = True,click_first = True):
        try:
            loc = getattr(self,'_%s' %loc)
            if clear_first:
                self.find_element(*loc).clear()
            if click_first:
                self.find_element(*loc).click()
            self.find_element(*loc).send_keys(value)
        except AttributeError:
            print(u'%s 页面没有 %s locator ' %(self,loc))


class LoginPage(Page):
    '''
    登录页面模型
    '''
    #定位器
    username_loc = (By.NAME,'j_username')
    password_loc = (By.NAME,'j_password')

    #操作

    def open(self):
        self._open(self.url)

    def type_username(self,username):
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self,password):
        self.find_element(*self.password_loc).send_keys(password)

    def submit(self):
        self.find_element(*self.password_loc).send_keys(Keys.ENTER)




def test_user_login(driver,username,password):
    '''

    :param driver:
    :param username:
    :param password:
    :return:
    '''

    login_page = LoginPage(driver)
    login_page.open()
    login_page.type_username(username)
    login_page.type_password(password)
    login_page.submit()

def main():
    try:
        driver = webdriver.Chrome("../drivers/chromedriver.exe")
        username = 'ceshitl'
        password = '123456a'
        test_user_login(driver,username,password)
    finally:
        driver.close()

if __name__ == "__main__":
    main()


