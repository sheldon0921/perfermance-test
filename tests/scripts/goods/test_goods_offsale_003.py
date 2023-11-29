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
1、新增并发布商品
2、商品库存充足
3、上架商品
4、单sku
测试步骤：
1、下架商品
预期结果：
1、下架成功
2、全部sku列表的第一条数据
3、商品状态：待上架
4、展示商品的sku图
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
        # 新增并发布，上架商品
        addGoodsRes = self.goods.addGoods(self.addPostageParam, self.addSpecTemplateParam, self.addGoodsParam)
        self.logger.info("addGoodRes: {0}".format(addGoodsRes.json()))
        self.spuId = addGoodsRes.json()["data"]["spu_id"]
        with allure.step(f"新增 spu: {self.spuId} 名称: {self.addGoodsParam['spu_name']} 的商品"):
            assert addGoodsRes.json()["data"]["spu_id"] is not None
        self.saleParam = {"spu_id": [], "sku_id": []}
        self.saleParam["spu_id"].append(self.spuId)
        # print("*******************",self.saleParam)
        onsaleRes = self.goods.saleGoods(self.saleParam)
        self.logger.info("onsaleRes: {0}".format(onsaleRes))
        # print("%%%%%%%%%%",onsaleRes)
        with allure.step(f"上架 spu: {self.spuId} 名称: {self.addGoodsParam['spu_name']} 的商品"):
            assert onsaleRes["data"]["fail_num"] == 0
        self.offsaleParam = self.saleParam
        yield self.offsaleParam, self.spuId

        # 删除添加的商品
        delGoods = {"channel_type": 1, "spu_id": self.spuId}
        print("&&&&&&&", delGoods)
        delRes = self.goods.delSpu(delGoods).json()
        with allure.step(f"通过 spu: {self.spuId} 删除商品 {self.addGoodsParam['spu_name']} "):
            assert delRes["message"] == "success"
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

    @allure.story('新增并上架单sku商品，可以下架成功，且展示商品sku图')
    @pytest.mark.smoke
    def test_goods_offsaleGoods(self, ini):
        offsaleRes = self.goods.offsaleGoods(self.offsaleParam)
        print("^^^^^^^^:", offsaleRes)
        self.logger.info("offsaleRes: {0}".format(offsaleRes))
        with allure.step(f"下架 spu: {self.spuId} 名称: {self.addGoodsParam['spu_name']} 的商品"):
            assert offsaleRes["code"] == 200 and offsaleRes['message'] == "success"
        # 查询全部sku列表的第一条数据
        goodlistParam = {"searchType": 4, "searchParams": {"searchString": {"keyword": str(self.spuId), "type": 4},
                                                           "searchGoodsStatus": 0,
                                                           "searchSort": {"sortColumn": 0, "sortType": 0}}, "page": 1,
                         "size": 10}
        goodlistRes = self.goods.queryGoodsList(goodlistParam)
        # print("888",goodlistRes)
        self.logger.info("goodlistRes: {0}".format(goodlistRes))
        # 商品状态显示上架中
        # 展示商品的sku图
        goodstatus = goodlistRes["data"]["list"][0]["status"]["valueString"]
        picture = goodlistRes["data"]["list"][0]["sku_image"]
        with allure.step(f"通过 spu: {self.spuId} 查询全部spu列表第一条数据，且sku图为 {picture}"):
            assert goodlistRes["data"]["list"][0]["spu_id"] == self.spuId
            assert goodstatus == "待上架"
            assert picture == self.addGoodsParam["sku"][0]["resource"]["sku_picture"][0]["url"]

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

