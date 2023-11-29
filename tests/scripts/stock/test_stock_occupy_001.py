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
class Test_stock_occupy_001(object):

    @pytest.fixture()
    def ini(self):
        self.goods=Goods()
        self.logger = Logger.Logger()
        self.stock=Stock()
        #查询上架前可分配库存
        param={"page":1,"size":10,"first_value":"TestSKU005","first_type":"material_no","second_type":"all","min_value":"","max_value":"","source_id":0,"time_type":"create","start_time":"","end_time":""}
        res=self.stock.queryStockList(param)
        self.logger.info("queryStockList:{0}".format(res))
        self.stockNu=res['data']['list'][0]['stock']
        # 新增上架商品
        dict={
            "material_id":161634822358848,
            "material_no":'TestSKU005'
        }
        self.Res = self.goods.beforeOperation(dict)
        yield self.Res,self.stockNu
        self.goods.afterOperation(self.Res)

    @allure.story('上架商品占用库存')
    @pytest.mark.smoke
    def test_stock_occupy_001(self,ini):

        # 在全部spu列表中查询商品占用库存
        listParam = {"page": 1, "size": 1000, "searchParams": {"searchChannel": 0, "searchChannelOwnership": 0,
                                                               "searchString": {"keyword": str(self.Res['spuID']), "type": 4},
                                                               "searchInt": {"high": 0, "low": 0, "type": 1},
                                                               "searchNeedDelete": 2,
                                                               "searchTime": {"beginTimestamp": 0, "endTimestamp": 0,
                                                                              "type": 1}, "searchGoodsStatus": -1,
                                                               "searchReleaseStatus": 1,
                                                               "searchSort": {"sortColumn": 0, "sortType": 1}}}
        listRes = self.goods.listSpu(listParam)
        self.logger.info('listRes:{0}'.format(listRes))
        online_stock=listRes['data']['list'][0]['stock']['online_stock']
        #上架后查询可分配库存
        time.sleep(15)
        param = {"page": 1, "size": 10, "first_value": "TestSKU005", "first_type": "material_no", "second_type": "all",
                 "min_value": "", "max_value": "", "source_id": 0, "time_type": "create", "start_time": "",
                 "end_time": ""}
        res = self.stock.queryStockList(param)
        stocknu=res['data']['list'][0]['stock']
        with allure.step(f"占用后库存 {stocknu} = 占用前库存{self.stockNu} - 商品占用库存{online_stock}"):
            assert stocknu==self.stockNu - online_stock