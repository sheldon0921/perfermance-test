from tests.common.sendRequest.getXrequestId import GetXRequestId
from tests.login.singletonHttpClient import SingletonHttpClient
from utils.readerIniFile import ReaderIniFile
from utils.myRandom import MyRandom
from tests.login.login import Login
from utils.parseJson import ParseJson
from utils.myTime import Mytime
from log.log import Logger
import json


class SendRequestForOnline(object):

    def __init__(self, enterpriseInfo):
        self.consoleUrl = ReaderIniFile.value(section="console_sys_info", key="consoleBaseUrl")
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")
        self.httpClient = SingletonHttpClient.get_instance(flag="onLine")
        res = Login.loginNew(enterpriseID=enterpriseInfo["enterpriseID"])
        token = res["data"]["token"]
        if enterpriseInfo['enterpriName'] == '韩束官方优选店':
            app_version = 'v2.6.8'
        else:
            app_version = res['data']['app_version']
        self.headers = {
            'Token': token,
            'Enterprise-Hash': enterpriseInfo["enterpriseHash"],
            'App-Version': app_version,
            # 'Ep-Version': '5',
            'content-type': 'application/json',
            'X-Request-ID': GetXRequestId.retXRequestId()
        }

    def sendRequest(self, url:str, params:str, method="Post", version="eCommerce"):
        """
        :param method:
        :param platform:
        :param url:
        :param params:
        :return:
        """
        if version.lower() == "supermark":
            self.headers["Ep-Version"] = '5'
        self.headers["X-Request-ID"] = GetXRequestId.retXRequestId()
        if url.startswith(self.consoleUrl):
            # url = "{0}/{1}".format(self.consoleUrl, url)
            if str(method).upper() == "POST":
                res = self.httpClient.Post(url=url, json=params, headers=self.headers)
            elif str(method).upper() == "GET":
                res = self.httpClient.GET(url=url, params=params, headers=self.headers)
        elif url.startswith(self.shopBaseUrl):
            # url = "{0}/{1}".format(self.shopBaseUrl, url)
            if str(method).upper() == "POST":
                res = self.httpClient.Post(url=url, json=params, headers=self.headers)
            elif str(method).upper() == "GET":
                res = self.httpClient.GET(url=url, params=params, headers=self.headers)
        if res.status_code == 200:
            return res
        else:
            raise Exception("Call {0} interface failed !".format(url), res.text)


if __name__ == '__main__':
    # 线上小程序接口测试

    enterpriseInfo = {
        "enterpriName": "三优邻里爱家",
        "enterpriseHash": "b64d5577124ec0e2f9908d2f96b042aa",
        "enterpriseID": "132499313773824",
        "province": "重庆市",
        "city": "重庆市"
    }
    params = {"template_type": "my"}
    url = "gw-shop/app/v1/new-template/page-config"
    myRequest = SendRequestForOnline(enterpriseInfo)
    res = myRequest.sendRequest(platform="SHOP", method="POST", params=params, url=url)
    print("result: {0}".format(ParseJson.parseJson(res.json(), "template_code")))
    print(res.json())
    # 线上后台接口测试
