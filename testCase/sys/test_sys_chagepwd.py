from common.commonData import Commondata
import pytest
import allure
from conftest import http
@allure.feature("修改密码验证")
class Test_sys_chagepwd:
    @allure.story('修改密码成功验证')
    @pytest.mark.zhang
    def test_login_changePwd (self):
        path='/sys/changePwd'
        data = {'userId': 125,
                'userName':Commondata.userName,
                'oldPwd':Commondata.password,
                'password':Commondata.chagepwd}
        resp=http.post(path,data)
        assert resp['code']==200
        assert resp['msg'] == '操作成功'
        print('更改密码功能验证')

    @allure.story('改回密码功能验证')
    @pytest.mark.zhang
    def test_login_replayPwd (self):
        path='/sys/changePwd'
        data = {'userId': 125,
                'userName':Commondata.userName,
                'oldPwd':Commondata.chagepwd,
                'password':Commondata.password}
        resp=http.post(path,data)
        assert resp['code']==200
        assert resp['msg'] == '操作成功'
        print('改回密码功能验证')

    @allure.story('旧密码错误验证')
    @pytest.mark.zhang
    def test_login_returnPwd (self):
        path='/sys/changePwd'
        data = {'userId': 125,
                'userName':Commondata.userName,
                'oldPwd':123789456,
                'password':Commondata.password}
        resp=http.post(path,data)
        assert resp['code']==411
        assert resp['msg'] == '旧密码错误'
        print('旧密码错误')