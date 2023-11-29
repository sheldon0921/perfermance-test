from log.log import Logger
from utils.readerFile import ReaderFile
from tests.common.goods.console.specTemplate import SpecTemplate
from utils.myJson import MyJson
from tests.common.goods.console.postage import Postage
from utils.myTime import Mytime
from utils.myRandom import MyRandom
from tests.common.goods.console.goods import Goods
import time
import pytest
import allure
"""
前置条件：
已有待上架的商品
测试步骤：
1、修改spu级别的规格模板
预期结果：
保存成功
"""
@allure.feature('商品')
class Test_goods_updateGoods_002(object):

    @pytest.fixture()
    def ini(self):
        self.mytime = Mytime()
        self.myrandom = MyRandom()
        self.goods = Goods()
        self.logger = Logger.Logger()
        self.specTemplate = SpecTemplate()
        self.postage = Postage()
        self.addPostageParam = ReaderFile.readerJson("addPostage.json")
        self.addSpecTemplateParam = ReaderFile.readerJson("addSpecTemplate.json")
        self.addGoodsParam = ReaderFile.readerJson("addGoods.json")
        #新增商品，保存
        timeNow = self.mytime.getCurrTimeStamp()
        random = self.myrandom.getRandomStr(3)
        self.addSpecTemplateParam["template_name"] = "新规格" + str(timeNow) + str(random)
        addGoodsRes = self.goods.addGoods(self.addPostageParam, self.addSpecTemplateParam, self.addGoodsParam)
        self.spuId = addGoodsRes.json()["data"]["spu_id"]
        self.logger.info("addGoodRes: {0}".format(addGoodsRes.json()))
        with allure.step(f"新增 spu: {self.spuId} 名称: {self.addGoodsParam['spu_name']} 的商品"):
            assert addGoodsRes.json()["data"]["spu_id"] is not None
        self.publishGoodsParam = addGoodsRes.json()["data"]
        # 查询新增的规格模板
        time.sleep(1)
        params = {"tag_id":"","start_time":"","end_time":"","page":1,"size":10,"template_name":self.addSpecTemplateParam["template_name"]}
        res = self.specTemplate.listSpecTemplate(params)
        self.oldSpecTemplateId = res["data"]["list"][0]["id"]
        # print("8888888：        ",self.oldpostageID)
        # 发布上面新增的商品
        publishRes = self.goods.publishGoods(self.publishGoodsParam)
        self.logger.info("publishRes: {0}".format(publishRes.json()))
        # print("addGoodRes: {0}".format(publishRes.json()))
        with allure.step(f"发布商品： {self.addGoodsParam['spu_name']} "):
            assert publishRes.json()["data"]["spu_id"] is not None


        # 新增一个用于修改的规格模板
        # time.sleep(1)
        timeNow = self.mytime.getCurrTimeStamp()
        random = self.myrandom.getRandomStr(3)
        self.addSpecTemplateParam["template_name"] = "新规格1" + str(timeNow) + str(random)
        res = self.specTemplate.addSpecTemplate(self.addSpecTemplateParam)  # 调接口创建邮费模板
        print('########:{0}'.format(res))
        addSpecTemplateID=res['data']['id']
        self.logger.info("add SpecTemplate res: {0}".format(res))
        with allure.step(f"新增修改的规格模板：{self.addSpecTemplateParam['template_name']}"):
            assert res["code"] == 200 and res["message"] == "success"
        # 查询新增的规格模板
        params = {"tag_id":"","start_time":"","end_time":"","page":1,"size":10,"attribute_template_id":addSpecTemplateID}
        res = self.specTemplate.listSpecTemplate(params)
        self.logger.info("Query specTemplate info {0}".format(res))
        with allure.step(f"通过模板ID：{addSpecTemplateID} 查询：{self.addSpecTemplateParam['template_name']}"):
            assert res["data"]["list"][0]["template_name"] == self.addSpecTemplateParam["template_name"]
        self.newSpecTemplateId = res["data"]["list"][0]["id"]
        print("99999999:     ",self.newSpecTemplateId)

        yield self.publishGoodsParam,self.spuId,self.newSpecTemplateId,self.oldSpecTemplateId

        # 删除新建商品时新增的规格模板
        delParam = {"attribute_template_id": self.oldSpecTemplateId}
        delRes = self.specTemplate.deleteSpecTemplate(delParam)
        self.logger.info("delRes {0}".format(delRes.json()))
        print("delRes {0}".format(delRes.json()))
        with allure.step(f"通过模板ID :{self.oldSpecTemplateId} 删除旧的规格模板"):
            assert delRes.status_code == 200 and delRes.json()["message"] == "success"

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

    @allure.story('已有商品修改spu级别规格模板')
    @pytest.mark.smoke
    def test_goods_publishGoods(self, ini):
        # 修改spu规格模板
        spuId = self.publishGoodsParam
        param = {"attribute_template_id": self.newSpecTemplateId}
        updateGoodRes = self.goods.updateGoods(spuId,param).json()
        self.logger.info("updateGoodRes: {0}".format(updateGoodRes))
        print("updateGoodRes: {0}".format(updateGoodRes))
        with allure.step(f"修改规格模板后的商品spu为: {spuId['spu_id']} "):
            assert updateGoodRes["code"] == 200 and updateGoodRes["message"] == "success" and updateGoodRes["data"]["spu_id"] == spuId["spu_id"]
        # 查看详情中spu级别规格
        res = self.goods.queryGoodsDetail(spuId).json()
        self.logger.info("detailGoodRes: {0}".format(res))
        print("detailGoodRes%%%%%%%%%%%%%%%%%%%%%: {0}".format(res))
        SpecTemplate = res["data"]["list"][0]["attribute_template_id"]
        with allure.step(f"修改后的规格模板为: {SpecTemplate} "):
            assert int(SpecTemplate) == self.newSpecTemplateId

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


