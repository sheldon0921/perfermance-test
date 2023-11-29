import json
from tests.login.login import Login
from tests.login.singletonHttpClient import SingletonHttpClient
from utils.readerIniFile import ReaderIniFile
from utils.myTime import Mytime
from utils.myRandom import MyRandom



class ShopOrder:
    def __init__(self):
        self.httpClient = SingletonHttpClient.get_instance(flag="onLine")
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")

    # @params datas 下单所需的请求参数
    # @return 将访问该接口返回的数据直接返回给调用方
    def add_order(self,datas,enterpriseID,enterpriseHash):
        '''测试生成订单接口'''
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
        datas["user_address_id"] = res['data']["userAddressId"]
        url = "{0}/gw-shop/app/v1/store-order/add".format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url, json=datas, headers=headers)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call /gw-shop/app/v1/store-order/add interface failed !", res.text)

    def confirm_order(self, datas, enterpriseID, enterpriseHash):
        '''测试确认订单接口'''
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
        datas["user_address_id"] = res["data"]["userAddressId"]
        url = "{0}/gw-shop/app/v1/store-order/confirm".format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url,json=datas,headers=headers)
        if res.status_code == 200:
            # return res.json()
            return res
        else:
            raise Exception("Call /gw-shop/app/v1/store-order/confirm !", res.text)

    def cancel_order(self,headers,datas):
        url = "{0}/gw-shop/app/v1/main-order/machine".format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url, json=datas, headers=headers)
        if res.status_code == 200:
            # return res.json()
            return res
        else:
            raise Exception("Call /gw-shop/app/v1/main-order/machine !", res.text)

    def store_orderlist(self,datas, enterpriseID, enterpriseHash):
        '''查询订单列表'''
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
        datas["user_address_id"] = res["data"]["userAddressId"]
        url = "{0}/gw-shop/app/v1/store-order/list".format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url, json=datas, headers=headers)
        if res.status_code == 200:
            return res.json()
            # return res
        else:
            raise Exception("Call /gw-shop/app/v1/main-order/machine !", res.text)



