import requests
import json

session=requests.session()
proxies={'http':'http://localhost:8888'}
headers={"Content-Type":"application/json;charset=UTF-8"}
resp_login=session.post(url="http://192.168.1.203:8083/sys/login",
                   proxies=proxies,
                   data='{"userName":"15935153219","password":"123456"}',
                   headers=headers)
resp_dict = json.loads(resp_login.text)   # 将json格式转换成字典格式
token=resp_dict['object']['token']  #   获取字典中的token值
headers['token']=token  #   将token值加入到headers字典中


data_token={"token":token}  #创建一个data的dict，添加了token数据
data_json=json.dumps(data_token)    #将python对象专程json
resp_get=session.post(url="http://192.168.1.203:8083/sys/getUserInfo",
                   proxies=proxies,
                   data=data_json,
                   headers=headers)

print(resp_get.status_code)
print(resp_get.text)
resp_logout=session.post(url="http://192.168.1.203:8083/sys/logout",
                   proxies=proxies,
                   data=data_json,
                   headers=headers)

print(resp_logout.text)
print(resp_logout.status_code)