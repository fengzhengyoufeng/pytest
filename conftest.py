from util.httputil import HttpUtil
from common.commonData import Commondata
import pytest
http=HttpUtil()
@pytest.fixture(scope='session',autouse=True)
def session_login():
    path = "/sys/login"
    data={'userName':Commondata.userName,
          'password':Commondata.password}
    resp_login=http.post(path,data)
    Commondata.token=resp_login['object']['token']






# import pytest
# import requests
# import json
#
# http = requests.session()
# proxies = {'http': 'http://localhost:8888'}
# headers = {"Content-Type": "application/json;charset=UTF-8"}
# @pytest.fixture(scope='session',autouse=True)
# class Conftest():
#     def session_fixture(self):
#
#         resp_login = http.post(url="http://192.168.1.20s3:8083/sys/login",
#                                   proxies=proxies,
#                                   data='{"userName":"15935153219","password":"123456"}',
#                                   headers=headers)
#         assert resp_login.status_code==200
#         print('登录成功')
#         resp_dict = json.loads(resp_login.text)  # 将json格式转换成字典格式
#         token = resp_dict['object']['token']  # 获取字典中的token值
#         headers['token'] = token  # 将token值加入到headers字典中
#
#         data_token = {"token": token}  # 创建一个data的dict，添加了token数据
#         data_json = json.dumps(data_token)  # 将python对象专程json
#         return token
#         yield
#         resp_logout = http.post(url="http://192.168.1.203:8083/sys/logout",
#                                    proxies=proxies,
#                                    data=data_json,
#                                    headers=headers)
#         assert resp_logout.status_code == 200
#         print('退出登录
