
#导包
import unittest
#创建测试类----继承父类unitest.TestCase
import api
from api.api_login import ApiLogin
from tools.assert_common import assert_common


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #调用
        cls.api_login =ApiLogin()


#创建测试方法----必须以test开头
    def test01_login_success(self,mobile='13800000002',password="123456"):
        r= self.api_login.api_login(mobile,password)
        print(r.json())
        #获取token
        token = r.json().get("data")
        api.headers["Authorization"]="Bearer "+token
        print("登录后的headers为: ",api.headers)
        #断言

        assert_common(self,r)



