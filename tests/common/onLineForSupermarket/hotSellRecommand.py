from tests.login.singletonHttpClient import SingletonHttpClient
from utils.readerIniFile import ReaderIniFile
import time


class HotSellRecommand():

    httpClient = SingletonHttpClient.get_instance(flag="onLine")
    shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")

    def activityRobotUser(self, header, datas):
        locator = "/gw-shop/app/v1/activity-center/activity-robot-user"
        url = "{0}{1}".format(self.shopBaseUrl,locator)
        res = self.httpClient.Post(url=url, headers=header, json=datas)
        time.sleep(2)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call {0} failed !".format(locator), res.text)