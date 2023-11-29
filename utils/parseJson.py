from types import GeneratorType as generator
from utils.readerFile import ReaderFile
from typing import List, Dict
from itertools import chain
import objectpath
import json


class ParseJson:
    @staticmethod
    def parse_json_by_objectpath(res_json: Dict, expr: str) -> (str, List, int):
        """
        :param res_json: 字典数据
        :param expr: objectpath提取表达式,
        :return: json提取结果
        """
        tree = objectpath.Tree(res_json)
        extract_content = tree.execute(expr)

        if isinstance(extract_content, (generator, chain)):
            return list(extract_content)
        else:
            return extract_content

    @staticmethod
    def parseJson(myJson, *args):
        """
        获取指定路径下key对应的Value
        """
        keyStr = "$..*[@"
        for key in args:
             keyStr = keyStr+"."+key
        keyStr = keyStr+"]"
        print(keyStr)
        valueList = ParseJson.parse_json_by_objectpath(myJson, keyStr)
        return valueList

    @staticmethod
    def getAllValue(myJson, key):
        """
        获取所有key对应的value
        """
        keyStr = "$.."+key
        return ParseJson.parse_json_by_objectpath(myJson, keyStr)


if __name__ == '__main__':
    resJson = ReaderFile.readerJson("addMutiSkuGoods.json")
    # print(ParseJson.parseJson(resJson, "id"))
    print(ParseJson.parseJson(resJson, *["attributeData[0]", "attribute_items[0]", "id"]))