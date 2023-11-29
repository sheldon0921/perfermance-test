# coding=utf-8

from tests.common.goods.console.specTemplate import SpecTemplate
from tests.common.goods.console.postage import Postage
from tests.common.goods.console.goods import Goods
from utils.readerFile import ReaderFile
from utils.myJson import MyJson
from log.log import Logger
import pytest
from utils.myTime import Mytime
import allure

'''
前置条件：
    1.规格模板已关联商品
测试步骤：
    1.删除规格模板，有预期结果1
预期结果：
    1.删除失败
'''

@allure.feature('商品')
class Test_goods_unPublish(object):
    @pytest.fixture()
    def ini(self):
        self.myJson = MyJson()
        self.goods = Goods()
        self.logger = Logger.Logger()
        self.postage = Postage()
        self.specTemplate = SpecTemplate()
        self.addPostageParam = ReaderFile.readerJson("addPostage.json")
        self.addSpecTemplateParam = ReaderFile.readerJson("addSpecTemplate.json")
        self.addGoodsParam = ReaderFile.readerJson("addGoods.json")
        self.delSpecParam = {"attribute_template_id": 123456789}
        yield self.addPostageParam, self.addSpecTemplateParam, self.addGoodsParam, self.delSpecParam, self.myJson, self.postage
        # 删除添加的商品
        delGoods = {"channel_type": 1, "spu_id": self.spuId}
        with allure.step(f"通过 spu: {self.spuId} 删除商品 {self.addGoodsParam['spu_name']} "):
            delRes = self.goods.delSpu(delGoods).json()
        print("delGoods: {0}".format(delRes))
        # 删除规格模板
        self.delSpecParam["attribute_template_id"] = self.specTemplateId
        delRes = self.specTemplate.deleteSpecTemplate(self.delSpecParam)
        with allure.step(f"通过规格模板ID : {self.specTemplateId} 删除规格模板 "):
            assert delRes.status_code == 200
        # 删除邮费模板
        for postageID in self.postageIdList:
            delParam = {"postage_id": postageID}
            delRes = self.postage.delete_postage(delParam)
            self.logger.info("delRes {0}".format(delRes.json()))
            print("delRes {0}".format(delRes.json()))
            # assert delRes.status_code == 200 and delRes.json()["message"] == "success"
        with allure.step(f"通过邮费模板ID : {postageID} 删除邮费模板 "):
            pass

    @allure.story('新增已关联商品的规格模板，且不可以删除')
    @pytest.mark.smoke
    def test_goods_updateSpecTemplate(self, ini):
        addGoodsRes = self.goods.addGoods(self.addPostageParam, self.addSpecTemplateParam, self.addGoodsParam)
        self.logger.info("addGoodRes: {0}".format(addGoodsRes.json()))
        print("addGoodRes: {0}".format(addGoodsRes.json()))
        self.spuId = addGoodsRes.json()["data"]["spu_id"]
        with allure.step(f"新增 spu: {self.spuId} 名称: {self.addGoodsParam['spu_name']} 的商品"):
            assert self.spuId is not None
        # 查询商品关联的规格模板
        goodsDetailParam = {"spu_id": self.spuId}
        self.resDetail = self.goods.queryGoodsDetail(goodsDetailParam)
        self.logger.info("resDetail: {0}".format(self.resDetail.json()))
        print("resDetail: {0}".format(self.resDetail.json()))
        self.listData = self.resDetail.json()["data"]["list"][0]
        self.specTemplateId = self.resDetail.json()["data"]["list"][0]["attribute_template_id"]
        with allure.step(f"通过 spu: {self.spuId} 查询商品规格模板 ID {self.specTemplateId}"):
            pass
        # 删除规格模板,关联商品的规格模板不能被删除

        self.postageId = self.resDetail.json()["data"]
        print("specTemplateId 0 {0}".format(self.specTemplateId))
        self.delSpecParam["attribute_template_id"] = self.specTemplateId
        delRes = self.specTemplate.deleteSpecTemplate(self.delSpecParam)
        self.logger.info("delRes {0}".format(delRes.json()))
        with allure.step(f"通过规格模板ID : {self.specTemplateId} 删除规格模板失败 "):
            assert delRes.json()["code"] == 1400002 and delRes.json()["message"] == "规格模板删除失败"
        # 获取该商品关联的邮费模板
        self.postageIdList = list()
        if "sku" in self.listData:
            skuList = self.listData["sku"]
            for i in range(0, len(skuList)):
                postageId = skuList[i]["postage"][1]["postage_id"]
                self.postageIdList.append(postageId)
        else:
            postageId = self.listData["postage"][1]["postage_id"]
            self.postageIdList.append(postageId)








