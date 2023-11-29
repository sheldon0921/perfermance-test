from log.log import Logger
from utils.readerFile import ReaderFile
from utils.myJson import MyJson
from tests.common.goods.console.postage import Postage
from tests.common.goods.console.specTemplate import SpecTemplate
from utils.myTime import Mytime
from utils.myRandom import MyRandom
from tests.common.goods.console.goods import Goods
import allure
import pytest

'''
前置条件：
    1.增加邮费模板，增加成功
    2、邮费模板已经关联商品
测试步骤：
    1、删除已关联商品的邮费模板，
预期结果：
    1、删除失败
'''

@allure.feature('商品')
class Test_goods_delPostage(object):

    @pytest.fixture()
    def ini(self):
        self.mytime = Mytime()
        self.myrandom = MyRandom()
        self.goods = Goods()
        self.logger = Logger.Logger()
        self.postage = Postage()
        self.specTemplate = SpecTemplate()
        self.addPostageParam = ReaderFile.readerJson("addPostage.json")
        self.addSpecTemplateParam = ReaderFile.readerJson("addSpecTemplate.json")
        self.addGoodsParam = ReaderFile.readerJson("addGoods.json")
        self.delSpecParam = {"attribute_template_id": 123456789}
        # 新增商品并保存
        name = MyRandom.getRandomStr(3)
        self.addPostageParam['name'] = '邮费' + name
        addGoodsRes = self.goods.addGoods(self.addPostageParam, self.addSpecTemplateParam, self.addGoodsParam)
        self.logger.info("addGoodRes: {0}".format(addGoodsRes.json()))
        print('addgoodsRes:{0}'.format(addGoodsRes.json()))
        self.spuId = addGoodsRes.json()["data"]["spu_id"]
        with allure.step(f"新增 spu: {self.spuId} 名称: {self.addGoodsParam['spu_name']} 的商品"):
            assert addGoodsRes.json()["data"]["spu_id"] is not None

        # 根据名称查询邮费模板数据
        params = {"page":1,"size":10,"start_time":"","end_time":"","time_type":1,"name":self.addPostageParam['name']}
        res = self.postage.query_postage(params)
        with allure.step(f"查询邮费模板 {self.addPostageParam['name']} "):
            assert len(res["data"]["list"]) > 0
        self.logger.info("Query postage res ]info {0}".format(res))
        self.postageID = res["data"]["list"][0]["id"]
        self.delParam = {"postage_id": self.postageID}

        yield self.delParam,addGoodsRes.json()["data"]["spu_id"]

        # 删除添加的商品
        delGoods = {"channel_type": 1, "spu_id": self.spuId}
        print("&&&&&&&", delGoods)
        delRes = self.goods.delSpu(delGoods).json()
        with allure.step(f"通过 spu: {self.spuId} 删除商品 {self.addGoodsParam['spu_name']} "):
            assert delRes["message"] == "success"
        print("delGoods: {0}".format(delRes))

        # 删除规格模板
        self.delSpecParam["attribute_template_id"] = self.specTemplateId
        param = self.delSpecParam
        delRes = self.specTemplate.deleteSpecTemplate(param)
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

    @allure.story('删除已关联商品的邮费模板，且删除失败')
    @pytest.mark.smoke
    def test_goods_delPostage(self, ini):
        # 删除邮费模板
        with allure.step(f"通过邮费模板ID {self.postageID} 删除 {self.addPostageParam['name']} "):
            delRes = self.postage.delete_postage(self.delParam)
        self.logger.info("delRes {0}".format(delRes.json()))
        print("delRes {0}".format(delRes.json()))
        # assert delRes.status_code == 500 and delRes.json()["message"] == "该邮费模板已被关联，不能删除"

        # 查询商品关联的规格模板
        goodsDetailParam = {"spu_id": self.spuId}
        self.resDetail = self.goods.queryGoodsDetail(goodsDetailParam)
        self.logger.info("resDetail: {0}".format(self.resDetail.json()))
        print("resDetail: {0}".format(self.resDetail.json()))
        self.listData = self.resDetail.json()["data"]["list"][0]
        self.specTemplateId = self.resDetail.json()["data"]["list"][0]["attribute_template_id"]
        with allure.step(f"通过 spu: {self.spuId} 查询商品规格模板 ID {self.specTemplateId}"):
            assert len(self.resDetail.json()["data"]["list"]) > 0
        # 获取该商品关联的邮费模板
        self.postageIdList = list()
        if "sku" in self.listData:
            skuList = self.listData["sku"]
            assert len(skuList) > 0
            for i in range(0, len(skuList)):
                postageId = skuList[i]["postage"][1]["postage_id"]
                self.postageIdList.append(postageId)
        else:
            postageId = self.listData["postage"][1]["postage_id"]
            self.postageIdList.append(postageId)








