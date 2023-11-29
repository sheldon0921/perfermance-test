from tests.login.singletonHttpClient import SingletonHttpClient
from utils.readerIniFile import ReaderIniFile
from utils.myRandom import MyRandom
from tests.login.login import Login
from utils.myTime import Mytime
import json


class NewIndex:
    httpClient = SingletonHttpClient.get_instance(flag="onLine")
    shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")

    @staticmethod
    def newTemplatePageConfig(header, param):
        params = {"extract_id": param, "template_type": "index", "sign": "1faaf5ebc918fecb229160433d1a8961"}
        location = "/gw-shop/app/v1/new-template/page-config"
        url = "{0}{1}".format(NewIndex.shopBaseUrl, location)
        res = NewIndex.httpClient.Post(url=url, headers=header, json=params)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call {0} !".format(location), res.text)

    @staticmethod
    def categorySearchSpuList(header, param):
        params = {"category_id": param, "page": 1, "size": 10, "sort_field": "default", "sort": "DESC"}
        location = "/gw-shop/app/v1/goods/category-search-spu-list"
        url = "{0}{1}".format(NewIndex.shopBaseUrl, location)
        res = NewIndex.httpClient.Post(url=url, headers=header, json=params)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call {0} !".format(location), res.text)


    @staticmethod
    def newTemplateFlashSale(header, params):
        # params = {"category_id": param, "page": 1, "size": 10, "sort_field": "default", "sort": "DESC"}
        location = "/gw-shop/app/v1/new-template/flash-sale"
        url = "{0}{1}".format(NewIndex.shopBaseUrl, location)
        res = NewIndex.httpClient.Post(url=url, headers=header, json=params)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call {0} !".format(location), res.text)

    @staticmethod
    def actGoodsLstForFlaseSale(header, param):
        """
        限时购专题页
        """
        params = {"activity_rule_id": param, "list_search": {"type": 12, "activity_status": 9}, "is_new": 1,
                  "method": "list", "page": 1, "size": 10}
        location = "/gw-shop/app/v1/activity-center/activity-goods-list"
        url = "{0}{1}".format(NewIndex.shopBaseUrl, location)
        res = NewIndex.httpClient.Post(url=url, headers=header, json=params)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call {0} !".format(location), res.text)

    @staticmethod
    def actGoodsLstForTodayHot(header):
        """
        限时购专题页
        """
        params = {"method":"list","list_search":{"type":25,"activity_status":22},"page":1,"size":10}
        location = "/gw-shop/app/v1/activity-center/activity-goods-list"
        url = "{0}{1}".format(NewIndex.shopBaseUrl, location)
        res = NewIndex.httpClient.Post(url=url, headers=header, json=params)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call {0} !".format(location), res.text)

    @staticmethod
    def actGoodsLstForPT(header):
        """
        拼团专题页
        """
        params = {"list_search": {"type": 14, "activity_status": 9}, "method": "list", "page": 1, "size": 10}
        location = "/gw-shop/app/v1/activity-center/activity-goods-list"
        url = "{0}{1}".format(NewIndex.shopBaseUrl, location)
        res = NewIndex.httpClient.Post(url=url, headers=header, json=params)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call {0} !".format(location), res.text)

    @staticmethod
    def groupSearchSpuList(header, categoryId):
        params = {"category_id": categoryId, "page": 1, "size": 10}
        location = "/gw-shop/app/v1/goods/group-search-spu-list"
        url = "{0}{1}".format(NewIndex.shopBaseUrl, location)
        res = NewIndex.httpClient.Post(url=url, headers=header, json=params)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call {0} !".format(location), res.text)

    @staticmethod
    def categoryLevel(header):
        params = {}
        location = "/gw-shop/app/v1/category/category-level"
        url = "{0}{1}".format(NewIndex.shopBaseUrl, location)
        res = NewIndex.httpClient.Post(url=url, headers=header, json=params)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call {0} !".format(location), res.text)


    @staticmethod
    def storeCartModel(header):
        params = {}
        location = "/gw-shop/app/v1/store-cart/store-cart-model"
        url = "{0}{1}".format(NewIndex.shopBaseUrl, location)
        res = NewIndex.httpClient.Post(url=url, headers=header, json=params)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call {0} !".format(location), res.text)

    @staticmethod
    def newBuyAct(header,categoryId):
        params = {"page":1,"size":999,"activity_rule_id":categoryId,"list_search":{"type":11}}
        location = "/gw-shop/app/v1/new-template/new-buy"
        url = "{0}{1}".format(NewIndex.shopBaseUrl, location)
        res = NewIndex.httpClient.Post(url=url, headers=header, json=params)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call {0} !".format(location), res.text)


if __name__ == '__main__':
    NewIndex.newTemplatePageConfig()
