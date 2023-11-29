from tests.common.goods.console.specTemplate import SpecTemplate
from utils.readerFile import ReaderFile
from log.log import Logger
import pytest
from utils.myTime import Mytime
import time
import allure


'''
测试步骤：
    1.增加规格模板，增加成功
    2.查询1增加的结果，查询成功
'''

@allure.feature('商品')
class Test_goods_addSpecTemplate_001(object):

    @pytest.fixture()
    def ini(self):
        self.logger = Logger.Logger()
        self.specTemplate = SpecTemplate()
        self.addParam = ReaderFile.readerJson("addSpecTemplate.json")

        yield self.specTemplate, self.addParam, self.logger

        # 删除规格模板
        delParam = {"attribute_template_id": self.templateId}
        with allure.step(f"通过规格模板ID : {self.templateId} 删除规格模板 "):
            delRes = self.specTemplate.deleteSpecTemplate(delParam)
            assert delRes.status_code == 200 and delRes.json()["message"] == "success"

    @allure.story('新增规格模板，并通过ID查询成功')
    @pytest.mark.smoke
    def test_addSpecTemplate_001(self, ini):
        # 增加规格模板
        # startTime = Mytime.getCurrTimeStamp()
        # time.sleep(3)
        res = self.specTemplate.addSpecTemplate(self.addParam)
        # endTime = Mytime.getCurrTimeStamp()
        self.logger.info("add specification template res: {0}".format(res))
        addRes = res["data"]
        assert self.addParam["template_name"] == addRes["template_name"] and addRes["id"] is not None
        self.templateId = addRes["id"]
        with allure.step(f"新增 id: {self.templateId} 名称: {self.addParam['template_name']} 的规格模板"):
            pass
        # 查询规格模板
        listParam = {"tag_id":"","start_time":"","end_time":"","page":1,"size":10,"attribute_template_id":str(self.templateId)}
        with allure.step(f"查询ID为 {self.templateId} 的规格模板"):
            listRes = self.specTemplate.listSpecTemplate(listParam)
            assert len(listRes["data"]["list"]) == 1 and listRes["data"]["list"][0]["id"] == addRes["id"]
        self.logger.info("list data length: {0}, data contents {1}".format(len(listRes["data"]["list"]), listRes))
        # count = 0
        # while len(listRes["data"]["list"]) == 0:
        #     time.sleep(1)
        #     listRes = self.specTemplate.listSpecTemplate(listParam)
        #     self.logger.info("times {0}list data length: {1}, data contents {2}".format(count,len(listRes["data"]["list"]), listRes))
        #     count = count+1
        #     if count == 80:
        #         break




