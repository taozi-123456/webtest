from time import sleep

from Common.BasePage import Base_Page
from Page_Locators.login_locator import login_locator as loc
from Page_Locators.home_locator import Home_PageLocator as hloc
class Page_Login(Base_Page):
    def login(self,username,passwd):

        #点击登录按钮
        self.click_element(hloc.login_loc,"点击登录图标")
        #输入用户名
        self.input_text(loc.username_loc,"输入用户名",username)
        #输入密码
        self.input_text(loc.passwd_loc, "输入用户名",passwd)
        #点击登录
        self.click_element(loc.loginbutton_loc,"点击登录")
    #获取用户名和密码错误登录失败的文本信息
    def get_fail_text(self):
        return self.get_text(loc.error_messge,"获取登录失败的数据")
    #获取用户名和密码为空登录失败的文本信息
    def get_fail_spark_text(self):
        return self.get_text(loc.error_messge_spark,"获取登录失败的数据")
