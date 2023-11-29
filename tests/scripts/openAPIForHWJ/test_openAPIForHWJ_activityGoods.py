from tests.common.openAPIForHWJ.shopForHWJ import ShopForHWJ
from utils.shopForDDCApiAssert import ShopForDDCApiAssert
# from tests.common.onLine.getGoodsSpu import GetGoodsSpu
# from tests.common.onLine.shopOrder import ShopOrder
from log.log import Logger
import pytest
import allure
import time
import json


@allure.feature("订单活动模块对外接口")
class Test_OpenAPIForHWJ_ordinaryGoods(object):

    @pytest.fixture()
    def ini(self):
        # self.order = ShopOrder()
        # self.getspu = GetGoodsSpu()
        self.logger = Logger.Logger()
        self.shopForHWJ = ShopForHWJ()
        self.shopForDDCApiAssert = ShopForDDCApiAssert()
        # self.orderNo = None
        yield self.logger,self.shopForHWJ,self.shopForDDCApiAssert
        # 取消订单
        with allure.step("取消订单"):
            cancleOrderRes = self.shopForHWJ.cancleHWJOrder(self.orderNo)
        self.logger.info("cancleOrderRes: {0}".format(cancleOrderRes))
        # 删除订单
        with allure.step("删除订单"):
            deleteOrderRes = self.shopForHWJ.deleteHWJOrder(self.orderNo)
        self.logger.info("deleteOrderRes: {0}".format(deleteOrderRes))



    @pytest.mark.onLineIndex
    @allure.story("购买一口价活动商品流程")
    @pytest.mark.skip(reason="skip")
    def test_openApi_monitor(self, ini):
        # 获取好物集中维达的一口价商品
        # with allure.step("获取好物集中维达的一口价商品"):
        #     hwjActivityGoodsList = self.shopForHWJ.get_hwj_onePriceGoodsList()
        # self.logger.info("hwjActivityGoodsList: {0}".format(hwjActivityGoodsList))
        # actRuleInfo = hwjActivityGoodsList["data"]["activity_rule_info"]
        # quotaNum = actRuleInfo["quota_num"]
        # aloneSpuList = hwjActivityGoodsList["data"]["activity_spu_list"]["alone_spu"]
        # aloneSpuLen = len(aloneSpuList)
        # doubleSpuList = hwjActivityGoodsList["data"]["activity_spu_list"]["double_spu"]
        # doubleSpuLen = len(doubleSpuList)
        # idList = []
        # if aloneSpuLen >= quotaNum:
        #     self.logger.info("aloneSpuLen: {0}".format(aloneSpuLen))
        #     for alonItem in range(0, quotaNum):
        #         idList.append(aloneSpuList[alonItem]["sku_list"][0]["id"])
        # elif doubleSpuLen >= quotaNum:
        #     self.logger.info("doubleSpuLen: {0}".format(doubleSpuLen))
        #     for doubleItem in range(0,quotaNum):
        #         idList.append(doubleSpuList[doubleItem]["sku_list"][0]["id"])
        # else:
        #     self.logger.info("aloneSpuLen: {0},doubleSpuLen: {1}".format(aloneSpuLen, doubleSpuLen))
        #     for alonItem in range(0, aloneSpuLen):
        #         idList.append(aloneSpuList[alonItem]["sku_list"][0]["id"])
        #     for doubleItem in range(0,quotaNum-aloneSpuLen):
        #         idList.append(doubleSpuList[doubleItem]["sku_list"][0]["id"])
        #
        # # 构造请求参数
        # with allure.step("构造请求参数"):
        #     goodsList = []
        # for skuID in idList:
        #     goodsList.append({"sku_id": skuID, "quantity": 1})
        #
        # self.logger.info("goodsList: {0}".format(goodsList))
        # activityInfo = {
        #             "act_id": actRuleInfo["id"],
        #             "n_piece": actRuleInfo["n_piece"],
        #             "n_price": actRuleInfo["n_price"],
        #             "act_title": actRuleInfo["name"],
        #             "limit_count": quotaNum
        #         }
        # self.logger.info("activityInfo: {0}".format(activityInfo))
        # 调用order/pay(generate-self.orderNo)
        # goodsLoist= [{
        #     "sku_id": 133727669368000,
        #     "quantity": 1
        # }, {
        #     "sku_id": 147520550583104,
        #     "quantity": 1
        # }, {
        #     "sku_id": 147520468148288,
        #     "quantity": 1
        # }]
        # activityInfo = {
        #             "act_id": 147522075849728,
        #             "n_piece": 3,
        #             "n_price": 15400,
        #             "act_title": "【一口价】好物集",
        #             "limit_count": 3
        #         }

        # 因为该参数需要一口价活动的活动ID,目前无法获取到。需要定期维护，维护方法：在好物集中一口价模块找到参与一口价的商家，购买其商品，下单，抓取order-pay接口的参数，替换下面参数就可以
        # 修改 loginHWJShop类中对应小程序的企业信息
        goodsList = {"enterprise_id":142545910142016,"delivery_address":"西部国际广场(西安市雁塔区高新路2号)","delivery_name":"test","delivery_mobile":"13888888888","province":"陕西省","city":"西安市","area":"雁塔区","is_temple":0,"is_order_confirm":1,"goods_data":[{"sku_id":145263427602816,"quantity":1},{"sku_id":145263436904832,"quantity":1},{"sku_id":145263443714432,"quantity":1},{"sku_id":147480210438272,"quantity":1},{"sku_id":145263436544384,"quantity":1},{"sku_id":145263429104000,"quantity":1},{"sku_id":145263436728704,"quantity":1}],"is_car":True,"discount_id":-1,"postage_card_id":0,"use_balance":True,"act_info":{"act_id":146265306010688,"n_piece":7,"n_price":7900,"act_title":"79元任选7件0406","limit_count":0},"order_type":2}
        orderPayRes = self.shopForHWJ.hwj_orderPay(goodsList, activityInfo=True)
        self.logger.info("orderPayRes: {0}".format(orderPayRes))
        orderPayTemplate = {
            "code": 0,
            "message": "",
            "order_no": "416189077573300",
            "appid": "wx7f6bf1836bd694ac",
            "final_amount": 9900,
            "order_type": 2
        }
        with allure.step("生成主订单号(/third-order/generate-orderNo),该接口属于内部调用。调用/hwj/order-pay接口会去调用生成主订单接口"):
            self.shopForDDCApiAssert.match_class(orderPayTemplate,orderPayRes)
        self.orderNo = orderPayRes["order_no"]
        assert self.orderNo is not None
        # 生成活动票据
        ticketByorderTemplate = {
            "code": 200,
            "message": "success",
            "request_id": "d88490d6-0901-400f-b263-79d2056b6598",
            "data": {
                "ticket_id": 148758044448064
            }
        }
        ticketByorderNoRes = self.shopForHWJ.ticketByorderNo(self.orderNo)
        self.logger.info("ticketByorderNoRes: {0}".format(ticketByorderNoRes))
        with allure.step("生成活动票据(/activity-center/ticket-by-orderno)"):
            self.shopForDDCApiAssert.match_class(ticketByorderTemplate, ticketByorderNoRes)
        ticketId = ticketByorderNoRes["data"]["ticket_id"]
        # 生成预支付订单
        thirdOrderCreateTemplate={
            "code": 200,
            "message": "success",
            "request_id": "14a7af33-ed7f-449a-8441-a00ec85c5653",
            "data": {
                "main_order_no": "416189077573300",
                "final_amount": 9900
            }
        }
        thirdOrderCreateRes = self.shopForHWJ.thirdOrderCreate(self.orderNo, ticketNo=ticketId)
        self.logger.info("thirdOrderCreateRes: {0}".format(thirdOrderCreateRes))
        with allure.step("生成预支付订单(/third-order/create)"):
            self.shopForDDCApiAssert.match_class(thirdOrderCreateTemplate, thirdOrderCreateRes)
        # 判断订单是否支付
        orderIsPayTemplate = {'code': 200, 'message': 'success', 'request_id': 'autoTest-7b9d-4091-b4af-vJ1618912414', 'data': {'is_pay': 0}}
        orderIsPayRes = self.shopForHWJ.orderIsPay(self.orderNo)
        # orderIsPayRes = json.loads(json.dumps(orderIsPayRes).replace("\'", "\""))
        self.logger.info("orderIsPayRes: {0}".format(orderIsPayRes))
        with allure.step("判断订单是否支付(/store-order/is-pay)"):
            self.shopForDDCApiAssert.match_class(orderIsPayTemplate, orderIsPayRes)
        # 获取预支付信息(调起支付弹窗)
        payMentDetailTemplate={
            "code": 200,
            "message": "success",
            "request_id": "edc9c23f-cb0c-44e8-a3d1-d1c2781f75c3",
            "data": {
                "credential": {
                    "appId": "wx7f6bf1836bd694ac",
                    "timeStamp": "1618907764",
                    "nonceStr": "NGDW86kgpOKRUQGq",
                    "package": "prepay_id=wx201636049156749e2ab702fea545900000",
                    "signType": "MD5",
                    "paySign": "5BCFC0E74831A20880EA78E7FD2F1F0F"
                },
                "risk_type": 1,
                "risk_msg": ""
            }
        }
        orderPaymentDetailRes = self.shopForHWJ.orderPaymentDetail(self.orderNo)
        self.logger.info("orderPaymentDetailRes: {0}".format(orderPaymentDetailRes))
        with allure.step("获取预支付信息,调起支付弹窗(/v1/payment/detail)"):
            self.shopForDDCApiAssert.match_class(payMentDetailTemplate,orderPaymentDetailRes)
        # 链路信息记录
        writeTraceTemplate = {
            "code": 200,
            "message": "success",
            "request_id": "4e8f883d-fa6d-4837-af9a-3c3254f38bb4",
            "data": {}
        }
        params = {"action": "access"}
        writeTraceRes = self.shopForHWJ.writeTrace(params)
        self.logger.info("writeTraceRes: {0}".format(writeTraceRes))
        with allure.step("链路信息记录(/trace/write-trace)"):
            self.shopForDDCApiAssert.match_class(writeTraceTemplate, writeTraceRes)



        # spuID = hwjBCWGoodsList["goods_list"][0]["id"]
        # # 返回的商品列表中不包含商品的sku id,查询商品详情，获取商品的sku id
        # goodsDetail = self.shopForHWJ.get_hwj_goodsDetail(spuID)
        # self.logger.info("hwjBCWGoodsDetail: {0}".format(goodsDetail))
        # skuID = goodsDetail["sku_data"][0]["sku_id"]
        # # /gw-shop/app/v1/third-order/generate-self.orderNo这个接口是内部调用的，在调用/hwj/order-pay这个接口时，会自动调用generate-self.orderNo接口
        # orderPayRes = self.shopForHWJ.hwj_orderPay(skuID)
        # self.logger.info("orderPayRes: {0}".format(orderPayRes))
        # self.orderNo = orderPayRes["order_no"]
        # assert self.orderNo is not None
        # # 生成订单
        # createRes = self.shopForHWJ.thirdOrderCreate(self.orderNo)
        # self.logger.info("createRes: {0}".format(createRes))
        # OrderCreateTemplate = {
        #     'code': 200,
        #     'message': 'success',
        #     'request_id': 'autoTest-7b9d-4091-b4af-bY1618820800',
        #     'data': {
        #         'main_order_no': '416188208038035',
        #         'final_amount': 5733
        #     }
        # }
        # mainOrderNo = createRes["data"]["main_order_no"]
        # # res=ShopForDDCApiAssert().match_class(resTemplate,createRes)
        # ShopForDDCApiAssert().match_class(OrderCreateTemplate,createRes)
        # # 判断订单是否支付
        # isPayRes = self.shopForHWJ.orderIsPay(mainOrderNo)
        # isPayTemplate = {
        #     'code': 200,
        #     'message': 'success',
        #     'request_id': 'autoTest-7b9d-4091-b4af-XA1618884688',
        #     'data': {
        #         'is_pay': 0
        #     }
        # }
        # self.logger.info("res: {0}".format(isPayRes))
        # ShopForDDCApiAssert().match_class(isPayTemplate, isPayRes)
        # # 获取预支付信息  todo token问题暂时无法调通
        # paymentDetailRes = self.shopForHWJ.orderPaymentDetail(mainOrderNo)
        # self.logger.info("paymentDetailRes: {0}".format(paymentDetailRes))
        # # 链路信息记录
        # params = {"sku_id": skuID, "spu_id": spuID, "action": "ordered", "object_id":mainOrderNo}
        # writeTraceRes = self.shopForHWJ.writeTrace(params)
        # self.logger.info("writeTraceRes: {0}".format(writeTraceRes))
        # writeTraceTemplate = {
        #     "code": 200,
        #     "message": "success",
        #     "request_id": "78defd00-2f92-4d53-bab5-8ba8c5b1437f",
        #     "data": {}
        # }
        # ShopForDDCApiAssert().match_class(writeTraceTemplate, writeTraceRes)

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
        # self.self.orderNo = res["data"][0]["order_id"]
        # assert res["code"] == 200
        # self.logger.info("self.orderNo is： {0}".format(rederNo))
        # assert rederNo is not None
        # data = {"status": [20, 23], "page": 1, "size": 10}
        # res = self.order.store_orderlist(datas=data, enterpriseID=enterpriseID, enterpriseHash=enterpriseHash)
        # id = res['data']['list'][0]['main_order_info']['id']
        # param = {"id": id, "event": "customer_cancel", "refund_reason_id": 0}
        # res = self.order.cancel_order(datas=param, enterpriseID=enterpriseID, enterpriseHash=enterpriseHash)
        # assert res.json()["code"] == 200