from common.commonData import Commondata
from conftest import http
import pytest
import allure
import random
class Test_user_Exist:
    user = "139" + str(random.randint(10000000, 100000000))
    @allure.story('注册功能验证')
    @pytest.mark.jiang
    def test_login_succ (self):
        path_add='user/saveOrUpdateUser'
        data = {"nickName": '你十大爷的',
                "userName": self.user,
                "telNo": "",
                "email": "",
                "address": "",
                "roleIds": "",
                "regionId": 1,
                "regionLevel": 1}
        resp=http.post(path_add,data)
        assert resp['code'] == 200
        print('注册验证')
        print(resp)
        # 重新登陆并且获取id
    @allure.story('注册账号登录验证')
    @ pytest.mark.jiang
    def test_newLogin(self):
        path = "/sys/login"
        data = {'userName': self.user,
                'password': Commondata.password}
        resp_login = http.post(path, data)
        print(resp_login)
        # assert resp['code'] == 200
        id=resp_login['object']['userId']  # 获取字典中的id值
        print(id)
        print('aaa。。。。')


        #查看详情

