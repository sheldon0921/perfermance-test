from tests.common.onLineForSupermarket.extractList import ExtractList
from tests.login.singletonHttpClient import SingletonHttpClient
from utils.operationExcel import OperationExcel, ExcelVarles
from utils.readerIniFile import ReaderIniFile
from utils.parseJson import ParseJson
from utils.readerFile import ReaderFile
import pytest
import allure
import json


class Test_single_interface(object):
    excel = OperationExcel()
    obj = SingletonHttpClient.get_instance(flag="onLine")
    shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")

    @pytest.mark.singleInterfaceExcel
    @pytest.mark.parametrize('datas', ReaderFile.readerJson("singleInterfaceCombineData.json"))
    def test_single_interface(self, datas):
        enterpriName = datas["enterpriName"]
        enterpriseID = datas["enterpriseID"]
        enterpriseHash = datas["enterpriseHash"]
        province = datas['province']
        city = datas['city']
        # 如果接口不在某些企业跑，则直接结束
        enterpriseLst = datas[ExcelVarles.removeEnterprise]
        if enterpriseLst != "":
            enterpriseLst = eval(enterpriseLst)
            for removeEnterpriName in enterpriseLst:
                if enterpriName == removeEnterpriName:
                    return
        list = ExtractList()
        content = ReaderFile.readerJson("singleInterfaceHeader.json")
        if len(content) != 0 and enterpriseHash == content["Enterprise-Hash"]:
            header = content
        else:
            header = list.getHeader(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        with open(ReaderIniFile.getConfigFilePath("data", "singleInterfaceHeader.json"), 'w',
                  encoding="utf-8") as f:
            f.write(json.dumps(header))

        # for datas in self.excel.runs():
        param = datas[ExcelVarles.params]
        # 对请求参数做 反序列化的处理
        if len(str(param).strip()) == 0:
            pass
        elif len(str(param).strip()) >= 0:
            # param = json.loads(param)
            try:
                param = eval(param)
            except TypeError:
                pass

        # 判断是否使用位置信息，如果使用则将位置信息拼入到参数中
        def isUsePosition(value, p):
            if value == "y":
                p["province"] = province
                p["city"] = city

        isUsePosition(datas[ExcelVarles.isUsePosition], param)
        print(datas)
        # 执行前置条件关联的测试点
        preconditions = datas[ExcelVarles.casePre]
        if preconditions is not None and preconditions != "":
            preItem = self.excel.case_prev(datas[ExcelVarles.casePre])
            preUrl = preItem[ExcelVarles.caseUrl]
            url = self.shopBaseUrl + preUrl
            preParam = preItem[ExcelVarles.params]
            if type(preParam) == dict:
                rp = eval(preParam)
                isUsePosition(preItem[ExcelVarles.isUsePosition], rp)
                r = self.obj.Post(url=url, json=rp, headers=header)
            r = self.obj.Post(url=url, headers=header)
            rJson = r.json()
            print("-!!! {0}接口返回信息：{1}".format(preUrl, rJson))
            # 关联url获取关联字段的值
            relationFileds = datas[ExcelVarles.relationFiled]
            fileds = dict()
            if relationFileds is None or len(relationFileds) == 0:
                pass
            else:
                relationFileds = eval(relationFileds)
                for key, value in relationFileds.items():
                    # fileds[value] = rJson["data"]["list"][0][key]
                    fileds[value] = ParseJson.parseJson(rJson,key)[0]

            # 替换被关联测试点中参数信息的变量
            if len(fileds) != 0:
                if len(param) != 0:
                    for k, v in fileds.items():
                        sourceValue = param[k]
                        if type(sourceValue) == list:
                            param[k] = [v]
                        elif type(sourceValue) ==str:
                            param[k] = v
                else:
                    param = fileds

        # 状态码
        status_code = int(datas[ExcelVarles.statusCode])

        def case_assert_result(r):
            assert r.status_code == status_code
            assert datas[ExcelVarles.expect] in json.dumps(r.json(), ensure_ascii=False)

        def getUrl():
            # return str(datas[ExcelVarles.caseUrl]).replace('{bookID}', readContent())
            return str(datas[ExcelVarles.caseUrl])

        url = self.shopBaseUrl + getUrl()
        if datas[ExcelVarles.method] == 'get':
            if len(param) == 0:
                r = self.obj.GET(url=url, headers=header)
            else:
                r = self.obj.GET(url=url, headers=header, params=param)
            print("-!!! {0}接口返回信息：{1}".format(url, r.json()))
            case_assert_result(r=r)

        elif datas[ExcelVarles.method] == 'post':
            r = self.obj.Post(url=url,
                              json=param, headers=header)
            print("-!!! {0}接口返回信息：{1}".format(url, r.json()))
            case_assert_result(r=r)

        elif datas[ExcelVarles.method] == 'put':
            r = self.obj.PUT(url=url, json=param, headers=header)
            print("-!!! {0}接口返回信息：{1}".format(url, r.json()))
            case_assert_result(r=r)

        elif datas[ExcelVarles.method] == 'delete':
            r = self.obj.DELETE(url=url, headers=header)
            print("-!!! {0}接口返回信息：{1}".format(url, r.json()))
            case_assert_result(r=r)


if __name__ == '__main__':
    pytest.main(["-s", "-v", "test_single_interface.py", "--alluredir", "./report/result"])

    # import subprocess
    #
    # subprocess.call('allure generate report/result/ -o report/html --clean', shell=True)
    # subprocess.call('allure open -h 127.0.0.1 -p  8088 ./report/html', shell=True)
