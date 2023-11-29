from tests.common.sendRequest.sendRequest import SendRequest
from tests.login.singletonHttpClient import SingletonHttpClient
from utils.readerIniFile import ReaderIniFile
from utils.readerFile import ReaderFile
from tests.common.onLineForSupermarket.activity import Activity
from utils.parseJson import ParseJson



class OrderForSm(object):
    def __init__(self):
        self.send = SendRequest()
        self.activity = Activity()
        self.httpClient = SingletonHttpClient.get_instance(flag="onLine")
        self.shopUrl=ReaderIniFile.value(key="shopBaseUrl")
        self.consoleUrl = ReaderIniFile.value(section="console_sys_info", key="consoleBaseUrl")
        self.enterpriseID = ReaderIniFile.value(key="enterpriseId")
        self.orderConfirmParam = ReaderFile.readerJson('orderConfirmForSm.json')
        self.orderAddParam = ReaderFile.readerJson('orderAddForSm.json')

    #确认订单
    def confirmOrderForSm(self, param):
        '''

        :param param:{
                        "sku_id": ,
                        "cart_id": ,
                        "extract_id": ,
                        "extract_longitude": ,
                        "extract_latitude": ,
                        "extract_bs_hours": ,
                        "extract_address": ,
                    }
        :return: 返回json格式数据
        '''
        self.orderConfirmParam["goods_data"][0]["sku_id"] = param["sku_id"]
        self.orderConfirmParam["goods_data"][0]["cart_id"] = param["cart_id"]
        self.orderConfirmParam["goods_data"][0]["extract_id"] = param["extract_id"]
        self.orderConfirmParam["goods_data"][0]["extract_longitude"] = param["extract_longitude"]
        self.orderConfirmParam["goods_data"][0]["extract_latitude"] = param["extract_latitude"]
        self.orderConfirmParam["goods_data"][0]["extract_bs_hours"] = param["extract_bs_hours"]
        self.orderConfirmParam["goods_data"][0]["extract_address"] = param["extract_address"]
        url='{0}/gw-shop/app/v1/store-order/confirm'.format(self.shopUrl)
        res=self.send.sendRequest(url,self.orderConfirmParam)
        if res.json()["code"] == 200:
            return res.json()
        else:
            raise Exception('confirmOrder failed',res.text)

        # 下单

    def placeOrderForSm(self, header,param, type=True):
        '''

        :param param:  {
                        "store_id": ,
                        "freight_encrypt": ,
                        "sku_id": ,
                        "cart_id": ,
                        "price": ,
                        "take_point_id":,
                        "work_id":
                        "encrypted_discount_activity":
                    }
        :return: 返回json格式数据
        '''
        try:
            self.orderAddParam["order_data_encrypt"] = param["order_data_encrypt"]
            self.orderAddParam["encrypted_merchant_coupons"] = param["encrypted_merchant_coupons"]
            self.orderAddParam["encrypted_wx_coupons"] = param["encrypted_wx_coupons"]
        except KeyError:
            pass
        print("3333333333333333333333333333333333", param)
        print("2222222222222222222222222222222222", self.orderAddParam)
        self.orderAddParam["list"][0]["store_id"] = param["store_id"]
        self.orderAddParam["list"][0]["work_id"] = param["worker_id"]
        self.orderAddParam["list"][0]["freight_encrypt"] = param["freight_encrypt"]
        # self.orderAddParam["list"][0]["order_data_encrypt"] = param["order_data_encrypt"]
        list = []
        for i in param['goodsData']:
            self.orderAddParam["list"][0]["goods_data"][0]["sku_id"] = i["sku_id"]
            self.orderAddParam["list"][0]["goods_data"][0]["quantity"] = i["quantity"]
            self.orderAddParam["list"][0]["goods_data"][0]["cart_id"] = i["cart_id"]
            self.orderAddParam["list"][0]["goods_data"][0]["price"] = i["price"]
            self.orderAddParam["list"][0]["goods_data"][0]["take_point_id"] = i["take_point_id"]
            if type == False:
                param = {
                    "spu_id": i['spu_id'],
                    "rule_id": i["activity_id"],
                    "type": i["activity_type"],
                    "price": i["activity_price"],
                    "sku_id": i['sku_id'],
                    "buy_num": 1,
                    "extract_id": i["extract_id"],
                    "store_id": param["store_id"]
                }
                res = self.activity.getActivityTicket(param)
                # self.log.info("getActivityTicket:{0}".format(res))
                if 'ticket_id' in  res['data']:
                    ticket_id = res['data']['ticket_id']
                else:
                    raise Exception("未获取到ticket_id",res)
                self.orderAddParam["list"][0]["goods_data"][0]["activity_type"] = i["activity_type"]
                self.orderAddParam["list"][0]["goods_data"][0]["activity_id"] = i["activity_id"]
                self.orderAddParam["ticket_id"] = ticket_id
                self.orderAddParam["list"][0]["goods_data"][0]["type"] = i["activity_type"]
            list.append(self.orderAddParam["list"][0]["goods_data"][0].copy())

        # self.orderAddParam["type"] = self.orderAddParam["list"][0]["goods_data"][0]["activity_type"]
        self.orderAddParam["list"][0]["goods_data"] = list
        url = '{0}/gw-shop/app/v1/store-order/add'.format(self.shopUrl)
        print("00000000000000000000000000000000000000:", self.orderAddParam)
        # self.orderAddParam = {"api_type":1,"list":[{"store_id":152431166726016,"work_id":0,"freight_encrypt":"eyJpdiI6InpYUkVRVzBcL3dlK3VWRUU4WllkR3pBPT0iLCJ2YWx1ZSI6Im5KZFwvdUtpZFptdjZhaXVTUkJUNEtBPT0iLCJtYWMiOiIzYjAyNWZiOTkxODBiODQ4MTFmZWJmZjllNzVjNWI1OTVlNDBhZWRlYjI1MzRkMDU5ZTJkMDc0NjY2ODIxZTBiIn0=","goods_data":[{"sku_id":155305820766272,"quantity":3,"type":1,"cart_id":155323616129728,"price":100,"delivery_type":2,"take_point_id":152431172010240,"activity_type":1,"activity_id":0,"goods_type":1}],"take_goods_time_start":1622250000,"take_goods_time_end":1622527200}],"type":1,"remarks":"","user_coupon_id":0,"encrypted_wx_coupons":"","order_data_encrypt":"78nk6AJBeyJpdiI6IllBK3lyTDk3SnBCcFQ5eDVYQU9qTEE9PSIsInZhbHVlIjoiQkxEOHIrSVE1RWVkbnFlc1JTYXVsZEhWSVcyZEFVcmRUaWZnNGs0RktHS3lZeHZ2UXdWUFpvOUFhek5RN09HSjRmbEx4dG90MlFsbzN3Y09JXC95VTBlUEI3c1FyS3k3OUY1T2ZTQlM0NkFwK3FHNVZsYWNPanQ4b0o1RTNHWmFiTitZcnNkcEdwWGwwMnRHVEw4eTFcL3ZyZlFqSWZIeEVNQ0ZhSVhONDRSdmNLazIzaUlVb093cnYwbVRWU1wvcFo0WEcrZ3pcL0hSMDNqTlI3U1VVbGtnb0JwSm1UQVpkYzE0QVJ4ZEZJRkg5bitsdmF5N1ZaeFdiUDRiZFQyVVlGQ1phSVZ6dVBKd29nd0p6WmVEN2VcLzU1dz09IiwibWFjIjoiYTY1Y2Y2ZTJlODU0MjZkMzBkMGRmMzU3YzA0ZTdmNjEzZTUzMWQwNDUxNTRiOGYwYmNkOTk2YmMyMTZjOTdmOCJ9","take_goods_name":"345","take_goods_mobile":"18291990180","subscriber_info":{}}
        # res = self.send.sendRequest(url, self.orderAddParam)
        res = self.httpClient.Post(url=url,json=self.orderAddParam,headers=header)
        if res.json()["code"] == 200:
            return res.json()
        else:
            raise Exception("placeOrder failed", res.text)

    def confirmOrderBydetail(self,param:dict):
        """
        通过商品详情确认订单

        """
        try:
            params = {
                "goods_data": [
                    {
                        "sku_id": param['sku_id'],
                        "number": param["number"],
                        "cart_id": 0,
                        "activity_id": param['activity_id'],
                        "activity_type": param['activity_type'],
                        "delivery_type": 2,
                        "extract_id": param['extract_id'],
                        "extract_longitude": param['extract_longitude'],
                        "extract_latitude": param['extract_latitude'],
                        "extract_name":param['extract_name'] ,
                        "extract_address": param['extract_address'],
                        "extract_is_nearest": 0
                    }
                ],
                "user_address_id": param['user_address_id'],
                "user_latitude": "34.222590",
                "user_longitude": "108.948780"
            }

        except KeyError:
            params = {
                "goods_data": [
                    {
                        "sku_id": param['sku_id'],
                        "number": param["number"],
                        "cart_id": 0,
                        "extract_id": param['extract_id'],
                        "extract_longitude": param['extract_longitude'],
                        "extract_latitude": param['extract_latitude'],
                        "extract_bs_hours": param['extract_bs_hours'],
                        "extract_address": param['extract_address']
                    }
                ]
            }

        # try:
        #     number = param["number"]
        #     params["number"] = number
        # except KeyError:
        #     pass

        # print("%%%%%%%%%%%%%%%%%%%%%%:",params)
        url = '{0}/gw-shop/app/v1/store-order/confirm'.format(self.shopUrl)
        res = self.send.sendRequest(url=url,params=params,method="post")
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("confirmOrder failed", res.text)

    def placeOrderBydetail(self,param:dict):
        """
        通过商品详情下单
        """
        param = {
            "list": [
                {
                    "store_id": param['store_id'],
                    "work_id": param['work_id'],
                    "freight_encrypt": param['freight_encrypt'],
                    "goods_data": [
                        {
                            "sku_id": param['sku_id'],
                            "quantity": 1,
                            "type": 12,
                            "cart_id": 0,
                            "price": param['price'],
                            "delivery_type": 2,
                            "take_point_id": param['take_point_id'],
                            "activity_type": 12,
                            "activity_id": param['activity_id'],
                        }
                    ]
                }
            ],
            "type": 1,
            "user_coupon_id": 0,
            "ticket_id": param['ticket_id'],
            "order_data_encrypt": param['order_data_encrypt'],
            "take_goods_name": "白喆",
            "take_goods_mobile": "17319905367",
        }
        url = '{0}/gw-shop/app/v1/store-order/add'.format(self.shopUrl)
        res = self.send.sendRequest(url=url,params=param,method="post")
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("placeOrder failed", res.text)

    def getOrderList(self,header):
        param={"status":[20,23],"page":1,"size":10}
        url = '{0}/gw-shop/app/v1/store-order/list'.format(self.shopUrl)
        res = self.httpClient.Post(url=url,data=param,headers=header)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("getOrderId failed", res.text)

    def cancleOrder(self,orderNo):
        """
        orderNo 订单编号
        """
        params = self.getOrderList()
        for i in params['data']['list']:
            for key in i['main_order_info']:
                if i['main_order_info'][key] == orderNo:
                    index = params['data']['list'].index(i)
                    continue
        orderId = params['data']['list'][index]['main_order_info']['id']
        params={"id":orderId,"event":"customer_cancel","refund_reason_id":0}
        url = '{0}/gw-shop/app/v1/main-order/machine'.format(self.shopUrl)
        res = self.send.sendRequest(url=url , params=params , method="post")
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("cancelOrder failed", res.text)

    def getOrderDetail(self, param):
        """
        :param param: {"order_id":orderId,"main_order_no":orderNo}
        :return:
        """
        url = '{0}/gw-shop/app/v1/store-order/detail'.format(self.shopUrl)
        res = self.send.sendRequest(url, param)
        if res.json()["code"] == 200:
            return res.json()
        else:
            raise Exception("getOrderDetail failed", res.text )

    def cancleOrderByorderNo(self,orderNo):
        """
        通过订单号取消未支付的订单，如果传入的订单号在未支付的订单列表中，则取消订单
        :param orderNo: 订单号
        :return:
        """
        if orderNo is None:
            return
        param = {"status": [20, 23], "page": 1, "size": 100}
        url = "{0}/gw-shop/app/v1/store-order/list".format(self.shopUrl)
        res = self.send.sendRequest(url, param).json()
        if res["code"] == 200:
            if len(res["data"]["list"]) == 0:
                return
            if str(res).find(orderNo) != -1:
                return self.cancleOrder(orderNo)
        else:
            raise Exception("getOrderDetail failed", res.text )

    def delOrderByorderNo(self,main_orderNo,orderId,orderNo):
        """
        通过订单号删除已完成的订单，如果传入的订单号在未支付的订单列表中，则取消并删除订单
        :param orderNo: 订单号
        :return:
        """
        param = {"order_id": orderId, "main_order_no": main_orderNo}
        detailRes = self.getOrderDetail(param)
        if ParseJson.parseJson(detailRes,"order_status")[0] == 200:
            self.cancleOrder(main_orderNo)
        else:
            param = {"order_no": str(orderNo)}
            url = "{0}/gw-shop/app/v1/order/del".format(self.shopUrl)
            res = self.send.sendRequest(url, param)
            if res.json()["code"] == 200 and res.json()["message"] == "success":
                return True
            else:
                raise Exception("getOrderDetail failed", res.text )

    def queryConsoleOrderList(self):
        param = {
                "search": {
                    "status": 0,
                    "type": "",
                    "start_time": "",
                    "end_time": "",
                    "order_time_sort": "",
                    "pay_time_sort": "",
                    "unread_remark": "",
                    "delivery_type": 0,
                    "goods_type": "spu_name",
                    "goods_value": "",
                    "order_no": ""
                },
                "page": 1,
                "size": 300
            }
        url = '{0}/gw-console/v1/order/list'.format(self.consoleUrl)
        res = self.send.sendRequest(url,param)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("query console order list fail",res.text)

    def delConsoleOrder(self,orderNo):
        """
        通过主订单号删除后台订单
        """
        param = {"order_no":orderNo}
        url = '{0}/gw-shop/app/v1/manual/delete-order'.format(self.consoleUrl)
        res = self.send.sendRequest(url,param)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("delete console order fail",res.text)



