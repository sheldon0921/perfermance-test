from tests.common.sendRequest.getXrequestId import GetXRequestId
from tests.login.singletonHttpClient import SingletonHttpClient
from utils.readerIniFile import ReaderIniFile
from tests.login.httpclient import HttpClient
from utils.myRandom import MyRandom
from tests.login.login import Login
from utils.parseJson import ParseJson
from utils.myTime import Mytime
from log.log import Logger
import json


class SendRequest(object):

    def __init__(self):
        self.consoleUrl = ReaderIniFile.value(section="console_sys_info", key="consoleBaseUrl")
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")
        self.httpClient = SingletonHttpClient.get_instance()
        # self.httpClient = HttpClient()
        self.logger = Logger.Logger()

    def sendRequest(self, url: str, params: dict, method="Post"):
        """
        :param method: 请求方式
        :param url: 请求url
        :param params: 请求参数
        :return: 返回结果
        """
        if url.startswith(self.consoleUrl):
            if str(method).upper() == "POST":
                res = self.httpClient.Post(url=url, json=params)
            elif str(method).upper() == "GET":
                res = self.httpClient.GET(url=url, params=params)
        elif url.startswith(self.shopBaseUrl):
            if str(method).upper() == "POST":
                res = self.httpClient.Post(url=url, json=params)
            elif str(method).upper() == "GET":
                res = self.httpClient.GET(url=url, params=params)
        if res.status_code == 200:
            return res
        else:
            raise Exception("Call {0} interface failed !".format(url), res.text)


if __name__ == '__main__':
    myRequest = SendRequest()
    # 自动化脚本小程序接口测试
    url = "https://shop-api-crs.vchangyi.com/gw-shop/app/v1/category/category-list"
    params = {}
    print(myRequest.sendRequest(method="post", url=url, params=params).json())

    # # 自动化脚本后台接口测试
    # params = {"size":1000}
    # url = "https://crs-api.vchangyi.com/gw-console/v1/store/list"
    # print("store list: {0}".format(ParseJson.parseJson(myRequest.sendRequest(method="post", url=url, params=params).json(),"is_super_admin")))
