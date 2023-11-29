from tests.common.onLineForSupermarket.extractList import *
from utils.readerFile import ReaderFile
from log.log import Logger
# from tests.common.onLineForSupermarket.getGoodsSpu import GetGoodsSpu
import json
import pytest

import allure


@allure.feature("(商超)选择门店列表页")
class Test_Index:

    @pytest.fixture()
    def ini(self):
        # 实例化对象
        self.logger = Logger.Logger()
        self.list = ExtractList()

        yield self.logger, self.list

    @allure.story("查询自提门店列表")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_get_extract_list(self, enterpriseInfo, ini):
        '''(选择门店列表接口)自提门店列表接口'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        datas = {"need_commonly_used":True,"need_last_used":True,"need_address_info":True,"province":"","city":"","area":"","longitude":"108.948780","latitude":"34.222590","keywords":""}
        with allure.step(f"{enterpriName}小程序自提门店列表接口"):
            res = self.list.extract_list(datas,header)
        print("user detail interface response msg:  ", res)
        assert res["code"] == 200
        assert res["message"] == "success"

    @allure.story("查询区域列表")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_get_region_list(self, enterpriseInfo, ini):
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        with allure.step(f"{enterpriName}小程序自提门店列表接口"):
            res = self.list.region_list(datas=None, header=header)
        print("user detail interface response msg:  ", res)
        assert res["code"] == 200
        assert res["message"] == "success"

    @allure.story("查询区域列表")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_mini_subscribe_record(self, enterpriseInfo, ini):
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        data = {
                "object_id": 0,
                "object_type": "16",
                "type": 1,
                "touch_id": "mall-index-subscribeNewFu",
                "pri_tmpl_id": [
                    "KdIobjdcDJbCgCA6awupC-qtzAjZi1g7KbbpE69nJ1o",
                    "mujnS2hON1sW92DmMXdB71kddsC1J7P3mHYZxsDkguk"
                ],
                "store_id": 172107231852864,
                "page_query": {
                    "extract_id": 172107232412096
                }
            }
        with allure.step(f"{enterpriName}小程序自提门店列表接口"):
            res = self.list.mini_subscribe_record(datas=data, headers=header)
        print("user detail interface response msg:  ", res)
        assert res["code"] == 200
        assert res["message"] == "success"