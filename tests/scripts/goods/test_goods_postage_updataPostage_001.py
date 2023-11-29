from log.log import Logger
from utils.readerFile import ReaderFile
from tests.common.goods.console.postage import Postage
from utils.myRandom import MyRandom
from utils.myTime import Mytime
import pytest
import allure

'''
前置条件：
    1.增加邮费模板，增加成功
测试步骤：
    1、未关联商品的邮费模板，修改成功
'''

@allure.feature('商品')
class Test_goods_updatePostage(object):

    @pytest.fixture()
    def ini(self):
        self.mytime = Mytime()
        self.myrandom = MyRandom()
        self.logger = Logger.Logger()
        self.postage = Postage()
        self.addParam = ReaderFile.readerJson("addPostage.json") #从json文件中读取添加邮费模板的参数
        self.updateparam = ReaderFile.readerJson("updatePostage.json")
        name = str(Mytime.getCurrTimeStamp) + MyRandom.getRandomStr(3)
        self.addParam['name'] = "邮费"+ name
        # print("88888:     ",self.addParam["name"])
        addRes = self.postage.addPostage(self.addParam) #添加邮费模板
        with allure.step(f"新增邮费模板 {self.addParam['name']} "):
            assert  addRes.status_code == 200
        self.logger.info("addRes {0}".format(addRes.json()))
        # 按名称查询邮费模板
        params = {"page": 1, "size": 10, "start_time": "", "end_time": "", "time_type": 1,"name": self.addParam['name']}
        listRes = self.postage.query_postage(params)
        self.logger.info("listRes {0}".format(listRes))
        self.postageID = listRes["data"]["list"][0]["id"] # 获取新建成功的邮费模板id
        self.updateparam["postage_id"] = self.postageID
        with allure.step(f"查询邮费模板 {self.addParam['name']} "):
            assert listRes["data"]["list"][0]["name"] == self.addParam["name"] and self.postageID is not None
        self.logger.info("addRes {0}".format(addRes))

        yield self.postageID,self.updateparam

        # 删除邮费模板，恢复环境
        delParam = {"postage_id": self.postageID}
        res = self.postage.delete_postage(delParam)
        # assert res.status_code == 200 and res.json()['message'] == "success"

    @allure.story('新增未关联商品的邮费模板，且可以修改成功')
    @pytest.mark.smoke
    def test_goods_updatePostage(self, ini):
        # 修改邮费规格
        updateparam = self.updateparam
        updateRes = self.postage.edit_postage(updateparam)
        self.logger.info("updateRes: {0}".format(updateRes))
        with allure.step(f"修改邮费模板 {self.addParam['name']} "):
            assert updateRes["code"] == 200 and updateRes["message"] == "success"

