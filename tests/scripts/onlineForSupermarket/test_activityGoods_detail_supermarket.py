# from tests.common.onLine.goodsDetail import GoodsDetail
from tests.common.onLineForSupermarket.indexInfo import PageConfig
from tests.common.onLineForSupermarket.smGoodsDetail import GoodsDetail
from tests.common.onLineForSupermarket.extractList import ExtractList
from utils.readerFile import ReaderFile
from utils.parseJson import ParseJson
from log.log import Logger
import json
import pytest
import allure


@allure.feature("(商超)活动商品")
class Test_Goods_Detail:

    @pytest.fixture()
    def ini(self):
        # 实例化对象
        self.logger = Logger.Logger()
        self.goods = GoodsDetail()
        self.list=ExtractList()
        self.getspu = PageConfig()
        yield self.logger, self.goods


    @allure.story("限时购商品详情页加密短链接")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_get_goods_encryptShortLink(self, enterpriseInfo, ini):
        '''加密短链接'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo["province"]
        city = enterpriseInfo["city"]
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        with allure.step(f"查询 {enterpriName} 的限时购活动加密短链接"):
            goodsList = self.goods.queryGoods(header, province, city, "limitTime")
        if len(goodsList) == 0:
            return
        print("goodsList: {0}".format(goodsList))
        spu_id = goodsList[0]["spu_id"]
        sku_id = goodsList[0]["sku_id"]
        roleId = goodsList[0]["activity_rule_id"]
        datas = {"spu_id": spu_id, "type": 14, "rule_id": roleId, "enterprise_id": "","sku_id": sku_id, "api_type": 1}
        with allure.step(f"查询 {enterpriName} 的商品详情页面"):
            res = self.goods.encryptShortLink(datas, header)
        print("goods detail interface response msg: ", res.json())
        assert res.status_code == 200 and res.json()["code"]

    @allure.story("拼团商品详情页加密短链接")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_get_goods_encryptShortLink_001(self, enterpriseInfo, ini):
        '''加密短链接'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo["province"]
        city = enterpriseInfo["city"]
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        with allure.step(f"查询 {enterpriName} 的限时购活动加密短链接"):
            goodsList = self.goods.queryGoods(header, province, city, "groupWork")
        if len(goodsList) == 0:
            return
        print("goodsList: {0}".format(goodsList))
        spu_id = goodsList[0]["spu_id"]
        sku_id = goodsList[0]["sku_id"]
        roleId = goodsList[0]["activity_rule_id"]
        datas = {"spu_id": spu_id, "type": 14, "rule_id": roleId, "enterprise_id": "","sku_id": sku_id, "api_type": 1}
        with allure.step(f"查询 {enterpriName} 的商品详情页面"):
            res = self.goods.encryptShortLink(datas,header)
        print("goods detail interface response msg: ", res.json())
        assert res.status_code == 200 and res.json()["code"]


    @allure.story("拼团活动商品详情页评论列表")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_comment_list(self, enterpriseInfo, ini):
        '''商品评论列表'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo["province"]
        city = enterpriseInfo["city"]
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        with allure.step(f"查询 {enterpriName} 的限时购活动加密短链接"):
            goodsList = self.goods.queryGoods(header, province, city, "groupWork")
        if len(goodsList) == 0:
            return
        # print("goodsList: {0}".format(goodsList))
        spu_id = goodsList[0]["spu_id"]
        datas = {"spu_id": spu_id, "page": 1, "size": 5}
        interfaceUrl = "gw-shop/app/v1/goods/comment-list"
        with allure.step(f"查询 {enterpriName} 的商品详情页面"):
            res = self.goods.commonFuncPost(datas,header, interfaceUrl=interfaceUrl)
        print("goods detail interface response msg: ", res.json())
        assert res.status_code == 200 and res.json()["code"]

    @allure.story("限时购活动商品详情页评论列表")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_comment_list_01(self, enterpriseInfo, ini):
        '''商品评论列表'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo["province"]
        city = enterpriseInfo["city"]
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        with allure.step(f"查询 {enterpriName} 的限时购活动加密短链接"):
            goodsList = self.goods.queryGoods(header, province, city, "limitTime")
        if len(goodsList) == 0:
            return
        # print("goodsList: {0}".format(goodsList))
        spu_id = goodsList[0]["spu_id"]
        datas = {"spu_id": spu_id, "page": 1, "size": 5}
        interfaceUrl = "gw-shop/app/v1/goods/comment-list"
        with allure.step(f"查询 {enterpriName} 的商品详情页面"):
            res = self.goods.commonFuncPost(datas, header, interfaceUrl=interfaceUrl)
        print("goods detail interface response msg: ", res.json())
        assert res.status_code == 200 and res.json()["code"]

    @allure.story("限时购活动商品详情页微信推荐")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_wx_limitTimeRecommend(self, enterpriseInfo, ini):
        '''商品评论列表'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo["province"]
        city = enterpriseInfo["city"]
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        with allure.step(f"查询 {enterpriName} 的限时购活动加密短链接"):
            goodsList = self.goods.queryGoods(header, province, city, "limitTime")
        if len(goodsList) == 0:
            return
        # print("goodsList: {0}".format(goodsList))
        sku_id = goodsList[0]["sku_id"]
        datas = {"type": 1, "sku_id": sku_id}
        interfaceUrl = "gw-shop/app/v1/page/wx-recommend"
        with allure.step(f"查询 {enterpriName} 的商品详情页面"):
            res = self.goods.commonFuncGet(datas, header, interfaceUrl=interfaceUrl)
        print("goods detail interface response msg: ", res.json())
        assert res.status_code == 200 and res.json()["code"]


    @allure.story("拼团活动商品详情页微信推荐")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_wx_pTRecommend(self, enterpriseInfo, ini):
        '''商品评论列表'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo["province"]
        city = enterpriseInfo["city"]
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        with allure.step(f"查询 {enterpriName} 的限时购活动加密短链接"):
            goodsList = self.goods.queryGoods(header, province, city, "groupWork")
        if len(goodsList) == 0:
            return
        # print("goodsList: {0}".format(goodsList))
        sku_id = goodsList[0]["sku_id"]
        datas = {"type": 1, "sku_id": sku_id}
        interfaceUrl = "gw-shop/app/v1/page/wx-recommend"
        with allure.step(f"查询 {enterpriName} 的商品详情页面"):
            res = self.goods.commonFuncGet(datas,header, interfaceUrl=interfaceUrl)
        print("goods detail interface response msg: ", res.json())
        assert res.status_code == 200 and res.json()["code"]


    @allure.story("限时购活动商品详情页自提点列表")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_goodsDetail_extractList(self, enterpriseInfo, ini):
        '''商品评论列表'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo["province"]
        city = enterpriseInfo["city"]
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        with allure.step(f"查询 {enterpriName} 的限时购活动加密短链接"):
            goodsList = self.goods.queryGoods(header, province, city, "groupWork")
        if len(goodsList) == 0:
            return
        # print("goodsList: {0}".format(goodsList))
        storeIds = []
        if len(goodsList) >3:
            for i in range(0, 3):
                storeIds.append(goodsList[i]["sku_id"])
        datas = {"goods_id":144698028717184,"goods_num":1,"store_ids": storeIds,"longitude":"108.939840","latitude":"34.341270","need_time_info":True,"friend_recommend_extract_id":""}
        interfaceUrl = "gw-shop/app/v1/extract/list"
        with allure.step(f"查询 {enterpriName} 的商品详情页面"):
            res = self.goods.commonFuncPost(datas,header,
                                            interfaceUrl=interfaceUrl)
        print("goods detail interface response msg: ", res.json())
        assert res.status_code == 200 and res.json()["code"]

    @allure.story("拼团商品详情页列表")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_goodsDetail_groupWork(self, enterpriseInfo, ini):
        '''商品评论列表'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo["province"]
        city = enterpriseInfo["city"]
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        with allure.step(f"查询 {enterpriName} 的拼团活动商品详情页面"):
            goodsList = self.goods.queryGoods(header, province, city, "groupWork")
        if len(goodsList) == 0:
            return
        # self.logger.info("goodsList: {0}".format(goodsList))
        sku_id = goodsList[0]["sku_id"]
        datas = {"goods_id":sku_id,"goods_num":1,"enterprise_id":enterpriseID,"longitude":"","latitude":"","need_time_info":True,"friend_recommend_extract_id":""}
        interfaceUrl = "gw-shop/app/v1/extract/list"
        with allure.step(f"查询 {enterpriName} 的商品详情页面"):
            res = self.goods.commonFuncPost(datas,header,
                                            interfaceUrl=interfaceUrl)
        self.logger.info("goods detail interface response msg: {0}".format(res.json()))
        assert res.status_code == 200 and res.json()["code"]

    @allure.story("限时购商品详情页列表")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_goodsDetail_limitTime(self, enterpriseInfo, ini):
        '''商品评论列表'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo["province"]
        city = enterpriseInfo["city"]
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        with allure.step(f"查询 {enterpriName} 的限时购活动商品详情页面"):
            goodsList = self.goods.queryGoods(header, province, city, "limitTime")
        if len(goodsList) == 0:
            return
        # self.logger.info("goodsList: {0}".format(goodsList))
        sku_id = goodsList[0]["sku_id"]
        datas = {"goods_id":sku_id,"goods_num":1,"enterprise_id":enterpriseID,"longitude":"","latitude":"","need_time_info":True,"friend_recommend_extract_id":""}
        interfaceUrl = "gw-shop/app/v1/extract/list"
        with allure.step(f"查询 {enterpriName} 的限时购活动商品详情页面"):
            res = self.goods.commonFuncPost(datas,header,
                                            interfaceUrl=interfaceUrl)
        self.logger.info("goods detail interface response msg: {0}".format(res.json()))
        assert res.status_code == 200 and res.json()["code"]

    @allure.story("确认加入拼团列表")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_goodsDetail_sureJoinGroupList(self, enterpriseInfo, ini):
        '''确认加入拼团列表'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo["province"]
        city = enterpriseInfo["city"]
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        with allure.step(f"查询 {enterpriName} 的限时购活动加密短链接"):
            goodsList = self.goods.queryGoods(header, province, city, "groupWork")
        if len(goodsList) == 0:
            return
        print("goodsList: {0}".format(goodsList))
        roleId = goodsList[0]["activity_rule_id"]
        datas = {"activity_rule_id":roleId}
        interfaceUrl = "gw-shop/app/v1/activity-center/group/sure-join-group-list"
        with allure.step(f"查询 {enterpriName} 的商品详情页面"):
            res = self.goods.commonFuncPost(datas,header,
                                            interfaceUrl=interfaceUrl)
        print("goods detail interface response msg: ", res.json())
        assert res.status_code == 200 and res.json()["code"]
