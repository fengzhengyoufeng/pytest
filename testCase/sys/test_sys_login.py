from common.commonData import Commondata
from conftest import http
import allure
@allure.feature("登录验证检测")
class   Test_sys_login:
    @allure.story('登录成功验证')
    def test_login_succ (self):
        path='/sys/login'
        data = {'userName': Commondata.userName,
                'password': Commondata.password}
        resp=http.post(path,data)
        assert resp['code'] == 200
        assert resp['object']['userId'] == 125
        assert resp['msg'] == '操作成功'
        print('用户名密码正确登录验证')

    @allure.story('用户名正确密码错误进行登录验证')
    def test_login_fail_falsePwd (self):
        path='/sys/login'
        data = {'userName': Commondata.userName,
                'password': '12312'}
        resp=http.post(path,data)
        assert resp['code'] == 410
        assert resp['msg'] == "用户名或密码错误"
        print('用户名正确密码错误进行登录验证')

    @allure.story('用户名不存在进行登录验证')
    def test_login_fail_falsePhone (self):
        path='/sys/login'
        data = {'userName': '123456789',
                'password':Commondata.password}
        resp=http.post(path,data)
        assert resp['code'] == 301
        assert resp['msg'] == "用户不存在"
        print('用户名不存在进行登录验证')

    @allure.story('禁用的用户进行登录验证')
    def test_login_fail_ban_user (self):
        path='/sys/login'
        data = {'userName': '18634812833',
                'password':Commondata.password}
        resp=http.post(path,data)
        assert resp['code'] == 3010
        assert resp['msg'] == "此账户禁止登录"
        print('禁用的用户进行登录验证')