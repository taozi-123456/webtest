#登录页面的元素定位
from time import sleep

from selenium.webdriver.common.by import By
class login_locator:
    #用户名输入框
    username_loc=(By.XPATH,'//input[@name="username"]')
    #密码输入框
    passwd_loc=(By.XPATH,'//input[@name="password"]')
    #登录按钮
    loginbutton_loc=(By.XPATH,'//input[@name="signon"]')

    #错误提示信息
    error_messge=(By.XPATH,'//ul[@class="messages"]/li[1]')
    #登录明和密码任一个为空时的提示信息
    error_messge_spark=(By.XPATH,'//p[1]')
if __name__ == '__main__':
    pass
    # from selenium import webdriver
    # driver = webdriver.Chrome()
    # loc=login_locator()
    # driver.get("https://petstore.octoperf.com/actions/Catalog.action")
    # driver.maximize_window()
    # login_loc = (By.LINK_TEXT, "Sign In")
    # driver.find_element(*login_loc).click()
    # sleep(3)
    # driver.find_element(*loc.username_loc).send_keys("taozi1")
    #
    # ele=driver.find_element(*loc.passwd_loc)
    # ele.clear()
    # ele.send_keys("123456")
    # driver.find_element(*loc.loginbutton_loc).click()

