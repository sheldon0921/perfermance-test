from tests.login.login import Login
from tests.login.singletonHttpClient import SingletonHttpClient
from utils.readerIniFile import ReaderIniFile
from utils.myTime import Mytime
from utils.myRandom import MyRandom

class City_distribution:

    def __init__(self):
        self.httpClient = SingletonHttpClient.get_instance(flag="onLine")
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")
        self.consoleUrl = ReaderIniFile.value(section="console_sys_info", key="consoleBaseUrl")

    def sku_city_delivery(self, datas, enterpriseID, enterpriseHash):
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
        url = "{0}/gw-shop/app/v1/goods/sku-city-delivery".format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url, json=datas, headers=headers)
        if res.status_code == 200:
            return res.json()
            # return res
        else:
            raise Exception("Call /gw-console/v1/city-distribution/delivery-details !", res.text)

    def get_delivery_freight(self, datas, enterpriseID, enterpriseHash):
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
        url = "{0}/gw-shop/app/v1/city-distribution/get-delivery-freight".format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url, json=datas, headers=headers)
        if res.status_code == 200:
            return res.json()
            # return res
        else:
            raise Exception("Call /gw-shop/app/v1/city-distribution/get-delivery-freight !", res.text)

    def city_sku_list(self, datas, enterpriseID, enterpriseHash):
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
        url = "{0}/gw-shop/app/v1/collect-bills/city-sku-list".format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url, json=datas, headers=headers)
        if res.status_code == 200:
            return res.json()
            # return res
        else:
            raise Exception("Call /gw-shop/app/v1/collect-bills/city-sku-list !", res.text)

    def delivery_detail(self, datas, enterpriseID, enterpriseHash):
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
        url = "{0}/gw-shop/app/v1/city-distribution/delivery-detail".format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url, json=datas, headers=headers)
        if res.status_code == 200:
            return res.json()
            # return res
        else:
            raise Exception("Call /gw-shop/app/v1/city-distribution/delivery-detail !", res.text)


