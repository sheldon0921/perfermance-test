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
验证普通商品列表数据默认按照创建时间倒序排列

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
        self.addGoodsParam = ReaderFile.readerJson("addMutiSkuGoods.json")
        self.addGoodsParam["is_release"] = 1

        # 新增并发布商品1(多sku)
        addGoodsRes1 = self.goods.addGoods(self.addPostageParam, self.addSpecTemplateParam, self.addGoodsParam)
        self.logger.info("addGoodRes: {0}".format(addGoodsRes1.json()))

        self.spuId1 = addGoodsRes1.json()["data"]["spu_id"]
        with allure.step(f"新增 spu: {self.spuId1} 名称: {self.addGoodsParam['spu_name']} 的商品"):
            assert addGoodsRes1.json()["data"]["spu_id"] is not None
        # self.saleParam = {"spu_id": [], "sku_id": []}
        # self.saleParam["spu_id"].append(self.spuId)

        # 新增并发布商品2(多sku）
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

        # 上架新增的两个spu
        for i in self.spuIdList:
            self.saleParam =  {"spu_id": [i], "sku_id": []}
            saleRes = self.goods.saleGoods(self.saleParam)
            self.logger.info("saleRes: {0}".format(saleRes))
            with allure.step(f"通过 spu: {i} 上架商品 {self.addGoodsParam['spu_name']} "):
                assert saleRes["code"] == 200 and saleRes["data"]["fail_num"] == 0


        yield self.spuIdList,self.spuId2,self.spuId1,self.saleParam

        # 下架新增的两个商品
        for i in self.spuIdList:
            offSaleParam = {"spu_id": [i], "sku_id": []}
            offSaleRes = self.goods.offsaleGoods(offSaleParam)
            self.logger.info("offsaleRes: {0}".format(offSaleRes))
            with allure.step(f"通过 spu: {i} 下架商品 {self.addGoodsParam['spu_name']} "):
                assert offSaleRes["code"] == 200 and offSaleRes["data"]["fail_num"] == 0

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

    @allure.story('普通商品列表数据默认按照创建时间倒序排列')
    @pytest.mark.smoke
    def test_goods_skuList(self, ini):
        # 修改先创建的商品，重新查询列表，判断仍然是后创建的商品置顶
        # 修改spu基础素材
        spuId = {"spu_id":self.spuId1}
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

        # 查询普通商品列表中的全部数据
        listParam = {"searchType": 2,
         "searchParams": {"searchString": {"keyword": "", "type": 1}, "searchInt": {"high": 0, "low": 0, "type": 1},
                          "searchChannel": 0, "searchTime": {"beginTimestamp": 0, "endTimestamp": 0, "type": 1},
                          "searchGoodsStatus": 0, "searchChannelOwnership": 0,
                          "searchSort": {"sortColumn": 0, "sortType": 0}}, "page": 1, "size": 1000}
        listRes = self.goods.queryGoodsList(listParam)["data"]["list"]
        self.logger.info("listRes: {0}".format(listRes))
        spu1Ids = []
        spu2Ids = []
        for index, value in enumerate(listRes):
            if value["spu_id"] == self.spuId1:
                spu1Ids.append([value["sku_id"],index,value["time"]["created_at"]])
            elif value["spu_id"] == self.spuId2:
                spu2Ids.append([value["sku_id"], index,value["time"]["created_at"]])
            else:
                continue
        print("99999999:   ",spu1Ids,spu2Ids)
        # 判断商品按照创建时间倒序排列
        assert spu1Ids[0][1] or spu1Ids[1][1] > spu2Ids[0][1] or spu2Ids[1][1]
        if spu1Ids[0][1] > spu1Ids[1][1]:
            assert spu1Ids[0][2] <= spu1Ids[1][2]
        else:
            assert spu1Ids[0][2] >= spu1Ids[1][2]
        if spu2Ids[0][1] > spu2Ids[1][1]:
            assert spu2Ids[0][2] <= spu2Ids[1][2]
        else:
            assert spu2Ids[0][2] >= spu2Ids[1][2]

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
        # print("11111:    ",self.postageIdList)
        # print("22222: ",self.specTemplateIdList)


