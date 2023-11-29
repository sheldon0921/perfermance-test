# from tests.common.onLine.goodsDetail import GoodsDetail
from tests.common.onLineForSupermarket.indexInfo import PageConfig
from tests.common.onLineForSupermarket.indexInfo import Hotgoods
from tests.common.onLineForSupermarket.indexInfo import VisitExtract
from tests.common.onLineForSupermarket.smGoodsDetail import GoodsDetail
from tests.common.onLineForSupermarket.extractList import ExtractList
from tests.common.onLineForSupermarket.newIndex import NewIndex
from tests.common.onLineForSupermarket.userDetail import UserDetail
from utils.readerFile import ReaderFile
from utils.parseJson import ParseJson
from log.log import Logger
import json
import pytest,time
import allure


@allure.feature("(商超)商品")
class Test_Goods_Detail:

    @pytest.fixture()
    def ini(self):
        # 实例化对象
        self.logger = Logger.Logger()
        self.goods = GoodsDetail()
        self.list=ExtractList()
        self.getspu = PageConfig()
        self.hotgoods = Hotgoods()
        self.visit = VisitExtract()
        self.data = {"user_latitude": "34.222590", "user_longitude": "108.948780"}
        yield self.logger, self.goods

    @allure.story("查询商品详情")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_get_goods_detail(self, enterpriseInfo, ini):
        '''商品详情接口'''
        time.sleep(10)
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        header = self.list.getHeader(enterpriseHash=enterpriseHash,enterpriseID=enterpriseID)
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
        res=self.list.extract_list(param,header)
        self.logger.info("extract_list :{0}".format(res))
        for i in res['data']['list']:
            extract_id = i['id']
            extract_name = i['name']
            self.logger.info("#####extract_name :{0}".format(extract_name))
            print("#####:{0}".format(extract_id))
            param = {"origin_store_id": extract_id}
            extractRes = self.visit.visit_extract(param,header)
            param = {"page": 1, "size": 10,"extract_id":extract_id}
            if enterpriName != "壹号土猪优选":
                hotlistres = self.hotgoods.hot_sku_list(param, header)
            else:
                hotlistres = NewIndex.actGoodsLstForTodayHot(header)
            self.logger.info("hot_sku_list :{0}".format(res))
            if len(hotlistres['data']['list']) != 0:
                spu_id = hotlistres['data']['list'][0]['spu_id']
                sku_id = hotlistres['data']['list'][0]['sku_id']
                break
        datas = {"spu_id": spu_id, "sku_id": sku_id, "api_type": 1}
        with allure.step(f"查询 {enterpriName} 的商品详情页面"):
            res = self.goods.get_goods_detail(datas,header)
        print("goods detail interface response msg: ", res.json())
        assert res.status_code == 200 and res.json()["code"]

    @allure.story("加密短链接")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_get_goods_encryptShortLink(self, enterpriseInfo, ini):
        '''加密短链接'''
        time.sleep(10)
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
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
        self.logger.info("extract_list :{0}".format(res))
        spu_id = 0
        sku_id = 0
        for i in res['data']['list']:
            extract_id = i['id']
            extract_name = i['name']
            self.logger.info("#####extract_name :{0}".format(extract_name))
            print("#####:{0}".format(extract_id))
            param = {"origin_store_id": extract_id}
            extractRes = self.visit.visit_extract(param, header)
            param = {"page": 1, "size": 10}
            if enterpriName != "壹号土猪优选":
                hotlistres = self.hotgoods.hot_sku_list(param, header)
            else:
                hotlistres = NewIndex.actGoodsLstForTodayHot(header)
            self.logger.info("hot_sku_list :{0}".format(res))
            if len(hotlistres['data']['list']) != 0:
                spu_id = hotlistres['data']['list'][0]['spu_id']
                sku_id = hotlistres['data']['list'][0]['sku_id']
                break
        if spu_id == 0 or sku_id == 0:
            raise Exception("{0}企业无限时购商品".format(enterpriName))
        else:
            datas = {"spu_id": spu_id, "type": 1, "enterprise_id": "", "sku_id": sku_id,
                     "api_type": 1}
            with allure.step(f"查询 {enterpriName} 的商品详情页面"):
                res = self.goods.encryptShortLink(datas,header)
            print("goods detail interface response msg: ", res.json())
            assert res.status_code == 200 and res.json()["code"]


    @allure.story("商品评论列表")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_comment_list(self, enterpriseInfo, ini):
        '''商品评论列表'''
        time.sleep(10)
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        param = {
            "need_commonly_used": True,
            "need_last_select": True,
            "need_address_info": True,
            "province": province,
            "city": city,
            "keywords": "",
            "current_extract_id": 0,
            "is_filter_invalid": False
        }
        res = self.list.extract_list(param, header)
        self.logger.info("extract_list :{0}".format(res))
        for i in res['data']['list']:
            extract_id = i['id']
            extract_name = i['name']
            self.logger.info("#####extract_name :{0}".format(extract_name))
            print("extractID:{0},extractName:{1}".format(extract_id, extract_name))
            param = {"origin_store_id": extract_id}
            extractRes = self.visit.visit_extract(param, header)
            param = {"page": 1, "size": 10}
            if enterpriName != "壹号土猪优选":
                hotlistres = self.hotgoods.hot_sku_list(param, header)
            else:
                hotlistres = NewIndex.actGoodsLstForTodayHot(header)
            self.logger.info("hot_sku_list :{0}".format(res))
            if len(hotlistres['data']['list']) != 0:
                spu_id = hotlistres['data']['list'][0]['spu_id']
                sku_id = hotlistres['data']['list'][0]['sku_id']
                break
        datas = {"spu_id": spu_id, "page": 1, "size": 5}
        interfaceUrl = "gw-shop/app/v1/goods/comment-list"
        with allure.step(f"查询 {enterpriName} 的商品详情页面"):
            res = self.goods.commonFuncPost(datas,header, interfaceUrl=interfaceUrl)
        print("goods detail interface response msg: ", res.json())
        assert res.status_code == 200 and res.json()["code"]

    @allure.story("微信推荐")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_wx_recommend(self, enterpriseInfo, ini):
        '''微信推荐'''
        time.sleep(10)
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
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
        self.logger.info("extract_list :{0}".format(res))
        for i in res['data']['list']:
            extract_id = i['id']
            extract_name = i['name']
            self.logger.info("#####extract_name :{0}".format(extract_name))
            print("#####:{0}".format(extract_id))
            param = {"origin_store_id": extract_id}
            extractRes = self.visit.visit_extract(param, header)
            param = {"page": 1, "size": 10}
            if enterpriName != "壹号土猪优选":
                hotlistres = self.hotgoods.hot_sku_list(param, header)
            else:
                hotlistres = NewIndex.actGoodsLstForTodayHot(header)
            self.logger.info("hot_sku_list :{0}".format(res))
            if len(hotlistres['data']['list']) != 0:
                spu_id = hotlistres['data']['list'][0]['spu_id']
                sku_id = hotlistres['data']['list'][0]['sku_id']
                break
        datas = {"type": 1, "sku_id": sku_id}
        interfaceUrl = "gw-shop/app/v1/page/wx-recommend"
        with allure.step(f"查询 {enterpriName} 的商品详情页面"):
            res = self.goods.commonFuncGet(datas,header, interfaceUrl=interfaceUrl)
        print("goods detail interface response msg: ", res.json())
        assert res.status_code == 200 and res.json()["code"]

    @allure.story("订阅状态")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_get_goods_subscribeStatus(self, enterpriseInfo, ini):
        '''订阅状态'''
        time.sleep(10)
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
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
        self.logger.info("extract_list :{0}".format(res))
        for i in res['data']['list']:
            extract_id = i['id']
            extract_name = i['name']
            self.logger.info("#####extract_name :{0}".format(extract_name))
            print("#####:{0}".format(extract_id))
            param = {"origin_store_id": extract_id}
            extractRes = self.visit.visit_extract(param, header)
            param = {"page": 1, "size": 10}
            if enterpriName != "壹号土猪优选":
                hotlistres = self.hotgoods.hot_sku_list(param, header)
            else:
                hotlistres = NewIndex.actGoodsLstForTodayHot(header)
            self.logger.info("hot_sku_list :{0}".format(res))
            if len(hotlistres['data']['list']) != 0:
                spu_id = hotlistres['data']['list'][0]['spu_id']
                sku_id = hotlistres['data']['list'][0]['sku_id']
                break
        datas = {"object_type": 12, "object_ids": [sku_id]}
        interfaceUrl = "gw-shop/app/v1/common/subscribe-status"
        with allure.step(f"查询 {enterpriName} 的商品详情页面"):
            res = self.goods.commonFuncPost(datas,header,
                                           interfaceUrl=interfaceUrl)
        print("goods detail interface response msg: ", res.json())
        assert res.status_code == 200 and res.json()["code"]

    @allure.story("商品详情页自提点列表")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_goodsDetail_extractList(self, enterpriseInfo, ini):
        '''商品详情页自提点列表'''
        time.sleep(10)
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
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
        self.logger.info("extract_list :{0}".format(res))
        for i in res['data']['list']:
            extract_id = i['id']
            extract_name = i['name']
            self.logger.info("#####extract_name :{0}".format(extract_name))
            print("#####:{0}".format(extract_id))
            param = {"origin_store_id": extract_id}
            extractRes = self.visit.visit_extract(param, header)
            param = {"page": 1, "size": 10}
            if enterpriName != "壹号土猪优选":
                hotlistres = self.hotgoods.hot_sku_list(param, header)
            else:
                hotlistres = NewIndex.actGoodsLstForTodayHot(header)
            self.logger.info("hot_sku_list :{0}".format(res))
            if len(hotlistres['data']['list']) != 0:
                spu_id = hotlistres['data']['list'][0]['spu_id']
                sku_id = hotlistres['data']['list'][0]['sku_id']
                break
        datas = {"goods_id":sku_id,"goods_num":1,"enterprise_id":enterpriseID,"longitude":"","latitude":"","need_time_info":True,"friend_recommend_extract_id":""}
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
        '''拼团商品详情页列表'''
        time.sleep(10)
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
            res = self.goods.commonFuncPost(datas, header,
                                            interfaceUrl=interfaceUrl)
        self.logger.info("goods detail interface response msg: {0}".format(res.json()))
        assert res.status_code == 200 and res.json()["code"]

    @allure.story("限时购商品详情页列表")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_goodsDetail_limitTime(self, enterpriseInfo, ini):
        '''限时购商品详情页列表'''
        time.sleep(10)
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
            res = self.goods.commonFuncPost(datas, header,
                                            interfaceUrl=interfaceUrl)
        self.logger.info("goods detail interface response msg: {0}".format(res.json()))
        assert res.status_code == 200 and res.json()["code"]

    @allure.story("今日爆款分享卡片")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_goodsDetail_generateShareImg(self, enterpriseInfo, ini):
        """
        今日爆款分享卡片
        :param enterpriseInfo:
        :param ini:
        :return:
        """
        time.sleep(10)
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        param = {
            "need_commonly_used": True,
            "need_last_select": True,
            "need_address_info": True,
            "province": province,
            "city": city,
            "keywords": "",
            "current_extract_id": 0,
            "is_filter_invalid": False
        }
        res = self.list.extract_list(param, header)
        self.logger.info("extract_list :{0}".format(res))
        for i in res['data']['list']:
            extract_id = i['id']
            extract_name = i['name']
            self.logger.info("#####extract_name :{0}".format(extract_name))
            print("#####:{0}".format(extract_id))
            param = {"origin_store_id": extract_id}
            extractRes = self.visit.visit_extract(param, header)
            print("extractRes: {0}".format(extractRes))
            param = {"page": 1, "size": 10}
            if enterpriName != "壹号土猪优选":
                hotlistres = self.hotgoods.hot_sku_list(param, header)
            else:
                hotlistres = NewIndex.actGoodsLstForTodayHot(header)
            self.logger.info("hot_sku_list :{0}".format(res))
            if len(hotlistres['data']['list']) != 0:
                sku_id = hotlistres['data']['list'][0]['sku_id']
                break
        genarateShareImgRes = self.goods.genarateShareImg(sku_id,header)
        assert genarateShareImgRes["data"]["url"] is not None
        print("genarateShareImgRes: {0}".format(genarateShareImgRes))


    @allure.story("商品详情页生成分享海报")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_goodsDetail_qrCode(self,enterpriseInfo,ini):
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        userDetail = UserDetail.getUserDetail(header)
        openId = userDetail["data"]["open_id"]
        userId = userDetail["data"]["id"]
        param = {
            "need_commonly_used": True,
            "need_last_select": True,
            "need_address_info": True,
            "province": province,
            "city": city,
            "keywords": "",
            "current_extract_id": 0,
            "is_filter_invalid": False
        }
        res = self.list.extract_list(param, header)
        self.logger.info("extract_list :{0}".format(res))
        sku_id = 0
        spu_id = 0
        for i in res['data']['list']:
            extract_id = i['id']
            extract_name = i['name']
            self.logger.info("#####extract_name :{0}".format(extract_name))
            print("#####:{0}".format(extract_id))
            param = {"origin_store_id": extract_id}
            extractRes = self.visit.visit_extract(param, header)
            print("extractRes: {0}".format(extractRes))
            param = {"page": 1, "size": 10}
            if enterpriName != "壹号土猪优选":
                hotlistres = self.hotgoods.hot_sku_list(param, header)
            else:
                hotlistres = NewIndex.actGoodsLstForTodayHot(header)
            self.logger.info("hot_sku_list :{0}".format(res))
            if len(hotlistres['data']['list']) != 0:
                sku_id = hotlistres['data']['list'][0]['sku_id']
                spu_id = hotlistres['data']['list'][0]['spu_id']
                break
        if sku_id == 0 or spu_id ==0:
            raise Exception("无商品",hotlistres)
        else:
            datas = {
                "path":"goods/goods-detail/goods-detail?&open_id="+openId+"&id="+str(userId)+"&sku_id="+str(sku_id)+"&type=25&rule_id=177265487674240&extract_id="+str(extract_id),
                "spu_id":str(spu_id)}
            res = self.goods.goodsDetailQRCode(header,datas)
            print("resssss: {0}".format(res))
            assert res["code"] == 200 and res["message"] == "success"
            assert res["data"]["qrcode"] is not None
