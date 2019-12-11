#导包
import unittest

import api
from api.api_employee import ApiEmployee
from parameterized import parameterized
#创建测试类---必须继承Unitest.TestCase
from tools.assert_common import assert_common
from tools.read_txt import read_txt


class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #创建ApiEmployee对象
        cls.api_employee =ApiEmployee()


#创建测试方法----必须以test开头
    #新增员工
    # parameterized.expand(read_txt("employee_post.txt"))
    def test01_post_employee(self,username="jaysbu1",mobile="13987654020",workNumber="1123451"):
        r= self.api_employee.api_post_employee(username,mobile,workNumber)
        #查看响应信息
        print(r.json())
        #获取员工id
        api.user_id  =r.json().get("data").get("id")
        print("新增员工的ID为: ",api.user_id)
        #断言
        assert_common(self,r)

    #修改员工assert_common(self,r)
    def test02_put_employee(self,username="jack112"):
        r= self.api_employee.api_put_employee(username)
        print("修改后员工的结果为: ",r.json())
        #断言
        assert_common(self,r)

    #查询员工
    def test03_get_employee(self):
        r= self.api_employee.api_get_employee()
        print("查询员工结果是: ",r.json())
        #断言
        assert_common(self,r)



    #删除员工
    def test04_delete_employee(self):
        r= self.api_employee.api_delete_employee()
        print("删除员工后结果为: ",r.json())
        #断言
        assert_common(self,r)
