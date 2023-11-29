import json
from tests.login.login import Login
from tests.login.singletonHttpClient import SingletonHttpClient
from utils.readerIniFile import ReaderIniFile
from tests.common.onLineForSupermarket.extractList import ExtractList
from utils.myTime import Mytime
from utils.myRandom import MyRandom


class GoodsDetail:

    def __init__(self):
        self.httpClient = SingletonHttpClient.get_instance(flag="onLine")
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")

    def get_goods_detail(self, datas, header):
        # 发送登录请求，获取token

        url = "{0}/gw-shop/app/v1/goods/detail".format(self.shopBaseUrl)
        # res = requests.post(url=url, json=datas, headers=headers)
        res = self.httpClient.Post(url=url, json=datas, headers=header)
        if res.status_code == 200:
            # return res.json()
            return res
        else:
            raise Exception("Call /gw-shop/app/v1/goods/detail interface failed !", res.text)

    def encryptShortLink(self, datas,header):
        # 发送登录请求，获取token

        url = "{0}/gw-shop/app/v1/common/encrypt-short-link".format(self.shopBaseUrl)
        # res = requests.post(url=url, json=datas, headers=headers)
        res = self.httpClient.Post(url=url, json=datas, headers=header)
        if res.status_code == 200:
            # return res.json()
            return res
        else:
            raise Exception("Call /gw-shop/app/v1/common/encrypt-short-link interface failed !", res.text)

    def commonFuncPost(self, datas,header,interfaceUrl):
        # 发送登录请求，获取token

        url = "{0}/{1}".format(self.shopBaseUrl, interfaceUrl)
        # res = requests.post(url=url, json=datas, headers=headers)
        res = self.httpClient.Post(url=url, json=datas, headers=header)
        if res.status_code == 200:
            # return res.json()
            return res
        else:
            raise Exception("Call {0} interface failed !".format(interfaceUrl), res.text)


    def commonFuncGet(self, datas,header, interfaceUrl):
        # 发送登录请求，获取token

        url = "{0}/{1}".format(self.shopBaseUrl, interfaceUrl)
        # res = requests.post(url=url, json=datas, headers=headers)
        res = self.httpClient.GET(url=url, params=datas, headers=header)
        if res.status_code == 200:
            # return res.json()
            return res
        else:
            raise Exception("Call {0} interface failed !".format(interfaceUrl), res.text)
    def queryGoods(self,header,province,city, goodsType):
        '''遍历门店，返回不同活动的商品信息'''
        goodsList = []
        goods = GoodsDetail()
        params = {"list_search": {"type": 14, "activity_status": 9}, "method": "list"}
        if goodsType == "limitTime":
            params["list_search"]["type"] = 12
        elif goodsType == "groupWork":
            pass
        elif goodsType == "hotGoodsAct":
            params["list_search"]["type"] = 25
            params["list_search"]["activity_status"] = 22
        datas = {"need_commonly_used":False,"need_last_used":False,"need_address_info":True,"province":province,"city":city,"area":"","longitude":"108.948780","latitude":"34.222590","keywords":""}
        storeList = ExtractList().extract_list(datas=datas,header=header)
        if len(storeList) == 0:
            return
        for store in storeList["data"]["list"]:
            storeID = store["id"]
            print("storeID {0}".format(storeID))
            datas = {"origin_store_id": storeID}
            url = "gw-shop/app/v1/user/visit-extract"
            res = goods.commonFuncPost(datas,header,interfaceUrl=url)
            # print("visitExtractRes: {0}".format(res.json()))
            url = "gw-shop/app/v1/activity-center/activity-goods-list"
            res = goods.commonFuncPost(params, header,interfaceUrl=url)
            print("res.json()[data][list]: {0}".format(res.json()))
            if res.json()['code'] == 200:
                goodsList = res.json()["data"]["list"]
                if len(goodsList) != 0:
                    return goodsList

        return goodsList

    def genarateShareImg(self, skuID, header):
        """
        今日爆款生成爆款卡片
        :param skuID:
        :return:
        """
        # 3 热卖推荐 25 今日爆款
        datas = {"type": 3, "sku_id": skuID, "rule_id": 0}
        url = "{0}/gw-shop/app/v1/activity-center/generate-share-img".format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url, json=datas, headers=header)
        resJson = res.json()
        if res.status_code == 200 and resJson["code"] == 200 and resJson["message"] == "success":
            return resJson

    def goodsDetailQRCode(self, header, datas):
        url = "{0}/gw-shop/app/v1/app-code/goods-detail-qrcode".format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url, json=datas, headers=header)
        resJson = res.json()
        if res.status_code == 200 and resJson["code"] == 200 and resJson["message"] == "success":
            return resJson
        else:
            raise Exception("call {0} fail!".format(url),resJson)
