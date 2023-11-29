from utils.readerFile import ReaderFile
from utils.readerIniFile import ReaderIniFile
from log.log import Logger
from tests.common.onLineForSupermarket.indexInfo import PageConfig
from tests.common.onLineForSupermarket.smGoodsDetail import GoodsDetail
from tests.common.onLineForSupermarket.order import Shoporder
from tests.common.onLineForSupermarket.order import Store_cart
from tests.common.onLineForSupermarket.order import Wx_list
from tests.common.onLineForSupermarket.order import Get_order_setting
from tests.common.onLineForSupermarket.order import Common_config
from tests.common.onLineForSupermarket.order import User_center_mobile
from tests.common.onLineForSupermarket.order import Activity_goods_list
from tests.common.onLineForSupermarket.extractList import ExtractList
from tests.common.onLineForSupermarket.shopcart import Shopcart
from tests.common.sendRequest.sendRequestForOnline import SendRequestForOnline
from tests.common.onLineForSupermarket.indexInfo import VisitExtract
from tests.common.onLineForSupermarket.indexInfo import Hotgoods
from tests.login.singletonHttpClient import SingletonHttpClient
from tests.common.onLineForSupermarket.newIndex import NewIndex
from utils.parseJson import ParseJson
import json
import pytest
import allure

@allure.feature("(商超)购物车")
class Test_shop_cart:
    shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")
    httpClient = SingletonHttpClient.get_instance()
    @pytest.fixture()
    def ini(self):
        # 实例化对象
        self.logger = Logger.Logger()
        self.shop=Shopcart()
        self.goods = GoodsDetail()
        self.list = ExtractList()
        self.getspu = PageConfig()
        self.store = Store_cart()
        self.wxlist = Wx_list()
        self.common = Common_config()
        self.center = User_center_mobile()
        self.get = Get_order_setting()
        self.activity = Activity_goods_list()
        self.visit = VisitExtract()
        self.hotgoods = Hotgoods()
        self.visit = VisitExtract()
        yield self.logger

    @allure.story("微信推荐商品")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_wx_recommend(self, enterpriseInfo, ini):
        '''购物车微信推荐接口'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        res = self.shop.wx_recommend(datas=None, enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        with allure.step(f"{enterpriName}微信推荐商品"):
            assert res["code"] == 200
            assert res["message"] == "success"

    @allure.story("购物车设置")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_cart_setting(self, enterpriseInfo, ini):
        '''购物车设置接口'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        res = self.shop.cart_setting(datas=None, enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        with allure.step(f"{enterpriName}购物车设置"):
            assert res["code"] == 200
            assert res["message"] == "success"

    @allure.story("购物车列表")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_store_cart_list(self, enterpriseInfo, ini):
        '''购物车列表接口'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        datas={"selected_sku_ids":[],"latitude":"","longitude":""}
        res = self.shop.store_cart_list(datas=datas, enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        print(res)
        with allure.step(f"{enterpriName}购物车列表"):
            assert res["code"] == 200
            assert res["message"] == "success"

    @allure.story("商城上传")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_wx_mall_upload(self, enterpriseInfo, ini):
        '''购物车上传接口'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        datas = {"type":2,"ids":[]}
        res = self.shop.wx_mall_upload(datas=datas, enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        print(res)
        with allure.step(f"{enterpriName}商城上传"):
            assert res["code"] == 200
            assert res["message"] == "success"

    @allure.story("购物车更新")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    # @pytest.mark.skip("数据有误")
    def test_store_cart_update(self, enterpriseInfo, ini):
        '''商品详情页自提点列表'''
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
            self.visit.visit_extract(param, header)
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
        url = "{0}/gw-shop/app/v1/store-cart/add".format(self.shopBaseUrl)
        params = {"sku_id":sku_id,"number":1,"delivery_type":1}
        #TODO 方法调用错误，sendRequest未传 version = 'supermark',走到电商
        # myRequest = SendRequestForOnline(enterpriseInfo)
        # res = myRequest.sendRequest(method="POST", params=params, url=url)
        res = self.httpClient.Post(url=url,json=params,headers=header)
        self.logger.info("storeCart :{0}".format(res))
        # 查询购物车
        datas = {"selected_sku_ids": [], "latitude": "", "longitude": ""}
        url = "{0}/gw-shop/app/v1/store-cart/list".format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url, json=datas, headers=header)
        cartId = ParseJson.parseJson(res.json(),"cart_id")
        '''购物车更新接口'''
        datas = {"cart_id":int(cartId[0]),"number":0,"type":1,"activity_id":0}
        res = self.shop.store_cart_update(datas=datas, headers=header)
        print(res)
        with allure.step(f"{enterpriName}购物车更新"):
            assert res["code"] == 200
            assert res["message"] == "success"

    @allure.story("订阅状态")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_subscribe_status(self, enterpriseInfo, ini):
        '''购物车订阅状态接口'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        datas = {"object_ids":[],"object_type":12}
        res = self.shop.subscribe_status(datas=datas, enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        print(res)
        with allure.step(f"{enterpriName}订阅状态"):
            assert res["code"] == 200
            assert res["message"] == "success"

    @allure.story("清楚失效商品")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_clear_invalid(self, enterpriseInfo, ini):
        '''购物车清楚失效商品接口'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        datas = {
                "goods_data": [
                    {
                        "sku_id": 150348393804480,
                        "number": 2,
                        "is_store_take": 0
                    }
                ]
            }
        res = self.shop.clear_invalid(datas=datas, enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        print(res)
        with allure.step(f"{enterpriName}清楚失效商品"):
            assert res["code"] == 200
            assert res["message"] == "success"

    @allure.story("定价帮助")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_help_price(self, enterpriseInfo, ini):
        """购物车定价帮助"""
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        res = self.shop.help_price(datas=None,enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        with allure.step(f"{enterpriName}定价帮助"):
            assert res["code"] == 200
            assert res["message"] == "success"

    @allure.story("足迹")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_goods_foot_list(self, enterpriseInfo, ini):
        """我的足迹"""
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        data = {"page":1,"size":100}
        res = self.shop.goods_foot_list(datas=data, enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        with allure.step(f"{enterpriName}足迹"):
            assert res["code"] == 200
            assert res["message"] == "success"

    @allure.story("我的活动")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_my_activity_list(self, enterpriseInfo, ini):
        """我的活动"""
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
        extractId = res["data"]["list"][0]["id"]

        param = {"origin_store_id": extractId}
        self.visit.visit_extract(param, header)
        data = {}
        res = self.shop.my_activity_list(header , data)
        with allure.step(f"{enterpriName}我的活动"):
            assert res["code"] == 200
            assert res["message"] == "success"


    # @allure.story("购物车更新")
    # @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    # @pytest.mark.onLineSupermarket
    # def test_cart_update(self):
    #     self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
    #     enterpriName = enterpriseInfo["enterpriName"]
    #     enterpriseID = enterpriseInfo["enterpriseID"]
    #     enterpriseHash = enterpriseInfo["enterpriseHash"]
    #     header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)



