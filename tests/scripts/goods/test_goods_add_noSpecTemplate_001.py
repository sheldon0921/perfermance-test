from tests.common.goods.console.specTemplate import SpecTemplate
from tests.common.goods.console.postage import Postage
from tests.common.goods.console.goods import Goods
from tests.common.goods.shop.goods import Goods as ShopGoods
from tests.common.goods.console.stock import Stock
from utils.readerFile import ReaderFile
from utils.myJson import MyJson
from log.log import Logger
import pytest
from utils.myTime import Mytime
import allure

'''
前置条件：
    1.商品模块功能正常
测试步骤：
    1.添加商品时，规格模板为空，有预期结果1

预期结果：
    1.添加商品失败
'''

@allure.feature('商品')
class Test_goods_add_noSpecTemplate_001(object):
    @pytest.fixture()
    def ini(self):
        self.goods = Goods()
        self.logger = Logger.Logger()
        self.myJson = MyJson()
        self.specTemplate = SpecTemplate()
        self.postage = Postage()
        self.shopGoods = ShopGoods()
        self.stock = Stock()
        self.addPostageParam = ReaderFile.readerJson("addPostage.json")
        print("addPostageParam: {0}".format(self.addPostageParam))
        self.addGoodsParam = ReaderFile.readerJson("addGoodsNoSpecTemplate.json")
        self.delSpecParam = {"attribute_template_id": 123456789}
        yield self.shopGoods, self.addPostageParam, self.addGoodsParam, self.myJson, self.specTemplate, self.postage
        # # 删除添加的商品
        # delGoods = {"channel_type": 1, "sku_ids": [self.skuId]}
        # delRes = self.goods.delSku(delGoods).json()
        # print("delGoods: {0}".format(delRes))
        # # 删除规格模板
        # self.delSpecParam["attribute_template_id"] = self.specTemplateId
        # delRes = self.specTemplate.deleteSpecTemplate(self.delSpecParam)
        # assert delRes.status_code == 200
        # # 删除邮费模板
        # params = {"page":1,"size":1,"start_time":"","end_time":"","time_type":1}
        # res = self.postage.query_postage(params)  # 查询时间区间内邮费模板数据
        # self.logger.info("Query postage res ]info {0}".format(res))
        # self.postageID = res["data"]["list"][0]["id"]
        # delParam = {"postage_id":self.postageID}
        # delRes = self.postage.delete_postage(delParam)
        # self.logger.info("delRes {0}".format(delRes.json()))
        # print("delRes {0}".format(delRes.json()))
        # assert delRes.status_code == 200 and delRes.json()["message"] == "success"

    @pytest.mark.smoke
    @pytest.mark.xfail(reason="传入非法参数，添加商品预期失败")
    @pytest.mark.skip(reason="接口符合要求的情况下，增加商品会失败，目前会成功，造成环境脏数据")
    def test_goods_add_noSpecTemplate(self, ini):
        # 保存商品信息
        addGoodsRes = self.goods.addGoods(self.addPostageParam, "", self.addGoodsParam)
        self.logger.info("addGoodRes: {0}".format(addGoodsRes.json()))
        print("addGoodRes: {0}".format(addGoodsRes.json()))
        self.spuId = addGoodsRes.json()["data"]["spu_id"]
        assert self.spuId is not None

        # # 发布商品
        # publishParam = {"spu_id": self.spuId}
        # publishRes = self.goods.publishGoods(publishParam).json()
        # self.logger.info("publish res: {0}".format(publishRes))
        # assert publishRes["data"]["spu_id"] is not None
        # goodsListParam = {"searchType": 1, "searchParams": {"searchString": {"keyword": "", "type": 1},
        #                                                     "searchInt": {"high": 0, "low": 0, "type": 1},
        #                                                     "searchChannel": 0,
        #                                                     "searchTime": {"beginTimestamp": 0, "endTimestamp": 0,
        #                                                                    "type": 1}, "searchGoodsStatus": 0,
        #                                                     "searchChannelOwnership": 0,
        #                                                     "searchSort": {"sortColumn": 0, "sortType": 0}}, "page": 1,
        #                   "size": 1}
        # listSpuRes = self.goods.queryGoodsList(goodsListParam)
        # self.logger.info("spuListRes: {0}".format(listSpuRes))
        # print("spuListRes: {0}".format(listSpuRes))
        # goodsInfo = listSpuRes["data"]["list"][0]
        # self.skuId = goodsInfo["sku_id"]
        # # 商品是全部spu列表的第一条数据，状态为待上架
        # status = goodsInfo["status"]["valueString"]
        # assert status == "待上架"
        # assert goodsInfo["spu_id"] == self.spuId
        # assert goodsInfo["sku_image"] == "https://img-crs.vchangyi.com/goods16149152407290.jpg"
        # # 删除添加的商品
        # delGoods = {"channel_type": 1, "sku_ids": [self.skuId]}
        # delRes = self.goods.delSku(delGoods).json()
        # print("delGoods: {0}".format(delRes))
        #
        # # 查询库存数量
        # # {"page":1,"size":10,"first_value":"xtwl001","first_type":"material_no","second_type":"all","min_value":"","max_value":"","source_id":0,"time_type":"create","start_time":"","end_time":""}
        # stockParam = {"page": 1, "size": 10, "first_value": "xtwl001", "first_type": "material_no",
        #               "second_type": "all", "min_value": "", "max_value": "", "source_id": 0, "time_type": "create",
        #               "start_time": "", "end_time": ""}
        # stockListRes = self.stock.queryStockList(stockParam)
        # totalStock = stockListRes[0]["total_stock"]
        # # 修改库存数量
        # updateExpress = {"source_id": 133, "type": "3", "online": 1, "number": totalStock, "sku_id": self.skuId}
        # updateExpressRes = self.stock.updateChannelStock(updateExpress)
        # assert updateExpressRes["message"] == "未找到渠道信息"
        # # 查询商品关联的规格模板
        # goodsDetailParam = {"spu_id": self.spuId}
        # self.resDetail = self.goods.queryGoodsDetail(goodsDetailParam)
        # self.logger.info("resDetail: {0}".format(self.resDetail.json()))
        # print("resDetail: {0}".format(self.resDetail.json()))
        # self.specTemplateId = self.resDetail.json()["data"]["list"][0]["attribute_template_id"]







