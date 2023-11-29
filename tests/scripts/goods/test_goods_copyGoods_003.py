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
1、已有上架中状态商品(单sku)
测试步骤：
1、复制全部spu列表中上架中的商品
2、不做任何修改，直接保存
预期结果：
1、复制时商品的所有信息全部带入
2、保存成功
"""

@allure.feature('商品')
class Test_goods_copyGoods(object):

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
        # 新增商品，保存
        addGoodsRes = self.goods.addGoods(self.addPostageParam, self.addSpecTemplateParam, self.addGoodsParam)
        self.logger.info("addGoodRes: {0}".format(addGoodsRes.json()))
        self.spuId = addGoodsRes.json()["data"]["spu_id"]
        with allure.step(f"新增 spu: {self.spuId} 名称: {self.addGoodsParam['spu_name']} 的商品"):
            assert addGoodsRes.json()["data"]["spu_id"] is not None
        # 查询未发布商品列表的第一条数据
        listParam = {"page":1,"size":10,"searchParams":{"searchChannel":0,"searchChannelOwnership":0,"searchString":{"keyword":str(self.spuId),"type":4},"searchInt":{"high":0,"low":0,"type":1},"searchNeedDelete":2,"searchTime":{"beginTimestamp":0,"endTimestamp":0,"type":1},"searchGoodsStatus":-1,"searchReleaseStatus":0,"searchSort":{"sortColumn":0,"sortType":0}}}
        with allure.step(f"在未发布商品列表查询 spu为 {self.spuId} 的商品 {self.addGoodsParam['spu_name']} "):
            listRes = self.goods.listSpu(listParam)
            assert listRes["data"]["list"][0]["id"] == addGoodsRes.json()["data"]["spu_id"]
        self.logger.info("listRes: {0}".format(listRes))


        # 发布上面新增的商品
        publishParam = {"spu_id":self.spuId}
        with allure.step(f"发布 spu为 {self.spuId} 的商品 {self.addGoodsParam['spu_name']} "):
            publishRes = self.goods.publishGoods(publishParam)
            assert publishRes.json()["data"]["spu_id"] is not None
        self.logger.info("publishRes: {0}".format(publishRes.json()))
        # print("addGoodRes: {0}".format(publishRes.json()))


        # 上架商品
        self.saleParam = {"spu_id": [], "sku_id": []}
        self.saleParam["spu_id"].append(self.spuId)
        with allure.step(f"上架 spu为 {self.spuId} 的商品 {self.addGoodsParam['spu_name']} "):
            saleRes = self.goods.saleGoods(self.saleParam)
            assert saleRes["data"]["fail_num"] == 0
        self.logger.info("saleRes: {0}".format(saleRes))
        # print("saleRes: {0}".format(saleRes))


        yield self.addPostageParam, self.addGoodsParam, self.addSpecTemplateParam, self.spuId

        # 下架商品
        offsaleParam = self.saleParam
        with allure.step(f"下架商品  {self.addGoodsParam['spu_name']} "):
            offsaleRes = self.goods.offsaleGoods(offsaleParam)
        self.logger.info("osssale goods res ]info {0}".format(offsaleRes))
        print("offsaleRes: {0}".format(offsaleRes))

        # 删除添加的商品
        delGoods = {"channel_type": 1, "spu_id": self.spuId}
        print("&&&&&&&", delGoods)
        with allure.step(f"通过 spu: {self.spuId} 删除商品 {self.addGoodsParam['spu_name']} "):
            delRes = self.goods.delSpu(delGoods).json()
        print("delGoods1: {0}".format(delRes))
        delGoods = {"channel_type": 1, "spu_id": self.copySpuId}
        with allure.step(f"通过 copyspu: {self.copySpuId} 删除商品 {self.addGoodsParam['spu_name']} "):
            delRes = self.goods.delSpu(delGoods).json()
        print("delGoods2: {0}".format(delRes))
        # 删除规格模板
        self.delSpecParam["attribute_template_id"] = self.specTemplateId
        param = self.delSpecParam
        with allure.step(f"通过规格模板ID : {self.specTemplateId} 删除规格模板 "):
            delRes = self.specTemplate.deleteSpecTemplate(param)
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

    @allure.story('复制并保存上架的单sku商品，且在上架列表可以查到该商品')
    @pytest.mark.smoke
    def test_goods_copyGoods(self, ini):
        # 复制上架中商品（spu级别复制）
        param = {"spu_id": self.spuId}
        with allure.step(f"复制 spu: {self.spuId} 名称: {self.addGoodsParam['spu_name']} 的商品"):
            detialRes = self.goods.copyGoods(param)
            assert detialRes is not None
        self.logger.info("detialRes: {0}".format(detialRes))


        # 直接保存商品
        with allure.step(f"保存 spu: {self.spuId} 名称: {self.addGoodsParam['spu_name']} 的商品"):
            saveRes = self.goods.saveGoods(detialRes).json()
            assert saveRes["code"] == 200 and saveRes["data"] != None
        print("saveRes: {0}".format(saveRes))
        self.logger.info("saveRes: {0}".format(saveRes))

        self.copySpuId = saveRes["data"]['spu_id']

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
