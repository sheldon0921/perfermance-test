from tests.login.singletonHttpClient import SingletonHttpClient
from tests.common.onLineForSupermarket.extractList import ExtractList
from tests.login.serviceHeader import ServiceHeader
from utils.readerFile import ReaderFile
from utils.parseJson import ParseJson
from utils.myTime import Mytime
import hashlib, requests, pytest
import allure


class Test_service_order1(object):
    httpClient = SingletonHttpClient.get_instance(flag="onLine")
    list = ExtractList()

    @allure.story("服务】订单自提码核销接口")
    @pytest.mark.onLineSupermarket
    @pytest.mark.parametrize('enterpriseInfo', ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    def test_service_verify_take_goods_code(self, enterpriseInfo):
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        # if enterpriName in ["好宜多优选", "壹号土猪优选", "你我他优鲜"]:
        #     pass
        # else:
        header = ServiceHeader.getServiceHeader(authClient="shop", enterpriseHash=enterpriseHash)
        param = {
    "order_no": "116070716945",
    "take_goods_code": "SJ99",
    "enterprise_id": enterpriseID
}
        url = "https://shop-api-crs.vchangyi.com/gw-shop/service/v1/new-order/verify-take-goods-code"
        res = self.httpClient.Post(headers=header, url=url, json=param)
        print(res.url)
        print(res.headers)
        print(res.is_permanent_redirect)
        print("res: {0}".format(res.json()))
        assert res.status_code == 200 and \
               res.json()["code"] == 6006008
        assert res.json()["message"] == "订单不存在或已被删除"

    @allure.story("【服务】获取订单商品拆到仓库信息")
    @pytest.mark.onLineSupermarket
    @pytest.mark.parametrize('enterpriseInfo', ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    def test_service_split_goods_warehouse(self, enterpriseInfo):
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        # if enterpriName in ["好宜多优选", "壹号土猪优选", "你我他优鲜"]:
        #     pass
        # else:
        header = ServiceHeader.getServiceHeader(authClient="shop", enterpriseHash=enterpriseHash)
        param = {
  "goods_list": [
    {
      "sku_id": 1407872245743,
      "number": 1,
      "store_id": 130187700367,
      "extract_id": 1,
      "delivery_type": 2
    }
  ],
  "enterprise_id": enterpriseID
}
        url = "https://shop-api-crs.vchangyi.com/gw-shop/service/v1/new-order/split-goods-to-warehouse"
        res = self.httpClient.Post(headers=header, url=url, json=param)
        print(res.url)
        print(res.headers)
        print(res.is_permanent_redirect)
        print("res: {0}".format(res.json()))
        assert res.status_code == 200 and \
               res.json()["code"] == 409200
        assert res.json()["message"] == "订单商品拆单到仓出错"

    @allure.story("【服务】手工批量发货接口")
    @pytest.mark.onLineSupermarket
    @pytest.mark.parametrize('enterpriseInfo', ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    def test_service_send_goods_batch(self, enterpriseInfo):
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        # if enterpriName in ["好宜多优选", "壹号土猪优选", "你我他优鲜"]:
        #     pass
        # else:
        header = ServiceHeader.getServiceHeader(authClient="shop", enterpriseHash=enterpriseHash)
        param = {
    "enterprise_id": enterpriseID,
    "enterprise_hash": enterpriseHash,
    "data": [
        {
            "order_no": "123",
            "logistic_identity": "zto",
            "logistic_no": "123"
        }
    ]
}
        url = "https://shop-api-crs.vchangyi.com/gw-shop/service/v1/order/send-goods-batch"
        res = self.httpClient.Post(headers=header, url=url, json=param)
        print(res.url)
        print(res.headers)
        print(res.is_permanent_redirect)
        print("res: {0}".format(res.json()))
        assert res.status_code == 200 and \
               res.json()["code"] == 200
        assert res.json()["message"] == "success"
        assert res.json()["data"]["success_num"] == 0

    @allure.story("【服务】订单发货物流查询接口")
    @pytest.mark.onLineSupermarket
    @pytest.mark.parametrize('enterpriseInfo', ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    def test_service_query_order_logistic(self, enterpriseInfo):
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        # if enterpriName in ["好宜多优选", "壹号土猪优选", "你我他优鲜"]:
        #     pass
        # else:
        header = ServiceHeader.getServiceHeader(authClient="shop", enterpriseHash=enterpriseHash)
        param = {
    "order_no": 184659504721024,
    "source": 0
}
        url = "https://shop-api-crs.vchangyi.com/gw-shop/service/v1/order/query-order-logistic"
        res = self.httpClient.Post(headers=header, url=url, json=param)
        print(res.url)
        print(res.headers)
        print(res.is_permanent_redirect)
        print("res: {0}".format(res.json()))
        assert res.status_code == 200 and \
               res.json()["code"] == 200
        assert res.json()["message"] == "success"

    @allure.story("【服务】获取售后信息弹窗数据")
    @pytest.mark.onLineSupermarket
    @pytest.mark.parametrize('enterpriseInfo', ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    def test_service_order_refund_info_data(self, enterpriseInfo):
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        # if enterpriName in ["好宜多优选", "壹号土猪优选", "你我他优鲜"]:
        #     pass
        # else:
        header = ServiceHeader.getServiceHeader(authClient="shop", enterpriseHash=enterpriseHash)
        param = {
             "order_no": "116342099706538"
        }
        url = "https://shop-api-crs.vchangyi.com/gw-shop/service/v1/order/refund-info-data"
        res = self.httpClient.Post(headers=header, url=url, json=param)
        print(res.url)
        print(res.headers)
        print(res.is_permanent_redirect)
        print("res: {0}".format(res.json()))
        assert res.status_code == 200 and \
               res.json()["code"] == 1000000
        assert res.json()["message"] == "订单状态有误，请重新输入"

    @allure.story("【服务】订单接收活动通知")
    @pytest.mark.onLineSupermarket
    @pytest.mark.parametrize('enterpriseInfo', ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    def test_service_order_receive_notice_activity(self, enterpriseInfo):
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        # if enterpriName in ["好宜多优选", "壹号土猪优选", "你我他优鲜"]:
        #     pass
        # else:
        header = ServiceHeader.getServiceHeader(authClient="shop", enterpriseHash=enterpriseHash)
        param = {
			"main_order_no": "123",
			"event": "activity_send_to_open"
		}
        url = "https://shop-api-crs.vchangyi.com/gw-shop/service/v1/order-receive-notice/activity"
        res = self.httpClient.Post(headers=header, url=url, json=param)
        print(res.url)
        print(res.headers)
        print(res.is_permanent_redirect)
        print("res: {0}".format(res.json()))
        assert res.status_code == 200 and \
               res.json()["code"] == 200
        assert res.json()["message"] == "success"

    @allure.story("【服务】更新用户订单备注为已读状态")
    @pytest.mark.onLineSupermarket
    @pytest.mark.parametrize('enterpriseInfo', ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    def test_service_remark_to_read(self, enterpriseInfo):
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        # if enterpriName in ["好宜多优选", "壹号土猪优选", "你我他优鲜"]:
        #     pass
        # else:
        header = ServiceHeader.getServiceHeader(authClient="shop", enterpriseHash=enterpriseHash)
        param = {
            "enterprise_id": enterpriseID,
            "order_no": "18465950472102"
        }
        url = "https://shop-api-crs.vchangyi.com/gw-shop/service/v1/order/remark-to-read"
        res = self.httpClient.Post(headers=header, url=url, json=param)
        print(res.url)
        print(res.headers)
        print(res.is_permanent_redirect)
        print("res: {0}".format(res.json()))
        assert res.status_code == 200 and \
               res.json()["code"] == 200
        assert res.json()["message"] == "success"

    @allure.story("【服务】删除订单物流")
    @pytest.mark.onLineSupermarket
    @pytest.mark.parametrize('enterpriseInfo', ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    def test_service_logistics_delete(self, enterpriseInfo):
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        # if enterpriName in ["好宜多优选", "壹号土猪优选", "你我他优鲜"]:
        #     pass
        # else:
        header = ServiceHeader.getServiceHeader(authClient="shop", enterpriseHash=enterpriseHash)
        param = {
            "enterprise_id": enterpriseID,
               "order_no": "18465950472102",
            "logistic_no": "7534454964738"
        }
        url = "https://shop-api-crs.vchangyi.com/gw-shop/service/v1/order/logistics-delete"
        res = self.httpClient.Post(headers=header, url=url, json=param)
        print(res.url)
        print(res.headers)
        print(res.is_permanent_redirect)
        print("res: {0}".format(res.json()))
        assert res.status_code == 200 and \
               res.json()["code"] == 1000000
        assert res.json()["message"] == "订单物流不存在"

    @allure.story("【服务】接单")
    @pytest.mark.onLineSupermarket
    @pytest.mark.parametrize('enterpriseInfo', ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    def test_service_receive_service_order(self, enterpriseInfo):
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        # if enterpriName in ["好宜多优选", "壹号土猪优选", "你我他优鲜"]:
        #     pass
        # else:
        header = ServiceHeader.getServiceHeader(authClient="shop", enterpriseHash=enterpriseHash)
        param =   {
			"enterprise_id": enterpriseID,
			"order_no": "116346349118820",
			"service_staff_id": 164691425575552,
			"is_new": True,
			"service_store_id": 161636132470848
		}
        url = "https://shop-api-crs.vchangyi.com/gw-shop/service/v1/new-order/receive-service-order"
        res = self.httpClient.Post(headers=header, url=url, json=param)
        print(res.url)
        print(res.headers)
        print(res.is_permanent_redirect)
        print("res: {0}".format(res.json()))
        assert res.status_code == 200 and \
               res.json()["code"] == 409203
        assert res.json()["message"] == "此单已被别人抢走！"

    @allure.story("【服务】根据企业id获取订单统计数据")
    @pytest.mark.onLineSupermarket
    @pytest.mark.parametrize('enterpriseInfo', ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    def test_service_newOrder_orderStatistics(self, enterpriseInfo):
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        # if enterpriName in ["好宜多优选", "壹号土猪优选", "你我他优鲜"]:
        #     pass
        # else:
        header = ServiceHeader.getServiceHeader(authClient="shop", enterpriseHash=enterpriseHash)
        param = {"enterprise_id": enterpriseID,
                 "store_id": 0,
    "time_type": 0,
    "start_time": 1599580800,
    "end_time": 1599667199
                 }
        url = "https://shop-api-crs.vchangyi.com/gw-shop/service/v1/new-order/order-statistics"
        res = self.httpClient.Post(headers=header, url=url, json=param)
        print(res.url)
        print(res.headers)
        print(res.is_permanent_redirect)
        print("res: {0}".format(res.json()))
        assert res.status_code == 200 and \
               res.json()["code"] == 200
        assert res.json()["message"] == "success"

    @allure.story("检查预约时间")
    @pytest.mark.onLineSupermarket
    @pytest.mark.parametrize('enterpriseInfo', ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    def test_service_wxcouponDetail_byStock(self, enterpriseInfo):
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        # if enterpriName in ["好宜多优选", "壹号土猪优选", "你我他优鲜"]:
        #     pass
        # else:
        header = ServiceHeader.getServiceHeader(authClient="shop", enterpriseHash=enterpriseHash)
        param = {"enterprise_id": enterpriseID,
                 "coupon_stock_id": 15901609
                 }
        url = "https://shop-api-crs.vchangyi.com/gw-shop/service/v1/wx-coupon/detail-by-stock"
        res = self.httpClient.Post(headers=header, url=url, json=param)
        print(res.url)
        print(res.headers)
        print(res.is_permanent_redirect)
        print("res: {0}".format(res.json()))
        assert res.status_code == 422 and \
               res.json()["code"] == 6010006
        assert res.json()["message"] == "微信优惠劵不存在"