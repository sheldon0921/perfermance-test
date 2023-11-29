import json
from tests.login.login import Login
from tests.login.singletonHttpClient import SingletonHttpClient
from utils.readerIniFile import ReaderIniFile
from utils.myTime import Mytime
from utils.myRandom import MyRandom


class MePage(object):

    def __init__(self):
        self.httpClient = SingletonHttpClient.get_instance(flag="onLine")
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")

    def commonPostFunc(self, datas, enterpriseHash, enterpriseID, interfaceUrl):
        # 发送登录请求，获取token
        res = Login.loginNew(enterpriseID=enterpriseID)
        token = res["data"]["token"]
        app_version = res['data']['app_version']
        timeStamp = Mytime.getCurrTimeStamp()
        randomStr = MyRandom.getRandomStr(2)
        xRequestId = 'autoTest-7b9d-4091-b4af-{0}{1}'.format(randomStr, timeStamp)
        headers = {
            'Token': token,
            'Enterprise-Hash': enterpriseHash,
            'App-Version': app_version,
            'Ep-Version': '5',
            'content-type': 'application/json',
            'X-Request-ID': xRequestId
        }
        url = "{0}/{1}".format(self.shopBaseUrl,interfaceUrl)
        # res = requests.post(url=url, json=datas, headers=headers)
        res = self.httpClient.Post(url=url, json=datas, headers=headers)
        if res.status_code == 200:
            # return res.json()
            return res
        else:
            raise Exception("Call /gw-shop/app/v1/goods/detail interface failed !", res.text)

    def commonGetFunc(self, datas, enterpriseHash, enterpriseID, interfaceUrl):
        # 发送登录请求，获取token
        res = Login.loginNew(enterpriseID=enterpriseID)
        token = res["data"]["token"]
        app_version = res['data']['app_version']
        timeStamp = Mytime.getCurrTimeStamp()
        randomStr = MyRandom.getRandomStr(2)
        xRequestId = 'autoTest-7b9d-4091-b4af-{0}{1}'.format(randomStr, timeStamp)
        headers = {
            'Token': token,
            'Enterprise-Hash': enterpriseHash,
            'App-Version': app_version,
            'Ep-Version': '5',
            'content-type': 'application/json',
            'X-Request-ID': xRequestId
        }
        url = "{0}/{1}".format(self.shopBaseUrl,interfaceUrl)
        # res = requests.post(url=url, json=datas, headers=headers)
        res = self.httpClient.GET(url=url, headers=headers)
        if res.status_code == 200:
            # return res.json()
            return res
        else:
            raise Exception("Call /gw-shop/app/v1/goods/detail interface failed !", res.text)