#!/usr/local/bin/python3
# -*- coding:UTF-8 -*-
"""
@FileName           :conftest.py
@Copyright          :Copyright ©2014-2021 创业翼
@Author             :GourdBoy
@Date               :2021/12/15 4:44 下午
@ProjectName        :api-automated-testing
@ApplicationName    :PyCharm
"""

from utils.operationExcel import OperationExcel,ExcelVarles
from utils.parseJson import ParseJson
from utils.readerIniFile import ReaderIniFile
from utils.readerFile import ReaderFile
from filelock import FileLock
import pytest, os, math, json

consoleUrl = ReaderIniFile.value(section="console_sys_info", key="consoleLoginUrl")
shopUrl = ReaderIniFile.value(key="shopBaseUrl")


def convertTuple2Dict(sourceList):
    """
    将列表中的元组对象转换成字典
    :return: list
    """
    lst = list()
    for t in sourceList:
        d = {}
        d[t[0]] = t[1]
        lst.append(d)
    return lst


# @pytest.fixture(scope="session", autouse=True)
def pytest_sessionstart(session):
    """
    类的前置处理函数主要是将excel文件中的接口信息和企业信息拼接起来，
    将拼接起来的数据作为数据驱动的数据源
    :return:
    """
    with FileLock("session.lock"):
        with open(ReaderIniFile.getConfigFilePath("data", "singleInterfaceCombineData.json"), 'r') as f:
            # lines = f.readlines()
            lines = f.read()
        if len(lines) == 0:
            combinedData = list()
            excel = OperationExcel()
            enterpriseList = ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json")
            interfaceList = excel.runs()
            colNameStatusCode = "状态码"
            colNameExpect = "期望结果"
            colNameParam = "请求参数"
            for enterprise in enterpriseList:
                # 将excel中的每个接口信息和所有企业信息进行组合
                for interface in interfaceList:
                    # 如何接口参数有多组参数，则需将所有的参数和combinedData组合
                    interfaceParam = interface[ExcelVarles.params]
                    combineItem = dict(enterprise, **interface)
                    if interfaceParam != "":
                        paramObj = eval(interfaceParam)
                        paramType = type(paramObj)
                        if paramType == dict:
                            combinedData.append(combineItem)
                        elif paramType == list:
                            # 将"状态码"、"期望结果"、"请求参数"列转为如下格式
                            # [{"状态码":200},{"状态码":503},{"状态码":500},{"状态码":400}]
                            # [{"期望结果":success},{"期望结果":success},{"期望结果":success},{"期望结果":success}]
                            # [{"请求参数":{"a":1},{"请求参数":{"b":2}},{"请求参数":{"c":3}},{"请求参数":{"d":4}}]
                            interfaceStatusCode = eval(interface[ExcelVarles.statusCode])
                            interfaceExpect = eval(interface[ExcelVarles.expect])
                            listLength = len(paramObj)
                            statusCodeList = [colNameStatusCode] * listLength
                            expectList = [colNameExpect] * listLength
                            paramList = [colNameParam] * listLength
                            statusCodeTuple = list(zip(statusCodeList,interfaceStatusCode))
                            expectTuple = list(zip(expectList,interfaceExpect))
                            paramTuple = list(zip(paramList,paramObj))
                            sCodeCombineList = convertTuple2Dict(statusCodeTuple)
                            expectList = convertTuple2Dict(expectTuple)
                            paramList = convertTuple2Dict(paramTuple)
                            lst = list()
                            for index in range(0,len(paramObj)):
                                sCodeCombine = sCodeCombineList[index]
                                expect = expectList[index]
                                param =paramList[index]
                                combineTmp = dict(sCodeCombine, **expect)
                                lst.append(dict(combineTmp, **param))
                            # for etpInterface in combinedData:
                            for interfaceInfo in lst:
                                combinedData.append(dict(combineItem, **interfaceInfo))
                    else:
                        combinedData.append(combineItem)
            print("enterpriseInfo and interfaceInfo combined result: {0}".format(combinedData))

            with open(ReaderIniFile.getConfigFilePath("data", "singleInterfaceCombineData.json"), 'w',
                      encoding="utf-8") as f:
                f.write(json.dumps(combinedData))


def pytest_sessionfinish(session):
    # urlRecodeFileLst = ["shopUrlRecord.json", "consoleUrlRecord.json"]
    # category = ["Applet", "Console"]
    # shopFile = open("shopUrlRecord.json", 'a+', encoding='utf-8')
    # with open("{0}/consoleUrlRecord.json".format("data"), 'r', encoding='utf-8') as consoleFile:
    #     consoleURLLen = consoleFile.readlines()
    #     shopFile.write('\n')
    #     shopFile.write("{0} coverage interface: {1}\n".format("Console", consoleURLLen))
    #     for i in consoleFile:
    #         shopFile.write(i)

    with open("{}/environment.properties".format(session.config.rootdir), "a+") as ft:
        ft.truncate(0)
        # with open(ReaderIniFile.getConfigFilePath("data", "slowUrlRecord.json")) as fs:
        #     lines = fs.readlines()
        #     urlLength = len(lines)
        #     if urlLength != 0:
        #         ft.write("duration: url\n")
        #         for lineNum in range(0, len(lines)):
        #             separationUrl = lines[lineNum].split(" :duration ")
        #             ft.write("{0}={1}\n".format(str(separationUrl[1].replace(",\n", "")+"ms"), str(separationUrl[0])))
        #             # ft.write(lines[lineNum])
        #
        # with open(ReaderIniFile.getConfigFilePath("data", "urlRecord.json")) as fs:
        #     lines = fs.readlines()
        #     urlLength = len(lines)
        #     if urlLength != 0:
        #         ft.write("coverage/sum: {0}\n".format("{0}/184".format(urlLength)))
        #         for lineNum in range(0, len(lines)):
        #             ft.write("{0}={1}\n".format(lineNum+1, lines[lineNum].replace(",\n", "")+"ms"))
        #             # ft.write(lines[lineNum])

        with open(ReaderIniFile.getConfigFilePath("data", "urlRecord.json")) as fs:
            lines = fs.readlines()
            # 去除重复的url
            lst1 = []
            for item in lines:
                urls = item.split(" :duration ")[0]
                lst1.append(urls)
            removeDulicate = set(lst1)
            removeDulicateLst = list(removeDulicate)
            # 去除无效的记录
            lsts = []
            if len(removeDulicateLst) > 0:
                for line in removeDulicateLst:
                    if line.startswith(shopUrl):
                        lsts.append(line)
            urlLength = len(lsts)
            # print("remove duplicate interface: {0}".format(lsts))
            # 统计慢接口,响应大于500ms的次数大于等于总次数的百分之五十
            lists = []
            if urlLength != 0:
                ft.write("duration: url\n")
                for lst in lsts:
                    sumTimes = 0
                    timeout = 0
                    overTimeUrl = ""
                    overTime = 0.0

                    for line in lines:
                        targetRecords = str(line).split(" :duration ")
                        # print("lst: {0}".format(lst))
                        if lst == targetRecords[0]:
                            sumTimes += 1
                            try:
                                times = targetRecords[1].replace(",\n", "")
                                if float(times) >= 500:
                                    overTimeUrl = lst
                                    overTime = times
                                    timeout += 1
                            except ValueError:
                                pass
                    lists.append(sumTimes)
                    lists = sorted(lists,reverse=True)
                    # print("interface: {0},times: {1}".format(overTimeUrl, overTime))
                    if timeout >= math.floor(sumTimes/2) and timeout != 0 and sumTimes != 0:
                        # print("content: {0}".format(lst))
                        ft.write("{0}={1}\n".format(str(overTime)+"ms", overTimeUrl))
                    # ft.write(lines[lineNum])

            # 显示本次调的所有url数量
            if urlLength != 0:
                ft.write("coverage/sum: {0}\n".format("{0}/231".format(urlLength)))
                # 记录所有的url
                for lineNum in range(0, len(lists)):
                    if str(lsts[lineNum]).startswith(shopUrl):
                        ft.write("{0}={1} (times:{2})\n".format(lineNum + 1, lsts[lineNum].replace(",\n", "") ,lists[lineNum]))
                    # ft.write(lines[lineNum])


# coding:utf-8
# import requests
# import pytest
# from utils.config import Config
#
#
# # 登录小程序
# @pytest.fixture()
# def loginShop():
#     # 从配置文件获取登录小程序的参数,获取Token
#     baseUrl = Config.value(key="shopBaseUrl")
#     enterpriseID = Config.value(key="enterpriseId")
#     enterpriseHash = Config.value(key="enterpriseHash")
#     params = {
#         "enterprise_id": enterpriseID,
#         "size": 1,
#         "sign": 2121
#     }
#     loginUrl = "{0}/gw-shop/get_token".format(baseUrl)
#     res = requests.get(url=loginUrl, params=params)
#     # 拼接访问一般接口需要的header信息并返回
#     token = res.json()[0]["token"]
#     headers = {
#         'token': token,
#         'Enterprise-Hash': enterpriseHash,
#         'App-Version': 'V1.7.2'
#     }
#     if res.status_code == 200:
#         return headers
#     else:
#         raise Exception("Login fail!", res.text)
#
# # 登录管理后台
# def loginConsole():
#     pass
#
