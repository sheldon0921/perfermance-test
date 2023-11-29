from log.log import Logger
from utils.readerFile import ReaderFile
from tests.common.goods.console.specTemplate import SpecTemplate
from utils.myJson import MyJson
from tests.common.goods.console.postage import Postage
from utils.myTime import Mytime
from tests.common.goods.console.goods import Goods
import allure
import pytest
"""
前置条件：
已有待上架的商品
测试步骤：
1、修改商品spu基本信息（名称，卖点、基本素材）
2、保存
预期结果：
修改成功
"""
@allure.feature('商品')
class Test_goods_updateGoods_006(object):

    @pytest.fixture()
    def ini(self):
        self.goods = Goods()
        self.logger = Logger.Logger()
        self.specTemplate = SpecTemplate()
        self.postage = Postage()
        self.addPostageParam = ReaderFile.readerJson("addPostage.json")
        self.addSpecTemplateParam = ReaderFile.readerJson("addSpecTemplate.json")
        self.addGoodsParam = ReaderFile.readerJson("addGoods.json")
        #新增商品，保存
        addGoodsRes = self.goods.addGoods(self.addPostageParam, self.addSpecTemplateParam, self.addGoodsParam)
        self.logger.info("addGoodRes: {0}".format(addGoodsRes.json()))
        self.spuId = addGoodsRes.json()["data"]["spu_id"]
        with allure.step(f"新增 spu: {self.spuId} 名称: {self.addGoodsParam['spu_name']} 的商品"):
            assert addGoodsRes.json()["data"]["spu_id"] is not None
        self.publishGoodsParam = addGoodsRes.json()["data"]
        # 发布上面新增的商品
        publishRes = self.goods.publishGoods(self.publishGoodsParam)
        self.logger.info("publishRes: {0}".format(publishRes.json()))
        # print("addGoodRes: {0}".format(publishRes.json()))
        with allure.step(f"发布商品： {self.addGoodsParam['spu_name']} "):
            assert publishRes.json()["data"]["spu_id"] is not None

        # 上架商品
        self.saleParam = {"spu_id": [self.spuId], "sku_id": []}
        res = self.goods.saleGoods(self.saleParam)
        self.logger.info("res: {0}".format(res))
        with allure.step(f"上架商品： {self.addGoodsParam['spu_name']} "):
            assert res["code"] == 200 and res["data"]["fail_num"] == 0

        # 查询商品关联的规格模板
        goodsDetailParam = {"spu_id": self.spuId}
        print("*****************",goodsDetailParam)
        self.resDetail = self.goods.queryGoodsDetail(goodsDetailParam)
        self.logger.info("resDetail: {0}".format(self.resDetail.json()))
        print("resDetail: {0}".format(self.resDetail.json()))
        self.listData = self.resDetail.json()["data"]["list"][0]
        self.specTemplateId = self.listData["attribute_template_id"]
        with allure.step(f"通过 spu: {self.spuId} 查询商品规格模板 ID {self.specTemplateId}"):
            pass
        # 查询规格模板详细信息
        listDetailParam = {"attribute_template_id": self.specTemplateId}
        listDetailRes = self.specTemplate.listDetailSpecTemplate(listDetailParam)
        self.logger.info("add specTemplate res: {0}".format(listDetailRes))
        print("add specTemplate res: {0}".format(listDetailRes))
        with allure.step(f"通过规格模板 ID {self.specTemplateId} 查询模板详细信息"):
            assert "success" == listDetailRes["message"]
        # 拼接新的sku的规格ids
        self.useOneSpecTemplate = [MyJson().value(listDetailRes["data"], "id", 5),
                              MyJson().value(listDetailRes["data"], "id", 9)]
        # self.attribute_item_value = [MyJson().value(listDetailRes["data"], "attribute_item_value", 3),
        #                       MyJson().value(listDetailRes["data"], "attribute_item_value", 6)]

        # 查询商品详情，获取sku数据
        goodsDetailParam = {"spu_id": self.spuId}
        goodsDetailRes = self.goods.queryGoodsDetail(goodsDetailParam)
        self.logger.info("goodsDetailRes: {0}".format(goodsDetailRes.json()))
        with allure.step(f"通过 spu: {self.spuId} 获取商品sku"):
            assert goodsDetailRes.status_code == 200
        self.skuParams = goodsDetailRes.json()["data"]["list"][0]["sku"]

        yield self.publishGoodsParam,self.spuId,self.useOneSpecTemplate,self.skuParams,self.saleParam

        # 下架商品
        offsaleParam = self.saleParam
        offsaleRes = self.goods.offsaleGoods(offsaleParam)
        self.logger.info("osssale goods res ]info {0}".format(offsaleRes))
        print("offsaleRes: {0}".format(offsaleRes))

        # 删除添加的商品
        delGoods = {"channel_type": 1, "spu_id": self.spuId}
        delRes = self.goods.delSpu(delGoods).json()
        with allure.step(f"通过 spu: {self.spuId} 删除商品 {self.addGoodsParam['spu_name']} "):
            assert delRes["code"] == 200 and delRes["message"] == "success"
        print("delGoods: {0}".format(delRes))

        # 删除规格模板
        self.delSpecParam = {"attribute_template_id": self.specTemplateId}
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

    @allure.story('已有商品修改商品的spu基础信息')
    @pytest.mark.smoke
    def test_goods_publishGoods(self, ini):
        #修改spu基础素材
        spuId = self.publishGoodsParam
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
        with allure.step(f"修改商品的spu基本信息"):
            assert updateGoodRes["code"] == 200 and updateGoodRes["message"] == "success" and updateGoodRes["data"]["spu_id"] == spuId["spu_id"]
        # spu列表中该数据显示的图片是修改后的图片
        listParam = {
            "page": 1,
            "size": 1,
            "searchParams": {
                "searchString": {
                    "keyword": str(spuId["spu_id"]),
                    "type": 4
                },
                "searchChannel": 0,
                "searchChannelOwnership": 0,
                "searchInt": {
                    "high": 0,
                    "low": 0,
                    "type": 1
                },
                "searchNeedDelete": 2,
                "searchTime": {
                    "beginTimestamp": 0,
                    "endTimestamp": 0,
                    "type": 1
                },
                "searchGoodsStatus": -1,
                "searchReleaseStatus": 1,
                "searchSort": {
                    "sortColumn": 0,
                    "sortType": 1
                }
            }
        }
        listRes = self.goods.listSpu(listParam)
        self.logger.info("listRes: {0}".format(listRes))
        assert listRes["data"]["list"] != None
        # 展示商品设置的第一张主图
        picture = listRes["data"]["list"][0]["picture"]
        with allure.step(f"通过spu：{self.spuId} 查询商品主图 {picture}"):
            assert picture == param["spu_resource"]["banner_content"][0]["url"]
            assert listRes["data"]["list"][0]["spu_name"] == param["spu_name"]
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


