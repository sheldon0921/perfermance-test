from tests.common.onLineForSupermarket.extractList import ExtractList
from tests.login.singletonHttpClient import SingletonHttpClient
from tests.login.serviceHeader import ServiceHeader
from utils.readerIniFile import ReaderIniFile
from utils.readerFile import ReaderFile
import hashlib, requests, pytest,allure
from pytest_assume.plugin import assume
from utils.parseJson import ParseJson
from utils.myTime import Mytime


@allure.feature("综合")
class Test_service_interface(object):
    httpClient = SingletonHttpClient.get_instance(flag="onLine")
    shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")
    list = ExtractList()

    @allure.story("订单-获取订单数量")
    @pytest.mark.onLineSupermarket
    @pytest.mark.parametrize('enterpriseInfo', ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    def test_service_interface(self, enterpriseInfo):
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        header1 = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        param1 = {
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
        res = self.list.extract_list(param1, header1)
        print(res)
        storeId = ParseJson.parseJson(res,"object_id")[0]
        header = ServiceHeader.getServiceHeader(authClient="shop",enterpriseHash=enterpriseHash)
        param = {"enterprise_id":enterpriseID,"store_id":storeId,"status_list":[40,60]}
        url = "{0}/gw-shop/service/v1/order/store-order-count".format(self.shopBaseUrl)
        res = self.httpClient.Post(headers=header,url=url,json=param)
        print("res: {0}".format(res.json()))
        assert res.status_code == 200 and \
               res.json()["code"] == 200

    @allure.story("获取加盟商列表")
    @pytest.mark.onLineSupermarket
    @pytest.mark.parametrize('enterpriseInfo', ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    def test_service_listFranchisee(self, enterpriseInfo):
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        header = ServiceHeader.getServiceHeader(authClient="shop",enterpriseHash=enterpriseHash)
        param = {"page":1,"size":50,"enterprise_id":enterpriseID}
        url = "{0}/gw-shop/service/v1/franchisee/list".format(self.shopBaseUrl)
        res = self.httpClient.Post(headers=header,url=url,json=param)
        print("res: {0}".format(res.json()))
        assert res.status_code == 200 and \
               res.json()["code"] == 200

    @allure.story("获取用户地址")
    @pytest.mark.onLineSupermarket
    @pytest.mark.parametrize('enterpriseInfo', ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    def test_service_userAddress(self, enterpriseInfo):
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        loginHeader = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        param = {"user_address_id":loginHeader["user_address_id"],"enterprise_id":enterpriseID}
        url = "{0}/gw-shop/service/v1/user/user-address".format(self.shopBaseUrl)
        header = ServiceHeader.getServiceHeader(authClient="shop", enterpriseHash=enterpriseHash)
        res = self.httpClient.Post(headers=header, url=url, json=param)
        print("res: {0}".format(res.json()))
        assert res.status_code == 200 and \
               res.json()["code"] == 200

    @allure.story("门店列表")
    @pytest.mark.onLineSupermarket
    @pytest.mark.parametrize('enterpriseInfo', ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    def test_service_store(self, enterpriseInfo):
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        header1 = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        param1 = {
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
        res = self.list.extract_list(param1, header1)
        print(res)
        with allure.step("门店列表"):
            storeId = ParseJson.parseJson(res,"object_id")[0]
            loginHeader = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
            param = {"enterprise_id":enterpriseID,"store_ids":[storeId]}
            url = "{0}/gw-shop/service/v1/store/store/list".format(self.shopBaseUrl)
            header = ServiceHeader.getServiceHeader(authClient="work", enterpriseHash=enterpriseHash)
            res = self.httpClient.Post(headers=header, url=url, json=param)
            print("res: {0}".format(res.json()))
            assert res.status_code == 200 and \
                   res.json()["code"] == 200
        with allure.step("员工所处门店信息列表"):
            workPhone = res.json()["data"]["list"][0]["work_phone"]
            url = "{0}/gw-shop/service/v1/store/worker/list".format(self.shopBaseUrl)
            param = {"is_page": False, "mobile": workPhone, "enterprise_id": enterpriseID, "worker_status": 1, "type": 1}
            res = self.httpClient.Post(headers=header, url=url, json=param)
            print("res: {0}".format(res.json()))
            assert res.status_code == 200 and \
                   res.json()["code"] == 200

    @allure.story("门店设备列表")
    @pytest.mark.onLineSupermarket
    @pytest.mark.parametrize('enterpriseInfo', ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    def test_service_listEquipment(self, enterpriseInfo):
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        url = "{0}/gw-shop/service/v1/store/store/equipment-list".format(self.shopBaseUrl)
        param = {"area_id":"","store_id":"","equipment_type":"","page":1,"size":10,"apiVersion":"old","enterprise_id":enterpriseID}
        header = ServiceHeader.getServiceHeader(authClient="gw-shop", enterpriseHash=enterpriseHash)
        res = self.httpClient.Post(headers=header, url=url, json=param)
        print("res: {0}".format(res.json()))
        assert res.status_code == 200 and \
               res.json()["code"] == 200

    @allure.story("优惠券3")
    @pytest.mark.onLineSupermarket
    @pytest.mark.parametrize('enterpriseInfo', ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    def test_couponUser_myCouponReceive(self, enterpriseInfo):
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        header = self.list.getHeader(enterpriseHash,enterpriseID)
        url = "{0}/gw-shop/app/v1/coupon_user/my-coupon/receive".format(self.shopBaseUrl)
        param = {"id":1,"coupon_ids":2,"current_rule_content":""}
        res = self.httpClient.Post(url=url,json=param,headers=header)
        assert res.status_code == 200

    @allure.story("小程序收藏")
    @pytest.mark.onLineSupermarket
    @pytest.mark.parametrize('enterpriseInfo', ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    def test_pop_content(self, enterpriseInfo):
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        header = self.list.getHeader(enterpriseHash, enterpriseID)
        url = "{0}/gw-shop/app/v1/page/pop-content".format(self.shopBaseUrl)
        param = {"type":1}
        res = self.httpClient.Post(url=url,json=param,headers=header).json()
        assert res["code"] == 200 \
               and res["message"] == "success"
