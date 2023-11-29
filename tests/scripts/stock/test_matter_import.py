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
import pytest
import allure

@allure.feature('库存')
class Test_matter_import_001(object):
    @pytest.fixture()
    def ini(self):
        self.stock=Stock()
        self.logger = Logger.Logger()
    @allure.story('物料导入')
    @pytest.mark.smoke
    def test_matter_import(self,ini):
        id = self.stock.queryWarehouseId()
        file={
            "warehouse_id":(None,id),
            "operate_type":(None,1),
            "excel": ('物料导入模版.xlsx',open(ReaderIniFile.getConfigFilePath("data",'物料导入模版.xlsx'), 'rb'),'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
            "filename":'物料导入模版.xlsx'
        }
        print(ReaderIniFile.getConfigFilePath("data",'物料导入模版.xlsx'))
        Res=self.stock.matterInport(file)
        self.logger.info('Res:{0}'.format(Res))
        with allure.step(f"导入物料"):
            assert Res['code'] == 200 and Res['message'] == 'success'

