from tests.common.goods.console.specTemplate import SpecTemplate
from utils.readerFile import ReaderFile
from log.log import Logger
import pytest
from utils.myTime import Mytime
import time
import allure
'''
前置条件：
    1.新增规格模板成功
测试步骤：
    1.移动规格模板，有如下预期结果
预期结果：
    1.移动成功
    2.修改后时间为当前时间
    3.移动后置顶

'''

@allure.feature('商品')
class Test_goods_copySpecTemplate(object):
    @pytest.fixture()
    def ini(self):
        # 初始化logger/specTemplate对象
        self.logger = Logger.Logger()
        self.specTemplate = SpecTemplate()
        # 从json文件中读取添加规格模板的参数
        self.addParam = ReaderFile.readerJson("addSpecTemplate.json")
        self.updateParam = ReaderFile.readerJson("updateSpecTemplate.json")
        # self.addParam["template_name"] = "修改颜色大小模板"
        addRes = self.specTemplate.addSpecTemplate(self.addParam)
        self.templateId = addRes["data"]["id"]
        with allure.step(f"新增规格模板： {self.addParam['template_name']}"):
            assert self.addParam["template_name"] == addRes["data"]["template_name"] and self.templateId is not None
        self.logger.info("addRes {0}".format(addRes))
        yield self.specTemplate, self.addParam, self.logger, self.updateParam, self.templateId
        # 删除规格模板
        delParam = {"attribute_template_id": self.templateId}
        with allure.step(f"通过规格模板ID : {self.templateId} 删除规格模板 "):
            delRes = self.specTemplate.deleteSpecTemplate(delParam)
            assert delRes.status_code == 200 and delRes.json()["message"] == "success"
        self.logger.info("delRes {0}".format(delRes))

        # 在查询一次规格模板，查询不到,说明删除成功
        listParam = {"tag_id":"","start_time":"","end_time":"","page":1,"size":10,"attribute_template_id":self.templateId}
        with allure.step(f"通过规格模板ID : {self.templateId} 查询规格模板 "):
            listRes = self.specTemplate.listSpecTemplate(listParam)
            assert self.templateId not in listRes
        self.logger.info("listRes {0}".format(listRes))

    @allure.story('新增后移动规格模板，移动成功且置顶')
    @pytest.mark.smoke
    def test_goods_updateSpecTemplate(self, ini):
        # time.sleep(2)
        specTemplateLable = "规格模板"+Mytime.getCurrTime()
        param = {"attribute_template_id":self.templateId,"tag_name":specTemplateLable}
        copyBrforeTime = Mytime.getCurrTimeStamp()
        time.sleep(2)
        copyRes = self.specTemplate.copySpecTemplate(param)
        time.sleep(2)
        copyAfterTime = Mytime.getCurrTimeStamp()
        with allure.step(f"通过规格模板ID : {self.templateId} 移动规格模板 "):
            assert copyRes["code"] == 200 and copyRes["message"]
        # 移动完成功后，再次查询，判断是否置顶，判断时间是否是最新时间
        listParam = {"tag_id":"","start_time":"","end_time":"","page":1,"size":10,"attribute_template_id":self.templateId}
        listRes = self.specTemplate.listSpecTemplate(listParam)
        # self.logger.info("listRes {0}".format(listRes))
        self.logger.info("listRes {0}".format(listRes))
        print("listRes {0}".format(listRes))
        listData = listRes["data"]["list"][0]
        assert listData["id"] == self.templateId
        updateTime = listData["updated_at"]
        self.logger.info("copyBrforeTime: {0},copyAfterTime: {1},updateTime: {2}".format(copyBrforeTime,copyAfterTime,updateTime))
        with allure.step(f"判断移动前时间 {copyBrforeTime} <= 更新时间 {updateTime} <= 移动后时间 {copyAfterTime} "):
            assert copyBrforeTime <= updateTime <= copyAfterTime






