from tests.common.goods.console.specTemplate import SpecTemplate
from tests.common.goods.console.postage import Postage
from tests.common.goods.console.goods import Goods
from utils.readerFile import ReaderFile
from utils.myJson import MyJson
from log.log import Logger
import pytest
from utils.myRandom import MyRandom
from utils.myTime import Mytime
import allure
'''
前置条件：
    1.新增规格模板成功
    2.新增的规格模板关联已关联商品
测试步骤：
    1.已关联商品的规格模板不可新增/删除规格(此步骤未实现自动化：因为规格模板关联商品时，无新增规格的按钮，用户无法新增，在实际应用场景中无此场景，故未自动化)
    2.已关联商品的规格模板可任意新增参数
    3.已关联商品的规格模板参数不可删除

'''

@allure.feature('商品')
class Test_goods_updateSpecTemplate_002(object):
    @pytest.fixture()
    def ini(self):
        self.myJson = MyJson()
        self.goods = Goods()
        self.logger = Logger.Logger()
        self.postage = Postage()
        self.specTemplate = SpecTemplate()
        self.addPostageParam = ReaderFile.readerJson("addPostage.json")
        self.addSpecTemplateParam = ReaderFile.readerJson("addSpecTemplate.json")
        self.addGoodsParam = ReaderFile.readerJson("addGoods.json")
        self.delSpecParam = {"attribute_template_id": 123456789}
        yield self.addPostageParam, self.addSpecTemplateParam, self.addGoodsParam, self.delSpecParam, self.myJson, self.postage
        # 删除添加的商品
        delGoods = {"channel_type": 1, "spu_id": self.spuId}
        delRes = self.goods.delSpu(delGoods).json()
        with allure.step(f"通过 spu: {self.spuId} 删除商品 {self.addGoodsParam['spu_name']} "):
            assert delRes["code"] == 200 and delRes["message"] == "success"
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

    @allure.story('已关联商品的规格模板不可删除参数，可新增参数')
    @pytest.mark.smoke
    def test_goods_updateSpecTemplate(self, ini):
        self.addSpecTemplateParam['template_name']='颜色大小模板{0}'.format(MyRandom.getRandomStr(5))
        addGoodsRes = self.goods.addGoods(self.addPostageParam, self.addSpecTemplateParam, self.addGoodsParam)
        self.logger.info("addGoodRes: {0}".format(addGoodsRes.json()))
        print("addGoodRes: {0}".format(addGoodsRes.json()))
        self.spuId = addGoodsRes.json()["data"]["spu_id"]
        with allure.step(f"新增 spu: {self.spuId} 名称: {self.addGoodsParam['spu_name']} 的商品"):
            assert self.spuId is not None
        # 查询商品关联的规格模板
        goodsDetailParam = {"spu_id": self.spuId}
        self.resDetail = self.goods.queryGoodsDetail(goodsDetailParam)
        self.logger.info("resDetail: {0}".format(self.resDetail.json()))
        self.logger.info("resDetail: {0}".format(self.resDetail.json()))
        print("resDetail: {0}".format(self.resDetail.json()))
        self.listData = self.resDetail.json()["data"]["list"][0]
        self.specTemplateId = self.listData["attribute_template_id"]
        with allure.step(f"通过 spu: {self.spuId} 查询商品规格模板 ID {self.specTemplateId}"):
            assert len(self.resDetail.json()["data"]["list"]) > 0
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
        # 获取规格模板详情
        self.specTemplateId = self.resDetail.json()["data"]["list"][0]["attribute_template_id"]
        SpecTemDetailParam = {"attribute_template_id": self.specTemplateId}
        specTemResDeatil = self.specTemplate.listDetailSpecTemplate(SpecTemDetailParam)
        self.logger.info("specTemResDeatil {0}".format(specTemResDeatil))
        print("specTemResDeatil {0}".format(specTemResDeatil))
        # 规格模板中的规格添加属性
        addItemParam = {"template_name":self.addSpecTemplateParam['template_name'],"attribute_template_id":self.specTemplateId,"attributes":[{"attribute_item":["微"],"goods_attribute_id":140439341805696},{"attribute_item":["白"],"goods_attribute_id":140439341821376}],"del_attribute_ids":[],"del_attribute_item_ids":[],"tag_id":140439341770240}
        templateId = self.myJson.value(addItemParam,"id",1)
        itemOneId = self.myJson.value(addItemParam,"id",2)
        itemTwoId = self.myJson.value(addItemParam,"id",6)
        tagId = self.myJson.value(addItemParam,"id",10)
        addItemParam["attribute_template_id"] = templateId
        addItemParam["attributes"][0]["goods_attribute_id"] = itemOneId
        addItemParam["attributes"][1]["goods_attribute_id"] = itemTwoId
        addItemParam["tag_id"] = tagId
        self.specTemplate.updateSpecTemplate(addItemParam)
        # 获取使用中的属性ID
        specItemIdUseOne = self.myJson.value(specTemResDeatil,"id",3)
        # 删除使用中的属性
        itemUseParam = {"attribute_item_id": specItemIdUseOne}
        itemUseRes = self.specTemplate.itemUseStatus(itemUseParam)
        print("status: {0}".format(itemUseRes))
        with allure.step(f"删除规格模板使用中的属性 :{specItemIdUseOne}"):
            assert itemUseRes["data"]["used_count"] > 0
        # 获取未使用的属性ID
        specItemIdOne = self.myJson.value(specTemResDeatil, "id", 4)
        # 删除未使用的属性
        itemUseParam = {"attribute_item_id": specItemIdOne}
        itemUseRes = self.specTemplate.itemUseStatus(itemUseParam)
        print("status: {0}".format(itemUseRes))
        with allure.step(f"删除规格模板未使用的属性 :{specItemIdOne}"):
            assert itemUseRes["data"]["used_count"] == 0











