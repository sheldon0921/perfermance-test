from tests.common.goods.console.specTemplate import SpecTemplate
from utils.readerFile import ReaderFile
from log.log import Logger
import pytest
from utils.myTime import Mytime
import allure
'''
前置条件：
    1.新增规格模板成功
测试步骤：
    1.未关联商品的规格模板，删除成功

'''

@allure.feature('商品')
class test_goods_delSpecTemplate_001(object):


        @pytest.fixture()
        def ini(self):
            # 初始化logger/specTemplate对象
            self.logger = Logger.Logger()
            self.specTemplate = SpecTemplate()
            # 从json文件中读取添加规格模板的参数
            self.addParam = ReaderFile.readerJson("addSpecTemplate.json")
            addRes = self.specTemplate.addSpecTemplate(self.addParam)
            self.templateId = addRes["data"]["id"]
            with allure.step(f"新增ID为 {self.templateId} 的规格模板 {self.addParam['template_name']}"):
                assert self.addParam["template_name"] == addRes["data"]["template_name"] and self.templateId is not None
            self.logger.info("addRes {0}".format(addRes))
            yield self.specTemplate, self.logger, self.templateId

        @allure.story('新增未关联商品的规格模板，且可以删除成功')
        @pytest.mark.smoke
        def test_goods_del_noGoodsSpecTemplate(self,ini):
            # 删除规格模板
            delParam = {"attribute_template_id": self.templateId}
            delRes = self.specTemplate.deleteSpecTemplate(delParam)
            self.logger.info("delRes {0}".format(delRes))
            with allure.step(f"通过规格模板ID : {self.templateId} 删除规格模板 "):
                assert delRes.status_code == 200 and delRes.json()["message"] == "success"
            # 在查询一次规格模板，查询不到,说明删除成功
            listParam = {"tag_id": "", "start_time": "", "end_time": "", "page": 1, "size": 10}
            listRes = self.specTemplate.listSpecTemplate(listParam)
            self.logger.info("listRes {0}".format(listRes))
            with allure.step(f"通过规格模板ID : {self.templateId} 查询规格模板为空 "):
                assert self.templateId not in listRes
