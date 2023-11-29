from tests.common.sendRequest.sendRequestForOnline import SendRequestForOnline
from tests.common.onLine.category import Category
from utils.readerIniFile import ReaderIniFile
from utils.parseJson import ParseJson
from utils.readerFile import ReaderFile
import json, pytest, allure
from log.log import Logger


@allure.feature("小程序分类页")
class Test_Category:

    @pytest.fixture()
    def ini(self):
        # 实例化对象
        self.logger = Logger.Logger()
        self.category = Category()
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")
        yield self.logger, self.shopBaseUrl

    @allure.story("查询分类列表")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    def test_category_list(self, enterpriseInfo, ini):
        print("response message: {0}".format(self.category.categoryList(enterpriseInfo).json()))
        assert self.category.categoryList(enterpriseInfo).json()["code"] == 200
        assert self.category.categoryList(enterpriseInfo).json()["message"] == "success"

    @allure.story("查询spu列表")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    def test_spu_list(self, enterpriseInfo, ini):
        param = {"page": 1, "size": 10}
        url = "{0}/gw-shop/app/v1/goods/spu-list".format(self.shopBaseUrl)
        sendRequest = SendRequestForOnline(enterpriseInfo)
        spuListRes = sendRequest.sendRequest(url, param, "GET").json()
        print("spuListRes: {0}".format(spuListRes))
        spuListRes["code"] == 200 and spuListRes["message"] == "success"

    @allure.story("热词列表(hot-world-list)")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    def test_hot_world_list(self, enterpriseInfo, ini):
        param = {"size":50,"is_enable":1}
        url = "{0}/gw-shop/app/v1/goods/hot-words-list".format(self.shopBaseUrl)
        sendRequest = SendRequestForOnline(enterpriseInfo)
        spuListRes = sendRequest.sendRequest(url, param).json()
        print("spuListRes: {0}".format(spuListRes))
        spuListRes["code"] == 200 and spuListRes["message"]== "success"

    @allure.story("页面配置(page-config)")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    def test_page_config(self, enterpriseInfo, ini):
        param = {"template_type":"categories"}
        url = "{0}/gw-shop/app/v1/new-template/page-config".format(self.shopBaseUrl)
        sendRequest = SendRequestForOnline(enterpriseInfo)
        spuListRes = sendRequest.sendRequest(url, param).json()
        print("spuListRes: {0}".format(spuListRes))
        spuListRes["code"] == 200 and spuListRes["message"]== "success"