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
已有待上架的商品
测试步骤：
1、修改商品spu规格模板
2、保存
预期结果：
修改失败
"""
@allure.feature('商品')
class Test_goods_updateGoods_008(object):

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
        # 查询新增的邮费模板
        params = {"page": "1", "size": "1"}
        res = self.postage.query_postage(params)  # 查询时间区间内邮费模板数据
        self.logger.info("Query postage res info {0}".format(res))
        with allure.step(f"通过邮费模板名称: {self.addPostageParam['name']} 查询邮费模板"):
            assert len(res["data"]["list"]) == 1 and res["data"]["list"][0]["name"] == self.addPostageParam["name"]
        self.oldpostageID = res["data"]["list"][0]["id"]
        # print("8888888：        ", self.oldpostageID)
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
        # 新增一个用于修改的邮费模板
        startTime = Mytime.getCurrTimeStamp()
        time.sleep(1)
        self.addPostageParam["name"] = "修改的邮费模板"
        res = self.postage.addPostage(self.addPostageParam)  # 调接口创建邮费模板
        endTime = Mytime.getCurrTimeStamp()
        self.logger.info("add postage template res: {0}".format(res))
        with allure.step(f"新增邮费模板 {self.addPostageParam['name']}"):
            assert res.status_code == 200 and "success" in res.text
        # 查询新增的邮费模板
        params = {"page": "", "size": "", "start_time": startTime, "end_time": endTime, "time_type": ""}
        res = self.postage.query_postage(params)  # 查询时间区间内邮费模板数据
        self.logger.info("Query postage res info {0}".format(res))
        with allure.step(f"查询邮费模板 {self.addPostageParam['name']}"):
            assert len(res["data"]["list"]) == 1 and res["data"]["list"][0]["name"] == self.addPostageParam["name"]
        self.postageID = res["data"]["list"][0]["id"]
        print("99999999:     ", self.postageID)

        yield self.publishGoodsParam, self.spuId, self.postageID, self.oldpostageID

        # 删除新建商品时新增的邮费模板
        delParam = {"postage_id": self.oldpostageID}
        delRes = self.postage.delete_postage(delParam)
        self.logger.info("delRes {0}".format(delRes.json()))
        print("delRes {0}".format(delRes.json()))
        with allure.step(f"通过模板ID :{self.oldpostageID} 删除旧邮费模板"):
            assert delRes.status_code == 200 and delRes.json()["message"] == "success"

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
            # assert delRes.status_code == 500
        with allure.step(f"通过邮费模板ID : {postageID} 删除邮费模板 "):
            pass

    @allure.story('已有商品修改spu级别规格模板')
    @pytest.mark.smoke
    @pytest.mark.skip(reason = "接口目前未做校验")
    def test_goods_publishGoods(self, ini):
        # 修改spu邮费模板
        spuId = self.publishGoodsParam
        param = {"postage": [{
            "delivery_type": 1,
            "is_open": True,
            "postage_id": self.postageID,
            "settlement_type": 2
        }, {
            "delivery_type": 2,
            "is_open": True,
            "postage_id": 0
        }]}
        updateGoodRes = self.goods.updateGoods(spuId, param).json()
        self.logger.info("updateGoodRes: {0}".format(updateGoodRes))
        print("updateGoodRes: {0}".format(updateGoodRes))
        assert updateGoodRes["code"] == 200 and updateGoodRes["message"] == "success" and updateGoodRes["data"][
            "spu_id"] == spuId["spu_id"]

        # 查看详情中spu级别邮费
        res = self.goods.queryGoodsDetail(spuId).json()
        self.logger.info("detailGoodRes: {0}".format(res))
        print("detailGoodRes%%%%%%%%%%%%%%%%%%%%%: {0}".format(res))
        postage = res["data"]["list"][0]["postage"]
        assert len(postage) == 1 and postage[0]["postage_id"] != self.postageID
        # assert postage[0]["postage_id"] != self.postageID and postage[1]["postage_id"] != self.postageID
        # assert postage[0]["is_open"] == True and postage[1]["is_open"] == True

        # 查询商品关联的规格模板
        goodsDetailParam = {"spu_id": self.spuId}
        self.resDetail = self.goods.queryGoodsDetail(goodsDetailParam)
        self.logger.info("resDetail: {0}".format(self.resDetail.json()))
        print("resDetail: {0}".format(self.resDetail.json()))
        self.listData = self.resDetail.json()["data"]["list"][0]
        self.specTemplateId = self.listData["attribute_template_id"]
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


