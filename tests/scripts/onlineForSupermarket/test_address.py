from tests.common.onLineForSupermarket.address import Address
from tests.common.onLineForSupermarket.extractList import ExtractList
from utils.readerFile import ReaderFile
import json, pytest, allure, time
from log.log import Logger
from pytest import assume


class Test_address():

    logger = Logger.Logger()
    extractList = ExtractList()

    @pytest.fixture(scope="class", autouse=True)
    def ini(self):
        pass

    @allure.story("添加/删除地址")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_add_address(self,enterpriseInfo):
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        header = self.extractList.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        '''搜索地址'''
        data = {"keywords": "西安市政府", "region": "西安市", "store_id": 134065216855296}
        searchRes = Address.searchAddress(header,data)
        with assume: assert searchRes["code"] == 200
        with assume: assert searchRes["message"] == "success"
        '''添加地址'''
        data = {"id":0,"other_info":"2302","short_name":"西安市政府","province":"陕西省","city":"西安市","area":"未央区","address":"凤城八路109号","source":"2","default":"2","delivery_name":"章雨","delivery_mobile":"18476852465","lat":"34.343118809","lng":"108.939630405","type":"city_delivery"}
        res = Address.addAddress(header,data)
        with assume: assert res["code"] == 200
        with assume: assert res["message"] == "success"
        addressId = res["data"]["id"]
        '''删除地址'''
        data = {"id":addressId}
        delRes = Address.delAddress(header,data)
        with assume: assert delRes["code"] == 200
        with assume: assert delRes["message"] == "success"

    @allure.story("定位当前地址")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_addressByLocation(self,enterpriseInfo,ini):
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        header = self.extractList.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        param = {"lng":"108.948780","lat":"34.222590"}
        res = Address.addressByLocation(header,param)
        assert res["code"] == 200 \
               and res["message"] == "success"
