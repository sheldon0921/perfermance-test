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
1、修改商品配送方式
2、修改商品规格
3、修改sku价格
预期结果：
1、1/2/3均不可修改
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
        assert addGoodsRes.json()["data"]["spu_id"] is not None
        self.spuId = addGoodsRes.json()["data"]["spu_id"]
        self.saleParam = {"spu_id":[],"sku_id":[]}
        self.saleParam["spu_id"].append(self.spuId)
        # print("*******************",self.saleParam)
        onsaleRes = self.goods.saleGoods(self.saleParam)
        self.logger.info("onsaleRes: {0}".format(onsaleRes))
        # print("%%%%%%%%%%",onsaleRes)
        assert onsaleRes["data"]["fail_num"] == 0
        self.offsaleParam = self.saleParam
        yield self.offsaleParam,self.spuId

        # # 删除添加的商品
        # delGoods = {"channel_type": 1, "spu_id": self.spuId}
        # print("&&&&&&&", delGoods)
        # delRes = self.goods.delSpu(delGoods).json()
        # print("delGoods: {0}".format(delRes))
        # # 删除规格模板
        # self.delSpecParam["attribute_template_id"] = self.specTemplateId
        # delRes = self.specTemplate.deleteSpecTemplate(self.delSpecParam)
        # assert delRes.status_code == 200
        # # 删除邮费模板
        # params = {"page": 1, "size": 1, "start_time": "", "end_time": "", "time_type": 1}
        # res = self.postage.query_postage(params)  # 查询时间区间内邮费模板数据
        # self.logger.info("Query postage res ]info {0}".format(res))
        # self.postageID = res["data"]["list"][0]["id"]
        # delParam = {"postage_id": self.postageID}
        # delRes = self.postage.delete_postage(delParam)
        # self.logger.info("delRes {0}".format(delRes.json()))
        # print("delRes {0}".format(delRes.json()))
        # assert delRes.status_code == 200 and delRes.json()["message"] == "success"


    @pytest.mark.smoke
    @pytest.mark.skip(reason="上架商品修改，")
    def test_goods_offsaleGoods(self, ini):
        self.addGoodsParam["spu_id"] = self.spuId
        self.addPostageParam["name"] = "阿树新增邮费模板New"
        self.addSpecTemplateParam["template_name"] = "颜色大小模板New"
        addGoodsRes = self.goods.addGoods(self.addPostageParam, self.addSpecTemplateParam, self.addGoodsParam)
        print("addGoodRes: {0}".format(addGoodsRes))

        # 修改商品配送方式
        # goodsDetailParam = {"spu_id": self.spuId}
        # goodsDetailRes = self.goods.queryGoodsDetail(goodsDetailParam)
        # print("goodsDetailRes: {0}".format(goodsDetailRes.json()))
        # updateRes = self.goods.addGoods(goodsDetailRes["data"]["list"][0])
        # print("updateRes: {0}".format(updateRes))

        # 修改商品规格

        # # 修改sku价格
        # offsaleRes = self.goods.offsaleGoods(self.offsaleParam)
        # print("^^^^^^^^:",offsaleRes)
        # self.logger.info("offsaleRes: {0}".format(offsaleRes))
        # assert offsaleRes["code"] == 200 and offsaleRes['message'] == "success"
        # # 查询商品关联的规格模板
        # goodsDetailParam = {"spu_id": self.spuId}
        # self.resDetail = self.goods.queryGoodsDetail(goodsDetailParam)
        # self.logger.info("resDetail: {0}".format(self.resDetail.json()))
        # print("resDetail: {0}".format(self.resDetail.json()))
        # self.specTemplateId = self.resDetail.json()["data"]["list"][0]["attribute_template_id"]

