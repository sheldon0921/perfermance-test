from time import sleep
import allure
import pytest
from tests.common.order.shop.order import Order
from utils.readerFile import ReaderFile
from log.log import Logger
from tests.common.goods.console.goods import Goods as GD
from tests.common.order.console.order import Order as OR
from tests.common.goods.console.specTemplate import SpecTemplate
from tests.common.goods.console.postage import Postage
'''
测试步骤：
1.将商品添加购物车，下单后取消订单
预期结果：
取消订单成功
'''
@allure.feature('下单')
class Test_Order_shop(object):
    @pytest.fixture()
    def ini(self):
        self.order = Order()
        self.log = Logger()
        self.gd = GD()
        self.ord= OR()
        self.addPostageParam = ReaderFile.readerJson("addPostage.json")
        self.addSpecTemplateParam = ReaderFile.readerJson("addSpecTemplate.json")
        self.addGoodsParam = ReaderFile.readerJson("addMutiSkuGoods.json")
        self.addAddressParam=ReaderFile.readerJson('addUserAddress.json')
        self.placeOrderParam=ReaderFile.readerJson('placeOrder.json')
        self.specTemplate = SpecTemplate()
        self.postage = Postage()
        # 添加商品
        addGoodsRes = self.gd.addGoods(self.addPostageParam, self.addSpecTemplateParam, self.addGoodsParam)
        self.log.Logger().info("addGoodRes: {0}".format(addGoodsRes.json()))
        self.spuId = addGoodsRes.json()["data"]["spu_id"]
        with allure.step(f"新增 spu: {self.spuId} 名称: {self.addGoodsParam['spu_name']} 的商品"):
            assert addGoodsRes.json()["data"]["spu_id"] is not None

        # 发布商品
        publishgoodsparam = {'spu_id': self.spuId}
        publishRes = self.gd.publishGoods(publishgoodsparam)
        self.log.Logger().info('publishRes:{0}'.format(publishRes.json()))
        with allure.step(f"发布商品： {self.addGoodsParam['spu_name']} "):
            assert publishRes.json()["data"]["spu_id"] is not None
        self.goodsspuId = publishRes.json()['data']['spu_id']
        self.spuid = publishRes.json()['data']['spu_id']
        # 上架商品
        salegoodsparam = {'spu_id': [self.goodsspuId], 'sku_id': []}
        saleGoodsRes = self.gd.saleGoods(salegoodsparam)
        self.log.Logger().info('saleGoodsRes:{0}'.format(saleGoodsRes))
        # 查询商品sku_id
        queryparam = {"searchType": 2, "searchParams": {"searchString": {"keyword": str(self.spuid), "type": 4},
                                                        "searchInt": {"high": 0, "low": 0, "type": 1},
                                                        "searchChannel": 0,
                                                        "searchTime": {"beginTimestamp": 0, "endTimestamp": 0,
                                                                       "type": 1}, "searchGoodsStatus": 0,
                                                        "searchChannelOwnership": 0,
                                                        "searchSort": {"sortColumn": 0, "sortType": 0}}, "page": 1,
                      "size": 10}
        querygoodslistRes = self.gd.queryGoodsList(queryparam)
        self.skuId = self.skuid = self.postageid = querygoodslistRes['data']['list'][-1]['sku_id']
        #添加用户地址
        addAddressRes=self.order.addAddress(self.addAddressParam)
        self.log.Logger().info('addAddressRes:{0}'.format(addAddressRes))
        self.addressId=addAddressRes['data']['id']
        print('addAddressRes:{0}'.format(addAddressRes))
        with allure.step(f"新增用户收获地址"):
            assert addAddressRes['code'] == 200 and addAddressRes['message'] == 'success'

        yield self.addPostageParam, self.addSpecTemplateParam, self.addGoodsParam, self.specTemplate
        # 查询商品关联的规格模板
        goodsDetailParam = {"spu_id": self.spuId}
        self.resDetail = self.gd.queryGoodsDetail(goodsDetailParam)
        self.log.Logger().info("resDetail: {0}".format(self.resDetail.json()))
        self.listData = self.resDetail.json()["data"]["list"][0]
        self.specTemplateId = self.listData["attribute_template_id"]
        # 获取该商品关联的邮费模板
        self.postageIdList = list()
        skuList = self.listData["sku"]
        for i in range(0, len(skuList)):
            postageId = skuList[i]["postage"][1]["postage_id"]
            self.postageIdList.append(postageId)

        # 删除添加的商品
        delGoods = {"channel_type": 1, "spu_id": self.spuId}
        delRes = self.gd.delSpu(delGoods).json()
        # 删除规格模板
        self.delSpecParam = {"attribute_template_id": self.specTemplateId}
        delRes = self.specTemplate.deleteSpecTemplate(self.delSpecParam)
        with allure.step(f"通过规格模板ID : {self.specTemplateId} 删除规格模板 "):
            assert delRes.status_code == 200
        # 删除邮费模板
        for postageID in self.postageIdList:
            delParam = {"postage_id": postageID}
            delRes = self.postage.delete_postage(delParam)
            self.log.Logger().info("delRes {0}".format(delRes.json()))
            # assert delRes.status_code == 200 and delRes.json()["message"] == "success"
        with allure.step(f"通过邮费模板ID : {postageID} 删除邮费模板 "):
            pass
        # 删除用户地址
        deleteAddressparam = {"id": self.addressId}
        deleteAddressRes = self.order.deleteAddress(deleteAddressparam)
        self.log.Logger().info('deleteAddressRes:{0}'.format(deleteAddressRes))
        with allure.step(f"通过用户ID：{self.addressId} 删除用户收货地址"):
            assert deleteAddressRes['code'] == 200 and deleteAddressRes['message'] == 'success'
    @allure.story('加入购物车下单')
    @pytest.mark.smoke
    def test_order_shop_cart(self,ini):
        #添加购物车
        addStorecartparam={"sku_id":self.skuId,"number":1,"activity_id":0,"type":1}
        with allure.step(f"商品 {self.addGoodsParam['spu_name']} 加入购物车 "):
            addstorecartRes=self.order.addStorecart(addStorecartparam)
            assert addstorecartRes['code'] == 200 and addstorecartRes['message'] == 'success'
        self.log.Logger().info('addstorecartRes:{0}'.format(addstorecartRes))


        #购物车列表
        storecartListparam={"selected_sku_ids":[self.skuId],"latitude":"","longitude":""}
        storecartListRes=self.order.storecartList(storecartListparam)
        print('storecartListRes:{0}'.format(storecartListRes))
        self.cart_id=storecartListRes['data']['goods_data'][0]['goods_list'][0]['cart_id']
        self.log.Logger().info('storecartListRes:{0}'.format(storecartListRes))
        with allure.step(f"查询购物车列表"):
            assert storecartListRes['code'] == 200 and storecartListRes['message'] == 'success'

        #确认订单
        # orderparams = {"goods_data": [{"sku_id": self.skuId, "number": 1, "cart_id": self.cart_id, "activity_type": 1, "delivery_type": 1}]}
        orderparams = {"goods_data":[{"sku_id":self.skuId,"number":1,"cart_id":self.cart_id,"activity_type":1,"delivery_type":1}],"user_address_id":self.addressId}
        confirmOrderRes = self.order.confirmOrder(orderparams)
        freight_encrypt=confirmOrderRes['data']['list'][0]['freight']['freight_encrypt']
        print('freight_encrypt:{0}'.format(freight_encrypt))
        print('confirmOrderRes:{0}'.format(confirmOrderRes))
        self.log.Logger().info('confirmOrderRes:{0}'.format(confirmOrderRes))
        with allure.step(f"确认商品订单信息"):
            assert confirmOrderRes['code'] == 200 and confirmOrderRes['message'] == 'success'
        # 下单
        self.placeOrderParam['list'][0]['freight_encrypt']=freight_encrypt
        self.placeOrderParam['list'][0]['goods_data'][0]['sku_id']=self.postageid
        self.placeOrderParam['list'][0]['goods_data'][0]['cart_id']=self.cart_id
        self.placeOrderParam['user_address_id']=self.addressId
        print('placeOrderParam:{0}'.format(self.placeOrderParam))
        placeOrderRes = self.order.placeOrder(self.placeOrderParam)
        print('placeOrderRes:{0}'.format(placeOrderRes))

        self.log.Logger().info('placeOrderRes:{0}'.format(placeOrderRes))
        if placeOrderRes['message'] == '正在生成订单，请您稍后':
            sleep(2)
        assert placeOrderRes['code'] == 200 and placeOrderRes['message'] == 'success'
        #查询订单
        queryOrderparam={"page":1,"size":10}
        with allure.step(f"查询商品 {self.addGoodsParam['spu_name']} 订单 "):
            queryOrderRes=self.order.queryOrderlist(queryOrderparam)
            assert queryOrderRes['code'] == 200 and queryOrderRes['message'] == 'success'
        print('queryOrderRes:{0}'.format(queryOrderRes))
        self.log.Logger().info('queryOrderRes:{0}'.format(queryOrderRes))
        order_no=queryOrderRes['data']['list'][0]['order_no']
        #查询后台订单
        order_param={"search":{"status":0,"order_no":order_no},"page":1,"size":10}
        order_Res=self.ord.queryOrder(order_param)
        self.log.Logger().info('order_Res:{0}'.format(order_Res))
        with allure.step(f"查询全部订单，状态为：待支付"):
            assert order_Res['data']['list'][0]['status'] == 20 and order_Res['message'] == 'success'
        print('order_Res:{0}'.format(order_Res))

        #查询子订单
        orderNo = placeOrderRes['data'][0]['order_no']
        id=self.order.querySuborder(queryOrderRes, orderNo)

        #取消订单
        cancelOrderparam={"id":id,"event":"customer_cancel","refund_reason_id":0}
        cancelOrderRes=self.order.cancelOrder(cancelOrderparam)
        self.log.Logger().info('cancelOrderRes:{0}'.format(cancelOrderRes))
        with allure.step(f"通过订单ID：{id} 取消订单"):
            assert cancelOrderRes['code'] == 200 and cancelOrderRes['message'] == 'success'

        #查询订单状态：
        '''
        order_status | int |  订单状态：20 待支付，21 已取消，30 待确认, 40 待发货, 41 售后中(待发货)，60 待收货，80 已签收，81 售后中(退货退款)，83 部分退款，100 已完成，200退款中，201 退款失败，205 全部退款成功|
        '''
        orderDetailparam={"order_id":id,"main_order_no":orderNo}
        orderDetailRes=self.order.orderDetail(orderDetailparam)
        self.log.Logger().info('orderDetailRes:{0}'.format(orderDetailRes))
        with allure.step(f"商品订单状态为 ：已取消"):
            assert orderDetailRes['data']['order_data']['order_status'] == 21 and orderDetailRes['message'] == 'success'

        #查询后台已取消订单：

        orderparam={"search":{"status":21,"delivery_type":0,"order_no":order_no},"page":1,"size":10}
        orderRes=self.ord.queryOrder(orderparam)
        self.log.Logger().info('orderRes:{0}'.format(orderRes))
        with allure.step(f"查询后台订单，状态为：已取消"):
            assert orderRes['data']['list'][0]['status'] == 21 and orderRes['message'] == 'success'
        print('orderRes:{0}'.format(orderRes))
