from tests.common.onLine.indexInfo import *
from utils.readerFile import ReaderFile
from log.log import Logger
from tests.common.onLine.getGoodsSpu import GetGoodsSpu
from tests.common.sendRequest.sendRequestForOnline import SendRequestForOnline
import json
import pytest
import allure


@allure.feature("小程序首页")
class Test_Index:

    @pytest.fixture()
    def ini(self):
        # 实例化对象

        self.logger = Logger.Logger()
        self.user = User()
        self.getspu = GetGoodsSpu()
        self.liveBroadCast = LiveBroadCast()
        self.tabRedHot = TabRedHot()
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")
        yield self.logger, self.user, self.liveBroadCast, self.tabRedHot

    @allure.story("查询用户详情")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    def test_get_user_detail(self, enterpriseInfo, ini):
        '''(首页接口)获取用户详细接口'''
        # print("unique enterprise info: {0}".format(enterpriseInfo))
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        if enterpriName == "徐福记优选官方商城":
            return
        # print("\nenterpriName: ", enterpriName, "enterpriseHash: ", enterpriseHash)
        with allure.step(f"{enterpriName}小程序首页获取用户信息"):
            res = self.user.get_user_detail(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        # print("user detail interface response msg:  ", res)
        assert res["code"] == 200
        assert res["message"] == "success"

    @allure.story("获取直播信息")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    def test_list_live_broadcast(self, enterpriseInfo, ini):
        '''(首页接口)获取直播信息接口'''
        # print("unique enterprise info: {0}".format(enterpriseInfo))
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        # goodsName = enterpriseInfo["goodsName"]
        # spu_id = enterpriseInfo["spu_id"]
        # sku_id = enterpriseInfo["sku_id"]
        # print("\nenterpriName: ", enterpriName, "enterpriseHash: ", enterpriseHash)
        datas = {"status":3,"top_from":1}
        with allure.step(f"{enterpriName}小程序首页获取直播信息"):
            res = self.liveBroadCast.list_live_broadcast(datas=datas,enterpriseID=enterpriseID,enterpriseHash=enterpriseHash)
        # print("list live broadcast interface response msg:  ", res)
        assert res["code"] == 200
        assert res["message"] == "success"

    @allure.story("获取热区信息")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    def test_get_tab_red_dot(self, enterpriseInfo, ini):
        '''(首页接口)获取热区接口'''
        # print("unique enterprise info: {0}".format(enterpriseInfo))
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        # spu_id = enterpriseInfo["spu_id"]
        # sku_id = enterpriseInfo["sku_id"]
        # print("\nenterpriName: ", enterpriName, "enterpriseHash: ", enterpriseHash)
        with allure.step(f"{enterpriName}小程序首页获取热区信息"):
            res = self.tabRedHot.get_tab_red_dot(enterpriseID=enterpriseID,enterpriseHash=enterpriseHash)
        # print("get red dot interface response msg:  ", res)
        assert res["code"] == 200
        assert res["message"] == "success"


    @allure.story("初试化配置")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    def test_initial_setting(self, enterpriseInfo, ini):
        sendRequest = SendRequestForOnline(enterpriseInfo)
        url = "{0}/gw-shop/app/v1/common/initial-setting".format(self.shopBaseUrl)
        param = {"app_id":"wx7f6bf1836bd694ac","scene":1007,"page":"pages/index/index","options":"scene=1007&path=pages/index/index&query=%7B%22open_id%22:%22oJnCX5KQSZ2or4xUanoOo7Bd9-fw%22,%22share%22:%221%22,%22share_uid%22:%22131822439329728%22,%22source%22:%22shop%22,%22user_id%22:%22131822439329728%22%7D&referrerInfo=%22%22&shareTicket=%22%22"}
        res = sendRequest.sendRequest(url=url,params=param)
        assert res.json()["code"] == 200

    @allure.story("page/pop-content接口")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    def test_pop_content(self, enterpriseInfo, ini):
        sendRequest = SendRequestForOnline(enterpriseInfo)
        url = "{0}/gw-shop/app/v1/page/pop-content".format(self.shopBaseUrl)
        param = {"type":1}
        res = sendRequest.sendRequest(url=url,params=param)
        assert res.json()["code"] == 200

    @allure.story("页面配置接口")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    def test_initial_setting(self, enterpriseInfo, ini):
        sendRequest = SendRequestForOnline(enterpriseInfo)
        url = "{0}/gw-shop/app/v1/new-template/page-config".format(self.shopBaseUrl)
        param = {"template_type":"index"}
        res = sendRequest.sendRequest(url=url,params=param)
        print(res.json())
        assert res.json()["code"] == 200
