from tests.common.sendRequest.sendRequestForOnline import SendRequestForOnline
from tests.common.onLine.category import Category
from utils.readerIniFile import ReaderIniFile
from utils.parseJson import ParseJson
from utils.readerFile import ReaderFile
import json, pytest, allure
from log.log import Logger


@allure.feature("小程序我的页面")
class Test_Me_Page:

    @pytest.fixture()
    def ini(self):
        # 实例化对象
        self.logger = Logger.Logger()
        self.category = Category()
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")
        yield self.logger, self.shopBaseUrl

    @allure.story("查询score列表(score/list)")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    def test_score_list(self, enterpriseInfo, ini):
        param = {}
        url = "{0}/gw-shop/app/v1/score/list".format(self.shopBaseUrl)
        sendRequest = SendRequestForOnline(enterpriseInfo)
        spuListRes = sendRequest.sendRequest(url, param, "GET").json()
        print("spuListRes: {0}".format(spuListRes))
        spuListRes["code"] == 200 and spuListRes["message"] == "success"

    @allure.story("热区(tab-red-dot)")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    def test_tab_red_dot(self, enterpriseInfo, ini):
        param = {}
        url = "{0}/gw-shop/app/v1/content-manage/tab-red-dot".format(self.shopBaseUrl)
        sendRequest = SendRequestForOnline(enterpriseInfo)
        spuListRes = sendRequest.sendRequest(url, param, "GET").json()
        print("spuListRes: {0}".format(spuListRes))
        spuListRes["code"] == 200 and spuListRes["message"] == "success"

    @allure.story("用户中心/用户详情(user-center/detail)")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    def test_user_center_detail(self, enterpriseInfo, ini):
        param = {"type": 1}
        url = "{0}/gw-shop/app/v1/user-center/detail".format(self.shopBaseUrl)
        sendRequest = SendRequestForOnline(enterpriseInfo)
        spuListRes = sendRequest.sendRequest(url, param, "GET").json()
        print("spuListRes: {0}".format(spuListRes))
        spuListRes["code"] == 200 and spuListRes["message"] == "success"

    @allure.story("足迹")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    def test_goods_footprint_list(self, enterpriseInfo, ini):
        param = {"page":1,"size":15}
        url = "{0}/gw-shop/app/v1/goods-footprint/list".format(self.shopBaseUrl)
        sendRequest = SendRequestForOnline(enterpriseInfo)
        spuListRes = sendRequest.sendRequest(url, param).json()
        print("spuListRes: {0}".format(spuListRes))
        spuListRes["code"] == 200 and spuListRes["message"] == "success"

    @allure.story("优惠卷列表")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    def test_coupon_user_list(self, enterpriseInfo, ini):
        with allure.step(f"{enterpriseInfo['enterpriName']}我的页面/coupon_user/list"):
            param = {"page": 1, "size": 10000, "type": 1, "coupon_type": 3}
            url = "{0}/gw-shop/app/v1/coupon_user/list".format(self.shopBaseUrl)
            sendRequest = SendRequestForOnline(enterpriseInfo)
            spuListRes = sendRequest.sendRequest(url, param, "Get").json()
            print("spuListRes: {0}".format(spuListRes))
            spuListRes["code"] == 200 and spuListRes["message"] == "success"
        with allure.step(f"{enterpriseInfo['enterpriName']}我的页面/password-coupon/del-red-hot"):
            param = {}
            url = "{0}/gw-shop/app/v1/activity-center/password-coupon/del-red-hot".format(self.shopBaseUrl)
            spuListRes = sendRequest.sendRequest(url, param).json()
            spuListRes["code"] == 200 and spuListRes["message"] == "success"

    @allure.story("页面配置接口")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    def test_page_config(self, enterpriseInfo, ini):
        param = {"template_type":"my"}
        url = "{0}/gw-shop/app/v1/new-template/page-config".format(self.shopBaseUrl)
        sendRequest = SendRequestForOnline(enterpriseInfo)
        spuListRes = sendRequest.sendRequest(url, param,).json()
        print("spuListRes: {0}".format(spuListRes))
        spuListRes["code"] == 200 and spuListRes["message"] == "success"


    @allure.story("我的活动页面")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    def test_my_activity_list(self, enterpriseInfo, ini):
        param = {}
        url = "{0}/gw-shop/app/v1/user-center/my-activity-list".format(self.shopBaseUrl)
        sendRequest = SendRequestForOnline(enterpriseInfo)
        spuListRes = sendRequest.sendRequest(url, param,).json()
        print("spuListRes: {0}".format(spuListRes))
        spuListRes["code"] == 200 and spuListRes["message"] == "success"