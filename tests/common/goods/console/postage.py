from tests.login.httpclient import HttpClient
from tests.login.singletonHttpClient import SingletonHttpClient
from utils.readerIniFile import ReaderIniFile
from log.log import Logger
from utils.myTime import Mytime
from utils.readerFile import ReaderFile


class Postage(object):
    """
        邮费模板的增、删、改、查
    """

    def __init__(self):
        """
            实例化日志对象和http请求对象,从配置文件中获取请求接口的域名；
        """
        self.logger = Logger.Logger()
        # self.httpclient = HttpClient()
        self.httpclient = SingletonHttpClient.get_instance()
        # self.time = Mytime()
        self.shopUrl = ReaderIniFile.value(key="shopBaseUrl")
        self.consoleUrl = ReaderIniFile.value(section="console_sys_info", key="consoleBaseUrl")

    def addPostage(self, param):
        """
        新增邮费模板
        :param param: 邮费模板参数;
        :return: 增加成功返回的信息
        """
        url = "{0}/gw-console/v1/postage/add".format(self.consoleUrl)
        res = self.httpclient.Post(url=url, json=param)
        if res.status_code == 200:
            # print("*****************")
            return res
        else:
            raise Exception('call add postage interface fail !', res.text)

    def delete_postage(self,param):
        """
        删除邮费模板
        如果规格模板关联商品，存在删除失败的情况，为了提高代码复用率，此处不对状态码进行判断
        :param param:
        :return:
        """
        url = "{0}/gw-console/v1/postage/delete".format(self.consoleUrl)
        res = self.httpclient.Post(url=url,json=param)
        return res
        # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        # print(res.json())
        # if res.status_code == 200:
        #     return res.json()
        # else:
        #     # return res.text
        #     raise Exception('delete postage fail !', res.text)

    def query_postage(self,param):
        """
        查询邮费模板列表
        :param param: {"page":1,"size":10,"start_time":"","end_time":"","time_type":1,"name":""}
        :return:
        """
        url = "{0}/gw-console/v1/postage/list".format(self.consoleUrl)
        res = self.httpclient.Post(url=url,json=param)
        # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        # print(res.json())
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception('call query postage list fail !', res.text)

    def edit_postage(self, param):
        """
        编辑/修改邮费模板
        :param param:
        :return:
        """
        url = "{0}/gw-console/v1/postage/edit".format(self.consoleUrl)
        res = self.httpclient.Post(url=url, json=param) # 修改邮费模板
        # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        # print(res.json())

        if res.status_code == 200:
            # print("66666666666")
            url = "{0}/gw-console/v1/postage/detail".format(self.consoleUrl)
            detailparam = {"postage_id": param["postage_id"]}
            # print(param)
            # 查询修改后的邮费模板详情，如果名称与修改的名称一致，则说明修改成功
            res = self.httpclient.Post(url=url, json=detailparam)
            if res.status_code == 200:
                assert res.json()["data"]["name"] == param["name"]
                return res.json()
            else:
                raise Exception("check_postage_detal fail",res.text)
        else:
            raise Exception('edit_postage_fail !', res.text)

    def wx_area_list(self,param):
        """
        查询微信地址接口
        :param param:
        :return:
        """
        url = "{0}/gw-console/v1/wx-area/list".format(self.consoleUrl)
        res = self.httpclient.Post(url=url,json=param)
        # print(res.json())
        if res.status_code == 200:
            return res
        else:
            raise Exception('query wx_area_list  fail !', res.text)

    def check_detial_postage(self,param):
        """
        查看邮费模板详情接口
        :param param:
        :return:
        """
        url = "{0}/gw-console/v1/postage/detail".format(self.consoleUrl)
        res = self.httpclient.Post(url=url,json=param)
        # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        # print(res.json())
        if res.status_code == 200:
            return res
        else:
            raise Exception('check_postage_fail !', res.text)

    def relationSkuList(self, param):
        """
        param:   {
    "postage_id": 141340512534656,
    "search_type": 0,
    "source_id": 0,
    "page": 1,
    "size": 10
}
        """
        url = "{0}/gw-console/v1/postage/relation-sku-list".format(self.consoleUrl)
        res = self.httpclient.Post(url=url, json=param)
        if res.status_code == 200:
            return res
        else:
            raise Exception('get relationSkuList interface fail !', res.text)



if __name__ == '__main__':
    #批量删除未关联商品的邮费模板

    param = {"page":1,"size":10000,"start_time":"","end_time":"","time_type":1}
    res = Postage().query_postage(param)
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    # print(res["data"]["list"])
    for i in res["data"]["list"]:
        print(i["id"])
        param = {"postage_id": i["id"]}
        print(param)
        res = Postage().delete_postage(param)



    # params = {"need_region":3,"level":1,"area_ids":[]}
    # print(Postage().wx_area_list(params))

    # params = {"name":"彤彤8","type":[1],"weight":0,"settlement_type":1,"delivery_region":2,"rule_list":[{"code_list":[35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50],"base_fee":0,"free_shipping_fee":0,"free_shipping_num":0}]}
    # print(Postage().addPostage(params))

    # params = {}
    # print(Postage().query_postage(params))
    # print("#############################################")

    # params = {"postage_id": 118840238947008}
    # print(Postage().delete_postage(params)["code"])

    # params = {"postage_id": 139366850586432}
    #
    # print(Postage().check_detial_postage(params))
    # print("&&&&&&&&&&&&&&&&&&&&&&&&")

    # params = {"name":"修改ya","type":[1,2,3,4],"settlement_type":2,"delivery_region":1,
    #           "rule_list":[{"code_list":[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136],"base_fee":0,"free_shipping_fee":0,"free_shipping_num":0,"id":139378732158592}],
    #           "postage_id":140089924148352}
    # print(Postage().edit_postage(params))