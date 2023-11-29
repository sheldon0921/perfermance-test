from tests.common.sendRequest.sendRequestForOnline import SendRequestForOnline
from utils.readerIniFile import ReaderIniFile
from utils.parseJson import ParseJson
from utils.readerFile import ReaderFile
import json, pytest, allure
from log.log import Logger


@allure.feature("搜索商品列表页")
class Test_QueryGoodsList:

    @pytest.fixture()
    def ini(self):
        # 实例化对象
        self.logger = Logger.Logger()
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")
        yield self.logger, self.shopBaseUrl

    @allure.story("公共配置(common-config)")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    def test_common_config(self, enterpriseInfo, ini):
        param = {}
        url = "{0}/gw-shop/app/v1/common/config".format(self.shopBaseUrl)
        sendRequest = SendRequestForOnline(enterpriseInfo)
        spuListRes = sendRequest.sendRequest(url, param).json()
        print("spuListRes: {0}".format(spuListRes))
        spuListRes["code"] == 200 and spuListRes["message"]== "success"

    @allure.story("查询spu列表")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    def test_spu_list(self, enterpriseInfo, ini):
        param = {"category_id": "", "page": 1, "size": 10, "sort_field": "default", "sort": "DESC", "keywords": "软抽"}
        url = "{0}/gw-shop/app/v1/goods/spu-list".format(self.shopBaseUrl)
        sendRequest = SendRequestForOnline(enterpriseInfo)
        spuListRes = sendRequest.sendRequest(url, param, "GET").json()
        print("spuListRes: {0}".format(spuListRes))
        spuListRes["code"] == 200 and spuListRes["message"]== "success"