# -*- coding: utf-8 -*-
"""
csv文件转为json
"""
from utils.readerIniFile import ReaderIniFile
import csv, json


def transjson(csvFileName):
    tableData = []
    with open(ReaderIniFile.getConfigFilePath("data", csvFileName), 'r', encoding="gbk") as csvfile :
        reader = csv.DictReader(csvfile)
        for row in reader:
            # 读取的内容是字典格式的
            tableData.append(dict(row))
        # print(json.dumps(tableData, sort_keys=True, indent=2, ensure_ascii=False))
        result = json.dumps(tableData, sort_keys=True, indent=2, ensure_ascii=False)
        with open(ReaderIniFile.getConfigFilePath("data", "onLineEnterpriseInfo(supermarket).json"), "w+", encoding="gbk") as tf:
            tf.write(result)


if __name__ == '__main__':
    transjson('enterpriseForSupermarket.csv')