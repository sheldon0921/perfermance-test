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
    2.查询1增加的结果，查询成功
'''

@allure.feature('商品')
class Test_goods_addPostage(object):

    @pytest.fixture()
    def ini(self):
        self.mytime = Mytime()
        self.myrandom = MyRandom()
        self.logger = Logger.Logger()
        self.postage = Postage()
        self.addParam = ReaderFile.readerJson("addPostage.json")
        yield self.postage, self.addParam, self.logger
        # print(self.addParam,self.Postage)
        # 删除邮费模板
        delParam = {"postage_id": self.postageID}
        res = self.postage.delete_postage(delParam)
        # assert res.status_code == 200 and res.json()['message'] == "success"

    @allure.story('新增邮费模板，且可以查询成功')
    @pytest.mark.smoke
    def test_goods_addPostage(self, ini):
        #增加邮费模板
        # startTime = Mytime.getCurrTimeStamp()
        time.sleep(1)
        name = str(Mytime.getCurrTimeStamp) + MyRandom.getRandomStr(3)
        self.addParam['name']='邮费'+ name
        res = self.postage.addPostage(self.addParam)  # 调接口创建邮费模板
        # endTime = Mytime.getCurrTimeStamp()
        self.logger.info("add postage template res: {0}".format(res))
        with allure.step(f"新增邮费模板 {self.addParam['name']} "):
            assert res.status_code == 200 and "success" in res.text
        # 查询邮费模板
        params = {"page":1,"size":10,"start_time":"","end_time":"","time_type":1,"name":self.addParam['name']}
        res = self.postage.query_postage(params)  # 查询时间区间内邮费模板数据
        self.logger.info("Query postage res info {0}".format(res))
        print("Query postage res info {0}".format(res))
        self.postageID = res["data"]["list"][0]["id"]
        with allure.step(f"查询邮费模板 {self.addParam['name']} "):
            assert len(res["data"]["list"]) == 1 and res["data"]["list"][0]["name"] == self.addParam['name']

