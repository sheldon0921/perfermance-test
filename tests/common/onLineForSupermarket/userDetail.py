from tests.login.singletonHttpClient import SingletonHttpClient
from utils.readerIniFile import ReaderIniFile


class UserDetail:

    httpClient = SingletonHttpClient.get_instance(flag="onLine")
    shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")

    @staticmethod
    def getUserDetail(header):
        url = '{0}/gw-shop/app/v1/user/detail'.format(UserDetail.shopBaseUrl)
        res = UserDetail.httpClient.GET(url=url,headers=header)
        if res.status_code == 200:
            rJson = res.json()
            return res.json()
        else:
            raise Exception("call {0} failed".format(url),res.json())