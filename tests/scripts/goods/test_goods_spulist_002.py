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
测试步骤：
验证未发布商品列表数据默认按照创建时间倒序排列
"""
@allure.feature('商品')
class Test_goods_addgoods(object):

    @pytest.fixture()
    def ini(self):
        self.goods = Goods()
        self.logger = Logger.Logger()
        self.specTemplate = SpecTemplate()
        self.postage = Postage()
        self.addPostageParam = ReaderFile.readerJson("addPostage.json")
        self.addSpecTemplateParam = ReaderFile.readerJson("addSpecTemplate.json")
        self.addGoodsParam = ReaderFile.readerJson("addGoods.json")

        # 新增商品1
        addGoodsRes1 = self.goods.addGoods(self.addPostageParam, self.addSpecTemplateParam, self.addGoodsParam)
        self.logger.info("addGoodRes: {0}".format(addGoodsRes1.json()))
        self.spuId1 = addGoodsRes1.json()["data"]["spu_id"]
        with allure.step(f"新增 spu: {self.spuId1} 名称: {self.addGoodsParam['spu_name']} 的商品"):
            assert addGoodsRes1.json()["data"]["spu_id"] is not None
        # self.saleParam = {"spu_id": [], "sku_id": []}
        # self.saleParam["spu_id"].append(self.spuId)
        # 新增商品2
        time.sleep(1)
        addGoodsRes2 = self.goods.addGoods(self.addPostageParam, self.addSpecTemplateParam, self.addGoodsParam)
        self.logger.info("addGoodRes: {0}".format(addGoodsRes2.json()))
        self.spuId2 = addGoodsRes2.json()["data"]["spu_id"]
        with allure.step(f"新增 spu: {self.spuId2} 名称: {self.addGoodsParam['spu_name']} 的商品"):
            assert addGoodsRes2.json()["data"]["spu_id"] is not None
        # self.saleParam = {"spu_id": [], "sku_id": []}
        # self.saleParam["spu_id"].append(self.spuId)
        self.spuIdList = [self.spuId1,self.spuId2]
        print("uuuuuuuuuuuu:   ",self.spuIdList)

        yield self.spuIdList,self.spuId2,self.spuId1

        # 删除新增的两个商品
        for i in self.spuIdList:
            delGoods = {"channel_type": 1, "spu_id": i}
            # print("&&&&&&&", delGoods)
            delRes = self.goods.delSpu(delGoods).json()
            with allure.step(f"通过 spu: {i} 删除商品 {self.addGoodsParam['spu_name']} "):
                assert delRes["code"] == 200 and delRes["message"] == "success"
            # print("delGoods1: {0}".format(delRes))

        # 删除规格模板
        for i in self.specTemplateIdList:
            self.delSpecParam = {"attribute_template_id": i}
            delRes = self.specTemplate.deleteSpecTemplate(self.delSpecParam)
            with allure.step(f"通过规格模板ID : {i} 删除规格模板 "):
                assert delRes.status_code == 200

        # 删除邮费模板：
        for postageID in self.postageIdList:
            delParam = {"postage_id": postageID}
            delRes = self.postage.delete_postage(delParam)
            self.logger.info("delRes {0}".format(delRes.json()))
            # print("delRes {0}".format(delRes.json()))
            with allure.step(f"通过邮费模板ID : {postageID} 删除邮费模板 "):
                assert delRes.status_code == 200 and delRes.json()["message"] == "success"

    @allure.story('未发布商品列表数据默认按照创建时间倒序排列')
    @pytest.mark.smoke
    def test_goods_spuList(self, ini):
        # 修改先创建的商品，重新查询列表，判断仍然是后创建的商品置顶
        # 修改spu基础素材
        spuId = {"spu_id": self.spuId1}
        time.sleep(1)
        param = {"spu_name": "xt修改spu名称！！！", "sell_point": "xt修改卖点", "spu_resource": {
            "banner_content": [{
                "sort": 0,
                "file_type": 1,
                "url": "https://img-crs.vchangyi.com/goods16155376726210.jpg"
            }],
            "info_content": [{
                "sort": 0,
                "file_type": 1,
                "url": "https://img-crs.vchangyi.com/goods16155376826750.jpg"
            }],
            "banner_video": [],
            "poster_content": [{
                "sort": 0,
                "file_type": 1,
                "url": "https://img-crs.vchangyi.com/goods16155376923650.jpg"
            }],
            "card_content": [{
                "sort": 0,
                "file_type": 1,
                "url": "https://img-crs.vchangyi.com/goods16155376966330.jpg"
            }]
        }}
        updateGoodRes = self.goods.updateGoods(spuId, param).json()
        self.logger.info("updateGoodRes: {0}".format(updateGoodRes))
        print("updateGoodRes: {0}".format(updateGoodRes))
        with allure.step(f"查询 spu: {self.spuId1} 名称: {self.addGoodsParam['spu_name']} 的商品是否置顶"):
            assert updateGoodRes["code"] == 200 and updateGoodRes["message"] == "success" and updateGoodRes["data"]["spu_id"] == spuId["spu_id"]
        print("#####################################################")

        # 查询spu列表中的全部数据
        listParam = {"page": 1, "size": 1000, "searchParams": {"searchChannel": 0, "searchChannelOwnership": 0,
                                                               "searchString": {"keyword": "", "type": 1},
                                                               "searchInt": {"high": 0, "low": 0, "type": 1},
                                                               "searchNeedDelete": 2,
                                                               "searchTime": {"beginTimestamp": 0, "endTimestamp": 0,
                                                                              "type": 1}, "searchGoodsStatus": -1,
                                                               "searchReleaseStatus": 0,
                                                               "searchSort": {"sortColumn": 0, "sortType": 1}}}
        listRes = self.goods.listSpu(listParam)["data"]["list"]
        self.logger.info("listRes: {0}".format(listRes))
        ids = {}
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        for index, value in enumerate(listRes):
            if value["id"] == self.spuId1 or value["id"] == self.spuId2:
                ids[value["id"]] = index
            else:
                continue
        print("***********************:     ",ids)
        with allure.step(f"查询 spu: {self.spuId1} 列表顺序"):
            assert listRes[ids[self.spuId1]]["updated_at"] > listRes[ids[self.spuId2]]["updated_at"]
            assert ids[self.spuId1] > ids[self.spuId2]  # 判断先创建的商品在列表中的下标大于后创建的
            assert listRes[ids[self.spuId1]]["created_at"] < listRes[ids[self.spuId2]]["created_at"]
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

        # 查询商品关联的规格模板
        self.specTemplateIdList = []
        self.postageIdList = list()
        for i in self.spuIdList:
            goodsDetailParam = {"spu_id": i}
            self.resDetail = self.goods.queryGoodsDetail(goodsDetailParam)
            self.logger.info("resDetail: {0}".format(self.resDetail.json()))
            # print("33333resDetail: {0}".format(self.resDetail.json()))
            self.listData = self.resDetail.json()["data"]["list"][0]
            self.specTemplateIdList.append(self.listData["attribute_template_id"])
            with allure.step(f"通过 spu: {i} 查询商品规格模板 ID {self.specTemplateIdList}"):
                pass
            # 获取该商品关联的邮费模板
            skuList = self.listData["sku"]
            for j in range(0, len(skuList)):
                postageId = skuList[j]["postage"][1]["postage_id"]
                self.postageIdList.append(postageId)
        print("11111:    ", self.postageIdList)
        print("22222: ", self.specTemplateIdList)


