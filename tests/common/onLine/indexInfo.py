import json
from tests.login.login import Login
from tests.login.singletonHttpClient import SingletonHttpClient
from utils.readerIniFile import ReaderIniFile
from utils.myTime import Mytime
from utils.myRandom import MyRandom


class User:
    def __init__(self):
        self.httpClient = SingletonHttpClient.get_instance(flag="onLine")
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")

    def get_user_detail(self, enterpriseHash, enterpriseID):
        # 发送登录请求，获取token
        res = Login.loginNew(enterpriseID=enterpriseID)
        token = res["data"]["token"]
        timeStamp = Mytime.getCurrTimeStamp()
        randomStr = MyRandom.getRandomStr(2)
        xRequestId = 'autoTest-7b9d-4091-b4af-{0}{1}'.format(randomStr, timeStamp)
        headers = {
                   'token': token,
                   'Enterprise-Hash': enterpriseHash,
                   'App-Version': 'V1.7.2',
                   'X-Request-ID': xRequestId
        }
        url = "{0}/gw-shop/app/v1/user/detail".format(self.shopBaseUrl)
        res = self.httpClient.GET(url=url, headers=headers)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call /gw-shop/app/v1/user/detail interface failed !", res.text)


class LiveBroadCast:
    def __init__(self):
        self.httpClient = SingletonHttpClient.get_instance()
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")

    # @params token 用户登录token
    # @params datas 请求数据
    # @response 将接口返回的数据直接返回给调用方进行处理
    def list_live_broadcast(self,datas,enterpriseID,enterpriseHash):
        res = Login.loginNew(enterpriseID=enterpriseID)
        token = res["data"]["token"]
        timeStamp = Mytime.getCurrTimeStamp()
        randomStr = MyRandom.getRandomStr(2)
        xRequestId = 'autoTest-7b9d-4091-b4af-{0}{1}'.format(randomStr, timeStamp)
        headers = {
                   'token': token,
                   'Enterprise-Hash': enterpriseHash,
                   'App-Version': 'V1.7.2',
                   'X-Request-ID': xRequestId
        }
        url = "{0}/gw-shop/app/v1/app-center/live-broadcast/list".format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url, json=datas, headers=headers)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call /gw-shop/app/v1/app-center/live-broadcast/list interface failed !", res.text)



class TabRedHot:
    def __init__(self):
        self.httpClient = SingletonHttpClient.get_instance()
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")

    def get_tab_red_dot(self, enterpriseHash, enterpriseID):
        res = Login.loginNew(enterpriseID=enterpriseID)
        token = res["data"]["token"]
        timeStamp = Mytime.getCurrTimeStamp()
        randomStr = MyRandom.getRandomStr(2)
        xRequestId = 'autoTest-7b9d-4091-b4af-{0}{1}'.format(randomStr, timeStamp)
        headers = {
                   'token': token,
                   'Enterprise-Hash': enterpriseHash,
                   'App-Version': 'V1.7.2',
                   'X-Request-ID': xRequestId
        }
        url = "{0}/gw-shop/app/v1/content-manage/tab-red-dot".format(self.shopBaseUrl)
        res = self.httpClient.GET(url=url, headers=headers)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call /gw-shop/app/v1/content-manage/tab-red-dot interface failed !", res.text)