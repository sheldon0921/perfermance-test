from tests.login.singletonHttpClient import SingletonHttpClient
from tests.common.onLineForSupermarket.extractList import ExtractList
from tests.login.serviceHeader import ServiceHeader
from utils.readerFile import ReaderFile
from utils.parseJson import ParseJson
from utils.myTime import Mytime
import hashlib, requests, pytest
import allure


class Test_service_store(object):
    httpClient = SingletonHttpClient.get_instance(flag="onLine")
    list = ExtractList()

    @allure.story("商家券签名信息(新老组件数据)->内部调用")
    @pytest.mark.onLineSupermarket
    @pytest.mark.parametrize('enterpriseInfo', ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    def test_service_coupon_model(self, enterpriseInfo):
        """todo,灰度中"""
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        if enterpriName in ["好宜多优选", "壹号土猪优选", "你我他优鲜"]:
            pass
        else:
            header = ServiceHeader.getServiceHeader(authClient="shop", enterpriseHash=enterpriseHash)
            param = {"enterprise_id": enterpriseID,
                      "user_id":11,
                        "type":"new",
                        "coupon_ids": [
                            "170345728490048"]
                     }
            url = "https://shop-api-crs.vchangyi.com/gw-shop/service/v1/wx-coupon/coupon-model"
            res = self.httpClient.Post(headers=header, url=url, json=param)
            print(res.url)
            print(res.headers)
            print(res.is_permanent_redirect)
            print("res: {0}".format(res.json()))
            assert res.status_code == 200 and \
                   res.json()["code"] == 200
            assert res.json()["message"] == "success"

    @allure.story("新增优惠券")
    @pytest.mark.onLineSupermarket
    @pytest.mark.parametrize('enterpriseInfo', ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    def test_service_wx_coupon_add(self, enterpriseInfo):
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        header1 = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        header = ServiceHeader.getServiceHeader(authClient="shop", enterpriseHash=enterpriseHash)
        param = {"enterprise_id": enterpriseID,
                 "coupon_stock_id": "",
			"is_overlay": 2,
			"overlay_coupons": [],
			"range": [],
			"is_all": 1,
			"range_hide": [],
			"display_home": 1,
			"use_day_limit": 1,
			"tag_rule_type": 0,
			"remark": "",
                 }
        url = "https://shop-api-crs.vchangyi.com/gw-shop/service/v1/wx-coupon/add"
        res = self.httpClient.Post(headers=header, url=url, json=param)
        print(res.url)
        print(res.headers)
        print(res.is_permanent_redirect)
        print("res: {0}".format(res.json()))
        assert res.status_code == 200 and \
               res.json()["code"] == 400000
        assert res.json()["message"] == "优惠券批号有误"

    @allure.story("编辑优惠券-外部（好物集）")
    @pytest.mark.onLineSupermarket
    @pytest.mark.parametrize('enterpriseInfo', ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    def test_service_send_coupon_to_user(self, enterpriseInfo):
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        header1 = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        header = ServiceHeader.getServiceHeader(authClient="shop",enterpriseHash=enterpriseHash)
        param = {"enterprise_id":enterpriseID,
			"coupon_id": 177208382311237,
			"user_id": 18095576524819,
			"is_limit": 1,
			"source_data": []
		}
        url = "https://shop-api-crs.vchangyi.com/gw-shop/service/v1/wx-coupon/send-coupon-to-user"
        res = self.httpClient.Post(headers=header,url=url,json=param)
        print(res.url)
        print(res.headers)
        print(res.is_permanent_redirect)
        print("res: {0}".format(res.json()))
        assert res.status_code == 422 and \
               res.json()["code"] == 401013
        assert res.json()["message"] == "券被抢完了~"

    @allure.story("分类列表拖拽排序")
    @pytest.mark.onLineSupermarket
    @pytest.mark.parametrize('enterpriseInfo', ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    def test_service_store_category_sort(self, enterpriseInfo):
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        header1 = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        header = ServiceHeader.getServiceHeader(authClient="shop", enterpriseHash=enterpriseHash)
        param = {"enterprise_id": enterpriseID,
			"cate_tpl_id": 17259667331385,
			"category_id": 18079866392394,
			"pid": 0,
			"sort": 1,
            "type":1
                 }
        url = "https://shop-api-crs.vchangyi.com/gw-shop/service/v1/store/category/sort"
        res = self.httpClient.Post(headers=header, url=url, json=param)
        print(res.url)
        print(res.headers)
        print(res.is_permanent_redirect)
        print("res: {0}".format(res.json()))
        assert res.status_code == 200 and res.json()["code"] == 200
        assert res.json()["message"] == "success"

    @allure.story("获取分类模板设置详情")
    @pytest.mark.onLineSupermarket
    @pytest.mark.parametrize('enterpriseInfo', ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    def test_service_category_config_detail(self, enterpriseInfo):
        """todo,灰度中"""
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        if enterpriName in ["好宜多优选","壹号土猪优选","你我他优鲜"]:
            pass
        else:
            header = ServiceHeader.getServiceHeader(authClient="shop", enterpriseHash=enterpriseHash)
            param = {"enterprise_id": enterpriseID
                 }
            url = "https://shop-api-crs.vchangyi.com/gw-shop/service/v1/category/category-config-detail"
            res = self.httpClient.Post(headers=header, url=url, json=param)
            print(res.url)
            print(enterpriName)
            print(res.headers)
            print(res.is_permanent_redirect)
            print("res: {0}".format(res.json()))
            assert res.status_code == 200 and res.json()["code"] == 200
            assert res.json()["message"] == "success"

    @allure.story("保存分类模板设置")
    @pytest.mark.onLineSupermarket
    @pytest.mark.parametrize('enterpriseInfo', ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    def test_service_category_config_save(self, enterpriseInfo):
        """todo,灰度中"""
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        province = enterpriseInfo['province']
        city = enterpriseInfo['city']
        if enterpriName in ["好宜多优选", "壹号土猪优选", "你我他优鲜"]:
            pass
        else:
            header = ServiceHeader.getServiceHeader(authClient="shop", enterpriseHash=enterpriseHash)
            param = {"enterprise_id": enterpriseID,
        "level": 1,
        "config":{
            "show_group": 2,
            "show_cash": 1,
            "show_sign_price": 1
        }
    }
            url = "https://shop-api-crs.vchangyi.com/gw-shop/service/v1/category/category-config-save"
            res = self.httpClient.Post(headers=header, url=url, json=param)
            print(res.url)
            print(res.headers)
            print(res.is_permanent_redirect)
            print("res: {0}".format(res.json()))
            assert res.status_code == 200 and res.json()["code"] == 200
            assert res.json()["message"] == "success"

