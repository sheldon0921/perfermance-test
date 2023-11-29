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


class Stock(object):

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

    def matterInport(self,file):
        '''
        物料导入
        :param file: 参数类型为files，上传excel文件
        :return: 返回json格式数据
        '''
        url='{0}/gw-console/v1/warehouse/import-material'.format(self.consoleUrl)
        res=self.httpclient.Post(url=url,files=file)
        if res.status_code == 200 :
            return res.json()
        else:
            raise Exception('matterImport fail',res.text)

    def queryStockList(self,param):
        """
        查询库存管理的物料信息
        :param param: {"page":1,"size":10,"first_value":"","first_type":"all","second_type":"all","min_value":"","max_value":"","source_id":0,"time_type":"create","start_time":"","end_time":""}
        :return: 返回所有的物料列表
        """
        url = "{0}/gw-console/v1/material/list".format(self.consoleUrl)
        res = self.httpclient.Post(url=url, json=param)
        if res.status_code == 200 :
            return res.json()
        else:
            raise Exception('query meterial list interface fail !', res.text)
    def queryWarehouseId(self):
        """
        查询仓库ID
        """
        param = {"page":1,"size":10}
        url = '{0}/gw-console/v1/warehouse/list'.format(self.consoleUrl)
        res = self.httpclient.Post(url=url,json=param)
        if res.status_code == 200 :
            return res.json()['data']['list'][0]['id']
        else:
            raise Exception('query warehouse list interface fail !', res.text)

if __name__ == '__main__':
    print(Stock().queryWarehouseId())