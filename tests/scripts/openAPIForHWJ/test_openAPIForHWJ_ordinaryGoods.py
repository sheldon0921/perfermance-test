from tests.common.openAPIForHWJ.shopForHWJ import ShopForHWJ
from utils.shopForDDCApiAssert import ShopForDDCApiAssert
# from tests.common.onLine.getGoodsSpu import GetGoodsSpu
# from tests.common.onLine.shopOrder import ShopOrder
from log.log import Logger
import pytest
import allure
import time


@allure.feature("订单活动模块对外接口")
class Test_OpenAPIForHWJ_ordinaryGoods(object):

    @pytest.fixture()
    def ini(self):
        # self.order = ShopOrder()
        # self.getspu = GetGoodsSpu()
        self.logger = Logger.Logger()
        self.shopForHWJ = ShopForHWJ()
        yield self.logger,self.shopForHWJ
        try:
            # 取消订单
            with allure.step("取消订单"):
                self.shopForHWJ.cancleHWJOrder(self.mainOrderNo)
            # 删除订单
            with allure.step("删除订单"):
                self.shopForHWJ.deleteHWJOrder(self.mainOrderNo)
        except AttributeError:
            pass



    @pytest.mark.onLineIndex
    @allure.story("购买普通商品业务流程")
    # @pytest.mark.skip()
    def test_openApi_monitor(self, ini):
        # 获取好物集中的商品列表，并选择列表中的第一个商品
        with allure.step("获取好物集中的商品列表，并选择列表中的第一个商品"):
            hwjBCWGoodsList = self.shopForHWJ.get_hwj_goodsList(3)
        self.logger.info("hwjBCWGoodsList: {0}".format(hwjBCWGoodsList))
        spuID = hwjBCWGoodsList["goods_list"][-1]["id"]
        # 返回的商品列表中不包含商品的sku id,查询商品详情，获取商品的sku id
        goodsDetail = self.shopForHWJ.get_hwj_goodsDetail(spuID)
        self.logger.info("hwjBCWGoodsDetail: {0}".format(goodsDetail))
        skuID = goodsDetail["sku_data"][-1]["sku_id"]
        # /gw-shop/app/v1/third-order/generate-orderNo这个接口是内部调用的，在调用/hwj/order-pay这个接口时，会自动调用generate-orderNo接口
        goodsList =[{
            "sku_id": skuID,
            "quantity": 1
        }]
        orderPayRes = self.shopForHWJ.hwj_orderPay(goodsList)
        self.logger.info("orderPayRes: {0}".format(orderPayRes))
        try:
            orderNo = orderPayRes["order_no"]
        except KeyError:
            return
        with allure.step("生成主订单号(/third-order/generate-orderNo),该接口属于内部调用。调用/hwj/order-pay接口会去调用生成主订单接口"):
            assert orderNo is not None
        # 生成订单
        time.sleep(2)
        createRes = self.shopForHWJ.thirdOrderCreate(orderNo)
        self.logger.info("createRes: {0}".format(createRes))
        OrderCreateTemplate = {
            'code': 200,
            'message': 'success',
            'request_id': 'autoTest-7b9d-4091-b4af-bY1618820800',
            'data': {
                'main_order_no': '416188208038035',
                'final_amount': 5733
            }
        }
        self.mainOrderNo = createRes["data"]["main_order_no"]
        # res=ShopForDDCApiAssert().match_class(resTemplate,createRes)
        with allure.step("生成预支付订单(/third-order/create)"):
            ShopForDDCApiAssert().match_class(OrderCreateTemplate,createRes)
        # 判断订单是否支付
        isPayRes = self.shopForHWJ.orderIsPay(self.mainOrderNo)
        isPayTemplate = {
            'code': 200,
            'message': 'success',
            'request_id': 'autoTest-7b9d-4091-b4af-XA1618884688',
            'data': {
                'is_pay': 0
            }
        }
        self.logger.info("res: {0}".format(isPayRes))
        with allure.step("判断订单是否支付(/store-order/is-pay)"):
            ShopForDDCApiAssert().match_class(isPayTemplate, isPayRes)
        # 获取预支付信息  todo token问题暂时无法调通
        paymentDetailRes = self.shopForHWJ.orderPaymentDetail(self.mainOrderNo)
        self.logger.info("paymentDetailRes: {0}".format(paymentDetailRes))
        # 链路信息记录
        params = {"sku_id": skuID, "spu_id": spuID, "action": "ordered", "object_id":self.mainOrderNo}
        writeTraceRes = self.shopForHWJ.writeTrace(params)
        self.logger.info("writeTraceRes: {0}".format(writeTraceRes))
        writeTraceTemplate = {
            "code": 200,
            "message": "success",
            "request_id": "78defd00-2f92-4d53-bab5-8ba8c5b1437f",
            "data": {}
        }
        with allure.step("链路信息记录(/trace/write-trace)"):
            ShopForDDCApiAssert().match_class(writeTraceTemplate, writeTraceRes)


        # """下单接口"""
        # enterpriName = "好物集直营店"
        # enterpriseID = "134034389742592"
        # enterpriseHash = "6958815a8e394802a70e1c9a0495d46a"
        # Res = self.getspu.get_goods_spu(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        # if len(Res['data']['list']) > 0:
        #     # spu_id = Res['data']['list'][0]['spu_id']
        #     sku_id = Res['data']['list'][0]['default_sku_id']
        #     # goodsName = Res['data']['list'][0]['sku_name']
        # else:
        #     self.logger.info('{0}商品上架中'.format(enterpriName))
        # # print("\nenterpriName: ", enterpriName, "enterpriseHash: ", enterpriseHash)
        # if enterpriseID == '95489912226048':
        #     return
        # self.datas = {"goods_data": [{"sku_id": sku_id, "number": 1, "cart_id": 0, "delivery_type": 1}],
        #               "user_address_id": 0}
        # try:
        #     self.res = self.order.confirm_order(datas=self.datas, enterpriseID=enterpriseID,
        #                                         enterpriseHash=enterpriseHash)
        #     self.freight_encrypt = self.res.json()["data"]["list"][0]["freight"]["freight_encrypt"]
        #     self.sell_price = self.res.json()["data"]["list"][0]["goods_data"][0]["sell_price"]
        # except KeyError as e:
        #     self.logger.info(self.res.json()['message'])
        #     return
        # datas = {"api_type": 1,
        #          "list": [{"store_id": 0,
        #                    "work_id": 0,
        #                    "freight_encrypt": self.freight_encrypt,
        #                    "goods_data": [{"sku_id": sku_id,
        #                                    "quantity": 1,
        #                                    "type": 1,
        #                                    "cart_id": 0,
        #                                    "price": self.sell_price,
        #                                    "delivery_type": 1,
        #                                    "take_point_id": 0,
        #                                    "activity_type": 1,
        #                                    "activity_id": 0,
        #                                    "goods_type": 1}]
        #                    }],
        #          "type": 1,
        #          "remarks": "",
        #          "user_coupon_id": 0,
        #          "encrypted_wx_coupons": "",
        #          "order_data_encrypt": "",
        #          "user_address_id": 0}
        #
        # res = self.order.add_order(datas=datas, enterpriseID=enterpriseID, enterpriseHash=enterpriseHash)
        # time.sleep(2)
        # self.orderNo = res["data"][0]["order_id"]
        # assert res["code"] == 200
        # self.logger.info("orderNo is： {0}".format(rederNo))
        # assert rederNo is not None
        # data = {"status": [20, 23], "page": 1, "size": 10}
        # res = self.order.store_orderlist(datas=data, enterpriseID=enterpriseID, enterpriseHash=enterpriseHash)
        # id = res['data']['list'][0]['main_order_info']['id']
        # param = {"id": id, "event": "customer_cancel", "refund_reason_id": 0}
        # res = self.order.cancel_order(datas=param, enterpriseID=enterpriseID, enterpriseHash=enterpriseHash)
        # assert res.json()["code"] == 200