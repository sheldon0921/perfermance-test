# coding=utf-8
import os
from tests.login.httpclient import HttpClient
from tests.login.singletonHttpClient import SingletonHttpClient
from utils.readerIniFile import ReaderIniFile
from log.log import Logger
from utils.readerFile import ReaderFile
from tests.common.goods.console.specTemplate import SpecTemplate
from tests.common.goods.console.postage import Postage
from utils.myTime import Mytime
from utils.myJson import MyJson
from utils.myRandom import MyRandom


class Goods(object):

    def __init__(self):
        """
            实例化日志对象和http请求对象,从配置文件中获取请求接口的域名；
        """
        self.mytime = Mytime()
        self.logger = Logger.Logger()
        # self.httpclient = HttpClient()
        self.httpclient = SingletonHttpClient.get_instance()
        # self.consoleUrl = ReaderConfig.value(section="console_sys_info", key="consoleBaseUrl")
        # self.logger.info("url is: {0} ".format(self.consoleUrl))
        self.specTemplate = SpecTemplate()
        self.postage = Postage()
        self.shopUrl = ReaderIniFile.value(key="shopBaseUrl")
        self.consoleUrl = ReaderIniFile.value(section="console_sys_info", key="consoleBaseUrl")

    def queryGoods(self, param):
        """
        查询商品接口(小程序端查询）
        :param param: 请求接口参数;
        :return: 商品详情接口返回的数据
        """
        url = "{0}/gw-shop/app/v1/goods/detail".format(self.shopUrl)
        res = self.httpclient.Post(url=url, json=param)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception('call query goods interface fail !', res.text)

    def addGoods(self, postageParam, specTemplateParam, goodsParam):
        """
        新增商品接口
        :param postageParam: 邮费模板参数
        :param specTemplateParam: 规格模板参数
        :param goodsParam: 商品信息参数
        :return:
        """

        # 增加规格模板
        if specTemplateParam != "":
            res = self.specTemplate.addSpecTemplate(specTemplateParam)
            self.logger.info("add specification template res: {0}".format(res))
            addRes = res["data"]
            # print("addRes: {0}".format(addRes))
            specTemplateId = addRes["id"]
            assert specTemplateParam["template_name"] == addRes["template_name"] and addRes["id"] is not None
            # 查询规格模板详细信息
            listDetailParam = {"attribute_template_id": specTemplateId}
            listDetailRes = self.specTemplate.listDetailSpecTemplate(listDetailParam)
            self.logger.info("add specTemplate res: {0}".format(listDetailRes))
            print("add specTemplate res: {0}".format(listDetailRes))
            assert "success" == listDetailRes["message"]

            # 将规格模板参数拼接到商品信息中
            goodsParam["attribute_template_id"] = specTemplateId
            goodsParam["attr_selected_id"] = specTemplateId
            useOneSpecTemplate = [MyJson().value(listDetailRes["data"], "id", 3),
                                  MyJson().value(listDetailRes["data"], "id", 7)]
            goodsParam["sku"][0]["attribute_item_ids"] = useOneSpecTemplate
            # 商品为多SKU商品时，需要为第二个sku设置规格
            if len(goodsParam["sku"]) > 1:
                useTwoSpecTemplate = [MyJson().value(listDetailRes["data"], "id", 4),
                                      MyJson().value(listDetailRes["data"], "id", 8)]
                goodsParam["sku"][1]["attribute_item_ids"] = useTwoSpecTemplate

        # 增加邮费模板
        if postageParam != "":
            postageName = postageParam["name"] + MyRandom.getRandomStr(5)
            postageParam["name"] = postageName
            res = self.postage.addPostage(postageParam)
            self.logger.info("add postage template res: {0}".format(res.json()))
            assert res.status_code == 200 and "success" in res.text
            # 查询邮费模板
            listParam = {"page": 1, "size": 10, "start_time": "", "end_time": "", "time_type": 1, "name": postageName}
            listRes = self.postage.query_postage(listParam)
            self.logger.info("list data length: {0}, data contents {1}".format(len(listRes["data"]["list"]), listRes))
            assert len(listRes["data"]["list"]) > 0
            postageId = listRes["data"]["list"][0]["id"]
            self.logger.info("list data length: {0}, data contents {1}".format(len(listRes["data"]["list"]), listRes))
            # print("list data length: {0}, data contents {1}".format(len(listRes["data"]["list"]), listRes))
            # 将邮费模板参数拼接到商品信息中
            goodsParam["postage"][0]["postage_id"] = postageId
            # 多SKU商品，第二个SKU的物流信息是单独维护的，需要在创建一个邮费模板
            if len(goodsParam["sku"]) > 1:
                goodsParam["sku"][0]["postage"][0]["postage_id"] = postageId
                postageParam["name"] = "邮费2" + MyRandom.getRandomStr(5)
                self.postage.addPostage(postageParam)
                listParam = {"page": 1, "size": 10, "start_time": "", "end_time": "", "time_type": 1, "name": postageParam["name"]}
                listRes = self.postage.query_postage(listParam)
                assert len(listRes["data"]["list"]) > 0
                twoPostageId = listRes["data"]["list"][0]["id"]
                goodsParam["sku"][1]["postage"][0]["postage_id"] = twoPostageId

        currentTime = Mytime.getCurrTime()
        goodsParam["spu_name"] = goodsParam["spu_name"] + currentTime + MyRandom.getRandomStr(4)
        self.logger.info("addGoodsParam: {0}".format(goodsParam))

        url = "{0}/gw-console/v1/goods/save".format(self.consoleUrl)
        res = self.httpclient.Post(url=url, json=goodsParam)
        if res.status_code == 200:
            return res
        else:
            raise Exception('add goods interface fail !', res.text)


    def queryGoodsDetail(self,GoodsDetailParam):
        """
        商品详情接口
        :param {"spu_id": 140447434460032}
        :return:
        """

        url = "{0}/gw-console/v1/goods/detail".format(self.consoleUrl)
        res = self.httpclient.Post(url=url, json=GoodsDetailParam)
        if res.status_code == 200:
            return res
        else:
            raise Exception('query goods detail interface fail !', res.text)

    def delSpu(self, delGoodsParam):
        """
        删除商品 删除Spu
        :param param: {"channel_type":1,"spu_id":140445384103424}
        :return:
        """
        url = "{0}/gw-console/v1/goods/delete-spu".format(self.consoleUrl)
        res = self.httpclient.Post(url=url, json=delGoodsParam)
        if res.status_code == 200:
            return res
        else:
            raise Exception('delete spu interface fail !', res.text)

    def delSku(self, delSkuParam):
        """
        删除商品 删除Spu
        :param param: {"channel_type":1,"sku_ids":[140445384103424]}
        :return:
        """
        url = "{0}/gw-console/v1/goods/delete-sku".format(self.consoleUrl)
        res = self.httpclient.Post(url=url, json=delSkuParam)
        if res.status_code == 200:
            return res
        else:
            raise Exception('delete sku interface fail !', res.text)

    def listSpu(self,noPublishGoodsParam):
        """
               查询 未发布/复制的spu列表/spu全部列表
               :param param:{
                   "page": 1, #分页  （必填）
                   "size": 10, #分页大小  （必填）
                   "searchParams":  # （非必填）
                   {
               "searchChannel": 0,"searchChannelOwnership": 0,
               "searchString": {"keyword": "哈哈","type": 1   #	关键字搜索类型（1：商品名称，2：物料编码，4：spuId）  },
               "searchInt": {"high": 0,"low": 0,"type": 1},
               "searchNeedDelete": 2,
               "searchTime": {"beginTimestamp": 0,"endTimestamp": 0,"type": 1},
               "searchGoodsStatus": -1,  #商品状态（-1: 全部, 0：未上架，1：已上架，2：已删除）
               "searchReleaseStatus": 1,  #发布状态（0：未发布，1：已发布）
               "searchSort": {"sortColumn": 0,"sortType": 0}
                   }
               }
               :return: 查询列表
               """
        url = "{0}/gw-console/v1/goods/spu-draft-list".format(self.consoleUrl)
        res = self.httpclient.Post(url=url, json=noPublishGoodsParam)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception('delete sku interface fail !', res.text)

    def publishGoods(self, param):
        """
        发布商品
        :param param: {"spu_id":140407820538688}
        :return:
        """
        # 查看商品详情，拿取detail接口返回参数
        url = "{0}/gw-console/v1/goods/detail".format(self.consoleUrl)
        detailRes = self.httpclient.Post(url=url, json=param)
        self.logger.info("detailRes: {0}".format(detailRes.json()))
        if detailRes.status_code == 200:
            detailRes = detailRes.json()
            # print("=========", detailRes)
            # 查看详情成功，删除未选中的postage（is_open = false)
            try:
                index_postage = []
                # index_sku = []
                list1 = detailRes.get("data").get("list")
                # print("***:    ",list1)
                for i in range(0, len(list1)):
                    for j in range(len(list1[i].get("postage"))):
                        if list1[i]["postage"][j].get("is_open") == False:
                            index_postage.append(j)
                    if len(index_postage) != 0:
                        for m in range(len(index_postage)-1, -1, -1):
                            del list1[i]["postage"][m]
                    for j in range(len(list1[i].get("sku"))):
                        # print("%%%:   ",list1[i]["sku"][j].get("postage"))
                        index_sku = []
                        for k in range(len(list1[i]["sku"][j].get("postage"))):
                            if list1[i]["sku"][j]["postage"][k].get("is_open") == False:
                                index_sku.append(k)
                        if len(index_postage) != 0:
                            for m in range(len(index_sku)-1, -1, -1):
                                del list1[i]["sku"][j]["postage"][m]
                # print("+++++++++++++++", detailRes)
                self.logger.info("detailRes: {0}".format(detailRes.json()))
            except Exception as e:
                print(e)
            #拼接发布所需的其他参数
            publishParams = detailRes["data"]["list"][0]
            publishParams['spu_id'] = publishParams.pop("id")
            publishParams['backend_category_id'] = 102103103
            publishParams["is_release"] = 1  # is_release  0-未发布， 1-已发布
            publishParams.update({"type": 1, "depreciation": 0, "channel_type": 1})
            # print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            # print(publishParams)
            self.logger.info(" publishParams: {0}".format(publishParams))
            # 参数拼接完成，发布商品
            url = "{0}/gw-console/v1/goods/save".format(self.consoleUrl)
            publishRes = self.httpclient.Post(url=url, json=publishParams)
            self.logger.info("publishRes: {0}".format(publishRes))
            # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            # print(publishRes.json())
            if publishRes.status_code == 200 and publishRes.json()["message"] == "success":
                return publishRes
            else:
                raise Exception('call publish goods interface fail !', publishRes.text)
        else:
            raise Exception('call detial goods interface fail !', detailRes.text)

    def queryGoodsList(self,param):
        """
        查询待上架商品列表
        :param param: {
	"searchType": 3,  #1 全部 2 普通商品 3 活动商品 4 待上架商品 5 已失效商品 （必填）
	"searchParams": {
		"searchString": {
			"keyword": "",
			"type": 1   #1 商品名称 2 商品唯一编码 3 SKU ID 4 SPU ID
		},
		"searchInt": {
			"high": 0,
			"low": 0,
			"type": 1  #1 库存 2 销量 3 价格
		},
		"searchChannel": 0,
		"searchTime": {
			"beginTimestamp": 0,
			"endTimestamp": 0,
			"type": 1  # 1 创建时间 2 修改时间
		},
		"searchGoodsStatus": 0,
		"searchChannelOwnership": 0,
		"searchSort": {
			"sortColumn": 0,   #排序字段：1 价格 2 库存 3 销量 4 创建时间 5 修改时间
			"sortType": 0  #排序规则 ： 1 正序 2 倒序
		}
	},
	"page": 1,
	"size": 10
}
        :return:
        """
        url = "{0}/gw-console/v1/goods/goods-list".format(self.consoleUrl)
        res = self.httpclient.Post(url=url, json=param)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception('query goods list interface fail !', res.text)

    def saleGoods(self,param):
        """
        上架商品
        :param param: {”spu_id":[],"sku_id":[]}
        :return:
        """
        saleParams = {"data": [], "source_id": 133719584357376, "status": 2}
        if len(param["spu_id"]) == 0:
            # saleParams = {"data": [],"source_id": 133,"status": 2}
            skuParam = {}
            for i in param["sku_id"]:
                url = "{0}/gw-console/v1/goods/goods-list".format(self.consoleUrl)
                goodslistParam = {"searchType": 1,"searchParams": {"searchString": {"keyword": "140585154393088","type": 3}}}
                goodslistParam["searchParams"]["searchString"]["keyword"] = str(i)
                # print("goodslistParam:  ",goodslistParam)
                goodslistRes = self.httpclient.Post(url=url,json=goodslistParam).json()
                skuParam["source_id"] = goodslistRes["data"]["list"][0]["source_id"]
                skuParam["material_channel_id"] = goodslistRes["data"]["list"][0]["material_id"]
                skuParam["sku_id"] = i
                saleParams["data"].append(skuParam)
            saleParams["source_id"] = saleParams["data"][0]["source_id"]
        else:
            # saleParams = {"data": [], "source_id": 133, "status": 2}
            skuParam = {}
            for i in param["spu_id"]:
                print("i:    ",i)
                url = "{0}/gw-console/v1/goods/spu-draft-list".format(self.consoleUrl)
                spulistParam = {"searchParams": {"searchString": {"keyword": "","type": 4},"searchReleaseStatus": 1}}
                spulistParam["searchParams"]["searchString"]["keyword"] = str(i)
                print("spulistParam:    ", spulistParam)
                spulistRes = self.httpclient.Post(url=url,json=spulistParam).json()
                # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
                # print(spulistRes)
                skuParam["spu_id"] = i
                skuParam["source_id"] = spulistRes["data"]["list"][0]["source_id"]
                saleParams["data"].append(skuParam)
                # print("***********")
                # print(saleParams)
            saleParams["source_id"] = saleParams["data"][0]["source_id"]
            # print(saleParams)
        url = "{0}/gw-console/v1/goods/sale".format(self.consoleUrl)
        saleRes = self.httpclient.Post(url=url, json=saleParams)
        if saleRes.status_code == 200:
            return saleRes.json()
        else:
            raise Exception('onsale goods list interface fail !', saleRes.text)

    def offsaleGoods(self,param):
        """
        下架商品
        :param param: {”spu_id":[],"sku_id":[]}
        :return:
        """
        saleParams = {"data": [], "source_id": 133719584357376, "status": 1}
        if len(param["spu_id"]) == 0:
            # saleParams = {"data": [],"source_id": 133,"status": 2}
            skuParam = {}
            for i in param["sku_id"]:
                url = "{0}/gw-console/v1/goods/goods-list".format(self.consoleUrl)
                goodslistParam = {"searchType": 1,"searchParams": {"searchString": {"keyword": "140585154393088","type": 3}}}
                goodslistParam["searchParams"]["searchString"]["keyword"] = str(i)
                # print("goodslistParam:  ",goodslistParam)
                goodslistRes = self.httpclient.Post(url=url,json=goodslistParam).json()
                self.logger.info("goodslistRes: {0}".format( goodslistRes))
                skuParam["source_id"] = goodslistRes["data"]["list"][0]["source_id"]
                skuParam["material_channel_id"] = goodslistRes["data"]["list"][0]["material_id"]
                skuParam["sku_id"] = i
                saleParams["data"].append(skuParam)
                self.logger.info("saleParams: {0}".format(saleParams))
            saleParams["source_id"] = saleParams["data"][0]["source_id"]
        else:
            # saleParams = {"data": [], "source_id": 133, "status": 2}
            skuParam = {}
            for i in param["spu_id"]:
                print("i:    ",i)
                url = "{0}/gw-console/v1/goods/spu-draft-list".format(self.consoleUrl)
                spulistParam = {"searchParams": {"searchString": {"keyword": "","type": 4},"searchReleaseStatus": 1}}
                spulistParam["searchParams"]["searchString"]["keyword"] = str(i)
                print("spulistParam:    ", spulistParam)
                spulistRes = self.httpclient.Post(url=url,json=spulistParam).json()
                self.logger.info("spulistRes: {0}".format(spulistRes))
                # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
                # print(spulistRes)
                skuParam["spu_id"] = i
                skuParam["source_id"] = spulistRes["data"]["list"][0]["source_id"]
                saleParams["data"].append(skuParam)
                # print("***********")
                # print(saleParams)
            saleParams["source_id"] = saleParams["data"][0]["source_id"]
            # print(saleParams)
        self.logger.info("saleParams: {0}".format(saleParams))
        url = "{0}/gw-console/v1/goods/sale".format(self.consoleUrl)
        saleRes = self.httpclient.Post(url=url, json=saleParams)

        if saleRes.status_code == 200:
            return saleRes.json()
        else:
            raise Exception('onsale goods list interface fail !', saleRes.text)

    def copyGoods(self,param):
        """
            复制指定商品的商品详情
            :param param: {"spu_id":141502540823424} (复制spu级别商品）
            /
            {spu_id: 141502540823424, sku_id: 141502540885504}（复制sku级别商品）
            :return: 返回可做为保存接口入参格式的详情数据
            """
        url = "{0}/gw-console/v1/goods/get-delete-goods-detail".format(self.consoleUrl)
        res = self.httpclient.Post(url=url, json=param)
        self.logger.info("res: {0}".format(res))
        if res.status_code == 200:
            # return res.json()["data"]
            detailRes = res.json()["data"]
            detailRes['backend_category_id'] = 102103103
            try:
                index_postage = []
                # if detailRes["postage"][j].get("is_open") == False:
                #     index_postage.append(j)
                for i in range(len(detailRes.get("postage"))):
                    if detailRes.get("postage")[i].get("is_open") == False:
                        index_postage.append(i)
                if len(index_postage) != 0:
                    for m in range(len(index_postage) - 1, -1, -1):
                        del detailRes["postage"][m]


                for j in range(len(detailRes.get("sku"))):
                    # print("%%%:   ",list1[i]["sku"][j].get("postage"))
                    index_sku = []
                    for k in range(len(detailRes["sku"][j].get("postage"))):
                        if detailRes["sku"][j]["postage"][k].get("is_open") == False:
                            index_sku.append(k)
                    if len(index_postage) != 0:
                        for m in range(len(index_sku) - 1, -1, -1):
                            del detailRes["sku"][j]["postage"][m]
                self.logger.info("res: {0}".format(res))
                # print("+++++++++++++++", detailRes)
            except Exception as e:
                print(e)
            return detailRes
        else:
            raise Exception('delete sku interface fail !', res.text)

    def saveGoods(self,param):
        url = "{0}/gw-console/v1/goods/save".format(self.consoleUrl)
        res = self.httpclient.Post(url=url, json=param)
        if res.status_code == 200:
            return res
        else:
            raise Exception('save spu interface fail !', res.text)

    def updateGoods(self,spuId,param):
        """
        编辑商品信息
        spuID : {“spu_id":12456435677}
        param : {} 传入需要修改的参数键值对（必须是最外层的键值对）
        """
        url = "{0}/gw-console/v1/goods/detail".format(self.consoleUrl)
        detailRes = self.httpclient.Post(url=url, json=spuId)
        self.logger.info("detailRes: {0}".format(detailRes))
        if detailRes.status_code == 200:
            detailRes = detailRes.json()
            # print("=========", detailRes)
            # 查看详情成功，删除未选中的postage（is_open = false)
            try:
                index_postage = []
                # index_sku = []
                list1 = detailRes.get("data").get("list")
                # print("***:    ",list1)
                for i in range(0, len(list1)):
                    for j in range(len(list1[i].get("postage"))):
                        if list1[i]["postage"][j].get("is_open") == False:
                            index_postage.append(j)
                    if len(index_postage) != 0:
                        for m in range(len(index_postage) - 1, -1, -1):
                            del list1[i]["postage"][m]

                    for j in range(len(list1[i].get("sku"))):
                        # print("%%%:   ",list1[i]["sku"][j].get("postage"))
                        index_sku = []
                        for k in range(len(list1[i]["sku"][j].get("postage"))):
                            if list1[i]["sku"][j]["postage"][k].get("is_open") == False:
                                index_sku.append(k)
                        if len(index_postage) != 0:
                            for m in range(len(index_sku) - 1, -1, -1):
                                del list1[i]["sku"][j]["postage"][m]
                # print("+++++++++++++++", detailRes)
            except Exception as e:
                print(e)
            # 拼接save入参格式
            publishParams = detailRes["data"]["list"][0]
            # publishParams['spu_name'] = "阿西吧"
            publishParams['spu_id'] = publishParams.pop("id")
            # publishParams["is_release"] = 1  # is_release  0-未发布， 1-已发布
            publishParams.update({"type": 1, "depreciation": 0, "channel_type": 1})
            publishParams['backend_category_id'] = 102103103
            self.logger.info("publishParams: {0}".format(publishParams))
            # print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            # print(publishParams)
            # 替换需要修改的参数
            for i in param:
                for j in publishParams:
                    if i == j:
                        publishParams[j] = param[i]
            self.logger.info("publishParams: {0}".format(publishParams))
            # 使用save接口保存修改
            url = "{0}/gw-console/v1/goods/save".format(self.consoleUrl)
            res = self.httpclient.Post(url=url, json=publishParams)
            if res.status_code == 200:
                return res
            else:
                raise Exception('save spu interface fail !', res.text)
        else:
            raise Exception('call detial goods interface fail !', detailRes.text)

    def beforeOperation(self, dict=None):
        """
        商品下架操作：集成商品下架步骤及商品下架步骤之后的所有步骤
        :return: {'spuID': , 'goodsName': '', 'SpecTemplateID': '', 'postageID': [], 'skuID': }
        """
        retDict = {}
        addPostageParam = ReaderFile.readerJson("addPostage.json")
        addSpecTemplateParam = ReaderFile.readerJson("addSpecTemplate.json")
        addGoodsParam = ReaderFile.readerJson("addGoods.json")
        addGoodsParam["is_release"] = 1
        if dict != None:
            addGoodsParam['sku'][0]['material_id'] = dict['material_id']
            addGoodsParam['sku'][0]['material_no'] = dict['material_no']

        # 新增并发布商品
        addGoodsRes = self.addGoods(addPostageParam, addSpecTemplateParam, addGoodsParam)
        self.logger.info("addGoodRes: {0}".format(addGoodsRes.json()))
        spuId = addGoodsRes.json()["data"]["spu_id"]
        retDict["spuID"] = spuId
        saleParam = {"spu_id": [], "sku_id": []}
        saleParam["spu_id"].append(spuId)
        # 上架商品
        saleRes = self.saleGoods(saleParam)
        self.logger.info("saleRes: {0}".format(saleRes))
        # 在全部spu列表中查询该数据
        listParam = {"page": 1, "size": 1000, "searchParams": {"searchChannel": 0, "searchChannelOwnership": 0,
                                                               "searchString": {"keyword": str(spuId), "type": 4},
                                                               "searchInt": {"high": 0, "low": 0, "type": 1},
                                                               "searchNeedDelete": 2,
                                                               "searchTime": {"beginTimestamp": 0, "endTimestamp": 0,
                                                                              "type": 1}, "searchGoodsStatus": -1,
                                                               "searchReleaseStatus": 1,
                                                               "searchSort": {"sortColumn": 0, "sortType": 1}}}
        listRes = self.listSpu(listParam)
        self.logger.info("listRes: {0}".format(listRes))
        retDict["goodsName"] = listRes["data"]["list"][0]["spu_name"]
        # 查询商品关联的规格模板
        goodsDetailParam = {"spu_id": spuId}
        resDetail = self.queryGoodsDetail(goodsDetailParam)
        self.logger.info("resDetail: {0}".format(resDetail.json()))
        listData = resDetail.json()["data"]["list"][0]
        retDict["specTemplateID"] = listData["attribute_template_id"]
        # 获取该商品关联的邮费模板
        postageIdList = list()
        if "sku" in listData:
            skuList = listData["sku"]
            for i in range(0, len(skuList)):
                postageId = skuList[i]["postage"][1]["postage_id"]
                postageIdList.append(postageId)
        else:
            postageId = listData["postage"][1]["postage_id"]
            postageIdList.append(postageId)
        retDict["postageID"] = postageIdList
        # 查询商品sku_id
        queryparam = {"searchType": 2, "searchParams": {"searchString": {"keyword": str(spuId), "type": 4},
                                                        "searchInt": {"high": 0, "low": 0, "type": 1},
                                                        "searchChannel": 0,
                                                        "searchTime": {"beginTimestamp": 0, "endTimestamp": 0,
                                                                       "type": 1}, "searchGoodsStatus": 0,
                                                        "searchChannelOwnership": 0,
                                                        "searchSort": {"sortColumn": 0, "sortType": 0}}, "page": 1,
                      "size": 10}
        querygoodslistRes = self.queryGoodsList(queryparam)
        retDict["skuID"] = querygoodslistRes['data']['list'][-1]['sku_id']
        self.logger.info("retDict: {0}".format(str(retDict)))
        return retDict

    def afterOperation(self, params):
        """
        商品下架操作：集成商品下架步骤及商品下架步骤之后的所有步骤
        :param params {'spuID': , 'goodsName': '', 'SpecTemplateID': '', 'postageID': [], 'skuID': }
        :return: Boolean
        """
        #下架商品
        saleParam = {"spu_id": [params["spuID"]], "sku_id": []}
        offsaleRes = self.offsaleGoods(saleParam)
        self.logger.info("osssale goods res ]info {0}".format(offsaleRes))
        # 删除添加的商品
        delGoods = {"channel_type": 1, "spu_id": params["spuID"]}
        delRes = self.delSpu(delGoods).json()
        self.logger.info("del goods res: {0}".format(delRes))
        # 删除规格模板
        delSpecParam = {"attribute_template_id": params["specTemplateID"]}
        delRes = self.specTemplate.deleteSpecTemplate(delSpecParam)
        self.logger.info("del specTemplate res: {0}".format(delRes))
        # 删除邮费模板
        for postageID in params["postageID"]:
            delParam = {"postage_id": postageID}
            delRes = self.postage.delete_postage(delParam)
            self.logger.info("del postage Res {0}".format(delRes.json()))

if __name__ == '__main__':
    param =  {"spu_id": 183266770710272}
    goods = Goods()
    print(goods.publishGoods(param))
