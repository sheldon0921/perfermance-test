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


@allure.feature("活动")
class Test_Activity:

    @pytest.fixture()
    def ini(self):
        self.order = ShopOrder()
        self.logger = Logger.Logger()
        self.getspu = GetGoodsSpu()
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")
        yield self.order, self.logger

    @allure.story("一口价")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    def test_buy_out_price(self, enterpriseInfo, ini):
        url = "{0}/gw-shop/app/v1/activity-center/buy-out-price/detail".format(self.shopBaseUrl)
        params = {"activity_rule_id": ""}
        myRequest = SendRequestForOnline(enterpriseInfo)
        res = myRequest.sendRequest(method="POST", params=params, url=url)
        rJson = res.json()
        print(rJson)
        businessCode = rJson["code"]
        assert businessCode == 200 or businessCode == 60067001

    @allure.story("商品弹幕")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    def test_goods_barrage(self, enterpriseInfo, ini):
        url = "{0}/gw-shop/app/v1/goods/barrage".format(self.shopBaseUrl)
        myRequest = SendRequestForOnline(enterpriseInfo)
        res = myRequest.sendRequest(method="GET", params=None, url=url)
        rJson = res.json()
        print(rJson)
        businessCode = rJson["code"]
        assert businessCode == 200 or businessCode == 60067001

    @allure.story("定价帮助")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    def test_help_price(self, enterpriseInfo, ini):
        url = "{0}/gw-shop/app/v1/activity-center/help/prize".format(self.shopBaseUrl)
        myRequest = SendRequestForOnline(enterpriseInfo)
        res = myRequest.sendRequest(method="POST", params=None, url=url)
        print(res.json())
        assert res.json()["code"] == 200

    @allure.story("用户优惠券检查")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    def test_coupon_user_check(self, enterpriseInfo, ini):
        url = "{0}/gw-shop/app/v1/coupon_user/check".format(self.shopBaseUrl)
        params = {"merchant_coupon_stock_id":"","out_request_no":"","coupon_id":None,"mem_uid":"","coupon_type":2}
        myRequest = SendRequestForOnline(enterpriseInfo)
        res = myRequest.sendRequest(method="POST", params=params, url=url)
        print(res.json())
        assert res.json()["code"] == 200 or res.json()["code"] == 400000

    @allure.story("加购")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    def test_edit_cart(self, enterpriseInfo, ini):
        url = "{0}/gw-shop/app/v1/activity-center/buy-out-price/edit-cart".format(self.shopBaseUrl)
        params = {"activity_rule_id":148901179852608,"sku_id":148886349768320,"spu_id":148886349546432,"sku_picture":"https://img-crs.vchangyi.com/2020/08/27/64443eccd14321aab260edde3f14c4b6.jpg","sku_name":"【69元任选10件】洽洽红杏干100g","attribute_arr":["红杏"],"on_line_price":1766,"operate_type":"add","num":1}
        myRequest = SendRequestForOnline(enterpriseInfo)
        res = myRequest.sendRequest(method="POST", params=params, url=url)
        print(res.json())
        assert res.json()["code"] == 200 or res.json()["code"] == 290003 or res.json()["code"] == 209010

