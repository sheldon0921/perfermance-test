from log.log import Logger
from utils.readerFile import ReaderFile
from utils.myJson import MyJson
from tests.common.goods.console.postage import Postage
from tests.common.goods.console.specTemplate import SpecTemplate
from utils.myTime import Mytime
from tests.common.goods.console.goods import Goods
import allure
import pytest

"""
前置条件：
1、商品状态为待上架
测试步骤：
1、删除spu（001）
2、删除sku（002）
预期结果：
1、已失效列表的第一条数据
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
        #新增并发布，上架商品
        addGoodsRes = self.goods.addGoods(self.addPostageParam, self.addSpecTemplateParam, self.addGoodsParam)
        self.logger.info("addGoodRes: {0}".format(addGoodsRes.json()))
        self.spuId = addGoodsRes.json()["data"]["spu_id"]
        with allure.step(f"新增 spu: {self.spuId} 名称: {self.addGoodsParam['spu_name']} 的商品"):
            assert addGoodsRes.json()["data"]["spu_id"] is not None
        self.saleParam = {"spu_id":[],"sku_id":[]}
        self.saleParam["spu_id"].append(self.spuId)
        # print("*******************",self.saleParam)
        onsaleRes = self.goods.saleGoods(self.saleParam)
        self.logger.info("onsaleRes: {0}".format(onsaleRes))
        # print("%%%%%%%%%%",onsaleRes)
        with allure.step(f"上架 spu为 {self.spuId} 的商品 {self.addGoodsParam['spu_name']} "):
            assert onsaleRes["data"]["fail_num"] == 0
        self.offsaleParam = self.saleParam
        # 下架商品
        offsaleRes = self.goods.offsaleGoods(self.offsaleParam)
        self.logger.info("offsaleRes: {0}".format(offsaleRes))
        with allure.step(f"下架商品  {self.addGoodsParam['spu_name']} "):
            assert offsaleRes["code"] == 200 and offsaleRes['message'] == "success"
        goodlistParam = {"searchType":4,"searchParams":{"searchString":{"keyword":str(self.spuId),"type":4},"searchInt":{"high":0,"low":0,"type":1},"searchChannel":0,"searchTime":{"beginTimestamp":0,"endTimestamp":0,"type":1},"searchGoodsStatus":0,"searchChannelOwnership":0,"searchSort":{"sortColumn":0,"sortType":0}},"page":1,"size":10}
        goodlistRes = self.goods.queryGoodsList(goodlistParam)
        self.logger.info("goodlistRes: {0}".format(goodlistRes))
        assert goodlistRes["data"]["list"][0]["spu_id"] == self.spuId
        self.skuId = goodlistRes["data"]["list"][0]["sku_id"]
        yield self.offsaleParam, self.spuId,self.skuId

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

    @allure.story('待上架商品删除spu，且在已失效列表的第一条')
    # spu级别删除
    @pytest.mark.smoke
    def test_goods_delGoods001(self, ini):
        delGoods = {"channel_type": 1, "spu_id": self.spuId}
        # print("&&&&&&&", delGoods)
        delRes = self.goods.delSpu(delGoods).json()
        with allure.step(f"通过 spu: {self.spuId} 删除商品 {self.addGoodsParam['spu_name']} "):
            assert delRes["code"] == 200 and delRes['message'] == "success"
        self.logger.info("delRes: {0}".format(delRes))
        # print("delGoods: {0}".format(delRes))
        # 在已失效商品列表中的第一条数据
        goodlistParam = {"searchType":5,"searchParams":{"searchString":{"keyword":str(self.spuId),"type":4},"searchInt":{"high":0,"low":0,"type":1},"searchChannel":0,"searchTime":{"beginTimestamp":0,"endTimestamp":0,"type":1},"searchGoodsStatus":0,"searchChannelOwnership":0,"searchSort":{"sortColumn":0,"sortType":0}},"page":1,"size":10}
        goodlistRes = self.goods.queryGoodsList(goodlistParam)
        with allure.step(f"查询 spu: {self.spuId} 为已失效列表第一条数据 "):
            assert goodlistRes["data"]["list"][0]["spu_id"] == self.spuId
        # print("888********",goodlistRes)
        self.logger.info("goodlistRes: {0}".format(goodlistRes))


        # 查询商品关联的规格模板
        goodsDetailParam = {"spu_id": self.spuId}
        self.resDetail = self.goods.queryGoodsDetail(goodsDetailParam)
        self.logger.info("resDetail: {0}".format(self.resDetail.json()))
        # print("resDetail: {0}".format(self.resDetail.json()))
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

    @allure.story('待上架商品删除sku，且在已失效列表的第一条')
    @pytest.mark.smoke
    # sku级别删除
    def test_goods_delGoods002(self, ini):
        delGoods = {"channel_type": 1, "sku_ids": [self.skuId]}
        print("&&&&&&&", delGoods)
        delRes = self.goods.delSku(delGoods).json()
        with allure.step(f"通过 spu: {self.skuId} 删除商品 {self.addGoodsParam['spu_name']} "):
            assert delRes["code"] == 200 and delRes['message'] == "success"
        self.logger.info("delRes: {0}".format(delRes))
        print("delGoods: {0}".format(delRes))
        # 在已失效商品列表中的第一条数据
        goodlistParam = {"searchType":5,"searchParams":{"searchString":{"keyword":str(self.spuId),"type":4},"searchInt":{"high":0,"low":0,"type":1},"searchChannel":0,"searchTime":{"beginTimestamp":0,"endTimestamp":0,"type":1},"searchGoodsStatus":0,"searchChannelOwnership":0,"searchSort":{"sortColumn":0,"sortType":0}},"page":1,"size":10}
        goodlistRes = self.goods.queryGoodsList(goodlistParam)
        # print("888",goodlistRes)
        self.logger.info("goodlistRes: {0}".format(goodlistRes))
        with allure.step(f"查询 spu: {self.skuId} 为已失效列表第一条数据 "):
            assert goodlistRes["data"]["list"][0]["sku_id"] == self.skuId
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

