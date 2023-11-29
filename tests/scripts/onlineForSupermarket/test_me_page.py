from tests.common.onLineForSupermarket.mePage import MePage
from utils.readerFile import ReaderFile
from log.log import Logger
import allure,pytest


@allure.feature("(商超)我的页面")
class TestMePage(object):

    @pytest.fixture()
    def ini(self):
        self.logger = Logger.Logger()
        self.mePage = MePage()

    @allure.story("我的页面pageConfig")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_me_pageConfig(self,enterpriseInfo, ini):
        '''(首页接口)获取用户详细接口'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        params = {"template_type":"my"}
        url = "gw-shop/app/v1/new-template/page-config"
        with allure.step(f"{enterpriName}小程序首页获取用户信息"):
            res = self.mePage.commonPostFunc(params,enterpriseHash,enterpriseID,url)
        assert res.status_code == 200 and res.json()["code"]
        assert res.json()["message"] == "success"


    @allure.story("我的页面tabRedHot")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_me_pageConfig_001(self,enterpriseInfo, ini):
        '''(首页接口)获取用户详细接口'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        params = {"template_type":"my"}
        url = "gw-shop/app/v1/content-manage/tab-red-dot"
        with allure.step(f"{enterpriName}小程序首页获取用户信息"):
            res = self.mePage.commonGetFunc(params,enterpriseHash,enterpriseID,url)
        assert res.status_code == 200 and res.json()["code"]
        assert res.json()["message"] == "success"