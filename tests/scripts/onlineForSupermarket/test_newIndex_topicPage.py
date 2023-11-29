from tests.common.onLineForSupermarket.extractList import ExtractList
from tests.common.onLineForSupermarket.indexInfo import VisitExtract
from tests.common.onLineForSupermarket.newIndex import NewIndex
from utils.readerIniFile import ReaderIniFile
from utils.readerFile import ReaderFile
from utils.parseJson import ParseJson
from log.log import Logger
import json, pytest, allure


@allure.feature("(商超)购物车")
class Test_shop_cart:
    shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")

    # httpClient = SingletonHttpClient.get_instance()

    @pytest.fixture()
    def ini(self):
        # 实例化对象
        self.logger = Logger.Logger()
        self.list = ExtractList()
        self.newIndex = NewIndex()
        self.visit = VisitExtract()
        yield self.logger

    @allure.story("购物车更新")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_newTemplate_pageConfig(self, enterpriseInfo, ini):
        '''商品详情页自提点列表'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        if enterpriName != "晋锋优购" and enterpriName != "YJ渝教爱家":
            return
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        param = {
            "need_commonly_used": True,
            "need_last_select": True,
            "need_address_info": True,
            "province": province,
            "city": city,
            "longitude": "108.948780",
            "latitude": "34.222590",
            "keywords": "",
            "current_extract_id": 0,
            "is_filter_invalid": False
        }
        res = self.list.extract_list(param, header)
        extractId = res["data"]["list"][0]["id"]
        res = self.newIndex.newTemplatePageConfig(header, extractId)
        assert res["code"] == 200 and res["message"] == "success"
        param = {"origin_store_id": extractId}
        self.visit.visit_extract(param, header)
        try:
            categoryId = res["data"]["group_goods_data"][0]["id"]
            spuListRes = self.newIndex.categorySearchSpuList(header, categoryId)
            print(spuListRes)
            assert spuListRes["code"] == 200 and spuListRes["message"] == "success"
            assert len(spuListRes["data"]["list"]) > 0
        except KeyError as e:
            pass


    @allure.story("限时购组件数据")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_newTemplate_flashSale(self, enterpriseInfo, ini):
        '''商品详情页自提点列表'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        if enterpriName == "晋锋优购" or enterpriName == "YJ渝教爱家":
            return
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        param = {
            "need_commonly_used": True,
            "need_last_select": True,
            "need_address_info": True,
            "province": province,
            "city": city,
            "longitude": "108.948780",
            "latitude": "34.222590",
            "keywords": "",
            "current_extract_id": 0,
            "is_filter_invalid": False
        }
        res = self.list.extract_list(param, header)
        extractId = res["data"]["list"][0]["id"]
        res = self.newIndex.newTemplatePageConfig(header, extractId)
        assert res["code"] == 200 and res["message"] == "success"
        param = {"origin_store_id": extractId}
        self.visit.visit_extract(param, header)
        try:
            flashSaleActLst = res["data"]["time_to_buy_new_data"]
            if len(flashSaleActLst) == 0:
                return
            else:
                for act in flashSaleActLst:
                    actRuleId = act["activity_rule_id"]
                    if len(act["sku_list"]) > 0:
                        actRuleId = act["activity_rule_id"]
                        break

            param = {"rule_id": actRuleId, "extract_id": extractId}
            flashSaleList = self.newIndex.newTemplateFlashSale(header, param)
            assert flashSaleList["code"] == 200 and flashSaleList["message"] == "success"
            assert len(flashSaleList["data"]) >= 0
        except KeyError as e:
            pass

    @allure.story("限时购专题页")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_flashSale_topicPage(self, enterpriseInfo, ini):
        '''商品详情页自提点列表'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        if enterpriName == "晋锋优购" or enterpriName == "YJ渝教爱家":
            return
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        param = {
            "need_commonly_used": True,
            "need_last_select": True,
            "need_address_info": True,
            "province": province,
            "city": city,
            "longitude": "108.948780",
            "latitude": "34.222590",
            "keywords": "",
            "current_extract_id": 0,
            "is_filter_invalid": False
        }
        res = self.list.extract_list(param, header)
        extractId = res["data"]["list"][0]["id"]
        res = self.newIndex.newTemplatePageConfig(header, extractId)
        assert res["code"] == 200 and res["message"] == "success"
        param = {"origin_store_id": extractId}
        self.visit.visit_extract(param, header)
        try:
            flashSaleActLst = res["data"]["time_to_buy_new_data"]
            if len(flashSaleActLst) == 0:
                return
            else:
                for act in flashSaleActLst:
                    actRuleId = act["activity_rule_id"]
                    if len(act["sku_list"]) > 0:
                        actRuleId = act["activity_rule_id"]
                        break

            flashSaleTopicPage = self.newIndex.actGoodsLstForFlaseSale(header, actRuleId)
            assert flashSaleTopicPage["code"] == 200 and flashSaleTopicPage["message"] == "success"
            assert len(flashSaleTopicPage["data"]) >= 0
        except KeyError as e:
            pass

    @allure.story("拼团专题页")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_PT_topicPage(self, enterpriseInfo, ini):
        '''商品详情页自提点列表'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        if enterpriName != "晋锋优购" and enterpriName != "YJ渝教爱家":
            return
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        param = {
            "need_commonly_used": True,
            "need_last_select": True,
            "need_address_info": True,
            "province": province,
            "city": city,
            "longitude": "108.948780",
            "latitude": "34.222590",
            "keywords": "",
            "current_extract_id": 0,
            "is_filter_invalid": False
        }
        res = self.list.extract_list(param, header)
        extractId = res["data"]["list"][0]["id"]
        res = self.newIndex.newTemplatePageConfig(header, extractId)
        assert res["code"] == 200 and res["message"] == "success"
        param = {"origin_store_id": extractId}
        self.visit.visit_extract(param, header)
        pTTopicPage = self.newIndex.actGoodsLstForPT(header)
        assert pTTopicPage["code"] == 200 and pTTopicPage["message"] == "success"
        assert len(pTTopicPage["data"]["list"]) >= 0

    @allure.story("搜索拼团商品SPU列表")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_groupSearch_spuList(self, enterpriseInfo, ini):
        '''group_search_spu_list接口'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        if enterpriName != "晋锋优购" and enterpriName != "YJ渝教爱家":
            return
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        param = {
            "need_commonly_used": True,
            "need_last_select": True,
            "need_address_info": True,
            "province": province,
            "city": city,
            "longitude": "108.948780",
            "latitude": "34.222590",
            "keywords": "",
            "current_extract_id": 0,
            "is_filter_invalid": False
        }
        res = self.list.extract_list(param, header)
        extractId = res["data"]["list"][0]["id"]
        res = self.newIndex.newTemplatePageConfig(header, extractId)
        assert res["code"] == 200 and res["message"] == "success"
        param = {"origin_store_id": extractId}
        self.visit.visit_extract(param, header)
        try:
            categoryId = res["data"]["group_goods_data"][0]["id"]
            groupSearchSpuLst = self.newIndex.groupSearchSpuList(header, categoryId)
            assert groupSearchSpuLst["code"] == 200 and groupSearchSpuLst["message"] == "success"
            assert len(groupSearchSpuLst["data"]["list"]) >= 0
        except KeyError as e:
            pass

    @allure.story("分类级别")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_category_level(self, enterpriseInfo, ini):
        '''group_search_spu_list接口'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        if enterpriName != "晋锋优购" and enterpriName != "YJ渝教爱家":
            return
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        param = {
            "need_commonly_used": True,
            "need_last_select": True,
            "need_address_info": True,
            "province": province,
            "city": city,
            "longitude": "108.948780",
            "latitude": "34.222590",
            "keywords": "",
            "current_extract_id": 0,
            "is_filter_invalid": False
        }
        res = self.list.extract_list(param, header)
        extractId = res["data"]["list"][0]["id"]
        res = self.newIndex.newTemplatePageConfig(header, extractId)
        assert res["code"] == 200 and res["message"] == "success"
        param = {"origin_store_id": extractId}
        self.visit.visit_extract(param, header)
        categoryLevel = self.newIndex.categoryLevel(header)
        assert categoryLevel["code"] == 200 and categoryLevel["message"] == "success"


    @allure.story("购物车模型")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_store_cartModel(self, enterpriseInfo, ini):
        '''group_search_spu_list接口'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        if enterpriName != "晋锋优购" and enterpriName != "YJ渝教爱家":
            return
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        param = {
            "need_commonly_used": True,
            "need_last_select": True,
            "need_address_info": True,
            "province": province,
            "city": city,
            "longitude": "108.948780",
            "latitude": "34.222590",
            "keywords": "",
            "current_extract_id": 0,
            "is_filter_invalid": False
        }
        res = self.list.extract_list(param, header)
        extractId = res["data"]["list"][0]["id"]
        res = self.newIndex.newTemplatePageConfig(header, extractId)
        assert res["code"] == 200 and res["message"] == "success"
        param = {"origin_store_id": extractId}
        self.visit.visit_extract(param, header)
        categoryLevel = self.newIndex.storeCartModel(header)
        assert categoryLevel["code"] == 200 and categoryLevel["message"] == "success"


    @allure.story("新人购商品")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_new_buy(self, enterpriseInfo, ini):
        '''new-template/new-buy接口'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        if enterpriName != "晋锋优购" and enterpriName != "YJ渝教爱家":
            return
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        param = {
            "need_commonly_used": True,
            "need_last_select": True,
            "need_address_info": True,
            "province": province,
            "city": city,
            "longitude": "108.948780",
            "latitude": "34.222590",
            "keywords": "",
            "current_extract_id": 0,
            "is_filter_invalid": False
        }
        res = self.list.extract_list(param, header)
        extractId = res["data"]["list"][0]["id"]
        res = self.newIndex.newTemplatePageConfig(header, extractId)
        assert res["code"] == 200 and res["message"] == "success"
        param = {"origin_store_id": extractId}
        self.visit.visit_extract(param, header)
        try:
            categoryId = res["data"]["new_buy_data"]["new_buy_info"]["activity_rule_id"]
            groupSearchSpuLst = self.newIndex.newBuyAct(header, categoryId)
            assert groupSearchSpuLst["code"] == 200 and groupSearchSpuLst["message"] == "success"
            assert len(groupSearchSpuLst["data"]["list"]) >= 0
        except KeyError as e:
            pass