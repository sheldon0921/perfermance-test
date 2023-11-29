from log.log import Logger
from utils.readerFile import ReaderFile
from utils.myJson import MyJson
from tests.common.goods.console.postage import Postage
from utils.myTime import Mytime
from utils.myRandom import MyRandom
import time
import pytest
import allure

'''
测试步骤：
    1.增加邮费模板，增加成功
    2.查询邮费模板列表默认按照创建时间倒序排列
'''

@allure.feature('商品')
class Test_goods_addPostage(object):

    @pytest.fixture()
    def ini(self):
        self.myrandom = MyRandom()
        self.mytime = Mytime()
        self.logger = Logger.Logger()
        self.postage = Postage()
        self.addParam = ReaderFile.readerJson("addPostage.json")
        self.updateparam = ReaderFile.readerJson("updatePostage.json")

        # 增加邮费模板1
        timeNow = self.mytime.getCurrTimeStamp()
        random = self.myrandom.getRandomStr(3)
        self.addParam["name"] = "邮费"+str(timeNow)+str(random)
        self.name1 = self.addParam["name"]
        res = self.postage.addPostage(self.addParam)  # 调接口创建邮费模板
        self.logger.info("add postage template res: {0}".format(res))
        assert res.status_code == 200 and "success" in res.text

        # 增加邮费模板2
        time.sleep(1)
        timeNow = self.mytime.getCurrTimeStamp()
        random = self.myrandom.getRandomStr(3)
        self.addParam["name"] = "邮费" + str(timeNow) + str(random)
        self.name2 = self.addParam["name"]
        res = self.postage.addPostage(self.addParam)  # 调接口创建邮费模板
        self.logger.info("add postage template res: {0}".format(res))
        assert res.status_code == 200 and "success" in res.text
        self.postageNames = [self.name1,self.name2]


        yield self.postage, self.addParam, self.logger,self.updateparam,self.name2,self.name2,self.postageNames
        # print(self.addParam,self.Postage)

        # 删除邮费模板
        for i in self.postageIds:
            delParam = {"postage_id": i}
            res = self.postage.delete_postage(delParam)
            assert res.status_code == 200 and res.json()['message'] == "success"

    @pytest.mark.smoke
    @pytest.mark.skip
    def test_goods_addPostage(self, ini):
        # 查询邮费1的postageId
        params = {"page":1,"size":10,"start_time":"","end_time":"","time_type":1,"name":self.name1}
        res = self.postage.query_postage(params)
        self.logger.info("Query postage res info {0}".format(res))
        assert res["code"] == 200 and len(res["data"]["list"]) == 1
        self.postageId1 = res["data"]["list"][0]["id"]

        # 修改先创建的邮费模板信息，更新时间更新
        time.sleep(1)
        self.updateparam["name"] = self.name1
        self.updateparam["postage_id"] = self.postageId1
        updateparam = self.updateparam
        updateRes = self.postage.edit_postage(updateparam)
        self.logger.info("updateRes: {0}".format(updateRes))
        assert updateRes["code"] == 200 and updateRes["message"] == "success"

        # 查询邮费模板列表数据
        params = {"page": 1, "size": 100, "start_time": "", "end_time": "", "time_type": 1}
        res = self.postage.query_postage(params)
        self.logger.info("Query postage res info {0}".format(res))
        assert res["code"] == 200 and len(res["data"]["list"]) >= 2
        self.ids = {}
        res = res["data"]["list"]
        for index, value in enumerate(res):
            if value["name"] == self.postageNames[0] or self.postageNames[1]:
                self.ids[value["name"]] = [index, value["id"], value["created_at"], value["updated_at"]]
            else:
                continue
        self.postageIds = [self.ids[self.name1][1],self.ids[self.name2][1]]

        # 判断列表按照创建时间倒序排列
        assert self.ids[self.name1][3] > self.ids[self.name2][3]
        assert self.ids[self.name1][2] < self.ids[self.name2][2]
        assert self.ids[self.name1][0] > self.ids[self.name2][0]