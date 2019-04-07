# import pytest
# import json
# import conftest
#
# http=conftest.http
# proxies=conftest.proxies
# headers=conftest.headers
#
# token=conftest.Conftest.session_fixture
# headers['token']=token
# data_token = {"token": token}  # 创建一个data的dict，添加了token数据
# # data_json = json.dumps(data_token)  # 将python对象转换成json
# class Test_Sys():
#     def test_getUserInfo(this):
#
#         resp = http.post(url="http://192.168.1.203:8083/sys/getUserInfo",
#                                 proxies=proxies,
#                                 data=data_token,
#                                 headers=headers)
#         assert resp.status_code==200