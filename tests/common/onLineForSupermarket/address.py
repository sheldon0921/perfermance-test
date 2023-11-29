from tests.login.login import Login
from tests.login.singletonHttpClient import SingletonHttpClient
from utils.readerIniFile import ReaderIniFile
from utils.myTime import Mytime
from utils.myRandom import MyRandom


class Address(object):

    httpClient = SingletonHttpClient.get_instance(flag="onLine")
    shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")
    consoleUrl = ReaderIniFile.value(section="console_sys_info", key="consoleBaseUrl")

    @staticmethod
    def addAddress(header,data):
        location = "/gw-shop/app/v1/user/address-add"
        url = "{0}{1}".format(Address.shopBaseUrl,location)
        res = Address.httpClient.Post(url=url,headers=header,json=data)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("call {0} failed !".format(location),res.text)

    @staticmethod
    def delAddress(header,data):
        location = "/gw-shop/app/v1/user/address-delete"
        url = "{0}{1}".format(Address.shopBaseUrl,location)
        res = Address.httpClient.Post(url=url,headers=header,json=data)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("call {0} failed !".format(location),res.text)

    @staticmethod
    def searchAddress(header,data):
        location = "/gw-shop/app/v1/user/address-search"
        url = "{0}{1}".format(Address.shopBaseUrl,location)
        res = Address.httpClient.Post(url=url,headers=header,json=data)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("call {0} failed !".format(location),res.text)

    @staticmethod
    def addressByLocation(header,data):
        location = "/gw-shop/app/v1/map/address-by-location"
        url = "{0}{1}".format(Address.shopBaseUrl,location)
        res = Address.httpClient.Post(url=url,headers=header,json=data)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("call {0} failed !".format(location),res.text)

