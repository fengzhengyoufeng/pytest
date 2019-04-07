from common.commonData import Commondata
from conftest import http
import allure
@allure.feature('获取用户信息功能验证')
class Test_sys_getuserinfo:
    @allure.story('获取用户信息功能验证')
    def test_getUserInfo (self):
        path='/sys/getUserInfo'
        data={'token': Commondata.token}
        resp=http.post(path,data)
        assert resp['code']==200
        print('获取用户信息功能验证')