from tests.login.httpclient import HttpClient
from tests.login.singletonHttpClient import SingletonHttpClient
from utils.readerIniFile import ReaderIniFile
from log.log import Logger
from utils.readerFile import ReaderFile


class Goods(object):

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

    def queryGoodsDetail(self, param):
        """
        查询商品接口
        :param param: 请求接口参数;
        :return: 商品详情接口返回的数据
        """
        url = "{0}/gw-shop/app/v1/goods/detail".format(self.shopUrl)
        res = self.httpclient.Post(url=url, json=param)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception('call query goods interface fail !', res.text)

    # def addGoods(self, param):
    #     """
    #     新增商品接口
    #     :param param: 新增商品参数
    #     :return:
    #     """
    #     url = "{0}/gw-console/v1/goods/save".format(self.consoleUrl)
    #     res = self.httpclient.Post(url=url, json=param)
    #     if res.status_code == 200:
    #         return res
    #     else:
    #         raise Exception('add goods interface fail !', res.text)

    def queryGoodsByGoodsName(self,goodsName):
        param = {
            "category_id": 0,
            "page": 1,
            "size": 10,
            "sort_field": "default",
            "sort": "DESC",
            "keywords": goodsName
        }
        url = "{0}/gw-shop/app/v1/goods/spu-list".format(self.shopUrl)
        res = self.httpclient.GET(url=url, params=param)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception('call query goods interface fail !', res.text)


if __name__ == '__main__':
    goodsname = "大头盔6660308125251"
    print("33333333333",Goods().queryGoodsByGoodsName(goodsname))
    # sku_id=126995906483968
    # spu_id=126995906386624
    # params = {"spu_id":spu_id,  "sku_id":sku_id, "api_type":1}
    # print(Goods().queryGoods(params))