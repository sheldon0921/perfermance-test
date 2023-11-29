from tests.common.sendRequest.sendRequestForOnline import SendRequestForOnline
from utils.readerIniFile import ReaderIniFile
from utils.readerFile import ReaderFile
from log.log import Logger
import json


class CategoryForSm(object):

    def __init__(self):
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")

    def categoryList(self, enterpriseInfo):
        sendRequest = SendRequestForOnline(enterpriseInfo)
        url = "{0}/gw-shop/app/v1/category/category-list".format(self.shopBaseUrl)
        return sendRequest.sendRequest(url=url, params=None,version="supermarket")

    def categoryData(self, enterpriseInfo,pId):
        sendRequest = SendRequestForOnline(enterpriseInfo)
        param = {"category_id": pId, "page": 1, "size": 100}
        url = "{0}/gw-shop/app/v1/goods/spu-list".format(self.shopBaseUrl)
        return sendRequest.sendRequest(url=url, params=param, method="get",version="supermark").json()


