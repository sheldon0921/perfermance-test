from tests.common.goods.console.specTemplate import SpecTemplate
from utils.readerFile import ReaderFile
from log.log import Logger
import pytest
from utils.myTime import Mytime
import allure
from utils.myRandom import MyRandom
'''
前置条件：
    1.新增规格模板成功
测试步骤：
    1.修改模板标签和模板名称，修改成功

'''

@allure.feature('商品')
class Test_goods_updateSpecTemplate_002(object):
    @pytest.fixture()
    def ini(self):
        # 初始化logger/specTemplate对象
        self.logger = Logger.Logger()
        self.specTemplate = SpecTemplate()
        # 从json文件中读取添加规格模板的参数
        self.addParam = ReaderFile.readerJson("addSpecTemplate.json")
        self.updateParam = ReaderFile.readerJson("updateSpecTemplate.json")
        # self.addParam["template_name"] = "修改颜色大小模板"
        self.addParam['template_name']='颜色大小模板{0}'.format(MyRandom.getRandomStr(5))
        addRes = self.specTemplate.addSpecTemplate(self.addParam)
        print('###########{0}'.format(addRes))
        self.templateId = addRes["data"]["id"]
        with allure.step(f"新增规格模板 :{self.addParam['template_name']}"):
            assert self.addParam["template_name"] == addRes["data"]["template_name"] and self.templateId is not None
        self.logger.info("addRes {0}".format(addRes))
        yield self.specTemplate, self.addParam, self.logger, self.updateParam
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
        with allure.step(f"通过规格模板ID : {self.templateId} 查询规格模板 "):
            assert self.templateId not in listRes

    @allure.story('修改规格模板的标签和模板名称')
    @pytest.mark.smoke
    def test_goods_updateNameAndTagName(self, ini):
        pass
        # 修改规格模板
        updateparam = {"template_name":self.addParam['template_name'],"attribute_template_id":self.templateId,"attributes":[{"attribute_item":[],"goods_attribute_id":139335615691008},{"attribute_item":[],"goods_attribute_id":139329942582720},{"attribute_item":[],"goods_attribute_id":139329942597376}],"del_attribute_ids":[],"del_attribute_item_ids":[],"tag_name":"规格模板"}
        listRes = self.specTemplate.updateSpecTemplate(updateparam)
        self.logger.info("listRes: {0}".format(listRes))
        with allure.step(f"修改规格模板 :{self.addParam['template_name']}"):
            assert listRes["code"] == 200 and listRes["message"] == "success"







