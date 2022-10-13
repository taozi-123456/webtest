
import pytest
from Test_datas import login_data as ld
from Page_Object.page_login import Page_Login
from Page_Object.page_home import Page_Home
@pytest.mark.usefixtures("init")
class Test_login:
    #@pytest.mark.parametrize("case",ld.user_data)
    def test_login_success(self,init):
       Page_Login(init).login(*ld.user_data)
       #断言
       assert Page_Home(init).signout_exist()

    #执行用户名和密码输入错误失败的用例
    @pytest.mark.parametrize("case",ld.user_data_error)
    def test_login_fail(self, case, init):
           Page_Login(init).login(case["username"], case["passwd"])
           # 断言
           assert Page_Login(init).get_fail_text()==case["check"]

    # 执行用户名和密码为空失败的用例

    @pytest.mark.parametrize("case", ld.user_data_spark)
    def test_login_fail_spark(self, case, init):
        Page_Login(init).login(case["username"], case["passwd"])
        # 断言
        assert Page_Login(init).get_fail_spark_text() == case["check"]

