from tests.common.goods.console.specTemplate import SpecTemplate
from tests.common.goods.console.postage import Postage
from log.log import Logger
from utils.readerFile import ReaderFile
from utils.myJson import MyJson
from tests.common.goods.console.postage import Postage
from utils.myTime import Mytime
from tests.common.goods.console.goods import Goods
import time
import pytest
import allure
"""
测试步骤：
1、添加两个SKU商品，保存成功
2、发布商品

"""

@allure.feature('商品')
class Test_goods_add_mutiSku_publish_001(object):

    @pytest.fixture()
    def ini(self):
        self.goods = Goods()
        self.logger = Logger.Logger()
        self.addPostageParam = ReaderFile.readerJson("addPostage.json")
        self.addSpecTemplateParam = ReaderFile.readerJson("addSpecTemplate.json")
        self.addGoodsParam = ReaderFile.readerJson("addMutiSkuGoods.json")
        self.specTemplate = SpecTemplate()
        self.postage = Postage()
        yield self.addPostageParam, self.addSpecTemplateParam, self.addGoodsParam,self.specTemplate
        # 删除添加的商品
        delGoods = {"channel_type":1,"spu_id": self.spuId}
        with allure.step(f"通过 spu: {self.spuId} 删除商品 {self.addGoodsParam['spu_name']} "):
            delRes = self.goods.delSpu(delGoods).json()
        print("delGoods: {0}".format(delRes))
        # 删除规格模板
        self.delSpecParam = {"attribute_template_id": self.specTemplateId}
        with allure.step(f"通过规格模板ID : {self.specTemplateId} 删除规格模板 "):
            delRes = self.specTemplate.deleteSpecTemplate(self.delSpecParam)
            assert delRes.status_code == 200
        # 删除邮费模板
        # params = {"page":1,"size":1,"start_time":"","end_time":"","time_type":1}
        # res = self.postage.query_postage(params)  # 查询时间区间内邮费模板数据
        # self.logger.info("Query postage res ]info {0}".format(res))
        # self.postageID = res["data"]["list"][0]["id"]
        for postageID in self.postageIdList:
            delParam = {"postage_id":postageID}
            delRes = self.postage.delete_postage(delParam)
            self.logger.info("delRes {0}".format(delRes.json()))
            print("delRes {0}".format(delRes.json()))
        with allure.step(f"通过邮费模板ID : {postageID} 删除邮费模板 "):
            pass
            # assert delRes.status_code == 200 and delRes.json()["message"] == "success"
    @allure.story('添加多sku的商品，发布成功')
    @pytest.mark.smoke
    def test_goods_add_mutiSku_publish(self, ini):
        # 新增商品，保存
        addGoodsRes = self.goods.addGoods(self.addPostageParam, self.addSpecTemplateParam, self.addGoodsParam)
        self.logger.info("addGoodRes: {0}".format(addGoodsRes.json()))
        print("addGoodRes: {0}".format(addGoodsRes.json()))
        self.spuId = addGoodsRes.json()["data"]["spu_id"]
        with allure.step(f"新增 spu: {self.spuId} 名称: {self.addGoodsParam['spu_name']} 的商品"):
            assert addGoodsRes.json()["data"]["spu_id"] is not None

        # 发布上面新增的商品
        self.publishGoodsParam = {"spu_id": self.spuId}
        with allure.step(f"发布 spu: {self.spuId} 名称: {self.addGoodsParam['spu_name']} 的商品"):
            publishRes = self.goods.publishGoods(self.publishGoodsParam)
            assert publishRes.json()["data"]["spu_id"] is not None
        self.logger.info("publishRes: {0}".format(publishRes.json()))
        print("addGoodRes: {0}".format(publishRes.json()))


        # 查询商品关联的规格模板
        goodsDetailParam = {"spu_id": self.spuId}
        self.resDetail = self.goods.queryGoodsDetail(goodsDetailParam)
        self.logger.info("resDetail: {0}".format(self.resDetail.json()))
        print("resDetail: {0}".format(self.resDetail.json()))
        self.listData = self.resDetail.json()["data"]["list"][0]
        self.specTemplateId = self.listData["attribute_template_id"]
        with allure.step(f"通过 spu: {self.spuId} 查询商品规格模板 ID {self.specTemplateId}"):
            pass
        # 获取该商品关联的邮费模板
        self.postageIdList = list()
        skuList = self.listData["sku"]
        for i in range(0, len(skuList)):
            postageId = skuList[i]["postage"][1]["postage_id"]
            self.postageIdList.append(postageId)

        # print("self.postageIdList: {0}".format(self.postageIdList))
        self.logger.info("self.postageIdList: {0}".format(self.postageIdList))
        with allure.step(f"商品 {self.addGoodsParam['spu_name']} 的邮费模板为 {self.postageIdList}"):
            assert len(self.postageIdList) == 2





