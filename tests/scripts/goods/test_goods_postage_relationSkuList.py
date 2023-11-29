from log.log import Logger
from utils.readerFile import ReaderFile
from utils.myJson import MyJson
from tests.common.goods.console.postage import Postage
from tests.common.goods.console.specTemplate import SpecTemplate
from utils.myTime import Mytime
from tests.common.goods.console.goods import Goods
import time
import pytest
import allure
'''
前置条件：
    1.增加邮费模板，增加成功
    2、邮费模板已经关联商品
测试步骤：
    1、查看已关联列表的商品列表
预期结果：
    1、关联列表的商品与设置一致，校验不为空
'''

@allure.feature('商品')
class Test_goods_relationListPostage(object):

    @pytest.fixture()
    def ini(self):
        self.goods = Goods()
        self.logger = Logger.Logger()
        self.postage = Postage()
        self.specTemplate = SpecTemplate()
        self.addPostageParam = ReaderFile.readerJson("addPostage.json")
        self.addSpecTemplateParam = ReaderFile.readerJson("addSpecTemplate.json")
        self.addGoodsParam = ReaderFile.readerJson("addGoods.json")
        self.delSpecParam = {"attribute_template_id": 123456789}
        # 新增商品并保存
        name = int(time.time())
        self.addPostageParam['name'] = '阿树新增邮费模板{0}'.format(name)
        addGoodsRes = self.goods.addGoods(self.addPostageParam, self.addSpecTemplateParam, self.addGoodsParam)
        self.logger.info("addGoodRes: {0}".format(addGoodsRes.json()))
        self.spuId = addGoodsRes.json()["data"]["spu_id"]
        with allure.step(f"新增 spu: {self.spuId} 名称: {self.addGoodsParam['spu_name']} 的商品"):
            assert addGoodsRes.json()["data"]["spu_id"] is not None

        # 查询时间区间内邮费模板数据
        params = {"page":1,"size":10,"start_time":"","end_time":"","time_type":1,"name":self.addPostageParam['name']}
        with allure.step(f"查询邮费模板 {self.addPostageParam['name']} "):
            res = self.postage.query_postage(params)
        self.logger.info("Query postage res ]info {0}".format(res))
        self.postageID = res["data"]["list"][0]["id"]
        self.delParam = {"postage_id": self.postageID}
        self.relationListParam = {"postage_id": self.postageID,"search_type": 0,"source_id": 0,"page": 1,"size": 10}
        yield self.delParam,addGoodsRes.json()["data"]["spu_id"],self.relationListParam

        # 删除添加的商品
        delGoods = {"channel_type": 1, "spu_id": self.spuId}
        # print("&&&&&&&", delGoods)
        delRes = self.goods.delSpu(delGoods).json()
        with allure.step(f"通过 spu: {self.spuId} 删除商品 {self.addGoodsParam['spu_name']} "):
            assert delRes["code"] == 200
        # print("delGoods: {0}".format(delRes))

        # 删除规格模板
        self.delSpecParam["attribute_template_id"] = self.specTemplateId
        param = self.delSpecParam
        delRes = self.specTemplate.deleteSpecTemplate(param)
        with allure.step(f"通过规格模板ID : {self.specTemplateId} 删除规格模板 "):
            assert delRes.status_code == 200

        # 删除邮费模板
        delRes = self.postage.delete_postage(self.delParam)
        self.logger.info("delRes {0}".format(delRes.json()))
        # print("delRes {0}".format(delRes.json()))
        # assert delRes.status_code == 200 and delRes.json()["message"] == "success"

    @allure.story('新增邮费模板并关联商品，关联列表商品与设置一致')
    @pytest.mark.smoke
    def test_goods_Postage_relationList(self, ini):
        # 查看关联列表
        listRes = self.postage.relationSkuList(self.relationListParam)
        self.logger.info("listRes {0}".format(listRes.json()))
        with allure.step(f"通过邮费模板ID {self.postageID} 查看关联列表 "):
            assert listRes.status_code == 200 and listRes.json()["message"] == "success"
            assert listRes.json()["data"]["list"] != None
        # # 删除邮费模板
        # delRes = self.postage.delete_postage(self.delParam)
        # self.logger.info("delRes {0}".format(delRes.json()))
        # print("delRes {0}".format(delRes.json()))
        # assert delRes.status_code == 500 and delRes.json()["message"] == "该邮费模板已被关联，不能删除"

        # 查询商品关联的规格模板
        goodsDetailParam = {"spu_id": self.spuId}
        self.resDetail = self.goods.queryGoodsDetail(goodsDetailParam)
        self.logger.info("resDetail: {0}".format(self.resDetail.json()))
        # print("resDetail: {0}".format(self.resDetail.json()))
        self.specTemplateId = self.resDetail.json()["data"]["list"][0]["attribute_template_id"]
        with allure.step(f"通过 spu: {self.spuId} 查询商品规格模板 ID {self.specTemplateId}"):
            pass








