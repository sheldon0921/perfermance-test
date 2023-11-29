from tests.common.onLine.shopOrder import ShopOrder
from utils.readerFile import ReaderFile
from log.log import Logger
from tests.common.onLine.getGoodsSpu import GetGoodsSpu
import json
from utils.readerIniFile import ReaderIniFile
import pytest
import allure
from time import sleep
from tests.common.sendRequest.sendRequestForOnline import SendRequestForOnline


@allure.feature("订单")
class Test_Order:

    @pytest.fixture()
    def ini(self):
        self.order = ShopOrder()
        self.logger = Logger.Logger()
        self.getspu = GetGoodsSpu()
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")
        yield self.order, self.logger

    @allure.story("用户下单")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    @pytest.mark.skip(reason="暂时跳过！")
    def test_add_order(self, enterpriseInfo, ini):
        """下单接口"""
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        Res = self.getspu.get_goods_spu(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        if len(Res['data']['list']) > 0:
            # spu_id = Res['data']['list'][0]['spu_id']
            sku_id = Res['data']['list'][0]['default_sku_id']
            # goodsName = Res['data']['list'][0]['sku_name']
        else:
            self.logger.info('{0}商品上架中'.format(enterpriName))
        # print("\nenterpriName: ", enterpriName, "enterpriseHash: ", enterpriseHash)
        if enterpriseID == '95489912226048':
            return
        self.datas = {"goods_data":[{"sku_id":sku_id,"number":1,"cart_id":0,"delivery_type":1}],"user_address_id":0}
        try:
            self.res = self.order.confirm_order(datas=self.datas,enterpriseID=enterpriseID,enterpriseHash=enterpriseHash)
            self.freight_encrypt = self.res.json()["data"]["list"][0]["freight"]["freight_encrypt"]
            self.sell_price = self.res.json()["data"]["list"][0]["goods_data"][0]["sell_price"]
        except KeyError as e:
            self.logger.info(self.res.json()['message'])
            return
        datas = {"api_type": 1,
                 "list": [{"store_id": 0,
                           "work_id": 0,
                           "freight_encrypt": self.freight_encrypt,
                           "goods_data": [{"sku_id": sku_id,
                                           "quantity": 1,
                                           "type": 1,
                                           "cart_id": 0,
                                           "price": self.sell_price,
                                           "delivery_type": 1,
                                           "take_point_id": 0,
                                           "activity_type": 1,
                                           "activity_id": 0,
                                           "goods_type": 1}]
                                          }],
                 "type": 1,
                 "remarks": "",
                 "user_coupon_id": 0,
                 "encrypted_wx_coupons": "",
                 "order_data_encrypt": "",
                 "user_address_id": 0}

        res = self.order.add_order(datas=datas,enterpriseID=enterpriseID,enterpriseHash=enterpriseHash)
        sleep(3)
        assert res["code"] == 200
        assert res["data"][0]["order_id"] is not None
        data={"status": [20, 23], "page": 1, "size": 10}
        res=self.order.store_orderlist(datas=data,enterpriseID=enterpriseID,enterpriseHash=enterpriseHash)
        id=res['data']['list'][0]['main_order_info']['id']
        param={"id":id,"event":"customer_cancel","refund_reason_id":0}
        res=self.order.cancel_order(datas=param,enterpriseID=enterpriseID,enterpriseHash=enterpriseHash)
        assert res.json()["code"] == 200

    @allure.story("确认订单")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    def test_confirm_order(self, enterpriseInfo, ini):
        """订单确认接口"""
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        Res = self.getspu.get_goods_spu(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        if len(Res['data']['list']) > 0:
            # spu_id = Res['data']['list'][0]['spu_id']
            sku_id = Res['data']['list'][0]['default_sku_id']
            goodsName = Res['data']['list'][0]['sku_name']
        else:
            self.logger.info('{0}商品上架中'.format(enterpriName))
            return
        # print("\nenterpriName: ", enterpriName, "enterpriseHash: ", enterpriseHash)
        datas = {"goods_data":[{"sku_id":sku_id,"number":1,"cart_id":0,"delivery_type":1}],"user_address_id":0}
        with allure.step(f"{enterpriName}小程序的{goodsName}商品确认订单"):
            res = self.order.confirm_order(datas=datas,enterpriseID=enterpriseID,enterpriseHash=enterpriseHash)
        # print("confirm order msg: ", res)
        assert res.status_code == 200
        # self.assertTrue(res["data"]["list"][0]["store_info"]["id"] is not None)

    @allure.story("优惠券列表")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    def test_wx_list(self, enterpriseInfo, ini):
        url="{0}/gw-shop/app/v1/coupon/wx-list".format(self.shopBaseUrl)
        myRequest = SendRequestForOnline(enterpriseInfo)
        res=myRequest.sendRequest(method="GET", params=None, url=url)
        print(res.json())
        assert res.json()["code"] == 200

    @allure.story("获取订单配置")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    def test_get_order_setting(self, enterpriseInfo, ini):
        url = "{0}/gw-shop/app/v1/store-order/get-order-setting".format(self.shopBaseUrl)
        params={"type":1}
        myRequest = SendRequestForOnline(enterpriseInfo)
        res = myRequest.sendRequest( method="POST", params=params, url=url)
        print(res.json())
        assert res.json()["code"] == 200

    @allure.story("公共配置")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    def test_common_config(self, enterpriseInfo, ini):
        url = "{0}/gw-shop/app/v1/common/config".format(self.shopBaseUrl)
        myRequest = SendRequestForOnline(enterpriseInfo)
        res = myRequest.sendRequest(method="POST", params=None, url=url)
        print(res.json())
        assert res.json()["code"] == 200

    @allure.story("地址列表")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    def test_address_list(self, enterpriseInfo, ini):
        url = "{0}/gw-shop/app/v1/user/address-list".format(self.shopBaseUrl)
        myRequest = SendRequestForOnline(enterpriseInfo)
        res = myRequest.sendRequest( method="GET", params=None, url=url)
        print(res.json())
        assert res.json()["code"] == 200



    @allure.story("新增地址")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    def test_address_add(self, enterpriseInfo, ini):
        url = "{0}/gw-shop/app/v1/user/address-add".format(self.shopBaseUrl)
        params = {"id":0,"province":"上海市","city":"上海市","area":"静安区","address":"东部国际广场","provinceCode":"310000","cityCode":"310100","areaCode":"310106","source":"2","default":"2","zip_code":"","delivery_name":"老白","delivery_mobile":"17319905367","is_auth_address":"2","lat":"","lng":"","other_info":"东部国际广场"}
        myRequest = SendRequestForOnline(enterpriseInfo)
        res = myRequest.sendRequest( method="POST", params=params, url=url)
        print(res.json())

    @allure.story("地址详情")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    def test_address_detail(self, enterpriseInfo, ini):
        url = "{0}/gw-shop/app/v1/user/address-list".format(self.shopBaseUrl)
        myRequest = SendRequestForOnline(enterpriseInfo)
        res = myRequest.sendRequest( method="GET", params=None, url=url)
        print(res.json())
        try:
            id = res.json()['data'][0]['id']
            url = "{0}/gw-shop/app/v1/user/address-detail".format(self.shopBaseUrl)
            params = {"id": id}
            res = myRequest.sendRequest(method="POST", params=params, url=url)
            print(res.json())
        except KeyError:
            pass

    @allure.story("地址更新")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    def test_address_update(self, enterpriseInfo, ini):
        url = "{0}/gw-shop/app/v1/user/address-list".format(self.shopBaseUrl)
        myRequest = SendRequestForOnline(enterpriseInfo)
        res = myRequest.sendRequest( method="GET", params=None, url=url)
        try:
            id = res.json()['data'][0]['id']
            url = "{0}/gw-shop/app/v1/user/address-update".format(self.shopBaseUrl)
            params = {"id": id, "province": "陕西省", "city": "西安市", "area": "雁塔区", "address": "西部国际广场1号", "source": "2",
                      "default": 2, "zip_code": "", "delivery_name": "白喆", "delivery_mobile": "17319905367", "lat": "",
                      "lng": "", "other_info": "西部国际广场1号"}
            res = myRequest.sendRequest(method="POST", params=params, url=url)
            print(res.json())
        except KeyError:
            pass

    @allure.story("设置订单地址")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    def test_set_order_address(self, enterpriseInfo, ini):
        url = "{0}/gw-shop/app/v1/user/address-list".format(self.shopBaseUrl)
        myRequest = SendRequestForOnline(enterpriseInfo)
        res = myRequest.sendRequest( method="GET", params=None, url=url)
        try:
            id = res.json()['data'][0]['id']
            url = "{0}/gw-shop/app/v1/user/set-order-address".format(self.shopBaseUrl)
            params = {"id": id}
            res = myRequest.sendRequest(method="POST", params=params, url=url)
            print(res.json())
        except KeyError:
            pass

    @allure.story("删除地址")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    def test_address_delete(self, enterpriseInfo, ini):
        url = "{0}/gw-shop/app/v1/user/address-add".format(self.shopBaseUrl)
        params = {"id": 0, "province": "上海市", "city": "上海市", "area": "静安区", "address": "东部国际广场",
                  "provinceCode": "310000", "cityCode": "310100", "areaCode": "310106", "source": "2", "default": "2",
                  "zip_code": "", "delivery_name": "老白", "delivery_mobile": "17319905367", "is_auth_address": "2",
                  "lat": "", "lng": "", "other_info": "东部国际广场"}
        myRequest = SendRequestForOnline(enterpriseInfo)
        res = myRequest.sendRequest( method="POST", params=params, url=url)
        print(res.json())
        id = res.json()['data']['id']
        url = "{0}/gw-shop/app/v1/user/address-delete".format(self.shopBaseUrl)
        params = {"id": id}
        res = myRequest.sendRequest( method="POST", params=params, url=url)
        print(res.json())

    @allure.story("写入追踪")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    def test_address_delete(self, enterpriseInfo, ini):
        url = "{0}/gw-shop/app/v1/trace/write-trace".format(self.shopBaseUrl)
        params = {"action":"access"}
        myRequest = SendRequestForOnline(enterpriseInfo)
        res = myRequest.sendRequest( method="POST", params=params, url=url)
        print(res.json())

    @allure.story("购物车列表")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    def test_store_cart_list(self, enterpriseInfo, ini):
        url = "{0}/gw-shop/app/v1/store-cart/list".format(self.shopBaseUrl)
        params = {"latitude":"","longitude":""}
        myRequest = SendRequestForOnline(enterpriseInfo)
        res = myRequest.sendRequest(method="POST", params=params, url=url)
        print(res.json())

    @allure.story("标签红点")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    def test_tab_red_dot(self, enterpriseInfo, ini):
        url = "{0}/gw-shop/app/v1/content-manage/tab-red-dot".format(self.shopBaseUrl)
        myRequest = SendRequestForOnline(enterpriseInfo)
        res = myRequest.sendRequest(method="GET", params=None, url=url)
        print(res.json())

    @allure.story("购物车更新")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    @pytest.mark.skip("数据有误")
    def test_store_cart_update(self, enterpriseInfo, ini):
        url = "{0}/gw-shop/app/v1/store-cart/update".format(self.shopBaseUrl)
        params = {"cart_id":151592073854528,"number":0,"type":1,"activity_id":0}
        myRequest = SendRequestForOnline(enterpriseInfo)
        res = myRequest.sendRequest(method="POST", params=params, url=url)
        print(res.json())

    @allure.story("购物车删除")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    def test_store_cart_delete(self, enterpriseInfo, ini):
        url = "{0}/gw-shop/app/v1/store-cart/delete".format(self.shopBaseUrl)
        params = {"cart_ids":['']}
        myRequest = SendRequestForOnline(enterpriseInfo)
        res = myRequest.sendRequest(method="POST", params=params, url=url)
        print(res.json())

    @allure.story("商品结算校验")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    def test_store_cart_check(self, enterpriseInfo, ini):
        url='{0}/gw-shop/app/v1/goods/spu-list'.format(self.shopBaseUrl)
        myRequest = SendRequestForOnline(enterpriseInfo)
        res = myRequest.sendRequest(method="GET", params=None, url=url)
        if len(res.json()['data']['list'])>0:
            sku_id = res.json()['data']['list'][0]['default_sku_id']
        else:
            self.logger.info('{0}商品上架中'.format(enterpriseInfo["enterpriName"]))
            return
        url = '{0}/gw-shop/app/v1/store-cart/check'.format(self.shopBaseUrl)
        params={"goods_data": [{"sku_id": sku_id, "number": 1, "postage_delivery_type": 1, "is_store_take": 0, "reference_point_id": 0,"type": 1}]}
        myRequest = SendRequestForOnline(enterpriseInfo)
        res = myRequest.sendRequest(method="POST", params=params, url=url)
        print(res.json())

    @allure.story("加入购物车")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    def test_store_cart_add(self, enterpriseInfo, ini):
        url = '{0}/gw-shop/app/v1/goods/spu-list'.format(self.shopBaseUrl)
        myRequest = SendRequestForOnline(enterpriseInfo)
        res = myRequest.sendRequest(method="GET", params=None, url=url)
        if len(res.json()['data']['list']) > 0:
            sku_id = res.json()['data']['list'][0]['default_sku_id']
        else:
            self.logger.info('{0}商品上架中'.format(enterpriseInfo["enterpriName"]))
            return
        url = "{0}/gw-shop/app/v1/store-cart/add".format(self.shopBaseUrl)
        params = {"sku_id":sku_id,"number":1,"delivery_type":1}
        myRequest = SendRequestForOnline(enterpriseInfo)
        res = myRequest.sendRequest(method="POST", params=params, url=url)
        print(res.json())


