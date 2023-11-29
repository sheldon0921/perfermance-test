from tests.login.login import Login
from tests.login.singletonHttpClient import SingletonHttpClient
from utils.readerIniFile import ReaderIniFile
from utils.myTime import Mytime
from utils.myRandom import MyRandom

class Shopcart:

    def __init__(self):
        self.httpClient = SingletonHttpClient.get_instance(flag="onLine")
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")

    def wx_recommend(self, datas, enterpriseID, enterpriseHash):
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
        url = "{0}/gw-shop/app/v1/page/wx-recommend".format(self.shopBaseUrl)
        res = self.httpClient.GET(url=url, json=datas, headers=headers)
        if res.status_code == 200:
            return res.json()
            # return res
        else:
            raise Exception("Call /gw-shop/app/v1/page/wx-recommend !", res.text)

    def cart_setting(self, datas, enterpriseID, enterpriseHash):
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
        url = "{0}/gw-shop/app/v1/cart/setting".format(self.shopBaseUrl)
        res = self.httpClient.GET(url=url, json=datas, headers=headers)
        if res.status_code == 200:
            return res.json()
            # return res
        else:
            raise Exception("Call /gw-shop/app/v1/cart/setting !", res.text)

    def store_cart_list(self, datas, enterpriseID, enterpriseHash):
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
        url = "{0}/gw-shop/app/v1/store-cart/list".format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url, json=datas, headers=headers)
        if res.status_code == 200:
            return res.json()
            # return res
        else:
            raise Exception("Call /gw-shop/app/v1/store-cart/list !", res.text)


    def wx_mall_upload(self, datas, enterpriseID, enterpriseHash):
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
        url = "{0}/gw-shop/app/v1/wx-mall/is_upload".format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url, json=datas, headers=headers)
        if res.status_code == 200:
            return res.json()
            # return res
        else:
            raise Exception("Call /gw-shop/app/v1/wx-mall/is_upload !", res.text)

    def store_cart_update(self,headers ,datas):
        # res = Login.loginNew(enterpriseID=enterpriseID)
        # token = res["data"]["token"]
        # app_version = res['data']['app_version']
        # timeStamp = Mytime.getCurrTimeStamp()
        # randomStr = MyRandom.getRandomStr(2)
        # xRequestId = 'autoTest-7b9d-4091-b4af-{0}{1}'.format(randomStr, timeStamp)
        # headers = {
        #     'Token': token,
        #     'Enterprise-Hash': enterpriseHash,
        #     'App-Version': app_version,
        #     'Ep-Version': '5',
        #     'content-type': 'application/json',
        #     'X-Request-ID': xRequestId
        # }
        url = "{0}/gw-shop/app/v1/store-cart/update".format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url, json=datas, headers=headers)
        if res.status_code == 200:
            return res.json()
            # return res
        else:
            raise Exception("Call /gw-shop/app/v1/store-cart/update !", res.text)

    def subscribe_status(self, datas, enterpriseID, enterpriseHash):
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
        url = "{0}/gw-shop/app/v1/common/subscribe-status".format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url, json=datas, headers=headers)
        if res.status_code == 200:
            return res.json()
            # return res
        else:
            raise Exception("Call /gw-shop/app/v1/common/subscribe-status !", res.text)


    def clear_invalid(self, datas, enterpriseID, enterpriseHash):
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
        url = "{0}/gw-shop/app/v1/store-cart/clear-invalid".format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url, json=datas, headers=headers)
        if res.status_code == 200:
            return res.json()
            # return res
        else:
            raise Exception("Call /gw-shop/app/v1/store-order/clear-invalid !", res.text)

    def help_price(self, datas, enterpriseID, enterpriseHash):
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
        url = '{0}/gw-shop/app/v1/activity-center/help/prize'.format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url, json=datas, headers=headers)
        if res.status_code == 200:
            return res.json()
            # return res
        else:
            raise Exception("Call /gw-shop/app/v1/activity-center/help/prize !", res.text)

    def goods_foot_list(self, datas, enterpriseID, enterpriseHash):
        """
        {"page":1,"size":15}
        """
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
        url = '{0}/gw-shop/app/v1/goods-footprint/list'.format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url, json=datas, headers=headers)
        if res.status_code == 200:
            return res.json()
            # return res
        else:
            raise Exception("Call /gw-shop/app/v1/goods-footprint/list !", res.text)

    def my_activity_list(self, headers, datas):
        # res = Login.loginNew(enterpriseID=enterpriseID)
        # token = res["data"]["token"]
        # app_version = res['data']['app_version']
        # timeStamp = Mytime.getCurrTimeStamp()
        # randomStr = MyRandom.getRandomStr(2)
        # xRequestId = 'autoTest-7b9d-4091-b4af-{0}{1}'.format(randomStr, timeStamp)
        # headers = {
        #     'Token': token,
        #     'Enterprise-Hash': enterpriseHash,
        #     'App-Version': app_version,
        #     'Ep-Version': '5',
        #     'content-type': 'application/json',
        #     'X-Request-ID': xRequestId
        # }
        url = '{0}/gw-shop/app/v1/user-center/my-activity-list'.format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url, json=datas, headers=headers)
        if res.status_code == 200:
            return res.json()
            # return res
        else:
            raise Exception("Call /gw-shop/app/v1/user-center/my-activity-list !", res.text)



