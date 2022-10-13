"""
共享文件
放前置和后置
定义fixture前置后置-作用域-返回值
"""
import logging

import pytest
from selenium import webdriver
from Test_datas import global_datas as gd
@pytest.fixture
def init():
    #前置登录网站
    driver=webdriver.Chrome()
    logging.info("打开浏览器")
    driver.get(gd.login_url)
    driver.maximize_window()
    yield driver
    #后置退出浏览器
    driver.quit()