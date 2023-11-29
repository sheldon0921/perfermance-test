import os
from tests.login.httpclient import HttpClient
from tests.login.singletonHttpClient import SingletonHttpClient
from utils.readerIniFile import ReaderIniFile
from log.log import Logger
from utils.readerFile import ReaderFile
from tests.common.goods.console.specTemplate import SpecTemplate
from tests.common.goods.console.postage import Postage
from utils.myTime import Mytime
from utils.myJson import MyJson
from utils.myRandom import MyRandom

class Order(object):

    def __init__(self):
        """
            实例化日志对象和http请求对象,从配置文件中获取请求接口的域名；
        """
        self.mytime = Mytime()
        self.logger = Logger.Logger()
        # self.httpclient = HttpClient()
        self.httpclient = SingletonHttpClient.get_instance()
        # self.consoleUrl = ReaderConfig.value(section="console_sys_info", key="consoleBaseUrl")
        # self.logger.info("url is: {0} ".format(self.consoleUrl))
        self.specTemplate = SpecTemplate()
        self.postage = Postage()
        self.shopUrl = ReaderIniFile.value(key="shopBaseUrl")
        self.consoleUrl = ReaderIniFile.value(section="console_sys_info", key="consoleBaseUrl")

    def queryOrder(self, param):
        '''
        查询后台订单
        :param param: 订单编号
        :return: 返回json格式数据
        '''
        url = '{0}/gw-console/v1/order/list'.format(self.consoleUrl)
        res = self.httpclient.Post(url=url, json=param)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception('queryOrder fail', res.text)