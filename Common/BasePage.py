#页面操作的的各种方法
import logging
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Common.handle_path import screenshots_dir
from Common.my_loger import My_Logger, logger
from Page_Locators.home_locator import Home_PageLocator as hloc
class Base_Page:
    #定义driver方法
    def __init__(self, driver: WebDriver):
        self.driver = driver
    #失败截图方法
    def get_picture(self,page_action):
         #截图的命名格式 XX页面_XX操作__截图时间.png
         #获取当前的时间
         local_time=time.strftime("%Y-%M-%d-%H-%M-%S",time.localtime())
         #定义截图保存的路径
         file_path=os.path.join(screenshots_dir,"{}_{}.png".format(page_action,local_time))
         print(file_path)
         #记录截图输出的路径
         logger.info("错误截图输出的路径{}".format(file_path))
         #进行截图
         self.driver.save_screenshot(file_path)

    #等待元素可见
    def wait_visibi_time(self,locator,page_action,timeout=20,poll_frequency=0.5):
        try:
            WebDriverWait(self.driver,timeout,poll_frequency).until(EC.visibility_of_element_located(locator))
        except:
            logger.exception("等待元素可见失败")
            self.get_picture(page_action)
            raise
        else:
            logger.info("等待元素可见成功")


    #获取页面的元素
    def get_element(self,locator,page_action,timeout=20,poll_frequency=0.5):
        self.wait_visibi_time(locator,page_action,timeout,poll_frequency)
        logger.info("获取{}行为的{}元素".format(page_action,locator))
        try:
           ele=self.driver.find_element(*locator)
        except:
            logger.exception("获取页面元素失败")
            self.get_picture(page_action)
            raise
        else:
            return ele

    #点击元素
    def click_element(self,locator,page_action,timeout=20,poll_frequency=0.5):
        ele=self.get_element(locator,page_action,timeout,poll_frequency)
        logger.info("获取{}行为的{}元素".format(page_action, locator))
        try:
            ele.click()
        except:
            logger.exception("点击元素失败")
            self.get_picture(page_action)
            raise
    #输入文本
    def input_text(self,locator,page_action,value,timeout=20,poll_frequency=0.5):
         ele = self.get_element(locator, page_action, timeout, poll_frequency)
         logger.info("获取{}行为的{}元素输入{}元素".format(page_action, locator,value))
         try:
             ele.clear()
             ele.send_keys(value)
         except:
             logger.exception("输入元素失败")
             self.get_picture(page_action)
             raise


    #获取文本
    def get_text(self,locator,page_action,timeout=20,poll_frequency=0.5):
        ele = self.get_element(locator, page_action, timeout, poll_frequency)
        logger.info("获取{}行为的{}元素".format(page_action, locator))

        try:
           value= ele.text
        except:
            logger.exception("获取文本失败")
            self.get_picture(page_action)
            raise
        else:
            return value
    #获取元素属性
    def get_attribute(self,locator,page_action,name,timeout=20,poll_frequency=0.5):
        ele = self.get_element(locator, page_action, timeout, poll_frequency)
        logger.info("获取{}行为的{}元素".format(page_action, locator))

        try:
         value=ele.get_attribute(name)
        except:
            logger.exception("获取元素属性失败")
            self.get_picture(page_action)
            raise
        else:
            return value
if __name__ == '__main__':

    # 前置登录网站
    from selenium import webdriver
    from Page_Locators.login_locator import login_locator as loc
    driver=webdriver.Chrome()
    BP=Base_Page(driver)
    #logging.info("打开浏览器")
    driver.get("https://petstore.octoperf.com/actions/Catalog.action")
    driver.maximize_window()
    #
    #
    #
    BP.click_element(hloc.login_loc,"点击登录")
    #
    BP.input_text(loc.username_loc,"输入用户名","taozi")
    #
    BP.input_text(loc.passwd_loc, "输入用户名", "123456")
    BP.click_element(loc.loginbutton_loc,"点击登录")
    value=BP.get_text(loc.error_messge_spark,"获取登录失败的数据")
    print(value)

    # print(ww)
    # driver.quit()
