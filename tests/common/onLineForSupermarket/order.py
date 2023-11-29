import json
from tests.login.login import Login
from tests.login.singletonHttpClient import SingletonHttpClient
from utils.readerIniFile import ReaderIniFile
from utils.myTime import Mytime
from utils.myRandom import MyRandom

class Shoporder:

    def __init__(self):
        self.httpClient = SingletonHttpClient.get_instance(flag="onLine")
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")

    def confirm_order(self, datas,header):

        url = "{0}/gw-shop/app/v1/store-order/confirm".format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url, json=datas, headers=header)
        if res.status_code == 200:
            return res.json()
            # return res
        else:
            raise Exception("Call /gw-shop/app/v1/store-order/confirm !", res.text)
    def add_order(self,header,param):
        """
        下单
        """
        param = {
                "api_type": 1,
                "list": [
                    {
                        "store_id": param['store_id'],
                        "work_id": param['work_id'],
                        "freight_encrypt": param['freight_encrypt'],
                        "deliver_encrypt": "",
                        "goods_data": [
                            {
                                "sku_id": param['sku_id'],
                                "quantity": 1,
                                "type": param['type'],
                                "cart_id": 0,
                                "price": param['price'],
                                "delivery_type": 2,
                                "take_point_id": param['take_point_id'],
                                "activity_type": param['activity_type'],
                                "activity_id": param['activity_id'],
                                "goods_type": 1
                            }
                        ]
                    }
                ],
                "type": 1,
                "remarks": "",
                "user_coupon_id": 0,
                "encrypted_wx_coupons": "",
                "encrypted_merchant_coupons": "",
                "ticket_id": param['ticket_id'],
                "order_data_encrypt": param['order_data_encrypt'],
                "take_goods_name": "白喆",
                "take_goods_mobile": "17319905367",
            }
        url = '{0}/gw-shop/app/v1/store-order/add'.format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url, json=param, headers=header)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("placeOrder failed", res.text)

    def orderIsPay(self,header,param):
        """
        获取订单是否支付
        {"main_order_no":"1234356"}
        """
        url = '{0}/gw-shop/app/v1/store-order/is-pay'.format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url,json=param,headers=header)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("get order is pay fail",res.text)

    def getOrderSetting(self,header,datas):
        location = "/gw-shop/app/v1/store-order/get-order-setting"
        url = "{0}{1}".format(self.shopBaseUrl,location)
        res = self.httpClient.Post(url=url, json=datas, headers=header)
        if res.status_code == 200:
            return res.json()
            # return res
        else:
            raise Exception("Call {0} !".format(location), res.text)

    def store_orderlist(self,headers,datas):
        '''查询订单列表'''
        # datas["user_address_id"] = res["data"]["userAddressId"]
        url = "{0}/gw-shop/app/v1/store-order/list".format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url, json=datas, headers=headers)
        if res.status_code == 200:
            return res.json()
            # return res
        else:
            raise Exception("Call /gw-shop/app/v1/store-order/list !", res.text)

    def userExtractAddress(self,header,datas):
        location = "/gw-shop/app/v1/user/user-extract-address"
        url = "{0}{1}".format(self.shopBaseUrl,location)
        res = self.httpClient.Post(url=url, json=datas, headers=header)
        if res.status_code == 200:
            return res.json()
            # return res
        else:
            raise Exception("Call {0} !".format(location), res.text)

    def userCenterMobile(self,header,datas):
        location = "/gw-shop/app/v1/user-center/mobile"
        url = "{0}{1}".format(self.shopBaseUrl, location)
        res = self.httpClient.Post(url=url, json=datas, headers=header)
        if res.status_code == 200:
            return res.json()
            # return res
        else:
            raise Exception("Call {0} !".format(location), res.text)

    def confirmCheck(self,header,datas):
        location = "/gw-shop/app/v1/store-order/confirm-check"
        url = "{0}{1}".format(self.shopBaseUrl, location)
        res = self.httpClient.Post(url=url, json=datas, headers=header)
        if res.status_code == 200:
            return res.json()
            # return res
        else:
            raise Exception("Call {0} !".format(location), res.text)

    def delOrder(self,header,datas):
        #   {"order_no":"116305709166275"}
        location ="/gw-shop/app/v1/order/del"
        url = "{0}{1}".format(self.shopBaseUrl, location)
        res = self.httpClient.Post(url=url, json=datas, headers=header)
        if res.status_code == 200:
            return res.json()
            # return res
        else:
            raise Exception("Call {0} !".format(location), res.text)

    def mainOrderMachine(self,header,datas):
        # {"id":"172644182102912","event":"customer_cancel","refund_reason_id":0}
        location = "/gw-shop/app/v1/main-order/machine"
        url = "{0}{1}".format(self.shopBaseUrl, location)
        res = self.httpClient.Post(url=url, json=datas, headers=header)
        if res.status_code == 200:
            return res.json()
            # return res
        else:
            raise Exception("Call {0} !".format(location), res.text)

    def againBuy(self,header,datas):
        # {"order_no":"116305705573160"}
        location = "/gw-shop/app/v1/store-cart/again-buy"
        url = "{0}{1}".format(self.shopBaseUrl, location)
        res = self.httpClient.Post(url=url, json=datas, headers=header)
        if res.status_code == 200:
            return res.json()
            # return res
        else:
            raise Exception("Call {0} !".format(location), res.text)

    def serviceReason(self,header):
        datas = {"type":1}
        location = "/gw-shop/app/v1/new-order/reason-list"
        url = "{0}{1}".format(self.shopBaseUrl, location)
        res = self.httpClient.Post(url=url, json=datas, headers=header)
        if res.status_code == 200:
            return res.json()
            # return res
        else:
            raise Exception("Call {0} !".format(location), res.text)

    def orderDetail(self,header,datas):
        location = "/gw-shop/app/v1/store-order/detail"
        url = "{0}{1}".format(self.shopBaseUrl, location)
        res = self.httpClient.Post(url=url, json=datas, headers=header)
        if res.status_code == 200:
            return res.json()
            # return res
        else:
            raise Exception("Call {0} !".format(location), res.text)

    def serOrderDetail(self,header,param):
        """
        service 查询订单详情
        """
        url = '{0}/gw-shop/service/v1/order/detail'.format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url, json=param, headers=header)
        if res.status_code == 200:
            return res.json()
            # return res
        else:
            raise Exception("Call /gw-shop/service/v1/order/detail !", res.text)


    def cartList(self,header,param):
        """
        {"reference_point_id":147554336135040} extract_id
        """
        url = '{0}/gw-shop/app/v1/store-cart/list'.format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url,json=param,headers=header)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("get cart list fail!", res.text)

    def deleteCart(self,header,param):
        """
        {"cart_ids":[180797319367680]}  cartList 返回数据，order_cart_id
        """
        url = '{0}/gw-shop/app/v1/store-cart/delete'.format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url, json=param, headers=header)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("delete cart fail!", res.text)

    def getCartModel(self,header,param):
        """
        param = {}
        """
        url = '{0}/gw-shop/app/v1/store-cart/store-cart-model'.format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url,json=param,headers=header)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("get cart model fail", res.text)
    def storeCartNum(self,header,param):
        """
        {"spu_id":["164871223065152"],"type":1}
        """
        url = '{0}/gw-shop/app/v1/store-cart/store-cart-num'.format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url,json=param,headers=header)
        if res.status_code == 200:
            return res.json()
        else:
            print(res.status_code)
            raise Exception("get cart model fail", res.text)

    def outQuery(self,header,param):
        """
        service 【服务】查询订单票据
        {"type": 1,"params": {"ticket_id": ticket_id}}
        """
        url = '{0}/gw-shop/service/v1/order/out-query'.format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url,json=param,headers=header)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("out query fail",res.text)

    def updateOrderStatus(self,header,orderID):

        param = {"id":orderID,"event":"console_refuse_apply_refund","reject_reason":"111","logistic_identity":"","logistic_no":"","complete_type":""}
        url = "https://crs-api.vchangyi.com/gw-console/v1/new-order/update"
        res = self.httpClient.Post(url=url, json=param, headers=header)

class Store_cart:
    def __init__(self):
        self.httpClient = SingletonHttpClient.get_instance(flag="onLine")
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")

    def store_cart(self, datas,header):

        url = "{0}/gw-shop/app/v1/store-cart/check".format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url, json=datas, headers=header)
        if res.status_code == 200:
            return res.json()
            # return res
        else:
            raise Exception("Call /gw-shop/app/v1/store-cart/check !", res.text)

class Wx_list:
    def __init__(self):
        self.httpClient = SingletonHttpClient.get_instance(flag="onLine")
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")

    def wx_list(self, datas, header):

        url = "{0}/gw-shop/app/v1/coupon/wx-list".format(self.shopBaseUrl)
        res = self.httpClient.GET(url=url, json=datas, headers=header)
        if res.status_code == 200:
            return res.json()
            # return res
        else:
            raise Exception("Call /gw-shop/app/v1/coupon/wx-list !", res.text)

class Get_order_setting:
    def __init__(self):
        self.httpClient = SingletonHttpClient.get_instance(flag="onLine")
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")

    def get_order_setting(self, datas,header):

        url = "{0}/gw-shop/app/v1/store-order/get-order-setting".format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url, json=datas, headers=header)
        if res.status_code == 200:
            return res.json()
            # return res
        else:
            raise Exception("Call /gw-shop/app/v1/store-order/get-order-setting !", res.text)

class Common_config:
    def __init__(self):
        self.httpClient = SingletonHttpClient.get_instance(flag="onLine")
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")

    def common_config(self, datas, header):

        url = "{0}/gw-shop/app/v1/common/config".format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url, json=datas, headers=header)
        if res.status_code == 200:
            return res.json()
            # return res
        else:
            raise Exception("Call /gw-shop/app/v1/common/config !", res.text)

class User_center_mobile:
    def __init__(self):
        self.httpClient = SingletonHttpClient.get_instance(flag="onLine")
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")

    def user_center_mobile(self, datas,header):

        url = "{0}/gw-shop/app/v1/user-center/mobile".format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url, json=datas, headers=header)
        if res.status_code == 200:
            return res.json()
            # return res
        else:
            raise Exception("Call /gw-shop/app/v1/store-cart/check !", res.text)

class Activity_goods_list:
    def __init__(self):
        self.httpClient = SingletonHttpClient.get_instance(flag="onLine")
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")

    def activity_goods_list(self, header,datas):
        url = "{0}/gw-shop/app/v1/activity-center/activity-goods-list".format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url, json=datas, headers=header)
        if res.status_code == 200:
            return res.json()
            # return res
        else:
            raise Exception("Call /gw-shop/app/v1/store-cart/check !", res.text)

    def getTicketId(self, header, param):
        """
        获取活动票据
        param
        {"sku_list": [
            {
                "spu_id": 165753901335104,
                "rule_id": 179909206991872,
                "init_id": 0,
                "type": 25,
                "price": 1290,
                "sku_id": 165754241447808,
                "buy_num": 1,
                "sale_type": 2,
                "store_info": {
                    "extract_id": 149853605912192,
                    "store_id": 149816439188608
                },
                "sku_picture": "https://img-crs.vchangyi.com/goods16272065565710.jpg"
            }
    ]
}
        """

        url = '{0}/gw-shop/app/v1/activity-center/ticket'.format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url, json=param,headers=header)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("get ticket id fail", res.text)