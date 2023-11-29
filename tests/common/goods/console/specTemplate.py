from tests.login.httpclient import HttpClient
from tests.login.singletonHttpClient import SingletonHttpClient
from utils.readerIniFile import ReaderIniFile
from log.log import Logger
from utils.readerFile import ReaderFile
from utils.myTime import Mytime





class SpecTemplate(object):
    """
        模板规格的增、删、改、查
    """
    def __init__(self):
        """
            实例化日志对象和http请求对象,从配置文件中获取请求接口的域名；
        """
        # self.httpclient = HttpClient()
        self.httpclient = SingletonHttpClient.get_instance()
        self.logger = Logger.Logger()
        self.shopUrl = ReaderIniFile.value(key="shopBaseUrl")
        self.consoleUrl = ReaderIniFile.value(section="console_sys_info", key="consoleBaseUrl")

    def addSpecTemplate(self, param):
        """
        增加规格模板
        :param param: 规格模板参数;
        :return: 增加成功返回的信息
        """
        url = "{0}/gw-console/v1/attribute/template-add".format(self.consoleUrl)
        res = self.httpclient.Post(url=url, json=param)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception('call add specification template interface fail !', res.text)

    def deleteSpecTemplate(self, param):
        """  如果规格模板关联商品，存在删除失败的情况，为了提高代码复用率，此处不对状态码进行判断
        :param param: {"attribute_template_id":139159843859072}
        :return:
        """
        url = "{0}/gw-console/v1/attribute/template-delete".format(self.consoleUrl)
        res = self.httpclient.Post(url=url, json=param)
        return res
        # if res.status_code == 200:
        #     return res.json()
        # else:
        #     raise Exception('call delete specification template interface fail !', res.text)

    def listSpecTemplate(self, param):
        """
        查询规格模板
        :param param: {"tag_id": "", "start_time": startTime, "end_time": endTime, "page": 1, "size": 10}
        :return:
        """
        self.logger.info("listSpecTemplate param: {0}".format(param))
        url = "{0}/gw-console/v1/attribute/template-list".format(self.consoleUrl)
        res = self.httpclient.Post(url=url, json=param)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception('call list specification template fail !', res.text)


    def updateSpecTemplate(self,param):
        """
        修改规格模板
        :param param:
        :return:
        """
        # 查询需要修改的规格模板
        templateName = param["template_name"]
        listParam = {"tag_id":"","start_time":"","end_time":"","page":1,"size":10,"template_name":templateName}
        listRes = self.listSpecTemplate(listParam)
        targetData = listRes["data"]["list"][0]
        self.logger.info("targetData: {0}".format(targetData))
        if templateName == targetData["template_name"]:
            templateId = targetData["id"]
            tagID = targetData["tag_id"]
            self.logger.info("Template id: ".format(templateId))
            # 根据规格模板ID,获取规格模板的详细信息
            listDetailParam = {"attribute_template_id": templateId}
            detailUrl = "{0}/gw-console/v1/attribute/template-detail".format(self.consoleUrl)
            res = self.httpclient.Post(url=detailUrl, json=listDetailParam)
            if res.status_code == 200:
                self.logger.info("detail res: {0}".format(res.json()))
                attributeItems = res.json()["data"]["attributes"]
                for index in range(len(attributeItems)):
                    param["attributes"][index]["goods_attribute_id"] = attributeItems[index]["id"]
                param["attribute_template_id"] = templateId
                param["tag_id"] = tagID
                param["template_name"] = param["template_name"]+Mytime.getCurrTime()
            else:
                raise Exception('call specification template detail fail !', res.text)

            updateDetail = "{0}/gw-console/v1/attribute/template-update".format(self.consoleUrl)
            res = self.httpclient.Post(url=updateDetail, json=param)
            return res.json()
        else:
            raise Exception("params template_name is error,please check param.!")


    def copySpecTemplate(self,param):
        """
        移动（便签）
        :param param:
        :return:
        """
        url = "{0}/gw-console/v1/attribute/template-move".format(self.consoleUrl)
        res = self.httpclient.Post(url=url, json=param)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception('call list specification template fail !', res.text)

    def listDetailSpecTemplate(self,param):
        """
        查询规格模板详细信息
        :param param:
        :return:
        """
        url = "{0}/gw-console/v1/attribute/template-detail".format(self.consoleUrl)
        res = self.httpclient.Post(url=url, json=param)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception('call list specification template fail !', res.text)

    def itemUseStatus(self,param):
        """
        查询规格模板详细信息
        :param param:
        :return:
        """
        url = "{0}/gw-console/v1/attribute/item-use-status".format(self.consoleUrl)
        res = self.httpclient.Post(url=url, json=param)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception('call item-use-status fail !', res.text)


if __name__ == '__main__':
    # 批量删除规格模板
    specTemplate = SpecTemplate()
    listParam = {"tag_id": "", "start_time": "", "end_time": "", "page": 1, "size": 10000}
    # listRes = specTemplate.listSpecTemplate(listParam)
    listRes = specTemplate.listSpecTemplate(listParam)
    for specTemplateId in listRes["data"]["list"]:
        delSpecParam = {"attribute_template_id": specTemplateId["id"]}
        Logger.Logger().info("specTemplateId: {0}".format(specTemplateId["id"]))
        delRes = specTemplate.deleteSpecTemplate(delSpecParam)