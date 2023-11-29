from tests.common.goods.console.specTemplate import SpecTemplate
from utils.readerFile import ReaderFile
from log.log import Logger
import pytest
from utils.myTime import Mytime
import time
import allure
'''
前置条件：

测试步骤：
    1.判断列表内数据是否大于3位
    2、如果大于3位直接判断倒序
    3、如果小于3位，添加两条数据，判断倒序
预期结果：
    1.规格模板列表数据按照创建时间倒序排列
'''

@allure.feature('商品')
class Test_goods_listDetailSpecTemplate(object):
    @pytest.fixture()
    def ini(self):
        # 初始化logger/specTemplate对象
        self.logger = Logger.Logger()
        self.specTemplate = SpecTemplate()

        yield self.logger

    @allure.story('规格模板列表数据按照创建时间倒序排列')
    @pytest.mark.smoke
    def test_goods_templateList(self, ini):
        param = {"tag_id": "", "start_time": "", "end_time": "", "page": 1, "size": 100}
        res = self.specTemplate.listSpecTemplate(param)
        self.logger.info("res: {0}".format(res))
        with allure.step(f"查询规格模板列表 "):
            assert res["code"] == 200
        # 如果列表本身存在大于等于三条的数据，直接判断按照创建时间倒序
        if res["data"]["total"] >= 5:
            res = res["data"]["list"]
            with allure.step(f"规格模板列表数据倒叙排列 {res[-3]['updated_at']} >= {res[-2]['updated_at']} >= {res[-1]['updated_at']}"):
                assert res[-3]["updated_at"] >= res[-2]["updated_at"] >= res[-1]["updated_at"]
            # 修改第三条数据：


        # 如果列表本身存在数据小于3条，就自己添加几条数据进行判断
        else:
            self.templateIds = []
            for i in range(3):
                self.addParam = ReaderFile.readerJson("addSpecTemplate.json")
                self.addParam["template_name"] = "xt的规格模板" + str(i)
                addRes = self.specTemplate.addSpecTemplate(self.addParam)
                self.logger.info("addRes: {0}".format(addRes))
                self.templateIds.append(addRes["data"]["id"])
                assert self.addParam["template_name"] == addRes["data"][
                    "template_name"] and self.templateIds is not None
                time.sleep(1)
            assert len(self.templateIds) == 3
            param = {"tag_id": "", "start_time": "", "end_time": "", "page": 1, "size": 100}
            res = self.specTemplate.listSpecTemplate(param)
            self.logger.info("res: {0}".format(res))
            with allure.step(f"查询规格模板列表 "):
                assert res["code"] == 200
            res = res["data"]["list"]
            with allure.step(f"规格模板列表数据倒叙排列 {res[0]['updated_at']} >= {res[1]['updated_at']} >= {res[2]['updated_at']}"):
                assert res[0]["updated_at"] >= res[1]["updated_at"] >= res[2]["updated_at"]

            # 删除新增的几条数据
            for i in self.templateIds:
                param = {"attribute_template_id": i}
                delres = self.specTemplate.deleteSpecTemplate(param)
                self.logger.info("Res: {0}".format(delres.json()))
                assert delres.json()["code"] == 200








