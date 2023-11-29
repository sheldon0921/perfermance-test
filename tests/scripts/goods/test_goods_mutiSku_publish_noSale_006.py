from tests.common.goods.console.specTemplate import SpecTemplate
from tests.common.goods.console.postage import Postage
from tests.common.goods.console.goods import Goods
from tests.common.goods.shop.goods import Goods as ShopGoods
from utils.readerFile import ReaderFile
from utils.myJson import MyJson
from log.log import Logger
import pytest
from utils.myTime import Mytime
import time
import allure

'''
前置条件：
    1.规格模板和邮费模板创建成功
测试步骤：
    1.多(两个)SKU商品,保存商品信息，保存成功
    2.发布该商品，发布成功
    3.在小程序端搜索该商品，有预期结果1

预期结果：
    1.搜索不到该商品
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
        self.shopGoods = ShopGoods()
        self.addPostageParam = ReaderFile.readerJson("addPostage.json")
        self.addSpecTemplateParam = ReaderFile.readerJson("addSpecTemplate.json")
        self.addGoodsParam = ReaderFile.readerJson("addMutiSkuGoods.json")
        self.delSpecParam = {"attribute_template_id": 123456789}
        yield self.shopGoods, self.addPostageParam, self.addSpecTemplateParam, self.addGoodsParam, self.myJson, self.specTemplate, self.postage
        # 删除添加的商品
        delGoods = {"channel_type": 1, "sku_ids": self.skuIds}
        delRes = self.goods.delSku(delGoods).json()
        with allure.step(f"通过 spu: {self.spuId} 删除商品 {self.addGoodsParam['spu_name']} "):
            assert delRes["code"] == 200 and delRes["message"] == "success"
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

    @allure.story('发布多sku的商品，且小程序端查不到该商品')
    @pytest.mark.smoke
    def test_goods_publish_noSale(self, ini):
        # 保存商品信息
        self.addGoodsParam['sku'][1]['sku_name'] = '大豆油非转基因{0}'.format(int(time.time()))
        addGoodsRes = self.goods.addGoods(self.addPostageParam, self.addSpecTemplateParam, self.addGoodsParam)
        self.logger.info("addGoodRes: {0}".format(addGoodsRes.json()))
        print("addGoodRes: {0}".format(addGoodsRes.json()))
        self.spuId = addGoodsRes.json()["data"]["spu_id"]
        with allure.step(f"新增 spu: {self.spuId} 名称: {self.addGoodsParam['spu_name']} 的商品"):
            assert self.spuId is not None
        # 发布商品
        publishParam = {"spu_id": self.spuId}
        publishRes = self.goods.publishGoods(publishParam).json()
        self.logger.info("publish res: {0}".format(publishRes))
        with allure.step(f"发布 spu: {self.spuId} 名称: {self.addGoodsParam['spu_name']} 的商品"):
            assert publishRes["data"]["spu_id"] is not None
        goodsListParam = {"searchType": 1, "searchParams": {"searchString": {"keyword": str(self.spuId), "type": 4},
                                                            "searchInt": {"high": 0, "low": 0, "type": 1},
                                                            "searchChannel": 0,
                                                            "searchTime": {"beginTimestamp": 0, "endTimestamp": 0,
                                                                           "type": 1}, "searchGoodsStatus": 0,
                                                            "searchChannelOwnership": 0,
                                                            "searchSort": {"sortColumn": 0, "sortType": 0}}, "page": 1,
                          "size": 10}
        listSpuRes = self.goods.queryGoodsList(goodsListParam)
        self.logger.info("spuListRes: {0}".format(listSpuRes))
        print("spuListRes: {0}".format(listSpuRes))
        goodsInfo = listSpuRes["data"]["list"][0]
        # self.skuId = goodsInfo["sku_id"]
        self.skuIds = [listSpuRes["data"]["list"][0]["sku_id"], listSpuRes["data"]["list"][1]["sku_id"]]
        # 商品是全部spu列表的第一条数据，状态为待上架
        status = goodsInfo["status"]["valueString"]
        print('###########:{0}'.format(goodsInfo))
        with allure.step(f"查询 spu为 {self.spuId} 的商品 状态为 {status} "):
            assert status == "待上架"
            assert goodsInfo["spu_id"] == self.spuId
            assert goodsInfo["sku_image"] == "https://img-crs.vchangyi.com/goods161165268167720.png"
        # 在小程序端搜不到该商品
        goodsName = goodsInfo["sku_name"]
        searchResult = self.shopGoods.queryGoodsByGoodsName(goodsName)
        with allure.step(f"小程序端查询第一个商品 {goodsName} "):
            assert len(searchResult["data"]["list"]) == 0
        print("searchResult: {0}".format(searchResult))
        # 在小程序端搜索第二个商品
        goodsInfo = listSpuRes["data"]["list"][1]
        goodsName = goodsInfo["sku_name"]
        searchResult = self.shopGoods.queryGoodsByGoodsName(goodsName)
        with allure.step(f"小程序端查询第二个商品 {goodsName} "):
            assert len(searchResult["data"]["list"]) == 0
        print("searchResult: {0}".format(searchResult))

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







