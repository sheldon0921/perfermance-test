from tests.login.httpclient import HttpClient
from tests.login.singletonHttpClient import SingletonHttpClient
from utils.readerIniFile import ReaderIniFile
from log.log import Logger
from utils.readerFile import ReaderFile


class Stock(object):

    def __init__(self):
        """
            实例化日志对象和http请求对象,从配置文件中获取请求接口的域名；
        """
        self.logger = Logger.Logger()
        # self.httpclient = HttpClient()
        self.httpclient = SingletonHttpClient.get_instance()
        # self.consoleUrl = ReaderConfig.value(section="console_sys_info", key="consoleBaseUrl")
        # self.logger.info("url is: {0} ".format(self.consoleUrl))
        self.shopUrl = ReaderIniFile.value(key="shopBaseUrl")
        self.consoleUrl = ReaderIniFile.value(section="console_sys_info", key="consoleBaseUrl")

    def queryStockList(self,param):
        """
        查询库存管理的物料信息
        :param param: {"page":1,"size":10,"first_value":"","first_type":"all","second_type":"all","min_value":"","max_value":"","source_id":0,"time_type":"create","start_time":"","end_time":""}
        :return: 返回所有的物料列表
        """
        url = "{0}/gw-console/v1/material/list".format(self.consoleUrl)
        res = self.httpclient.Post(url=url, json=param)
        resInfo = res.json()
        if res.status_code == 200 and resInfo["message"] == "success":
            return resInfo["data"]["list"]
        else:
            raise Exception('query meterial list interface fail !', res.text)

    def updateChannelStock(self,param):
        """
        修改待上架的商品库存
        :param param: {"source_id":133,"type":"3","online":2,"number":"200","sku_id":140619507020544}
        :return:
        """
        url = "{0}/gw-console/v1/material-channel/update-channel-stock".format(self.consoleUrl)
        res = self.httpclient.Post(url=url, json=param)
        resInfo = res.json()
        if res.status_code == 200:
            return resInfo
        else:
            raise Exception('update channel stock interface fail !', res.text)