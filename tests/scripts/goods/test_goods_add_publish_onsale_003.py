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
"""
前置条件：
1、新增并发布商品
2、商品库存充足
测试步骤：
1、上架商品
预期结果：
1、在普通商品列表中可查询到
"""

@allure.feature('商品')
class Test_goods_add_publish_onsale_goods(object):

    @pytest.fixture()
    def ini(self):
        self.goods = Goods()
        self.logger = Logger.Logger()
        self.specTemplate = SpecTemplate()
        self.postage = Postage()
        self.addPostageParam = ReaderFile.readerJson("addPostage.json")
        self.addSpecTemplateParam = ReaderFile.readerJson("addSpecTemplate.json")
        self.addGoodsParam = ReaderFile.readerJson("addGoods.json")
        self.delSpecParam = {"attribute_template_id": 123456789}
        self.addGoodsParam["is_release"] = 1
        # 新增并发布商品
        addGoodsRes = self.goods.addGoods(self.addPostageParam, self.addSpecTemplateParam, self.addGoodsParam)
        self.logger.info("addGoodRes: {0}".format(addGoodsRes.json()))
        self.spuId = addGoodsRes.json()["data"]["spu_id"]
        with allure.step(f"新增 spu: {self.spuId} 名称: {self.addGoodsParam['spu_name']} 的商品"):
            assert addGoodsRes.json()["data"]["spu_id"] is not None
        self.saleParam = {"spu_id": [], "sku_id": []}
        self.saleParam["spu_id"].append(self.spuId)

        yield self.saleParam, self.spuId
        #下架商品
        offsaleParam = self.saleParam
        with allure.step(f"下架商品  {self.addGoodsParam['spu_name']} "):
            offsaleRes = self.goods.offsaleGoods(offsaleParam)
        self.logger.info("osssale goods res ]info {0}".format(offsaleRes))
        print("offsaleRes: {0}".format(offsaleRes))
        # 删除添加的商品
        delGoods = {"channel_type": 1, "spu_id": self.spuId}
        print("&&&&&&&",delGoods)
        with allure.step(f"通过 spu: {self.spuId} 删除商品 {self.addGoodsParam['spu_name']} "):
            delRes = self.goods.delSpu(delGoods).json()
        print("delGoods: {0}".format(delRes))
        # 删除规格模板
        self.delSpecParam["attribute_template_id"] = self.specTemplateId
        with allure.step(f"通过规格模板ID : {self.specTemplateId} 删除规格模板 "):
            delRes = self.specTemplate.deleteSpecTemplate(self.delSpecParam)
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

    @allure.story('添加发布商品，为普通商品列表第一条')
    @pytest.mark.smoke
    def test_goods_onsaleGoods(self, ini):
        with allure.step(f"上架 spu: {self.spuId} 名称: {self.addGoodsParam['spu_name']} 的商品"):
            saleRes = self.goods.saleGoods(self.saleParam)
            assert saleRes["data"]["fail_num"] == 0
        self.logger.info("saleRes: {0}".format(saleRes))
        # print("saleRes: {0}".format(saleRes))

        # 查询普通商品列表的该spu数据
        goodlistParam = {"searchType":2,"searchParams":{"searchString":{"keyword":str(self.spuId),"type":4},"searchInt":{"high":0,"low":0,"type":1},"searchChannel":0,"searchTime":{"beginTimestamp":0,"endTimestamp":0,"type":1},"searchGoodsStatus":0,"searchChannelOwnership":0,"searchSort":{"sortColumn":0,"sortType":0}},"page":1,"size":100}
        with allure.step(f"在普通商品列表查询 spu为 {self.spuId} 的商品 {self.addGoodsParam['spu_name']} "):
            goodlistRes = self.goods.queryGoodsList(goodlistParam)
            assert goodlistRes["data"]["list"][0]["spu_id"] == self.spuId
        # print("888",goodlistRes)
        self.logger.info("goodlistRes: {0}".format(goodlistRes))


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
        if "sku" in self.listData:
            skuList = self.listData["sku"]
            for i in range(0, len(skuList)):
                postageId = skuList[i]["postage"][1]["postage_id"]
                self.postageIdList.append(postageId)
        else:
            postageId = self.listData["postage"][1]["postage_id"]
            self.postageIdList.append(postageId)
