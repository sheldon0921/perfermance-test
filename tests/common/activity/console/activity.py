from tests.login.singletonHttpClient import SingletonHttpClient
from tests.common.goods.console.goods import Goods
from utils.readerIniFile import ReaderIniFile
from utils.readerFile import ReaderFile
from utils.myRandom import MyRandom
from utils.myTime import Mytime
from log.log import Logger
import time


class Activity(object):

    def __init__(self):
        self.mytime = Mytime()
        self.logger = Logger.Logger()
        self.goods = Goods()
        self.httpclient = SingletonHttpClient.get_instance()
        self.shopUrl = ReaderIniFile.value(key="shopBaseUrl")
        self.consoleUrl = ReaderIniFile.value(section="console_sys_info", key="consoleBaseUrl")

    def createActivity(self, createParam):
        """
        创建活动
        :param createParam: 创建活动的参数
        :return:
        """
        url = f"{self.consoleUrl}/gw-console/v1/activity-common/activity"
        createParam["name"] = createParam["name"]+Mytime.getCurrTime()+MyRandom.getRandomStr(4)
        createParam["start_at"] = Mytime.getCurrTimeStamp()
        time.sleep(10)
        createParam["end_at"] = Mytime.getCurrTimeStamp()
        res = self.httpclient.Post(url=url, data=createParam)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception('call activity-common/activity interface fail !', res.text)


if __name__ == '__main__':
    # activity = Activity()
    # activity
    print(Mytime.getCurrTimeStamp())
    time.sleep(10)
    print(Mytime.getCurrTimeStamp())