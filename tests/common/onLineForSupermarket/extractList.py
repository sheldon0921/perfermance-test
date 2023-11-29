from tests.common.sendRequest.sendRequestForOnline import SendRequestForOnline
from tests.login.singletonHttpClient import SingletonHttpClient
from utils.readerIniFile import ReaderIniFile
from tests.login.login import Login
from utils.myRandom import MyRandom
from utils.myTime import Mytime
from time import sleep
import json

class ExtractList:
    def __init__(self):
        self.httpClient = SingletonHttpClient.get_instance(flag="onLine")
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")

    def extract_list(self, datas,header):
        url = "{0}/gw-shop/app/v1/extract/list".format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url, headers=header,json=datas)
        sleep(2)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call /gw-shop/app/v1/extract/list failed !", res.text)

    def getHeader(self,enterpriseHash,enterpriseID):
        res = Login.loginNew(enterpriseID=enterpriseID)
        userAddressId = res["data"]["userAddressId"]
        userId = res["data"]["userId"]
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
            'X-Request-ID': xRequestId,
            'user_address_id': str(userAddressId),
            'user_id': str(userId)
        }
        return headers

    def region_list(self, header, datas):
        """
        区域列表
        :param enterpriseID:
        :param enterpriseHash:
        :param datas:
        :return:
        """
        locator = "/gw-shop/app/v1/extract/region-list"
        url = "{0}{1}".format(self.shopBaseUrl,locator)
        res = self.httpClient.Post(url=url, headers=header, json=datas)
        sleep(2)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call {0} failed !".format(locator), res.text)

    def mini_subscribe_record(self, headers,datas):
        locator = "/gw-shop/app/v1/common/mini-subscribe-record"
        url = "{0}{1}".format(self.shopBaseUrl,locator)
        res = self.httpClient.Post(url=url, headers=headers, json=datas)
        sleep(2)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call {0} failed !".format(locator), res.text)