from tests.common.goods.console.specTemplate import SpecTemplate
from tests.common.goods.console.postage import Postage
from utils.readerFile import ReaderFile
from log.log import Logger
import pytest
from utils.myTime import Mytime
from utils.myRandom import MyRandom
import time
import allure
'''
前置条件：

测试步骤：
    1.判断列表内数据是否大于3位
    2、如果大于3位直接判断倒序
    3、如果小于3位，添加两条数据，判断倒序
预期结果：
    1.邮费模板列表数据按照创建时间倒序排列
'''

@allure.feature('商品')
class Test_goods_listPostage(object):
    @pytest.fixture()
    def ini(self):
        # 初始化logger/specTemplate对象
        self.logger = Logger.Logger()
        self.specTemplate = SpecTemplate()
        self.postage = Postage()
        self.myrandom =MyRandom()
        self.mytime = Mytime()

        yield self.logger

    @allure.story('邮费模板列表数据按照创建时间倒序排列')
    @pytest.mark.smoke
    def test_goods_postageList(self, ini):
        param = {"page":1,"size":100,"start_time":"","end_time":"","time_type":1}
        res = self.postage.query_postage(param)
        self.logger.info("res: {0}".format(res))
        with allure.step(f"查询邮费模板列表"):
            assert res["code"] == 200
        # 如果列表本身存在大于等于5条的数据，直接判断按照创建时间倒序
        if res["data"]["total"] >= 5:
            res = res["data"]["list"]
            with allure.step(f"邮费模板创建时间倒序排列 {res[-3]['created_at']} >= {res[-2]['created_at']} >= {res[-1]['created_at']} "):
                assert res[-3]["created_at"] >= res[-2]["created_at"] >= res[-1]["created_at"]


        # 如果列表本身存在数据小于5条，就自己添加几条数据进行判断
        else:
            self.postageNames = []
            for i in range(3):
                self.addParam = ReaderFile.readerJson("addPostage.json")
                timeNow = self.mytime.getCurrTimeStamp()
                random = self.myrandom.getRandomStr(3)
                self.addParam["name"] = "邮费" + str(i) + str(timeNow) + str(random)
                self.postageNames.append(self.addParam["name"])
                addRes = self.postage.addPostage(self.addParam)
                self.logger.info("addRes: {0}".format(addRes))
                assert addRes.status_code == 200
                time.sleep(1)

            param = {"page": 1, "size": 100, "start_time": "", "end_time": "", "time_type": 1}
            res = self.postage.query_postage(param)
            self.logger.info("res: {0}".format(res))
            assert res["code"] == 200 and len(res["data"]["list"]) >= 3
            res = res["data"]["list"]
            assert res[-3]["created_at"] >= res[-2]["created_at"] >= res[-1]["created_at"]

            self.postageIds = []
            for i in res:
                for j in self.postageNames:
                    if i["name"] == j:
                        self.postageIds.append(i["id"])


            # 删除新增的几条数据
            for i in self.postageIds:
                param = {"postage_id":i}
                delres = self.postage.delete_postage(param)
                self.logger.info("Res: {0}".format(delres.json()))
                assert delres.json()["code"] == 200








