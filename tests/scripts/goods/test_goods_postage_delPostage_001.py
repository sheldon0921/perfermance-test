from log.log import Logger
from utils.readerFile import ReaderFile
from tests.common.goods.console.postage import Postage
from utils.myRandom import MyRandom
import pytest
import allure

'''
前置条件：
    1.增加邮费模板，增加成功
测试步骤：
    1、未关联商品的邮费模板，删除成功
'''

@allure.feature('商品')
class Test_goods_delPostage(object):

    @pytest.fixture()
    def ini(self):
        self.myrandom = MyRandom()
        self.logger = Logger.Logger()
        self.postage = Postage()
        self.addParam = ReaderFile.readerJson("addPostage.json") #从json文件中读取添加邮费模板的参数
        name = MyRandom.getRandomStr(3)
        self.addParam['name'] = '阿树新增邮费模板{0}'.format(name)
        addRes = self.postage.addPostage(self.addParam) #添加邮费模板
        self.logger.info("addRes {0}".format(addRes))
        params={"page":1,"size":10,"start_time":"","end_time":"","time_type":1,"name":self.addParam['name']}
        listRes = self.postage.query_postage(params) #查询邮费模板列表的第一条数据
        self.postageID = listRes["data"]["list"][0]["id"] # 获取新建成功的邮费模板id
        with allure.step(f"新增邮费模板 {self.addParam['name']} "):
            assert len(listRes["data"]["list"]) > 0
            assert listRes["data"]["list"][0]["name"] == self.addParam["name"] and self.postageID is not None
        self.logger.info("addRes {0}".format(addRes))
        yield self.postageID
        # yield
        # print("postageID: {0}".format(self.postageID))

    @allure.story('新增未关联商品的邮费模板，且可以删除成功')
    @pytest.mark.smoke
    def test_goods_delPostage(self, ini):
        #删除邮费模板
        delParam = {"postage_id":self.postageID}
        delRes = self.postage.delete_postage(delParam)
        self.logger.info("delRes {0}".format(delRes))
        # assert delRes.status_code == 200 and delRes.json()["message"] == "success"
        #查找上面删除的邮费模板id,查询不到，说明删除成功
        listParam = {"postage_id":self.postageID}
        listRes = self.postage.query_postage(listParam)
        # self.logger.info("listRes {0}".format(listRes))
        print("listRes {0}".format(self.postageID))
        with allure.step(f"通过邮费模板ID {self.postageID} 删除 {self.addParam['name']} "):
            assert self.postageID not in listRes









