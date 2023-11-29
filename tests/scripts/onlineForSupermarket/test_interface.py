from utils.readerFile import ReaderFile
from log.log import Logger
from tests.common.onLineForSupermarket.indexInfo import PageConfig
from tests.common.onLineForSupermarket.smGoodsDetail import GoodsDetail
from tests.common.onLineForSupermarket.order import Shoporder
from tests.common.onLineForSupermarket.order import Store_cart
from tests.common.onLineForSupermarket.order import Wx_list
from tests.common.onLineForSupermarket.order import Get_order_setting
from tests.common.onLineForSupermarket.order import Common_config
from tests.common.onLineForSupermarket.order import User_center_mobile
from tests.common.onLineForSupermarket.order import Activity_goods_list
from tests.common.onLineForSupermarket.extractList import ExtractList
from tests.common.onLineForSupermarket.indexInfo import VisitExtract
from tests.common.onLineForSupermarket.indexInfo import Hotgoods
from tests.common.onLineForSupermarket.orderForSm import OrderForSm
from tests.common.onLine.shopOrder import ShopOrder
from utils.parseJson import ParseJson
from tests.login.login import Login
from utils.myTime import Mytime
from utils.myRandom import MyRandom
import json
import pytest
import allure

@allure.feature("(商超)订单")
class Test_interface:

    @pytest.fixture()
    def ini(self):
        # 实例化对象
        self.logger = Logger.Logger()
        self.goods = GoodsDetail()
        self.list=ExtractList()
        self.visit = VisitExtract()
        self.getspu = PageConfig()
        self.shop=Shoporder()
        self.store=Store_cart()
        self.wxlist=Wx_list()
        self.common=Common_config()
        self.center=User_center_mobile()
        self.get=Get_order_setting()
        self.activity=Activity_goods_list()
        self.order = ShopOrder()
        self.hotgoods = Hotgoods()
        self.orderForSm = OrderForSm()
        self.data = {"user_latitude": "34.222590", "user_longitude": "108.948780"}
        yield self.logger


    @allure.story("获取购物车模板")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_get_cart_model(self,enterpriseInfo,ini):
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]
        if enterpriName == "好宜多优选" or \
                enterpriName == "壹号土猪优选" or \
                enterpriName == "你我他优鲜":
            return
        header = self.list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        param = {}
        res = self.shop.getCartModel(header,param)
        self.logger.info("getCartModel :{0}".format(res))
        assert res['code'] == 200 and \
               res['message'] == 'success'

