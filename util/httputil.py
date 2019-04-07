import requests
import json
from common.commonData import Commondata

class HttpUtil():
    def __init__(self):
        self.http=requests.session()
        self.headers={"Content-Type": "application/json;charset=UTF-8"}
    def post(self,path,data):
        host=Commondata.host
        data_json=json.dumps(data)
        if Commondata.token!=None:
            self.headers['token']=Commondata.token
        resp_login=self.http.post(url=host+path,
                             headers=self.headers,
                             data=data_json,
                             proxies=Commondata.proxies)
        assert resp_login.status_code==200
        resp_json=resp_login.text
        resp_dict=json.loads(resp_json)
        return resp_dict