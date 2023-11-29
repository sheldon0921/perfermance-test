from tests.common.onLine.shopOrder import ShopOrder
from tests.common.onLineForSupermarket.city_distribution import City_distribution
from utils.readerFile import ReaderFile
from log.log import Logger
from tests.common.onLine.getGoodsSpu import GetGoodsSpu
from tests.common.onLineForSupermarket.extractList import ExtractList
from utils.readerIniFile import ReaderIniFile
import pytest
import allure
from time import sleep
from tests.common.sendRequest.sendRequestForOnline import SendRequestForOnline

@allure.feature("同城配送")
class Test_city_distribution:

    @pytest.fixture()
    def ini(self):
        self.order = ShopOrder()
        self.city = City_distribution()
        self.logger = Logger.Logger()
        self.getspu = GetGoodsSpu()
        self.extract = ExtractList()
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")
        yield self.order, self.logger

    @allure.story("同城配送sku")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_sku_city_delivery(self, enterpriseInfo, ini):
        '''获取同城配送SKU'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        res = self.city.sku_city_delivery(datas=None, enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        with allure.step(f"{enterpriName}同城配送sku商品"):
            assert res["code"] == 200
            assert res["message"] == "success"

    @allure.story("获取达达运费")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_get_delivery_freight(self, enterpriseInfo, ini):
        '''获取达达运费接口'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        param = {"store_id":156677198607168,"cargo_price":1500,"receiver_address":None,"cargo_weight":1,"expect_finish_time_limit":1624354200}
        res = self.city.get_delivery_freight(datas=param, enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        with allure.step(f"{enterpriName}达达运费"):
            assert res["code"] == 400000
            assert res["message"] == "wx city code 字段是必须的"

    @allure.story("获取同城配送商品列表")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_city_sku_list(self, enterpriseInfo, ini):
        '''同城配送商品列表'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        param = {"page":1,"search":{"keywords":"","sort":1,"delivery_type":3},"size":10}
        res = self.city.city_sku_list(datas=param, enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        with allure.step(f"{enterpriName}同城配送商品列表"):
            assert res["code"] == 200
            assert res["message"] == "success"

    @allure.story("获取同城配送详情")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_delivery_detail(self, enterpriseInfo, ini):
        '''获取同城配送详情'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        param = {"store_id":156677198607168}
        res = self.city.delivery_detail(datas=param, enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        with allure.step(f"{enterpriName}获取同城配送详情"):
            assert res["code"] == 200
            assert res["message"] == "success"
