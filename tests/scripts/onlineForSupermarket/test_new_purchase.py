from tests.common.onLine.shopOrder import ShopOrder
from utils.readerFile import ReaderFile
from log.log import Logger
from tests.common.onLine.getGoodsSpu import GetGoodsSpu
from tests.common.onLineForSupermarket.extractList import ExtractList
from utils.readerIniFile import ReaderIniFile
import pytest
import allure
from time import sleep
from tests.common.sendRequest.sendRequestForOnline import SendRequestForOnline

@allure.feature("新人购")
class Test_Activity:

    @pytest.fixture()
    def ini(self):
        self.order = ShopOrder()
        self.logger = Logger.Logger()
        self.getspu = GetGoodsSpu()
        self.extract = ExtractList()
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")
        yield self.order, self.logger

    @allure.story("判断是否为新人")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_isnewuser(self, enterpriseInfo, ini):
        """
        是否是新人
        """
        url = '{0}/gw-shop/app/v1/activity-center/new-purchase/is-new-user'.format(self.shopBaseUrl)
        myRequest = SendRequestForOnline(enterpriseInfo)
        res = myRequest.sendRequest(url=url,params=None , method="post",version="supermark")
        print(res.json())
        assert res.json()["code"] == 200

    @allure.story("新人购详情页")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_newbuy(self,enterpriseInfo, ini):
        """
        新人购详情页
        """
        url = '{0}/gw-shop/app/v1/extract/list'.format(self.shopBaseUrl)
        myRequest = SendRequestForOnline(enterpriseInfo)
        res = myRequest.sendRequest(url=url, params=None, method="post", version="supermark")
        extract_id = res.json()['data']['list'][0]['id']
        print(extract_id)
        param = {"extract_id":extract_id,"template_type":"index"}
        url = '{0}/gw-shop/app/v1/new-template/page-config'.format(self.shopBaseUrl)
        myRequest = SendRequestForOnline(enterpriseInfo)
        res = myRequest.sendRequest(url=url, params=param, method="post", version="supermark")
        print(res.json())
        try:
            activity_rule_id = res.json()['data']['new_buy_data']['new_buy_info']['activity_rule_id']
        except KeyError:
            return
        param = {"page": 1, "size": 999, "activity_rule_id": activity_rule_id, "list_search": {"type": 11}}
        url = '{0}/gw-shop/app/v1/new-template/new-buy'.format(self.shopBaseUrl)
        myRequest = SendRequestForOnline(enterpriseInfo)
        res = myRequest.sendRequest(url=url, params=param, method="post", version="supermark")
        print(res.json())
        # todo
        assert res.json()["code"] == 200 or res.json()["code"] == 407010

    @allure.story("加购判断")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_checkcartgoods(self,enterpriseInfo, ini):
        """
        加购判断

        """
        url = '{0}/gw-shop/app/v1/extract/list'.format(self.shopBaseUrl)
        myRequest = SendRequestForOnline(enterpriseInfo)
        res = myRequest.sendRequest(url=url, params=None, method="post", version="supermark")
        extract_id = res.json()['data']['list'][0]['id']
        print(extract_id)
        param = {"extract_id": extract_id, "template_type": "index"}
        url = '{0}/gw-shop/app/v1/new-template/page-config'.format(self.shopBaseUrl)
        myRequest = SendRequestForOnline(enterpriseInfo)
        res = myRequest.sendRequest(url=url, params=param, method="post", version="supermark")
        print(res.json())
        try:
            activity_rule_id = res.json()['data']['new_buy_data']['new_buy_info']['activity_rule_id']
            spu_id = res.json()['data']['new_buy_data']['list'][0]['sku_list'][0]['spu_id']
        except KeyError:
            return
        except IndexError:
            return
        param = {"spu_id":spu_id,"activity_id":activity_rule_id,"request_type":2}
        url ='{0}/gw-shop/app/v1/activity-center/new-purchase/check-cart-goods'.format(self.shopBaseUrl)
        myRequest = SendRequestForOnline(enterpriseInfo)
        res = myRequest.sendRequest(url=url, params=param, method="post", version="supermark")
        print(res.json())
        assert res.json()["code"] == 200

    @allure.story("用户详情")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_userdetail(self,enterpriseInfo, ini):
        """
        用户详情
        """
        url = '{0}/gw-shop/app/v1/user/detail'.format(self.shopBaseUrl)
        myRequest = SendRequestForOnline(enterpriseInfo)
        res = myRequest.sendRequest(url=url, params=None, method="get", version="supermark")
        print(res.json())
        assert res.json()["code"] == 200
