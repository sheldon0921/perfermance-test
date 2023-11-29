from log.log import Logger
from utils.readerFile import ReaderFile
from utils.myJson import MyJson
from tests.common.goods.console.postage import Postage
from tests.common.goods.console.specTemplate import SpecTemplate
from utils.myTime import Mytime
from tests.common.goods.console.goods import Goods
from tests.common.goods.shop.goods import Goods as ShopGoods
import time
import pytest
import allure
"""
前置条件：
1、新增并发布商品
2、商品库存充足
测试步骤：
1、上架商品
2、在小程序端可搜索到
"""

@allure.feature('商品')
class Test_goods_add_publish_onsale_goods(object):

    @pytest.fixture()
    def ini(self):
        self.goods = Goods()
        self.logger = Logger.Logger()
        self.specTemplate = SpecTemplate()
        self.postage = Postage()
        self.shopGoods = ShopGoods()
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

        yield self.saleParam, self.spuId,self.addGoodsParam,self.shopGoods

        #下架商品
        offsaleParam = self.saleParam
        with allure.step(f"下架商品  {self.addGoodsParam['spu_name']} "):
            offsaleRes = self.goods.offsaleGoods(offsaleParam)
        self.logger.info("osssale goods res ]info {0}".format(offsaleRes))
        # print("offsaleRes: {0}".format(offsaleRes))
        # 删除添加的商品
        delGoods = {"channel_type": 1, "spu_id": self.spuId}
        # print("&&&&&&&",delGoods)
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

    @allure.story('添加发布商品，且可以在小程序端搜索到该商品')
    @pytest.mark.smoke
    def test_goods_onsaleGoods(self, ini):
        with allure.step(f"上架 spu: {self.spuId} 名称: {self.addGoodsParam['spu_name']} 的商品"):
            saleRes = self.goods.saleGoods(self.saleParam)
            assert saleRes["data"]["fail_num"] == 0
        self.logger.info("saleRes: {0}".format(saleRes))
        # print("saleRes: {0}".format(saleRes))

        # 查询全部spu列表的有该spu数据
        listParam = {"page":1,"size":10,"searchParams":{"searchChannel":0,"searchChannelOwnership":0,"searchString":{"keyword":str(self.spuId),"type":4},"searchInt":{"high":0,"low":0,"type":1},"searchNeedDelete":2,"searchTime":{"beginTimestamp":0,"endTimestamp":0,"type":1},"searchGoodsStatus":-1,"searchReleaseStatus":1,"searchSort":{"sortColumn":0,"sortType":0}}}
        with allure.step(f"在普通商品列表查询 spu为 {self.spuId} 的商品 {self.addGoodsParam['spu_name']} "):
            listRes = self.goods.listSpu(listParam)
            assert listRes["data"]["list"][0]["id"] == self.spuId
        self.logger.info("listRes: {0}".format(listRes))


        #在小程序端可查询到此商品
        spuName = listRes["data"]["list"][0]["spu_name"]
        searchResult = self.shopGoods.queryGoodsByGoodsName(spuName)
        count = 1
        while len(searchResult["data"]["list"]) == 0:
            time.sleep(1)
            searchResult = self.shopGoods.queryGoodsByGoodsName(spuName)
            self.logger.info(
                "times {0}list data length: {1}, data contents {2}".format(count, len(searchResult["data"]["list"]),
                                                                           searchResult))
            count = count + 1
            if count == 81:
                break
        with allure.step(f"小程序端商品为  {spuName}"):
            assert len(searchResult["data"]["list"]) == 1
        print("searchResult: {0}".format(searchResult))

        # 查询商品关联的规格模板
        goodsDetailParam = {"spu_id": self.spuId}
        self.resDetail = self.goods.queryGoodsDetail(goodsDetailParam)
        self.logger.info("resDetail: {0}".format(self.resDetail.json()))
        assert len(self.resDetail.json()["data"]["list"]) != 0
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

