from utils.readerFile import ReaderFile
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
from tests.common.onLineForSupermarket.indexInfo import VisitExtract
from tests.common.onLineForSupermarket.indexInfo import Hotgoods
from tests.common.onLineForSupermarket.orderForSm import OrderForSm
from tests.common.onLine.shopOrder import ShopOrder
from utils.parseJson import ParseJson
from tests.login.login import Login
from utils.myTime import Mytime
from utils.myRandom import MyRandom
import json
import pytest
import allure

@allure.feature("(商超)订单")
class Test_confirm_order:

    @pytest.fixture()
    def ini(self):
        # 实例化对象
        self.logger = Logger.Logger()
        self.goods = GoodsDetail()
        self.list=ExtractList()
        self.visit = VisitExtract()
        self.getspu = PageConfig()
        self.shop=Shoporder()
        self.store=Store_cart()
        self.wxlist=Wx_list()
        self.common=Common_config()
        self.center=User_center_mobile()
        self.get=Get_order_setting()
        self.activity=Activity_goods_list()
        self.order = ShopOrder()
        self.hotgoods = Hotgoods()
        self.orderForSm = OrderForSm()
        self.data = {"user_latitude": "34.222590", "user_longitude": "108.948780"}
        yield self.logger

    @allure.story("爆款商品确认订单")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_confirm_order(self, enterpriseInfo, ini):
        '''确认订单接口'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        if enterpriName == "和安优选":
            return
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        res = self.list.extract_list(self.data,header)
        print(res)
        for extract in res['data']['list']:
            extract_id = extract['id']
            bs_hours = extract['bs_hours'][0]
            extract_name = extract['extract_name']
            address = extract['address']
            param = {"origin_store_id": extract_id}
            self.visit.visit_extract(param, header)
            param = {"method":"list","list_search":{"type":25,"activity_status":22},"page":1,"size":10,"category_id":0,"is_new":1}
            goodsList = self.activity.activity_goods_list(header,param)
            try:
                sku_list = goodsList["data"]["list"]
            except KeyError as e:
                return
            if len(sku_list) is not 0:
                spu_id = sku_list[0]["spu_id"]
                sku_id = sku_list[0]["sku_id"]
                activity_rule_id = sku_list[0]["activity_rule_id"]
                break
            if extract == res['data']['list'][-1]:
                return
        # param = {"extract_id": extract_id, "template_type": "index"}
        # Res = self.getspu.page_config(param,header)
        # print(Res)
        # data = json.loads(Res['data']['templates']['content'])
        # for i in data['content'][0]['components']:
        #     if enterpriName != "胡燃优鲜" and i['name'] == "爆款专区":
        #         k = data['content'][0]['components'].index(i)
        #         sku_id = data['content'][0]['components'][k]['versions'][0]['data']['hotList'][0]['goodInfo']['sku_id']
        #     elif i['name'] == "今日爆款-新":
        #         k = data['content'][0]['components'].index(i)
        #         sku_id = data['content'][0]['components'][k]['versions'][0]['data']['activityList'][0]['sku_id']
        print(sku_id)
        datas = {"goods_data": [
            {"sku_id": sku_id, "number": 1, "cart_id": 0, "delivery_type": 2, "extract_id": extract_id,
             "extract_longitude": "120.50525", "extract_latitude": "32.353201", "extract_name": extract_name,
             "extract_bs_hours": [
                 bs_hours],
             "extract_address": address, "extract_is_nearest": 1}], "user_address_id": 0,
            "user_latitude": "34.222590", "user_longitude": "108.948780"}
        confirmOrderRes = self.shop.confirm_order(datas,header)
        self.logger.info("confirm order :{0}".format(confirmOrderRes))
        with allure.step(f"{enterpriName}爆款商品确认订单"):
            assert confirmOrderRes["code"] == 200
            assert confirmOrderRes["message"] == "success"
        datas = {"type":1}
        res = self.shop.getOrderSetting(header,datas)
        assert res["code"] == 200 \
               and res["message"] == "success"
        res = self.shop.userExtractAddress(header,datas)
        assert res["code"] == 200 \
               and res["message"] == "success"
        datas = {"encryptedData":"hDEgnvq8juKc8/DWoYX3QtQ+c4ikrUSVQC79FJPKO6nQ53pNDBwo3XHH50NV2R4gYoeg3Kw6KGSM3kSf3JXLLcyzlkjLrhcwui1mxC1LmoH00j2xJeD9r1n4PLTPVAAXNU8COaJE73At0IkJKFY4PXXpCt4HVHahc2lh/4EllDvcbYzNBUQDn2WfsqYJTpKkY/TGuTnErHMFUeTl0LNioA==","iv":"CSgC/48Y5uILYUkyk+g1SA=="}
        res = self.shop.userCenterMobile(header,datas)
        # assert res["code"] == 200 \
        #        and res["message"] == "success"

    @allure.story("购物车选择")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_store_cart_check(self,enterpriseInfo, ini):
        '''购物车选择接口'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        if enterpriName == "和安优选":
            return
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        res = self.list.extract_list(self.data,header)
        for extract in res['data']['list']:
            extract_id = extract['id']
            param = {"origin_store_id": extract_id}
            self.visit.visit_extract(param, header)
            param = {"method":"list","list_search":{"type":25,"activity_status":22},"page":1,"size":10,"category_id":0,"is_new":1}
            goodsList = self.activity.activity_goods_list(header,param)
            try:
                skuList = goodsList["data"]["list"]
            except KeyError as e:
                return
            if len(skuList) is not 0:
                sku_id = skuList[0]["sku_id"]
                break
            if extract == res['data']['list'][-1]:
                return

        # param = {"extract_id": extract_id, "template_type": "index"}
        # Res = self.getspu.page_config(param,header)
        # data = json.loads(Res['data']['templates']['content'])
        # for i in data['content'][0]['components']:
        #     if enterpriName != "胡燃优鲜" and i['name'] == "爆款专区":
        #         k = data['content'][0]['components'].index(i)
        #         sku_id = data['content'][0]['components'][k]['versions'][0]['data']['hotList'][0]['goodInfo']['sku_id']
        #     elif i['name'] == "今日爆款":
        #         k = data['content'][0]['components'].index(i)
        #         sku_id = data['content'][0]['components'][k]['versions'][0]['data']['activityList'][0]['sku_id']
        datas = {"goods_data": [
            {"sku_id": sku_id, "number": 1, "postage_delivery_type": 2, "is_store_take": 1,
             "reference_point_id": 0, "type": 1}]}
        res=self.store.store_cart(datas,header)
        with allure.step(f"{enterpriName}购物车选择"):
            assert res["code"] == 200
            assert res["message"] == "success"

    @allure.story("优惠券列表")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_coupon_wx_list(self, enterpriseInfo, ini):
        '''微信优惠券列表接口'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        res=self.wxlist.wx_list(None,header)
        with allure.step(f"{enterpriName}优惠券列表"):
            assert res["code"] == 200
            assert res["message"] == "success"

    @allure.story("获取订单配置")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_order_setting(self, enterpriseInfo, ini):
        '''订单配置接口'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        datas={"type":1}
        res = self.get.get_order_setting(datas,header)
        with allure.step(f"{enterpriName}获取订单配置"):
            assert res["code"] == 200
            assert res["message"] == "success"

    @allure.story("获取常用配置")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_common_config(self, enterpriseInfo, ini):
        '''常用配置接口'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        res = self.common.common_config(None, header)
        with allure.step(f"{enterpriName}获取常用配置"):
            assert res["code"] == 200
            assert res["message"] == "success"

    @pytest.mark.skip
    @allure.story("授权手机号")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_user_center_mobile(self, enterpriseInfo, ini):
        '''授权手机号接口'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        datas = {"encryptedData":"XFXOuf9akY01V61qZINJux2OxU85WTkado1bLgBXm8qgg1buiyBMEoJWESruyjHMlDY7Ix4S2H+IPyoyloHiDrtv53TruKOlHLvpHh5LUiztLrQtT4Ajo4f8/VFYbrP6242TrOxQv/gTKedzugKy1LyV+pkkzCI3A/Z3oXM2aZOmL/5JLx8ltKv9z5rF+UoDPL1bzXN3lFK9tVpcQ0z0bA==",
                 "iv":"V5/8XM0LOfndzWmLtl818Q=="}
        res = self.center.user_center_mobile(datas,header)
        with allure.step(f"{enterpriName}授权手机号"):
            assert res["code"] == 200
            assert res["message"] == "success"

    @allure.story("限时购商品确认订单")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_activity_goods_list(self, enterpriseInfo, ini):
        '''限时购确认订单接口'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        res = self.list.extract_list(datas=self.data,header = header)
        extract_id = res['data']['list'][0]['id']
        bs_hours = res['data']['list'][0]['bs_hours'][0]
        extract_name = res['data']['list'][0]['extract_name']
        address = res['data']['list'][0]['address']
        province = enterpriseInfo["province"]
        city = enterpriseInfo["city"]
        goodsList = self.goods.queryGoods(header, province, city, "limitTime")
        if len(goodsList) == 0:
            return
        else:
            sku_id = goodsList[0]['sku_id']
        print(sku_id)
        activity_id=goodsList[0]['activity_rule_id']
        datas={
                "goods_data": [{
                    "sku_id": sku_id,
                    "number": 1,
                    "cart_id": 0,
                    "activity_id": activity_id,
                    "activity_type": 12,
                    "delivery_type": 2,
                    "extract_id": extract_id,
                    "extract_longitude": "120.50525",
                    "extract_latitude": "32.353201",
                    "extract_name": extract_name,
                    "extract_bs_hours": [bs_hours],
                    "extract_address": address,
                    "extract_is_nearest": 1
                }],
                "user_address_id": 0,
                "user_latitude": "34.222590",
                "user_longitude": "108.948780"
            }
        res = self.shop.confirm_order(datas,header)
        with allure.step(f"{enterpriName}限时购商品确认订单"):
            assert res["code"] == 200
            assert res["message"] == "success"


    @allure.story("拼团商品确认订单")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_activity_goods_list_001(self, enterpriseInfo, ini):
        '''拼团商品确认订单接口'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        res = self.list.extract_list(self.data,header)
        extract_id = res['data']['list'][0]['id']
        bs_hours = res['data']['list'][0]['bs_hours'][0]
        extract_name = res['data']['list'][0]['extract_name']
        address = res['data']['list'][0]['address']
        province = enterpriseInfo["province"]
        city = enterpriseInfo["city"]
        goodsList = self.goods.queryGoods(header, province, city, "groupWork")
        print(goodsList)
        if len(goodsList) == 0:
            return
        else:
            sku_id = goodsList[0]['sku_id']
        activity_id = goodsList[0]['activity_rule_id']
        datas={
                "goods_data": [{
                    "sku_id": sku_id,
                    "number": 1,
                    "cart_id": 0,
                    "activity_id": activity_id,
                    "activity_type": 12,
                    "delivery_type": 2,
                    "extract_id": extract_id,
                    "extract_longitude": "120.50525",
                    "extract_latitude": "32.353201",
                    "extract_name": extract_name,
                    "extract_bs_hours": [bs_hours],
                    "extract_address": address,
                    "extract_is_nearest": 1
                }],
                "user_address_id": 0,
                "user_latitude": "34.222590",
                "user_longitude": "108.948780"
            }
        res = self.shop.confirm_order(datas,header)
        with allure.step(f"{enterpriName}拼团商品确认订单"):
            assert res["code"] == 200
            assert res["message"] == "success"

    @allure.story("订单列表")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_order_list(self,enterpriseInfo,ini):
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        res = Login.loginNew(enterpriseID=enterpriseID)
        token = res["data"]["token"]
        timeStamp = Mytime.getCurrTimeStamp()
        randomStr = MyRandom.getRandomStr(2)
        xRequestId = 'autoTest-7b9d-4091-b4af-{0}{1}'.format(randomStr, timeStamp)
        headers = {
            'token': token,
            'Enterprise-Hash': enterpriseHash,
            'App-Version': 'V1.7.2',
            'X-Request-ID': xRequestId
        }
        data={"status": [20, 23], "page": 1, "size": 10}
        res=self.shop.store_orderlist(headers,data)
        assert res["code"] == 200 and res["message"] == "success"

    @allure.story("爆款活动商品下单")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.smPlaceOrder
    def test_add_order(self, enterpriseInfo, ini):
        '''商品详情页自提点列表'''
        # time.sleep(10)
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        print("header1111111111111: {0}".format(header))
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
            bs_hours = i['bs_hours'][0]
            address = i['address']
            object_id = i["object_id"]
            self.logger.info("#####extract_name :{0}".format(extract_name))
            print("#####:{0}".format(extract_id))
            param = {"origin_store_id": extract_id}
            extractRes = self.visit.visit_extract(param, header)
            param = {"page": 1, "size": 10}
            hotlistres = self.hotgoods.hot_sku_list(param, header)
            self.logger.info("hot_sku_list :{0}".format(res))
            if hotlistres['data']['list'] != 0:
                spu_id = hotlistres['data']['list'][0]['spu_id']
                sku_id = hotlistres['data']['list'][0]['sku_id']
                price = hotlistres['data']['list'][0]['off_line_price']
                break
        datas = {"goods_data": [
            {"sku_id": sku_id, "number": 1, "cart_id": 0, "delivery_type": 2, "extract_id": extract_id,
             "extract_longitude": "120.43597888201475", "extract_latitude": "32.48979845975961", "extract_name": extract_name,
             "extract_bs_hours": [
                 bs_hours],
             "extract_address": address, "extract_is_nearest": 1}], "user_address_id": 0,
            "user_latitude": "34.222590", "user_longitude": "108.948780"}
        res = self.shop.confirm_order(datas, header)
        print(res)
        with allure.step(f"{enterpriName}爆款商品确认订单"):
            assert res["code"] == 200
            assert res["message"] == "success"
        freightEncrypt = ParseJson.parseJson(res,"freight_encrypt")[0]
        workId = ParseJson.parseJson(res,"worker_id")[0]
        encrypted_discount_activity = ParseJson.parseJson(res, 'encrypted_discount_activity')[0]
        # 确认订单检查接口
        datas = {"goods_data": [
            {"sku_id": sku_id, "number": 1, "delivery_type": 2, "activity_id": 0, "activity_type": 1,
             "goods_type": 1, "extract_id": extract_id, "store_id": object_id}]}
        res = self.shop.confirmCheck(header,datas)
        print("res : {0}".format(res))
        assert res["code"] == 200 \
               and res["message"] == "success"
        # 下单操作
        param = {
            "store_id": object_id,
            "freight_encrypt": freightEncrypt,
            "worker_id": workId,
            "order_data_encrypt": encrypted_discount_activity,
            "goodsData": [{
                "sku_id": sku_id,
                "cart_id": 0,
                "price": price,
                "take_point_id": extract_id,
                "quantity": 1
            }]
        }
        addOrderRes = self.orderForSm.placeOrderForSm(header,param)
        print("addOrderRes: {0}".format(addOrderRes))
        self.mainOrderNo = ParseJson.parseJson(addOrderRes, "order_no")[0]
        order_id = ParseJson.parseJson(addOrderRes, "order_id")[0]
        assert addOrderRes["code"] == 200 and \
               self.mainOrderNo is not None
        orderListRes = self.orderForSm.getOrderList(header=header)
        orderListData = orderListRes["data"]["list"]
        for orderItem in orderListData:
            if self.mainOrderNo == orderItem['main_order_no']:
                orderNo = orderItem['order_no']
                orderId = orderItem["main_order_info"]['id']
        # 订单详情页面
        datas = {"order_id": orderId, "main_order_no": self.mainOrderNo}
        res = self.shop.orderDetail(header=header,datas=datas)
        assert res["code"] == 200 \
               and res["message"] == "success"
        # 取消订单
        datas = {"id":str(orderId),"event":"customer_cancel","refund_reason_id":0}
        res = self.shop.mainOrderMachine(header,datas)
        print("mainOrderMachine res: {0}".format(res))
        assert res["code"] == 200 \
               and res["message"] == "success"
        datas = {"order_no": orderNo}
        # 删除订单
        res = self.shop.delOrder(header,datas)
        print("delOrder res: {0}".format(res))
        assert res["code"] == 200 \
               and res["message"] == "success"
        datas = {"order_no": orderNo}
        # 再次购买
        res = self.shop.againBuy(header,datas)
        print("againBuy res: {0}".format(res))
        assert res["code"] == 200 \
               and res["message"] == "success"

    @allure.story("取消订单原因列表")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_serviceReason(self,enterpriseInfo,ini):
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        res = self.shop.serviceReason(header=header)
        assert res["code"] == 200 \
               and res["message"] == "success"

    @allure.story("商品折扣价格")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_skuDiscountPrice(self,enterpriseInfo,ini):
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        print("header1111111111111: {0}".format(header))
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
            hotlistres = self.hotgoods.hot_sku_list(param, header)
            self.logger.info("hot_sku_list :{0}".format(res))
            try:
                if hotlistres['data']['list'] != 0:
                    spu_id = hotlistres['data']['list'][0]['spu_id']
                    sku_id = hotlistres['data']['list'][0]['sku_id']
                    break
            except Exception:
                return
            # 商品折扣
            params = {"sku_id": sku_id, "sale_type": 2, "number": 1, "is_ignore": 2}
            res = self.hotgoods.skuDiscountPrice(header,params)
            assert res["code"] == 200 \
                   and res["message"] == "success"
            # 生成分享海报
            params ={
                "path": "goods/goods-detail/goods-detail?&open_id=oYDNy5T2B8s5ObnjK-hliLrazLoI&id=154779257181120&sku_id="+sku_id+"&extract_id="+extract_id,
                "spu_id": spu_id
            }
            res = self.hotgoods.goodsDetailQRCode(header,params)
            assert res["code"] == 200 \
                   and res["message"] == "success"

    @allure.story("用户自提信息保存")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_userExtractInfoSave(self,enterpriseInfo,ini):
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        params = {"delivery_name": "大圣", "delivery_mobile": "13789762543"}
        res = self.hotgoods.userExtractInfoSave(header,params)
        assert res["code"] == 200 \
               and res["message"] == "success"

    @allure.story("去凑单接口")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_joinActivityData(self,enterpriseInfo,ini):
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        params = {"goods_amount":100}
        res = self.hotgoods.joinActivityData(header,params)
        assert res["code"] == 200 \
               and res["message"] == "success"
