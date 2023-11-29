from tests.common.goods.console.specTemplate import SpecTemplate
from tests.common.goods.console.postage import Postage
from log.log import Logger
from utils.readerFile import ReaderFile
from utils.myJson import MyJson
from tests.common.goods.console.postage import Postage
from utils.myTime import Mytime
from tests.common.goods.console.goods import Goods
import allure
import pytest
"""
前置条件：
1、添加两个SKU商品，保存成功
2、发布商品
3、商品库存充足
测试步骤：
1、上架商品
预期结果：
1、在全部sku列表的第一条数据
2、商品状态：上架中
3、展示商品的sku图
"""

@allure.feature('商品')
class Test_goods_add_mutiSku_publish_002(object):

    @pytest.fixture()
    def ini(self):
        self.goods = Goods()
        self.logger = Logger.Logger()
        self.addPostageParam = ReaderFile.readerJson("addPostage.json")
        self.addSpecTemplateParam = ReaderFile.readerJson("addSpecTemplate.json")
        self.addGoodsParam = ReaderFile.readerJson("addMutiSkuGoods.json")
        self.specTemplate = SpecTemplate()
        self.postage = Postage()
        # 新增商品，保存

        addGoodsRes = self.goods.addGoods(self.addPostageParam, self.addSpecTemplateParam, self.addGoodsParam)
        self.logger.info("addGoodRes: {0}".format(addGoodsRes.json()))

        self.spuId = addGoodsRes.json()["data"]["spu_id"]
        with allure.step(f"新增 spu: {self.spuId} 名称: {self.addGoodsParam['spu_name']} 的商品"):
            self.publishGoodsParam = {"spu_id":self.spuId}
            assert addGoodsRes.json()["data"]["spu_id"] is not None
        # 发布上面新增的商品
        with allure.step(f"发布 spu: {self.spuId} 名称: {self.addGoodsParam['spu_name']} 的商品"):
            publishRes = self.goods.publishGoods(self.publishGoodsParam)
            assert publishRes.json()["data"]["spu_id"] is not None
        self.logger.info("publishRes: {0}".format(publishRes.json()))
        # print("addGoodRes: {0}".format(publishRes.json()))

        self.saleParam = {"spu_id": [], "sku_id": []}
        self.saleParam["spu_id"].append(self.spuId)

        yield self.spuId,self.saleParam,self.addPostageParam, self.addSpecTemplateParam, self.addGoodsParam,self.specTemplate

        # 下架商品
        offsaleParam = self.saleParam
        with allure.step(f"下架商品  {self.addGoodsParam['spu_name']} "):
            offsaleRes = self.goods.offsaleGoods(offsaleParam)
        self.logger.info("osssale goods res ]info {0}".format(offsaleRes))
        print("offsaleRes: {0}".format(offsaleRes))

        # 删除添加的商品
        delGoods = {"channel_type":1,"spu_id": self.spuId}
        with allure.step(f"通过 spu: {self.spuId} 删除商品 {self.addGoodsParam['spu_name']} "):
            delRes = self.goods.delSpu(delGoods).json()
            assert delRes["code"] == 200 and delRes["message"] == "success"
        print("delGoods: {0}".format(delRes))
        # 删除规格模板
        self.delSpecParam = {"attribute_template_id": self.specTemplateId}
        with allure.step(f"通过规格模板ID : {self.specTemplateId} 删除规格模板 "):
            delRes = self.specTemplate.deleteSpecTemplate(self.delSpecParam)
            assert delRes.status_code == 200
        # 删除邮费模板
        for postageID in self.postageIdList:
            delParam = {"postage_id":postageID}
            delRes = self.postage.delete_postage(delParam)
            self.logger.info("delRes {0}".format(delRes.json()))
            print("delRes {0}".format(delRes.json()))
            # assert delRes.status_code == 200 and delRes.json()["message"] == "success"
        with allure.step(f"通过邮费模板ID : {postageID} 删除邮费模板 "):
            pass

    @allure.story('添加多sku的商品,上架商品，且为sku列表第一条')
    @pytest.mark.smoke
    def test_goods_add_mutiSku_publish(self, ini):
        # 上架商品
        with allure.step(f"上架 spu: {self.spuId} 名称: {self.addGoodsParam['spu_name']} 的商品"):
            saleRes = self.goods.saleGoods(self.saleParam)
            assert saleRes["data"]["fail_num"] == 0
        self.logger.info("saleRes: {0}".format(saleRes))
        # print("saleRes: {0}".format(saleRes))


        # 查询全部sku列表内搜索该spuid,可查询到两条数据
        goodlistParam = {"searchType":1,"searchParams":{"searchString":{"keyword":str(self.spuId),"type":4},"searchInt":{"high":0,"low":0,"type":1},"searchChannel":0,"searchTime":{"beginTimestamp":0,"endTimestamp":0,"type":1},"searchGoodsStatus":0,"searchChannelOwnership":0,"searchSort":{"sortColumn":0,"sortType":0}},"page":1,"size":1000}
        with allure.step(f"查询 spu为 {self.spuId} 的商品 {self.addGoodsParam['spu_name']} "):
            goodlistRes = self.goods.queryGoodsList(goodlistParam)
            assert len(goodlistRes["data"]["list"]) == 2
        # print("888",goodlistRes)
        self.logger.info("goodlistRes: {0}".format(goodlistRes))

        self.skuIds = []
        for i in goodlistRes["data"]["list"]:
            assert i["spu_id"] == self.spuId
            self.skuIds.append(i["sku_id"])
            # 商品状态显示上架中
            goodstatus = i["status"]["valueString"]
            with allure.step(f"商品 {self.addGoodsParam['spu_name']} 状态为 {goodstatus} "):
                assert goodstatus == "上架中"
            # # 展示商品的sku图
            # picture = i["sku_image"]
            # assert picture == self.addGoodsParam["sku"][0]["resource"]["sku_picture"][0]["url"]

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
