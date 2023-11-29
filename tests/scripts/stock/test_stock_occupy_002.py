from tests.common.goods.console.specTemplate import SpecTemplate
from tests.common.goods.console.postage import Postage
from log.log import Logger
from utils.readerFile import ReaderFile
from utils.myJson import MyJson
from tests.common.goods.console.postage import Postage
from utils.myTime import Mytime
from tests.common.goods.console.goods import Goods
from tests.common.stock.console.stock import Stock
from utils.readerIniFile import ReaderIniFile
import pytest,allure,time
import allure
@allure.feature('库存')
class Test_stock_occupy_002(object):

    @pytest.fixture()
    def ini(self):
        self.goods=Goods()
        self.logger = Logger.Logger()
        self.stock=Stock()

        yield
        #下架商品
        self.goods.afterOperation(self.Res)
        # 查询下架后可分配库存
        time.sleep(10)
        param = {"page": 1, "size": 10, "first_value": "TestSKU005", "first_type": "material_no", "second_type": "all",
                 "min_value": "", "max_value": "", "source_id": 0, "time_type": "create", "start_time": "",
                 "end_time": ""}
        res = self.stock.queryStockList(param)
        self.stockNu = res['data']['list'][0]['stock']
        with allure.step(f"下架后库存 {self.stockNu} = 上架后库存{self.stocknu} - 商品占用库存{self.online_stock}"):
            assert self.stockNu == self.stocknu + self.online_stock


    @allure.story('下架商品释放库存')
    @pytest.mark.smoke
    def test_stock_occupy_002(self,ini):
        dict = {
            "material_id": 161634822358848,
            "material_no": 'TestSKU005'
        }
        # 新增上架商品
        self.Res = self.goods.beforeOperation(dict)
        # 上架后查询可分配库存
        time.sleep(10)
        param = {"page": 1, "size": 10, "first_value": "TestSKU005", "first_type": "material_no", "second_type": "all",
                 "min_value": "", "max_value": "", "source_id": 0, "time_type": "create", "start_time": "",
                 "end_time": ""}
        res = self.stock.queryStockList(param)
        self.stocknu = res['data']['list'][0]['stock']

        # 在全部spu列表中查询商品占用库存
        listParam = {"page": 1, "size": 1000, "searchParams": {"searchChannel": 0, "searchChannelOwnership": 0,
                                                               "searchString": {"keyword": str(self.Res['spuID']),
                                                                                "type": 4},
                                                               "searchInt": {"high": 0, "low": 0, "type": 1},
                                                               "searchNeedDelete": 2,
                                                               "searchTime": {"beginTimestamp": 0, "endTimestamp": 0,
                                                                              "type": 1}, "searchGoodsStatus": -1,
                                                               "searchReleaseStatus": 1,
                                                               "searchSort": {"sortColumn": 0, "sortType": 1}}}
        listRes = self.goods.listSpu(listParam)
        self.logger.info('listRes:{0}'.format(listRes))
        self.online_stock = listRes['data']['list'][0]['stock']['online_stock']