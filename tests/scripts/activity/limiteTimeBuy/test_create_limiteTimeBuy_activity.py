from log.log import Logger
from tests.common.activity.console.activity import Activity
from tests.common.goods.console.goods import Goods
from utils.readerFile import ReaderFile
import pytest
import allure


@allure.feature("限时购活动")
class Test_create_limiteTimeBuy_activity(object):

    @pytest.fixture()
    def ini(self):
        self.activity = Activity()
        self.logger = Logger.Logger()
        self.createParam = ReaderFile.readerJson("limiteTimeBuy.json")
        self.goodsInfo = Goods.beforeOperation()
        yield

    @allure.story("创建限时购活动")
    @pytest.mark.smoke
    @pytest.mark.skip(reason="未完成的脚本")
    def test_create_limiteTime_activity(self):
        self.createParam["activity_sku"][0]["sku_id"] = self.goodsInfo["skuID"]
        self.createParam["activity_sku"][0]["spu_id"] = self.goodsInfo["spuID"]
        self.createParam["activity_sku"][0]["name"] = self.goodsInfo["goodsName"]
        self.createParam[""] = self.goodsInfo[""]
