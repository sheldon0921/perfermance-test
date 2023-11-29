from tests.common.onLineForSupermarket.hotSellRecommand import HotSellRecommand
from tests.common.onLineForSupermarket.extractList import ExtractList
from utils.readerFile import ReaderFile
import json, pytest, allure, time
from log.log import Logger
from pytest import assume


class Test_hotSellRecommand():

    hotSellRecommand = HotSellRecommand()
    extractList = ExtractList()
    logger = Logger.Logger()

    @pytest.fixture(scope="class", autouse=True)
    def ini(self):
        pass

    @allure.story("查询用户详情")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_activity_robot_user(self,enterpriseInfo):
        '''(首页接口)获取用户详细接口'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        header = self.extractList.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        res = self.hotSellRecommand.activityRobotUser(header,{})
        with assume: assert res["code"] == 200
        with assume: assert res["message"] == "success"
        with assume: assert len(res["data"]["data"]) is not 0
