from tests.common.sendRequest.sendRequestForOnline import SendRequestForOnline
from utils.readerIniFile import ReaderIniFile
from utils.readerFile import ReaderFile
from log.log import Logger


class Category(object):

    def __init__(self):
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")

    def categoryList(self, enterpriseInfo):
        sendRequest = SendRequestForOnline(enterpriseInfo)
        url = "{0}/gw-shop/app/v1/category/category-list".format(self.shopBaseUrl)
        param = {}
        return sendRequest.sendRequest(url=url, params=param)



