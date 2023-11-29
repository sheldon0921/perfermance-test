from tests.login.singletonHttpClient import SingletonHttpClient
from tests.common.openAPIForHWJ.shopForHWJLogin import ShopForHWJLogin
from utils.readerIniFile import ReaderIniFile
from utils.myTime import Mytime
import json


class ShopForHWJ(object):
    def __init__(self):
        self.httpclient = SingletonHttpClient.get_instance(flag="HWJ")
        self.shopHeaders = ShopForHWJLogin.loginHWJShop(loginShop="wd")
        self.shopDomain = ReaderIniFile.value(key="shopBaseUrl")

    def get_hwj_goodsList(self, brandID):
        getParam = {"start": 0, "limit": 10, "type": 0, "brand_id": brandID}
        hwjHeaders = ShopForHWJLogin.loginHWJShop("HWJ")
        url = "https://api-prod.haowuji123.com/hwj/brand/goods2"
        res = self.httpclient.Post(url=url, headers=hwjHeaders, json=getParam)
        if res.status_code ==200:
            return res.json()
        else:
            raise Exception("call /hwj/brand/goods2 failed",res.text)

    def get_hwj_goodsDetail(self, spuID):
        params = {"spu_id":spuID,"is_temple":0}
        hwjHeaders = ShopForHWJLogin.loginHWJShop("HWJ")
        url = "https://api-prod.haowuji123.com/hwj/goods-detail"
        res = self.httpclient.Post(url=url, headers=hwjHeaders, json=params)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("call /hwj/goods-detail failed", res.text)


    def get_hwj_activityGoodsList(self):
        # todo 好物集后台调用的接口
        hwjHeaders = ShopForHWJLogin.loginHWJShop("HWJ")
        url = "https://api-prod.haowuji123.com/micro-activity/v1/common/activity-goods-list/all"
        res = self.httpclient.Post(url=url, headers=hwjHeaders, json=params)
        if res.status_code ==200:
            return res.json()
        else:
            raise Exception("call /micro-activity/v1/common/activity-goods-list/all  failed", res.text)
    # todo activity_rule_id
    def get_hwj_onePriceGoodsList(self):
        # todo activity_rule_id enterprise_id
        # ReaderIniFile.value(section="open-api", key="enterprise_id")
        params = {
            "method": "activity.buy_out_price_detail",
            "data": {
                "activity_rule_id": "147522075849728",
                "enterprise_id": "102",
                "user_id": "8002726663315042"
            },
            "platform": "hwj"
        }
        hwjHeaders = ShopForHWJLogin.loginHWJShop("HWJ")
        url = "https://api-prod.haowuji123.com/hwj/oneprice/proxy"
        res = self.httpclient.Post(url=url, headers=hwjHeaders, json=params)
        if res.status_code ==200:
            return res.json()
        else:
            raise Exception("call /hwj/secKill/goods  failed", res.text)


    def hwj_orderPay(self, goodsList, activityInfo=None):
        if activityInfo is None:
            params = {
                "enterprise_id": 102,
                "delivery_address": "西部国际广场(西安市雁塔区高新路2号)",
                "delivery_name": "test",
                "delivery_mobile": "13888888888",
                "province": "陕西省",
                "city": "西安市",
                "area": "雁塔区",
                "is_temple": 0,
                "is_order_confirm": 1,
                "goods_data": goodsList,
                "is_car": False,
                "discount_id": -1,
                "postage_card_id": 0,
                "use_balance": True
            }
        else:
            params = goodsList
        #     params = {
        #         "enterprise_id": 102,
        #         "delivery_address": "西部国际广场(西安市雁塔区高新路2号)",
        #         "delivery_name": "test",
        #         "delivery_mobile": "13888888888",
        #         "province": "陕西省",
        #         "city": "西安市",
        #         "area": "雁塔区",
        #         "is_temple": 0,
        #         "is_order_confirm": 1,
        #         "goods_data": goodsList,
        #         "is_car": False,
        #         "discount_id": -1,
        #         "postage_card_id": 0,
        #         "use_balance": True,
        #         "act_info": activityInfo,
        #         "order_type": 2
        #     }

        hwjHeaders = ShopForHWJLogin.loginHWJShop("HWJ")
        url = "https://api-prod.haowuji123.com/hwj/order-pay"
        res = self.httpclient.Post(url=url, headers=hwjHeaders, json=params)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("call /hwj/order-pay fail", res.text)

    def ticketByorderNo(self, orderNo):
        """
        生成活动票据
        :param params: {"main_order_no":"12345"}
        :return:
        """
        params = {"main_order_no": orderNo}
        url = f"{self.shopDomain}/gw-shop/app/v1/activity-center/ticket-by-orderno"
        res = self.httpclient.Post(url=url, headers=self.shopHeaders, json=params)
        if res.status_code==200:
            return res.json()
        else:
            raise Exception("call /gw-shop/app/v1/activity-center/ticket-by-orderno fail", res.text)

    def orderIsPay(self, main_order_no):
        """
        订单是否支付
        :param params: {"main_order_no":"12345"}
        :return:
        """
        params = {"main_order_no":main_order_no}
        url = f"{self.shopDomain}/gw-shop/app/v1/store-order/is-pay"
        res = self.httpclient.Post(url=url, headers=self.shopHeaders, json=params)
        if res.status_code:
            return res.json()
        else:
            raise Exception("call /gw-shop/app/v1/store-order/is-pay fail", res.text)

    def orderPaymentDetail(self, mainOrderNo):
        """
        获取预支付信息（调起支付弹窗）
        :param params: {"order_no":"12345","is_order_now":1}
        :return:
        """
        params = {"order_no": mainOrderNo}
        url = f"{self.shopDomain}/gw-shop/app/v1/payment/detail"
        # params = json.dumps(params)
        res = self.httpclient.GET(url=url, headers=self.shopHeaders, params=params)
        if res.status_code==200:
            return res.json()
        else:
            raise Exception("call /gw-shop/app/v1/payment/detail fail", res.text)

    def writeTrace(self, params):
        # todo 返回的dict中的Data内容为空
        """
        链路信息记录
        :param params:{"sku_id": 142745970226176,"spu_id":142745969886528,"action":"ordered"}
        :return:
        """
        url = f"{self.shopDomain}/gw-shop/app/v1/trace/write-trace"
        res = self.httpclient.Post(url=url, headers=self.shopHeaders, json=params)
        if res.status_code ==200:
            return res.json()
        else:
            raise Exception("call /gw-shop/app/v1/trace/write-trace fail", res.text)

    def thirdOrderCreate(self, orderNo, ticketNo=None):
        """
        生成预支付订单
        :param params: {"main_order_no":"416185438623725","created_at":"1618543862"}
        :return:
        """
        # hwjHeaders = ShopForHWJLogin.loginHWJShop("HWJ")
        if ticketNo is None:
            params = {"main_order_no": str(orderNo), "created_at":str(Mytime.getCurrTimeStamp())}
        else:
            params = {"main_order_no": str(orderNo), "created_at": str(Mytime.getCurrTimeStamp()), "ticket_id": ticketNo}
        url = f"{self.shopDomain}/gw-shop/app/v1/third-order/create"
        res = self.httpclient.Post(url=url, headers=self.shopHeaders, json=params)
        if res.status_code ==200:
            return res.json()
        else:
            raise Exception("call /gw-shop/app/v1/third-order/create fail", res.text)

    def generateOrderNo(self, params):
        """
        生成订单编号
        :param params: {"main_order_no":"416185438623725","created_at":"1618543862"}
        :return:
        """
        url = f"{self.shopDomain}/gw-shop/app/v1/third-order/generate-orderNo"
        return self.httpclient.Post(url=url, headers=self.shopHeaders, json=params).json()

    # 取消订单
    def cancleHWJOrder(self,orderNo):
        params = {"action": 4, "order_no": orderNo}
        hwjHeaders = ShopForHWJLogin.loginHWJShop("HWJ")
        url = "https://api-prod.haowuji123.com/hwj/order-action"
        res = self.httpclient.Post(url=url, headers=hwjHeaders, json=params)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("call /hwj/order-action fail", res.text)

    def getNoPayOrder(self):
        params = {"status": 1, "start": 0, "limit": 6}
        hwjHeaders = ShopForHWJLogin.loginHWJShop("HWJ")
        url = "https://api-prod.haowuji123.com/hwj/orders"
        res = self.httpclient.Post(url=url, headers=hwjHeaders, json=params)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("call /hwj/orders fail", res.text)

    def deleteHWJOrder(self,orderNo):
        params = {"order_no":orderNo, "action":6}
        hwjHeaders = ShopForHWJLogin.loginHWJShop("HWJ")
        url = "https://api-prod.haowuji123.com/hwj/order-action"
        res = self.httpclient.Post(url=url, headers=hwjHeaders, json=params)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("call /hwj/order-action fail", res.text)



if __name__ == '__main__':
    # params = {
    #     "order_info": {
    #         "origin_amount": 26260,
    #         "shop_coupon_amount": 5000,
    #         "platform_coupon_amount": 1361,
    #         "final_amount": 10539,
    #         "logistics_price": 0,
    #         "delivery_address": "紫薇花园19号楼",
    #         "delivery_name": "李大本事",
    #         "delivery_mobile": "18706732507",
    #         "province": "陕西省",
    #         "city": "西安市",
    #         "area": "雁塔区",
    #         "zip_code": "",
    #         "wx_platform_stocks": [{
    #             "stock_id": "15468826",
    #             "stock_name": "好物集福利社—补贴",
    #             "coupon_value": 1361,
    #             "transaction_minimum": 1362,
    #             "no_cash": 0,
    #             "goods_tag": ["hwj_pay_main_003"]
    #         }],
    #         "wx_shop_stocks": [{
    #             "stock_id": "15499900",
    #             "stock_name": "蓝月亮50优惠券",
    #             "coupon_value": 5000,
    #             "transaction_minimum": 9900,
    #             "no_cash": 1,
    #             "goods_tag": []
    #         }],
    #         "goods_data": [{
    #             "spu_id": 142746223611521,
    #             "spu_no": "",
    #             "sku_id": 142746223876992,
    #             "sku_no": "10001241",
    #             "spu_name": "【119元3件】蓝月亮亮白增艳洗衣液500g*5袋 护衣护色薰衣草香 替换装",
    #             "category_name": "洗护",
    #             "spu_picture": "https://img-crs.vchangyi.com/goods16159722952440.jpg",
    #             "sku_picture": "https://img-crs.vchangyi.com/goods16159722952440.jpg",
    #             "original_price": 7380,
    #             "sell_price": 7380,
    #             "quantity": 1,
    #             "sku_attribute": [{
    #                 "attribute_name": "洗衣液",
    #                 "attribute_item_value": "亮白薰袋装500g*5"
    #             }],
    #             "material_channel_id": 0,
    #             "activity_type": 21,
    #             "activity_id": 144817809841920
    #         }, {
    #             "spu_id": 142746091765568,
    #             "spu_no": "",
    #             "sku_id": 142746091993856,
    #             "sku_no": "10001473",
    #             "spu_name": "【119元3件】蓝月亮深层洁净薰衣草香洗衣液组合1kg瓶装+1kg袋装*2",
    #             "category_name": "洗护",
    #             "spu_picture": "https://img-crs.vchangyi.com/goods16159722284980.jpg",
    #             "sku_picture": "https://img-crs.vchangyi.com/goods16159722284980.jpg",
    #             "original_price": 9900,
    #             "sell_price": 9900,
    #             "quantity": 1,
    #             "sku_attribute": [{
    #                 "attribute_name": "洗衣液",
    #                 "attribute_item_value": "洁净薰1kg+洁净薰袋1kg*2"
    #             }],
    #             "material_channel_id": 0,
    #             "activity_type": 21,
    #             "activity_id": 144817809841920
    #         }, {
    #             "spu_id": 142745969886528,
    #             "spu_no": "",
    #             "sku_id": 142745970226176,
    #             "sku_no": "10001483",
    #             "spu_name": "【119元3件】蓝月亮洗手液500g（瓶+瓶补）*2+ 抑菌吸收呵护健康",
    #             "category_name": "洗护",
    #             "spu_picture": "https://img-crs.vchangyi.com/goods16159721714010.jpg",
    #             "sku_picture": "https://img-crs.vchangyi.com/goods16159721714010.jpg",
    #             "original_price": 8980,
    #             "sell_price": 8980,
    #             "quantity": 1,
    #             "sku_attribute": [{
    #                 "attribute_name": "规格",
    #                 "attribute_item_value": "芦荟抑菌洗手液500g*4"
    #             }],
    #             "material_channel_id": 0,
    #             "activity_type": 21,
    #             "activity_id": 144817809841920
    #         }]
    #     }
    # }
    # mainOrderNo = ShopForHWJ().generateOrderNo(params)["data"]["main_order_no"]
    # print("mainOrderNo: {0}".format(mainOrderNo))
    # # print("ticketByorderNo: {0}".format(ShopForHWJ().ticketByorderNo({"main_order_no": mainOrderNo})))
    # print("thirdOrderCreate: {0}".format(ShopForHWJ().thirdOrderCreate({"main_order_no": str(mainOrderNo), "created_at": str(Mytime.getCurrTimeStamp())})))
    # print("orderIsPay: {0}".format(ShopForHWJ().orderIsPay({"main_order_no": str(mainOrderNo)})))
    # print("orderPaymentDetail: {0}".format(ShopForHWJ().orderPaymentDetail({"order_no": mainOrderNo})))
    # print("writeTrace: {0}".format(ShopForHWJ().writeTrace({"sku_id": 142745970226176,"spu_id":142745969886528,"action":"ordered"})))
    print("get goods list: {0}".format(ShopForHWJ().get_hwj_goodsList(18)))
