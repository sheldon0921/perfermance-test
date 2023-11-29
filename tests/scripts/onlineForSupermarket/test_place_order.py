from utils.readerFile import ReaderFile
from log.log import Logger
from tests.login.serviceHeader import ServiceHeader
from pytest_assume.plugin import assume
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
import time

@allure.feature("(商超)订单")
class Test_place_order:

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

    @allure.story("爆款商品下单")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_place_order(self, enterpriseInfo, ini):
        '''确认订单接口'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        if enterpriName == "和安优选":
            return
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        serviceHeader = ServiceHeader.getServiceHeader(authClient="shop", enterpriseHash=enterpriseHash)
        res = self.list.extract_list(self.data,header)
        self.logger.info("extractList :{0}".format(res))
        for extract in res['data']['list']:
            extract_id = extract['id']
            bs_hours = extract['bs_hours'][0]
            extract_name = extract['extract_name']
            address = extract['address']
            longitude = extract['longitude']
            latitude = extract['latitude']
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
        datas = {"city_optimization":1,
                 "goods_data":[
                     {"sku_id":sku_id,"number":1,"cart_id":0,"activity_id":activity_rule_id,"activity_type":25,
                      "delivery_type":2,"extract_id":extract_id,"extract_longitude":longitude,
                      "extract_latitude":latitude,"extract_name":extract_name,
                      "extract_bs_hours":[bs_hours],
                      "extract_address":address,"extract_is_nearest":1}],
                 "user_address_id":0,"user_latitude":latitude,"user_longitude":longitude,"delivery_type": 2,
        "global_discount_activity_id": 0}
        confirmOrderRes = self.shop.confirm_order(datas,header)
        self.logger.info("confirm order :{0}".format(confirmOrderRes))
        with allure.step(f"{enterpriName}爆款商品确认订单"):
            with assume:assert confirmOrderRes["code"] == 200
            with assume:assert confirmOrderRes["message"] == "success"
        datas = {"type":1}
        res = self.shop.getOrderSetting(header,datas)
        with assume:assert res["code"] == 200
        with assume:assert res["message"] == "success"
        res = self.shop.userExtractAddress(header,datas)
        with assume:
            assert res["code"] == 200
        with assume:
            assert res["message"] == "success"
        datas = {"encryptedData":"hDEgnvq8juKc8/DWoYX3QtQ+c4ikrUSVQC79FJPKO6nQ53pNDBwo3XHH50NV2R4gYoeg3Kw6KGSM3kSf3JXLLcyzlkjLrhcwui1mxC1LmoH00j2xJeD9r1n4PLTPVAAXNU8COaJE73At0IkJKFY4PXXpCt4HVHahc2lh/4EllDvcbYzNBUQDn2WfsqYJTpKkY/TGuTnErHMFUeTl0LNioA==","iv":"CSgC/48Y5uILYUkyk+g1SA=="}
        res = self.shop.userCenterMobile(header,datas)
        #获取活动票据
        store_id = confirmOrderRes['data']['list'][0]['store_info']['id']
        work_id = confirmOrderRes['data']['list'][0]['store_info']['worker_id']
        freight_encrypt = confirmOrderRes['data']['list'][0]['freight']['freight_encrypt']
        deliver_encrypt = confirmOrderRes['data']['list'][0]['deliver_encrypt']
        encrypted_discount_activity = confirmOrderRes['data']['discount_activity']['encrypted_discount_activity']
        off_line_price = confirmOrderRes['data']['list'][0]['goods_data'][0]['off_line_price']
        sku_picture = confirmOrderRes['data']['list'][0]['goods_data'][0]['sku_picture']
        param ={"sku_list": [
                        {
                            "spu_id": spu_id,
                            "rule_id": activity_rule_id,
                            "init_id": 0,
                            "type": 25,
                            "price": off_line_price,
                            "sku_id": sku_id,
                            "buy_num": 1,
                            "sale_type": 2,
                            "store_info": {
                                "extract_id": extract_id,
                                "store_id": store_id
                            },
                            "sku_picture": sku_picture
                        }
                ]
            }
        res = self.activity.getTicketId(header,param)
        self.logger.info("getTicketId :{0}".format(res))
        if res["code"] != 200:
            for i in range(3):
                time.sleep(3+i)
                res = self.activity.getTicketId(header, param)
                if res["code"] == 200:
                    break
                else:
                    raise Exception("获取票据id失败")
        with assume:assert res["code"] == 200
        with assume:assert res["message"] == "success"
        ticket_id = res['data']['ticket_id']
        #订单检查
        param = {
                "goods_data": [
                    {
                        "sku_id": sku_id,
                        "number": 1,
                        "delivery_type": 2,
                        "activity_id": activity_rule_id,
                        "activity_type": 25,
                        "goods_type": 1,
                        "extract_id": extract_id,
                        "store_id": store_id
                    }
                ]
            }
        res = self.shop.confirmCheck(header,param)
        self.logger.info("confirmcheck :{0}".format(res))
        with assume:assert res["code"] == 200
        with assume:assert res["message"] == "success"
        #下单
        param = {
                    "store_id": store_id,
                    "work_id": work_id,
                    "freight_encrypt": freight_encrypt,
                    # "deliver_encrypt":deliver_encrypt,
                    "sku_id": sku_id,
                    "quantity": 1,
                    "type": 25,
                    "price": off_line_price,
                    "delivery_type": 2,
                    "take_point_id": extract_id,
                    "activity_type": 25,
                    "activity_id": activity_rule_id,
                    "ticket_id": ticket_id,
                    "order_data_encrypt": encrypted_discount_activity,
        }
        res = self.shop.add_order(header,param)
        self.logger.info("place order :{0}".format(res))
        with assume:assert res["code"] == 200
        with assume:assert res["message"] == "success"
        main_order_no = res['data'][0]['order_no']
        order_id = res['data'][0]['order_id']
        # 查询订单票据
        param = {"type": 1, "params": {"ticket_id": ticket_id}}
        res = self.shop.outQuery(serviceHeader, param)
        self.logger.info("outQuery :{0}".format(res))
        with assume:assert res["code"] == 200
        with assume:assert res["message"] == "success"
        #查询订单是否支付
        param = {"main_order_no":main_order_no}
        res = self.shop.orderIsPay(header,param)
        self.logger.info("orderIsPay :{0}".format(res))
        is_pay = res['data']['is_pay']
        with assume:assert is_pay == 0
        #查询订单列表
        param = {"page":1,"size":10}
        res = self.shop.store_orderlist(header,param)
        self.logger.info("orderList :{0}".format(res))
        with assume:assert res["code"] == 200
        with assume:assert res["message"] == "success"
        orderData = res['data']['list']
        for order in orderData:
            if main_order_no == order['main_order_no']:
                main_order_id =  order['main_order_info']['id']
                order_no = order['order_no']
                self.logger.info("main_order_id :{0}".format(main_order_id))
            else:
                return
        #查询订单详情
        param = {"order_id":order_id,"main_order_no":main_order_no}
        res = self.shop.orderDetail(header,param)
        self.logger.info("orderDetail :{0}".format(res))
        with assume:assert res["code"] == 200
        with assume:assert res["message"] == "success"
        #查询订单详情service
        param = {"order_id":order_id,"main_order_no":main_order_no}
        res = self.shop.serOrderDetail(serviceHeader,param)
        self.logger.info("serOrderDetail :{0}".format(res))
        #取消订单
        param = {"id":main_order_id,"event":"customer_cancel","refund_reason_id":0}
        res = self.shop.mainOrderMachine(header,param)
        self.logger.info("mainOrderMachine :{0}".format(res))
        with assume:assert res["code"] == 200
        with assume:assert res["message"] == "success"
        #再次购买
        param = {"order_no":order_no}
        res = self.shop.againBuy(header,param)
        self.logger.info("againBuy :{0}".format(res))
        with assume:assert res["code"] == 200
        with assume:assert res["message"] == "success"
        #删除订单
        param = {"order_no":order_no}
        res = self.shop.delOrder(header,param)
        self.logger.info("delete order :{0}".format(res))
        with assume:assert res["code"] == 200
        with assume:assert res["message"] == "success"
        #查询购物车列表
        param = {"reference_point_id":extract_id}
        res = self.shop.cartList(header,param)
        self.logger.info("cartList :{0}".format(res))
        with assume:assert res["code"] == 200
        with assume:assert res["message"] == "success"
        cart_spu = res['data']['goods_data'][0]['goods_list'][0]['spu_id']
        order_cart_id = res["data"]["goods_data"][0]["order_cart_id"]
        #购物车商品数量 TODO 接口未全量
        if enterpriName == "壹号土猪优选" or enterpriName == "你我他优鲜":
            return
        param = {"spu_id":[cart_spu],"type":1}
        res = self.shop.storeCartNum(header,param)
        self.logger.info("storeCartNum :{0}".format(res))
        with assume:assert res["code"] == 200
        with assume:assert res["message"] == "success"
        #清空购物车
        param = {"cart_ids":[order_cart_id]}
        res = self.shop.deleteCart(header,param)
        self.logger.info("deleteCart :{0}".format(res))
        with assume:assert res["code"] == 200
        with assume:assert res["message"] == "success"
