#首页的元素定位
from selenium.webdriver.common.by import By
#from selenium import webdriver
class Home_PageLocator:
      # driver=webdriver.Chrome()
      # driver.get("https://petstore.octoperf.com/actions/Catalog.action")
      # driver.maximize_window()
      #登录元素定位
      login_loc=(By.LINK_TEXT,"Sign In")
      #推出登录元素可见
      signout_loc=(By.LINK_TEXT,"Sign Out")

