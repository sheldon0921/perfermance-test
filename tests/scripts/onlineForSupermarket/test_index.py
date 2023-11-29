from tests.common.onLineForSupermarket.indexInfo import *
from tests.common.onLineForSupermarket.extractList import *
from utils.readerFile import ReaderFile
from log.log import Logger
from pytest import assume
# from tests.common.onLineForSupermarket.getGoodsSpu import GetGoodsSpu
import json
import pytest

import allure


@allure.feature("(商超)小程序首页")
class Test_Index:

    @pytest.fixture()
    def ini(self):
        # 实例化对象
        self.logger = Logger.Logger()
        self.user = User()
        self.liveBroadCast = LiveBroadCast()
        self.tabRedHot = TabRedHot()
        self.popContent = PopContent()
        self.initialSetting = InitialSetting()
        self.shopShareImage = ShopShareImage()
        self.commonConfig = CommonConfig()
        self.pageConfig = PageConfig()
        self.userExtractOrder = UserExtractOrder()
        self.writeTrace = WriteTrace()
        self.list = ExtractList()
        self.data = {"user_latitude": "34.222590", "user_longitude": "108.948780"}
        yield self.list, self.logger, self.user, self.liveBroadCast, self.tabRedHot, self.popContent, self.initialSetting, self.shopShareImage, self.commonConfig, self.pageConfig, self.userExtractOrder, self.writeTrace

    @allure.story("查询用户详情")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_get_user_detail(self, enterpriseInfo, ini):
        '''(首页接口)获取用户详细接口'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        with allure.step(f"{enterpriName}小程序首页获取用户信息"):
            res = self.user.get_user_detail(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        assert res["code"] == 200
        assert res["message"] == "success"

    @allure.story("获取直播信息")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_list_live_broadcast(self, enterpriseInfo, ini):
        '''(首页接口)获取直播信息接口'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        datas = {"status": 3, "top_from": 1}
        with allure.step(f"{enterpriName}小程序首页获取直播信息"):
            res = self.liveBroadCast.list_live_broadcast(datas=datas, enterpriseID=enterpriseID,
                                                         enterpriseHash=enterpriseHash)
        assert res["code"] == 200
        assert res["message"] == "success"

    @allure.story("获取热区信息")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_get_tab_red_dot(self, enterpriseInfo, ini):
        '''(首页接口)获取热区接口'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        with allure.step(f"{enterpriName}小程序首页获取热区信息"):
            res = self.tabRedHot.get_tab_red_dot(enterpriseID=enterpriseID, enterpriseHash=enterpriseHash)
        assert res["code"] == 200
        assert res["message"] == "success"

    @allure.story("启动页合并优化")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_initial_Setting(self, enterpriseInfo, ini):
        '''(首页接口)启动页合并优化接口'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        datas = {"scene": 1001, "page": "pages/index/index",
                 "options": "scene=1001&path=pages/index/index&query=%22%22&referrerInfo=%22%22&shareTicket=%22%22"}
        with allure.step(f"{enterpriName}小程序首页启动页合并优化接口"):
            res = self.initialSetting.initial_Setting(datas=datas, enterpriseID=enterpriseID,
                                                      enterpriseHash=enterpriseHash)
        assert res["code"] == 200
        assert res["message"] == "success"

    #
    @allure.story("小程序分享商城")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_shop_share_image(self, enterpriseInfo, ini):
        '''(首页接口)小程序分享商城接口'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]

        with allure.step(f"{enterpriName}小程序分享商城接口"):
            res = self.shopShareImage.shop_share_image(enterpriseID=enterpriseID,
                                                       enterpriseHash=enterpriseHash)
        assert res["code"] == 200
        assert res["message"] == "success"

    @allure.story("获取配置信息")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_common_config(self, enterpriseInfo, ini):
        '''(首页接口)获取配置信息接口'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]

        with allure.step(f"{enterpriName}获取配置信息接口"):
            res = self.commonConfig.common_config(enterpriseID=enterpriseID,
                                                  enterpriseHash=enterpriseHash)
        assert res["code"] == 200
        assert res["message"] == "success"

    @allure.story("小程序页面模板")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_page_config(self, enterpriseInfo, ini):
        '''(首页接口)小程序页面模板接口'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        res = self.list.extract_list(self.data, header)
        lst = res["data"]["list"]
        extract_id = lst[0]["id"]
        data1 = {"extract_id": extract_id, "template_type": "index"}
        with allure.step(f"{enterpriName}小程序页面模板接口"):
            res = self.pageConfig.page_config(data1, header)
        assert res["code"] == 200
        assert res["message"] == "success"

    #
    @allure.story("用户待自提订单")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_user_extract_order(self, enterpriseInfo, ini):
        '''(首页接口)用户待自提订单接口'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]

        with allure.step(f"{enterpriName}用户待自提订单接口"):
            res = self.userExtractOrder.user_extract_order(enterpriseID=enterpriseID,
                                                           enterpriseHash=enterpriseHash)
        assert res["code"] == 200
        assert res["message"] == "success"

    #
    @allure.story("链路信息记录")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_write_trace(self, enterpriseInfo, ini):
        '''(首页接口)链路信息记录接口'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        params = {"action": "access"}
        with allure.step(f"{enterpriName}链路信息记录接口"):
            res = self.writeTrace.write_trace(enterpriseID=enterpriseID, enterpriseHash=enterpriseHash, params=params)
        assert res["code"] == 200
        assert res["message"] == "success"

    @allure.story("查询区域")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_get_region_list(self, enterpriseInfo, ini):
        '''(首页接口)获取区域列表'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        with allure.step(f"{enterpriName}小程序首页获取区域列表信息"):
            res = self.list.region_list(header=header, datas={})
            print("res: {0}".format(res))
        with assume: assert res["code"] == 200
        with assume: assert res["message"] == "success"
        with assume: assert len(res["data"]["list"]) is not 0


    @allure.story("解析traceId")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_decrypt_trace(self,ini,enterpriseInfo):
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        res = self.writeTrace.getAgreements(header)
        with assume: assert res["code"] == 200
        with assume: assert res["message"] == "success"

    @allure.story("首页模板")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_decrypt_trace(self,ini,enterpriseInfo):
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        param = {
            "extract_id": 163756566480896,
            "store_id": 163756561136128,
            "last_id": 0
        }
        res = self.writeTrace.newTemplateIndex(header,param)
        with assume: assert res["code"] == 200
        with assume: assert res["message"] == "success"


    @allure.story("分类列表")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_category_list(self,ini,enterpriseInfo):
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        header["content-type"] = "application/x-www-form-urlencoded"
        param = {}
        res = self.writeTrace.categoryList(header,param)
        with assume: assert res["code"] == 200
        with assume: assert res["message"] == "success"


    @allure.story("删除商品足迹")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_clean_goodsFoot(self,ini,enterpriseInfo):
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        param = {}
        res = self.writeTrace.cleanGoodsFoot(header,param)
        with assume: assert res["code"] == 200
        with assume: assert res["message"] == "success"


    @allure.story("积分记录")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_score_log(self,ini,enterpriseInfo):
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        param = {"page":1,"size":15}
        res = self.writeTrace.scoreLog(header,param)
        with assume: assert res["code"] == 200
        with assume: assert res["message"] == "success"


    @allure.story("更新个人信息")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_score_log(self,ini,enterpriseInfo):
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        param = {"avatar":"https://img-crs.vchangyi.com/2021/09/01/2a4d0942bd1f7705f4b0e1bb4a383703.png","real_name":"123"}
        res = self.writeTrace.userCenterEdit(header,param)
        with assume: assert res["code"] == 200
        with assume: assert res["message"] == "success"


    @allure.story("自提码列表")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_score_log(self,ini,enterpriseInfo):
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        param = {"avatar":"https://img-crs.vchangyi.com/2021/09/01/2a4d0942bd1f7705f4b0e1bb4a383703.png","real_name":"123"}
        res = self.writeTrace.mentionCode(header,param)
        with assume: assert res["code"] == 200
        with assume: assert res["message"] == "success"


    @allure.story("自提码列表")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_initial_setting(self,ini,enterpriseInfo):
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        param = {"app_id":"wxc6d01454c8d8aeea","scene":1001,"page":"pages/index/index","options":"scene=1001&path=pages/index/index&query=%7B%7D&referrerInfo=%22%22&shareTicket=%22%22"}
        res = self.writeTrace.initialSetting(header,param)
        with assume: assert res["code"] == 200
        with assume: assert res["message"] == "success"


    # @allure.story("自提码列表")
    # @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    # def test_check_time(self,ini,enterpriseInfo):
    #     self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
    #     enterpriName = enterpriseInfo["enterpriName"]
    #     enterpriseID = enterpriseInfo["enterpriseID"]
    #     enterpriseHash = enterpriseInfo["enterpriseHash"]
    #     header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
    #     param = {"time":"1631001121"}
    #     res = self.writeTrace.checkTime(header,param)
    #     with assume: assert res["code"] == 200
    #     with assume: assert res["message"] == "success"



    # @allure.story("获取文案")
    # @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    # def test_getAccess_token(self,ini,enterpriseInfo):
    #     self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
    #     enterpriName = enterpriseInfo["enterpriName"]
    #     enterpriseID = enterpriseInfo["enterpriseID"]
    #     enterpriseHash = enterpriseInfo["enterpriseHash"]
    #     header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
    #     param = {"type": 1}
    #     res = self.popContent(header,param)
    #     with assume: assert res["code"] == 200
    #     with assume: assert res["message"] == "success"


    @allure.story("根据关键词输入获取地址")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_addressByKeywords(self,ini,enterpriseInfo):
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        param = {
                    "keywords": "钟楼",
                    "region": "西安"
                }
        res = self.writeTrace.addressByKeywords(header,param)
        with assume: assert res["code"] == 200
        with assume: assert res["message"] == "success"


    @allure.story("根据关键词输入获取地址")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_locationByIP(self,ini,enterpriseInfo):
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        param = {
                    "ip": "1.85.216.132"
                }
        if enterpriName == "三优爱家":
            res = self.writeTrace.locationByIp(header,param)
            with assume: assert res["code"] == 200
            with assume: assert res["message"] == "success"


    @allure.story("地址解析")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_locationByIP(self,ini,enterpriseInfo):
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        param = {
                    "address": "陕西省西安市碑林区太白南路"
                }
        # if enterpriName == "三优爱家":
        res = self.writeTrace.addressAnalysis(header,param)
        with assume: assert res["code"] == 200
        with assume: assert res["message"] == "success"