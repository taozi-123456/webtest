from Common.BasePage import Base_Page
from Page_Locators.home_locator import Home_PageLocator as loc
class Page_Home(Base_Page):
    def signout_exist(self):
        try:
           self.wait_visibi_time(loc.signout_loc,"首页退出登录元素可见")
        except:
            return False
        else:
            return True