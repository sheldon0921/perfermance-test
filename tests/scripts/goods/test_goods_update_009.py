from log.log import Logger
from utils.readerFile import ReaderFile
from tests.common.goods.console.specTemplate import SpecTemplate
from utils.myJson import MyJson
from tests.common.goods.console.postage import Postage
from utils.myTime import Mytime
from tests.common.goods.console.goods import Goods
import time
import pytest
import allure
"""
前置条件：
已有已上架的商品
测试步骤：
1、修改spu级别的规格模板
预期结果：
保存成功
"""
@allure.feature('商品')
class Test_goods_updateGoods_009(object):

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
        assert addGoodsRes.json()["data"]["spu_id"] is not None
        self.publishGoodsParam = addGoodsRes.json()["data"]
        # 查询新增的规格模板
        time.sleep(1)
        params = {"tag_id":"","start_time":"","end_time":"","page":1,"size":1}
        res = self.specTemplate.listSpecTemplate(params)
        self.oldSpecTemplateId = res["data"]["list"][0]["id"]
        # print("8888888：        ",self.oldpostageID)
        # 发布上面新增的商品
        publishRes = self.goods.publishGoods(self.publishGoodsParam)
        self.logger.info("publishRes: {0}".format(publishRes.json()))
        # print("addGoodRes: {0}".format(publishRes.json()))
        assert publishRes.json()["data"]["spu_id"] is not None
        self.spuId = addGoodsRes.json()["data"]["spu_id"]
        # 上架商品
        self.saleParam = {"spu_id": [self.spuId], "sku_id": []}
        res = self.goods.saleGoods(self.saleParam)
        self.logger.info("res: {0}".format(res))
        assert res["code"] == 200 and res["data"]["fail_num"] == 0

        # 新增一个用于修改的规格模板
        startTime = Mytime.getCurrTimeStamp()
        time.sleep(1)
        self.addSpecTemplateParam["template_name"] = "修改的规格模板"
        res = self.specTemplate.addSpecTemplate(self.addSpecTemplateParam)  # 调接口创建邮费模板
        endTime = Mytime.getCurrTimeStamp()
        self.logger.info("add SpecTemplate res: {0}".format(res))
        assert res["code"] == 200 and res["message"] == "success"
        # 查询新增的规格模板
        params = {"tag_id":"","start_time":startTime,"end_time":endTime,"page":1,"size":1}
        res = self.specTemplate.listSpecTemplate(params)
        self.logger.info("Query specTemplate info {0}".format(res))
        assert res["data"]["list"][0]["template_name"] == self.addSpecTemplateParam["template_name"]
        self.newSpecTemplateId = res["data"]["list"][0]["id"]
        print("99999999:     ",self.newSpecTemplateId)

        yield self.saleParam,self.publishGoodsParam,self.spuId,self.newSpecTemplateId,self.oldSpecTemplateId

        # 删除新建商品时新增的规格模板
        delParam = {"attribute_template_id": self.oldSpecTemplateId}
        delRes = self.specTemplate.deleteSpecTemplate(delParam)
        self.logger.info("delRes {0}".format(delRes.json()))
        print("delRes {0}".format(delRes.json()))
        assert delRes.status_code == 200 and delRes.json()["message"] == "success"

        # 下架商品
        offsaleParam = self.saleParam
        offsaleRes = self.goods.offsaleGoods(offsaleParam)
        self.logger.info("osssale goods res ]info {0}".format(offsaleRes))
        print("offsaleRes: {0}".format(offsaleRes))

        # 删除添加的商品
        delGoods = {"channel_type": 1, "spu_id": self.spuId}
        delRes = self.goods.delSpu(delGoods).json()
        assert delRes["code"] == 200 and delRes["message"] == "success"
        print("delGoods: {0}".format(delRes))
        # 删除规格模板
        self.delSpecParam = {"attribute_template_id": self.specTemplateId}
        delRes = self.specTemplate.deleteSpecTemplate(self.delSpecParam)
        assert delRes.status_code == 200
        # 删除邮费模板
        for postageID in self.postageIdList:
            delParam = {"postage_id": postageID}
            delRes = self.postage.delete_postage(delParam)
            self.logger.info("delRes {0}".format(delRes.json()))
            print("delRes {0}".format(delRes.json()))
            # assert delRes.status_code == 200 and delRes.json()["message"] == "success"


    @pytest.mark.smoke
    @pytest.mark.skip(reason = "接口目前未做校验")
    def test_goods_publishGoods(self, ini):
        # 修改spu规格模板
        spuId = self.publishGoodsParam
        param = {"attribute_template_id": self.newSpecTemplateId}
        updateGoodRes = self.goods.updateGoods(spuId,param).json()
        self.logger.info("updateGoodRes: {0}".format(updateGoodRes))
        print("updateGoodRes: {0}".format(updateGoodRes))
        assert updateGoodRes["code"] == 200 and updateGoodRes["message"] == "success" and updateGoodRes["data"]["spu_id"] == spuId["spu_id"]
        # 查看详情中spu级别规格
        res = self.goods.queryGoodsDetail(spuId).json()
        self.logger.info("detailGoodRes: {0}".format(res))
        print("detailGoodRes%%%%%%%%%%%%%%%%%%%%%: {0}".format(res))
        SpecTemplate = res["data"]["list"][0]["attribute_template_id"]
        assert int(SpecTemplate) == self.oldSpecTemplateId

        # 查询商品关联的规格模板
        goodsDetailParam = {"spu_id": self.spuId}
        self.resDetail = self.goods.queryGoodsDetail(goodsDetailParam)
        self.logger.info("resDetail: {0}".format(self.resDetail.json()))
        print("resDetail: {0}".format(self.resDetail.json()))
        self.listData = self.resDetail.json()["data"]["list"][0]
        self.specTemplateId = self.listData["attribute_template_id"]
        # 获取该商品关联的邮费模板
        self.postageIdList = list()
        skuList = self.listData["sku"]
        # print("7777777777777777777777777777777777777777")
        # print(len(skuList))
        for i in range(0, len(skuList)):
            postageId = skuList[i]["postage"][1]["postage_id"]
            print(postageId)
            self.postageIdList.append(postageId)
        # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        # print(self.postageIdList)


