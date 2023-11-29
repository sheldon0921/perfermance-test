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
    1.规格模板和邮费模板创建成功
测试步骤：
    1.单SKU商品,保存商品信息，有预期结果1
    2.发布该商品，发布成功，有预期结果2
预期结果：
    1.保存成功
    2.待上架商品的第一条数据，状态为待上架
'''

@allure.feature('商品')
class Test_goods_publish_noSale(object):
    @pytest.fixture()
    def ini(self):
        self.goods = Goods()
        self.logger = Logger.Logger()
        self.myJson = MyJson()
        self.specTemplate = SpecTemplate()
        self.postage = Postage()
        self.addPostageParam = ReaderFile.readerJson("addPostage.json")
        self.addSpecTemplateParam = ReaderFile.readerJson("addSpecTemplate.json")
        self.addGoodsParam = ReaderFile.readerJson("addGoods.json")
        self.delSpecParam = {"attribute_template_id": 123456789}
        yield self.addPostageParam, self.addSpecTemplateParam, self.addGoodsParam, self.myJson, self.specTemplate, self.postage
        # 删除添加的商品
        delGoods = {"channel_type": 1, "sku_ids": [self.skuId]}
        delRes = self.goods.delSku(delGoods).json()
        with allure.step(f"通过 spu: {self.spuId} 删除商品 {self.addGoodsParam['spu_name']} "):
            assert delRes["message"] == "success"
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

    @allure.story('添加发布单sku商品，为待上架列表第一条，且为待上架状态')
    @pytest.mark.smoke
    def test_goods_publish_noSale(self, ini):
        # 保存商品信息
        addGoodsRes = self.goods.addGoods(self.addPostageParam, self.addSpecTemplateParam, self.addGoodsParam)
        self.logger.info("addGoodRes: {0}".format(addGoodsRes.json()))
        print("addGoodRes: {0}".format(addGoodsRes.json()))
        self.spuId = addGoodsRes.json()["data"]["spu_id"]
        with allure.step(f"保存 spu: {self.spuId} 名称: {self.addGoodsParam['spu_name']} 的商品"):
            assert self.spuId is not None
        # 发布商品
        publishParam = {"spu_id":self.spuId}
        publishRes = self.goods.publishGoods(publishParam).json()
        self.logger.info("publish res: {0}".format(publishRes))
        with allure.step(f"发布 spu: {self.spuId} 名称: {self.addGoodsParam['spu_name']} 的商品"):
            assert publishRes["data"]["spu_id"] is not None
        goodsListParam = {"searchType": 4, "searchParams": {"searchString": {"keyword": str(self.spuId), "type": 4},"searchSort": {"sortColumn": 0, "sortType": 0}}, "page": 1,"size": 10}
        goodsList = self.goods.queryGoodsList(goodsListParam)
        self.logger.info("goodsListRes: {0}".format(goodsList))
        print("goodsListRes: {0}".format(goodsList))
        # TODO 优化myJson中的方法
        print(self.myJson.value(goodsList["data"],"spu_id",1))
        self.logger.info(goodsList["data"]["list"][0]["spu_id"])
        self.skuId = goodsList["data"]["list"][0]["sku_id"]
        goodsStatus = goodsList["data"]["list"][0]["status"]["valueString"]
        with allure.step(f"商品 {self.addGoodsParam['spu_name']} 状态为 {goodsStatus} "):
            assert self.spuId == goodsList["data"]["list"][0]["spu_id"]
            assert "待上架" == goodsStatus

        # 查询商品关联的规格模板
        goodsDetailParam = {"spu_id": self.spuId}
        self.resDetail = self.goods.queryGoodsDetail(goodsDetailParam)
        self.logger.info("resDetail: {0}".format(self.resDetail.json()))
        print("resDetail: {0}".format(self.resDetail.json()))
        self.listData = self.resDetail.json()["data"]["list"][0]
        self.specTemplateId = self.resDetail.json()["data"]["list"][0]["attribute_template_id"]
        with allure.step(f"通过 spu: {self.spuId} 查询商品规格模板 ID {self.specTemplateId}"):
            pass
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






