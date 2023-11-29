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
前置条件：
1、添加两个SKU商品，保存成功
2、发布商品
测试步骤：
1、上架商品
预期结果：
1、全部spu列表的第一条数据
2、展示商品设置的第一张主图
3、商品状态：上架中
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
    @allure.story('添加多sku的商品，上架商品，且为spu列表第一条')
    @pytest.mark.smoke
    def test_goods_add_mutiSku_publish(self, ini):

        # 上架商品
        with allure.step(f"上架 spu: {self.spuId} 名称: {self.addGoodsParam['spu_name']} 的商品"):
            saleRes = self.goods.saleGoods(self.saleParam)
            assert saleRes["data"]["fail_num"] == 0
        self.logger.info("saleRes: {0}".format(saleRes))
        # print("saleRes: {0}".format(saleRes))


        # 在全部spu列表中查询该数据
        listParam = {"page":1,"size":1000,"searchParams":{"searchChannel":0,"searchChannelOwnership":0,"searchString":{"keyword":str(self.spuId),"type":4},"searchInt":{"high":0,"low":0,"type":1},"searchNeedDelete":2,"searchTime":{"beginTimestamp":0,"endTimestamp":0,"type":1},"searchGoodsStatus":-1,"searchReleaseStatus":1,"searchSort":{"sortColumn":0,"sortType":1}}}
        with allure.step(f"查询 spu为 {self.spuId} 的商品 {self.addGoodsParam['spu_name']} "):
            listRes = self.goods.listSpu(listParam)
            assert listRes["data"]["list"][0]["id"] == self.spuId
        self.logger.info("listRes: {0}".format(listRes))

        # 商品状态为上架中
        goodstatus = listRes["data"]["list"][0]["status"]["valueString"]
        with allure.step(f"商品 {self.addGoodsParam['spu_name']} 状态为 {goodstatus} "):
            assert goodstatus == "上架中"
        # 商品上架sku数量=商品总sku数量=2
        skuCount = listRes["data"]["list"][0]["count"]["all"]
        onsaleSkuCount = listRes["data"]["list"][0]["count"]["current"]
        with allure.step(f"商品上架sku数量 {skuCount} 等于商品总sku数量 {onsaleSkuCount} "):
            assert skuCount == onsaleSkuCount == 2

        # 展示商品设置的第一张主图
        picture = listRes["data"]["list"][0]["picture"]
        with allure.step(f"商品第一张主图 {picture} "):
            assert picture == self.addGoodsParam["spu_resource"]["banner_content"][0]["url"]
        # # 展示商品设置的第一张主图
        # picture = listRes["data"]["list"][0]["picture"]
        # assert picture == self.addGoodsParam["spu_resource"]["banner_content"][0]["url"]

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


