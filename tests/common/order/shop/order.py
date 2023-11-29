import os
print(os.path)
# from tests.login.httpclient import HttpClient
from tests.login.singletonHttpClient import SingletonHttpClient
from utils.readerIniFile import ReaderIniFile
from log.log import Logger
from utils.readerFile import ReaderFile
from tests.common.goods.console.specTemplate import SpecTemplate
from tests.common.goods.console.postage import Postage
from utils.myTime import Mytime
from utils.myJson import MyJson
import json


class Order(object):

    def __init__(self):
        self.httpclient = SingletonHttpClient.get_instance()
        self.shopUrl=ReaderIniFile.value(key="shopBaseUrl")
        self.enterpriseID = ReaderIniFile.value(key="enterpriseId")
        self.placeOrderParam = ReaderFile.readerJson('placeOrder.json')

    #确认订单
    def confirmOrder(self, param):
        '''

        :param param:{"goods_data":[{"sku_id":self.skuId,"number":1,"cart_id":self.cart_id,"activity_type":1,"delivery_type":1}],"user_address_id":self.addressId}
        :return: 返回json格式数据
        '''
        url='{0}/gw-shop/app/v1/store-order/confirm'.format(self.shopUrl)
        res=self.httpclient.Post(url=url,json=param)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception('confirmOrder failed',res.text)

    #下单
    def placeOrder(self,param):
        '''

        :param param:  data/placeOrder.json中的数据，需要替换 sku_id, cart_id, freight_encrypt, user_address_id
        :return: 返回json格式数据
        '''
        param = json.loads(json.dumps(param).replace("133",self.enterpriseID))
        url='{0}/gw-shop/app/v1/store-order/add'.format(self.shopUrl)
        res=self.httpclient.Post(url=url,json=param)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("placeOrder failed",res.text)

    #获取邮费配置
    def getpostAge(self,param):
        '''

        :param param: {"sku_id":self.postageid,"activity_id":"","module":"default"}
        :return: 返回json格式数据
        '''
        url='{0}/gw-shop/app/v1/goods/sku-postage'.format(self.shopUrl)
        res=self.httpclient.Post(url=url,json=param)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception('getpostAge failed',res.text)
    #加入购物车
    def addStorecart(self,param):
        '''

        :param param: {"sku_id":self.skuId,"number":1,"activity_id":0,"type":1}
        :return: 返回json格式数据
        '''
        url='{0}/gw-shop/app/v1/store-cart/add'.format(self.shopUrl)
        res=self.httpclient.Post(url=url,json=param)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception('addStorecart failed',res.text)
    #选择购物车商品
    # def checkGoods(self,param):
    #     url='{0}/gw-shop/app/v1/store-cart/check'.format(self.shopUrl)
    #     res=self.httpclient.Post(url=url,json=param)
    #     if res.status_code == 200:
    #         return res.json()
    #     else:
    #         raise Exception('checkGoods failed',res.text)
    #检查订单
    # def confirmcheck(self,param):
    #     url='{0}/gw-shop/app/v1/store-order/confirm-check'.format(self.shopUrl)
    #     res=self.httpclient.Post(url=url,json=param)
    #     if res.status_code == 200:
    #         return res.json()
    #     else:
    #         raise Exception('confirmcheck failed',res.text)
    #购物车列表
    def storecartList(self,param):
        '''

        :param param: {"selected_sku_ids":[sku_id],"latitude":"","longitude":""}
        :return:  返回json格式数据
        '''
        url='{0}/gw-shop/app/v1/store-cart/list'.format(self.shopUrl)
        res=self.httpclient.Post(url=url,json=param)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception('storecartList failed',res.text)
    #查询订单列表
    def queryOrderlist(self,param):
        '''

        :param param: {"page":1,"size":10}
        :return:    返回json格式数据
        '''
        url='{0}/gw-shop/app/v1/store-order/list'.format(self.shopUrl)
        res=self.httpclient.Post(url=url,json=param)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception('queryOrderlist failed',res.text)

    #主订单查询子订单
    def querySuborder(self,dict,param):
        '''

        :param dict:     字典格式，由查询订单列表返回数据
        :param param:   主订单编号
        :return:    返回子订单ID，类型str
        '''
        if len(dict['data']['list']) > 1:
            for i in dict['data']['list']:
                if i['main_order_no'] == param:
                    id = i['main_order_info']['id']
                    continue
        return int(id)
    #取消订单
    def cancelOrder(self,param):
        '''
        :param param: 数据格式：{"id":,"event":"customer_cancel","refund_reason_id":0}
        :return: 返回Json格式内容
        '''
        url='{0}/gw-shop/app/v1/main-order/machine'.format(self.shopUrl)
        res=self.httpclient.Post(url=url,json=param)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception('cancelOrder failed',res.text)
    #订单详情
    def orderDetail(self,param):
        '''

        :param param: {"order_id": 143642601439872  ,"main_order_no": 416164099886443   }
        :return:    返回json格式数据
        '''
        url='{0}/gw-shop/app/v1/store-order/detail'.format(self.shopUrl)
        res=self.httpclient.Post(url=url,json=param)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception('orderDetail failed',res.text)

    #添加默认地址
    def addAddress(self,param):
        '''

        :param param:  data/addUserAddress.json 的数据
        :return:    返回json格式数据
        '''
        url='{0}/gw-shop/app/v1/user/address-add'.format(self.shopUrl)
        res=self.httpclient.Post(url=url,json=param)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception('addAddress failed',res.text)
    #删除地址
    def deleteAddress(self,param):
        '''

        :param param: {'id':  地址ID}
        :return:    返回json格式数据
        '''
        url='{0}/gw-shop/app/v1/user/address-delete'.format(self.shopUrl)
        res=self.httpclient.Post(url=url,json=param)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception('deleteAddress failed',res.text)

    def directOrder(self,dict):
        '''
        用户直接下单
        :param dict: 传入类型为字典，键为： skuid，addressid
        :return: 返回字典类型，返回数据包括：主订单编号: main_order_no，子订单编号: order_no，子订单ID: order_id
        '''
        dict1={}
        param={"sku_id":dict['skuid'],"activity_id":"","module":"default"}
        self.getpostAge(param)
        params={"goods_data":[{"sku_id":dict['skuid'],"number":1,"cart_id":0,"delivery_type":1}],"user_address_id":dict['addressid']}
        res=self.confirmOrder(params)
        freight_encrypt = res['data']['list'][0]['freight']['freight_encrypt']
        self.placeOrderParam = ReaderFile.readerJson('placeOrder.json')
        self.placeOrderParam['list'][0]['freight_encrypt'] = freight_encrypt
        self.placeOrderParam['list'][0]['goods_data'][0]['sku_id'] = dict['skuid']
        self.placeOrderParam['list'][0]['goods_data'][0]['cart_id'] = 0
        self.placeOrderParam['user_address_id'] = dict['addressid']
        res=self.placeOrder(self.placeOrderParam)
        main_order_no=res['data'][0]['order_no']
        param={"page": 1, "size": 10}
        res=self.queryOrderlist(param)
        order_no=res['data']['list'][0]['order_no']
        order_id=self.querySuborder(res,main_order_no)
        dict1['main_order_no']=main_order_no
        dict1['order_no']=order_no
        dict1['order_id']=order_id
        return dict1

    def shopOrder(self,dict):
        '''
        用户添加购物车下单
        :param dict: 传入类型为字典，键为： skuid，addressid
        :return: 返回字典类型，返回数据包括：主订单编号: main_order_no，子订单编号: order_no，子订单ID: order_id
        '''
        dict1={}
        param={"sku_id":dict['skuid'],"number":1,"activity_id":0,"type":1}
        res=self.addStorecart(param)
        param={"selected_sku_ids":[dict['skuid']],"latitude":"","longitude":""}
        Res=self.storecartList(param)
        print(Res)
        cartid=Res['data']['goods_data'][0]['goods_list'][0]['cart_id']
        param={"goods_data":[{"sku_id":dict['skuid'],"number":1,"cart_id":cartid,"activity_type":1,"delivery_type":1}],"user_address_id":dict['addressid']}
        res=self.confirmOrder(param)
        freight_encrypt=res['data']['list'][0]['freight']['freight_encrypt']
        self.placeOrderParam['list'][0]['freight_encrypt'] = freight_encrypt
        self.placeOrderParam['list'][0]['goods_data'][0]['sku_id'] = dict['skuid']
        self.placeOrderParam['list'][0]['goods_data'][0]['cart_id'] = cartid
        self.placeOrderParam['user_address_id'] = dict['addressid']
        res=self.placeOrder(self.placeOrderParam)
        print(res)
        main_order_no = res['data'][0]['order_no']
        param = {"page": 1, "size": 10}
        res = self.queryOrderlist(param)
        order_no = res['data']['list'][0]['order_no']
        order_id = self.querySuborder(res, main_order_no)
        dict1['main_order_no'] = main_order_no
        dict1['order_no'] = order_no
        dict1['order_id'] = order_id
        return dict1

    def cancelorder(self,dict):
        '''
        取消订单
        :param dict: 传入类型为字典，键为：order_id
        :return: 返回json格式数据
        '''
        param={"id": dict['order_id'], "event": "customer_cancel", "refund_reason_id": 0}
        res=self.cancelOrder(param)
        print(res)

    def deladdress(self,dict):
        '''
        删除用户地址
        :param dict: 传入类型为字典，键为：addressid
        :return:  返回json格式数据
        '''
        param={"id": dict['addressid']}
        self.deleteAddress(param)





