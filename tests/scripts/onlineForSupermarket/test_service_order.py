from tests.login.singleInterfaceLoginConsole import SingleInterfaceLoginConsole
from tests.login.singletonHttpClient import SingletonHttpClient
from tests.common.onLineForSupermarket.extractList import ExtractList
from tests.common.onLineForSupermarket.order import Shoporder
from tests.login.serviceHeader import ServiceHeader
from utils.readerFile import ReaderFile
from utils.parseJson import ParseJson
from log.log import Logger
from utils.myTime import Mytime
import hashlib, requests, pytest


class Test_service_order(object):
    httpClient = SingletonHttpClient.get_instance(flag="onLine")
    log = Logger.Logger()
    shop = Shoporder()
    list = ExtractList()

    @pytest.mark.onLineSupermarket
    @pytest.mark.parametrize('enterpriseInfo', ReaderFile.readerJson("onLineEnterpriseInfo(supermarket)Baize.json"))
    def test_service_orderIndex(self, enterpriseInfo):
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        serviceHeader = ServiceHeader.getServiceHeader(authClient="shop", enterpriseHash=enterpriseHash)
        #查询storeid
        param = {
            "need_commonly_used": True,
            "need_last_select": True,
            "need_address_info": True,
            "province": province,
            "city": city,
            "longitude": "108.948780",
            "latitude": "34.222590",
            "keywords": "",
            "current_extract_id": 0,
            "is_filter_invalid": False
        }
        res = self.list.extract_list(param,header)
        self.log.info("extractList:{0}".format(res))
        storeId = ParseJson.parseJson(res,"object_id")[0]
        #查询订单列表
        param = {"page": 1, "size": 10}
        res = self.shop.store_orderlist(header, param)
        self.log.info("storeOederList :{0}".format(res))
        #更新订单状态
        param = {
                "id": 116346367183883,
                # "enterprise_id":enterpriseID,
                # "operate_store_id":storeId,
                "event": "customer_apply_refund_goods_money",
                "reject_reason": "拒绝退款",
                "logistic_identity": "",
                "logistic_no": ""
            }
        url = "https://shop-api-crs.vchangyi.com/gw-shop/service/v1/new-order/index"
        res = self.httpClient.Post(url=url,json=param,headers=serviceHeader)
        print(res.json())


# # 获取订单商品拆到仓库信息
#         param = {
#             "goods_list": [
#                 {
#                     "sku_id": sku_id,
#                     "number": 1,
#                     "store_id":store_id,
#                     "extract_id": extract_id,
#                     "delivery_type": 2
#         }],
#         "enterprise_id": enterpriseID
#         }
#         res = self.shop.splitGoodsToWarehouse(serviceHeader,param)
#         self.logger.info("splitGoodsToWarehouse :{0}".format(res))
#
#         def splitGoodsToWarehouse(self, header, param):
#             """
#             【服务】获取订单商品拆到仓库信息
#             {
#               "goods_list": [
#                 {
#                   "sku_id": 140787224574336,
#                   "number": 1,
#                   "store_id": 130187700367616,
#                   "extract_id": 1,
#                   "delivery_type": 2
#                 }],
#                 "enterprise_id": 99045793733312
#                 }
#             """
#             url = '{0}/gw-shop/service/v1/new-order/split-goods-to-warehouse'.format(self.shopBaseUrl)
#             res = self.httpClient.Post(url=url, json=param, headers=header)
#             if res.status_code == 200:
#                 return res.json()
#             else:
#                 raise Exception("split goods to warehouse fail", res.text)

    @pytest.mark.onLineSupermarket
    @pytest.mark.parametrize('enterpriseInfo', ReaderFile.readerJson("onLineEnterpriseInfo(supermarket)Baize.json"))
    def test_service_coupon_relation(self, enterpriseInfo):
        """
        获取可关联的代金券列表
        """
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        serviceHeader = ServiceHeader.getServiceHeader(authClient="shop", enterpriseHash=enterpriseHash)
        param = {
                "enterprise_id": enterpriseID,
                "coupon_stock_id": 15324358
            }
        url = "https://shop-api-crs.vchangyi.com/gw-shop/service/v1/coupon-relation/coupon-list"
        res = self.httpClient.Post(url=url, json=param, headers=serviceHeader).json()
        self.log.info("couponRelation :{0}".format(res))
        assert res['code'] == 200 and \
               res['message'] == 'success'

    @pytest.mark.onLineSupermarket
    @pytest.mark.parametrize('enterpriseInfo', ReaderFile.readerJson("onLineEnterpriseInfo(supermarket)Baize.json"))
    def test_service_coupon_relation_merchant(self, enterpriseInfo):
        """
        获取可关联的商家券列表
        """
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        serviceHeader = ServiceHeader.getServiceHeader(authClient="shop", enterpriseHash=enterpriseHash)
        param = {
            "enterprise_id": enterpriseID,
            "coupon_stock_id": 1287690000000435
        }
        url = "https://shop-api-crs.vchangyi.com/gw-shop/service/v1/coupon-relation/merchant-coupon-list"
        res = self.httpClient.Post(url=url, json=param, headers=serviceHeader).json()
        self.log.info("couponRelation :{0}".format(res))
        assert res['code'] == 200 and \
               res['message'] == 'success'

    @pytest.mark.onLineSupermarket
    @pytest.mark.parametrize('enterpriseInfo', ReaderFile.readerJson("onLineEnterpriseInfo(supermarket)Baize.json"))
    def test_service_coupon_list(self, enterpriseInfo):
        """
        获取可关联的优惠券列表
        """
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        serviceHeader = ServiceHeader.getServiceHeader(authClient="shop", enterpriseHash=enterpriseHash)
        param = {"coupon_stock_id":"","status":-1,"page":1,"size":10,"enterprise_id":enterpriseID}
        url = "https://shop-api-crs.vchangyi.com/gw-shop/service/v1/coupon-relation/list"
        res = self.httpClient.Post(url=url, json=param, headers=serviceHeader).json()
        self.log.info("couponRelationList :{0}".format(res))
        assert res['code'] == 200 and \
               res['message'] == 'success'

    # @pytest.mark.onLineSupermarket
    @pytest.mark.parametrize('enterpriseInfo', ReaderFile.readerJson("onLineEnterpriseInfo(supermarket)Baize.json"))
    def test_service_coupon_relation_relation(self, enterpriseInfo):
        """
        关联商家券和优惠券 TODO 校验优惠券批次号和商家券批次号
        """
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        serviceHeader = ServiceHeader.getServiceHeader(authClient="shop", enterpriseHash=enterpriseHash)
        param = {"coupon_stock_id":"15971461","merchant_coupon_stock_id":"1288870000000013","status":1,"enterprise_id":enterpriseID}
        url = "https://shop-api-crs.vchangyi.com/gw-shop/service/v1/coupon-relation/relation"
        res = self.httpClient.Post(url=url, json=param, headers=serviceHeader).json()
        self.log.info("couponRelation :{0}".format(res))
        assert res['code'] == 200 and \
               res['message'] == 'success'


    @pytest.mark.parametrize('enterpriseInfo', ReaderFile.readerJson("onLineEnterpriseInfo(supermarket)Baize.json"))
    def test_service_coupon_relation_changestatus(self, enterpriseInfo):
        """
        启用或禁用关联优惠券 TODO 校验优惠券批次号和商家券批次号
        """
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        serviceHeader = ServiceHeader.getServiceHeader(authClient="shop", enterpriseHash=enterpriseHash)
        param = {"enterprise_id": enterpriseID,"id": 124518504879936,"status": 0}
        url = "https://shop-api-crs.vchangyi.com/gw-shop/service/v1/coupon-relation/change-status"
        res = self.httpClient.Post(url=url, json=param, headers=serviceHeader).json()
        self.log.info("changeStatus :{0}".format(res))
        assert res['code'] == 200 and \
               res['message'] == 'success'

    @pytest.mark.onLineSupermarket
    @pytest.mark.parametrize('enterpriseInfo', ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    def test_service_order_out_statistics(self, enterpriseInfo):
        """
        订单对外统计接口
        """
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        serviceHeader = ServiceHeader.getServiceHeader(authClient="shop", enterpriseHash=enterpriseHash)
        param = {
    "type": 1,
    "params": {
        "enterprise_id": enterpriseID,
        "status": [40,60,62,41,80,81,83,100,200,205]
    }
}
        url = "https://shop-api-crs.vchangyi.com/gw-shop/service/v1/order/out-statistics"
        res = self.httpClient.Post(url=url, json=param, headers=serviceHeader).json()
        self.log.info("outStatistics :{0}".format(res))
        assert res['code'] == 200 and \
               res['message'] == 'success'

    @pytest.mark.onLineSupermarket
    @pytest.mark.parametrize('enterpriseInfo', ReaderFile.readerJson("onLineEnterpriseInfo(supermarket)Baize.json"))
    def test_service_export_order_statement(self, enterpriseInfo):
        """
        异步导出对账单接口
        """
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        serviceHeader = ServiceHeader.getServiceHeader(authClient="shop", enterpriseHash=enterpriseHash)
        param = {"start_time":1634572800,"end_time":1634745599,"enterprise_id":enterpriseID,"operator_id":140269187992704,"operator_name":"xuetong@vchangyi.com"}
        url = "https://shop-api-crs.vchangyi.com/gw-shop/service/v1/order/export-order-statement"
        res = self.httpClient.Post(url=url, json=param, headers=serviceHeader).json()
        self.log.info("exportOrderStatement :{0}".format(res))
        assert res['code'] == 200 and \
               res['message'] == 'success'

    @pytest.mark.onLineSupermarket
    @pytest.mark.parametrize('enterpriseInfo', ReaderFile.readerJson("onLineEnterpriseInfo(supermarket)Baize.json"))
    def test_service_update_order_staff(self, enterpriseInfo):
        """
        更新订单推广人
        """
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        serviceHeader = ServiceHeader.getServiceHeader(authClient="shop", enterpriseHash=enterpriseHash)
        param = {"order_no":"116346367466463","store_id":70,"store_staff_id":0}
        url = "https://shop-api-crs.vchangyi.com/gw-shop/service/v1/order/update-order-store-staff"
        res = self.httpClient.Post(url=url, json=param, headers=serviceHeader).json()
        self.log.info("orderStoreStaff :{0}".format(res))
        assert res['code'] == 200 and \
               res['message'] == 'success'

    @pytest.mark.onLineSupermarket
    @pytest.mark.parametrize('enterpriseInfo', ReaderFile.readerJson("onLineEnterpriseInfo(supermarket)Baize.json"))
    def test_service_order_refundInfoData(self, enterpriseInfo):
        """【服务】获取售后信息弹窗数据"""
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        serviceHeader = ServiceHeader.getServiceHeader(authClient="shop", enterpriseHash=enterpriseHash)
        param = {
            "order_no": 116346367466463,
            "refund_apply_type": 1,
            "order_goods_status": "未收到货",
            "user_problem": "不想要了",
            "return_goods_info": [
                {
                    "return_id": 180971001005056,
                    "return_num": 1
                }
            ]
        }
        url = "https://shop-api-crs.vchangyi.com/gw-shop/service/v1/order/after-sale-add"
        res = self.httpClient.Post(url=url, json=param, headers=serviceHeader).json()
        assert res['code'] == 200 and \
               res['message'] == 'success'

        consoleHeader = SingleInterfaceLoginConsole.loginConsole()
        orderId = 180971000967616
        self.shop.updateOrderStatus(consoleHeader,orderId)

    @pytest.mark.parametrize('enterpriseInfo', ReaderFile.readerJson("onLineEnterpriseInfo(supermarket)Baize.json"))
    def test_service_order_refundInfoData(self, enterpriseInfo):
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        param = {"order_no":"116347156753628"}
        url = "https://shop-api-crs.vchangyi.com/gw-shop/service/v1/order/refund-info-data"
        serviceHeader = ServiceHeader.getServiceHeader(authClient="shop", enterpriseHash=enterpriseHash)
        res = self.httpClient.Post(url=url, json=param, headers=serviceHeader).json()
        self.log.info("couponRelation :{0}".format(res))
        assert res['code'] == 200 and \
               res['message'] == 'success'

    @pytest.mark.onLineSupermarket
    @pytest.mark.parametrize('enterpriseInfo', ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    def test_service_newPurchase_isNewUser(self, enterpriseInfo):
        """【服务】是否为新用户"""
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        userId = header["user_id"]
        serviceHeader = ServiceHeader.getServiceHeader(authClient="shop", enterpriseHash=enterpriseHash)
        param = {"user_id": userId}
        url = "https://shop-api-crs.vchangyi.com/gw-shop/service/v1/user/is-new-user"
        res = self.httpClient.Post(url=url, json=param, headers=serviceHeader).json()
        self.log.info("couponRelation :{0}".format(res))
        assert res['code'] == 200 and \
               res['message'] == 'success'

    @pytest.mark.onLineSupermarket
    @pytest.mark.parametrize('enterpriseInfo', ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    def test_order_storeCartNum(self, enterpriseInfo):
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        if enterpriName == "好宜多优选" or enterpriName == "壹号土猪优选" or enterpriName == "你我他优鲜" :
            return
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        userId = header["user_id"]
        serviceHeader = ServiceHeader.getServiceHeader(authClient="shop", enterpriseHash=enterpriseHash)
        param = {"enterprise_id":enterpriseID,"spu_id":[],"type":1,"user_id":userId}
        url = "https://crs-api.vchangyi.com/gw-shop/service/v1/order/store-cart-num"
        res = self.httpClient.Post(url=url, json=param, headers=serviceHeader).json()
        self.log.info("couponRelation :{0}".format(res))
        assert res['code'] == 200 and \
               res['message'] == 'success'

    @pytest.mark.onLineSupermarket
    @pytest.mark.parametrize('enterpriseInfo', ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    def test_order_extractDetail(self, enterpriseInfo):
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        param = {
                "need_commonly_used": True,
                "need_last_select": True,
                "need_address_info": True,
                "province": province,
                "city": city,
                "longitude": "108.948780",
                "latitude": "34.222590",
                "keywords": "",
                "current_extract_id": 0,
                "is_filter_invalid": False
            }
        res = self.list.extract_list(param,header)
        extractId = ParseJson.parseJson(res, "id")[0]
        serviceHeader = ServiceHeader.getServiceHeader(authClient="shop", enterpriseHash=enterpriseHash)
        param = {"extract_id":extractId}
        url = "https://shop-api-crs.vchangyi.com/gw-shop/app/v1/extract/detail"
        res = self.httpClient.Post(url=url, json=param, headers=header).json()
        self.log.info("couponRelation :{0}".format(res))
        assert res['code'] == 200 and \
               res['message'] == 'success'