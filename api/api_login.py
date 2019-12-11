import api
import requests

class ApiLogin():

    @classmethod
    def __init__(self):
        #初始化
        self.url_login =api.BASE_URL+"/api/sys/login"
        self.hearders = api.headers

    def api_login(self,mobile,password):
        data={"mobile":mobile, "password":password}
        return requests.post(url=self.url_login,json=data,headers=api.headers)

