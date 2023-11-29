# coding=utf-8


import json
from log.log import Logger


class MyJson(object):
    # 实例化logger对象
    logger = Logger().Logger()
    # 按顺序存放查询到的key对应的value值
    valueList = []

    def __getListValue(self, obj: list, key: str):
        """
        传入的obj是list类型，遍历列表元素，根据列表元素的数据类型调对应方法处理数据
        :param obj: 传入的列表对象
        :param key: 需要查询key值
        :return:
        """
        for item in obj:
            if isinstance(item, dict):
                self.__getDictValue(item, key)
            elif isinstance(item, tuple):
                self.__getTupleValue(item, key)
            elif isinstance(item, list):
                self.__getListValue(item, key)

    def __getDictValue(self, obj: dict, key: str):
        """
        传入的obj是dict类型，遍历字典的k-v键值对，根据v的数据类型调对应方法处理数据
        :param obj: 传入的字典对象
        :param key: 需要查询key值
        :return:
        """
        for k, v in obj.items():
            if isinstance(v, dict):
                self.__getDictValue(v, key)
            elif isinstance(v, list):
                self.__getListValue(v, key)
            elif isinstance(v, tuple):
                self.__getTupleValue(v, key)
            elif k == key:
                self.valueList.append(v)

            # else:
            #     if k == key:
            #         self.valueList.append(v)
            #     else:
            #         if isinstance(v, str):
            #             self.logger.info("enter this branch, v type: {0} , v content: {1}".format(type(v), v))
            #             try:
            #                 v = json.loads(v)
            #                 self.logger.info("loads eng obj: {0},obj type: {1}".format(v, type(v)))
            #                 if isinstance(v, dict):
            #                     self.__getDictValue(v, key)
            #                 elif isinstance(v, list):
            #                     self.__getListValue(v, key)
            #                 elif isinstance(v, tuple):
            #                     self.__getTupleValue(v, key)
            #             except Exception:
            #                 pass

    def __getTupleValue(self, obj: tuple, key: str):
        """
        传入的obj是tuple类型，遍历tuple的元素，根据元素的数据类型调对应方法处理数据
        :param obj: 传入的元组对象
        :param key: 需要查询key值
        :return:
        """
        for item in obj:
            if isinstance(item, dict):
                self.__getDictValue(item, key)
            elif isinstance(item, list):
                self.__getListValue(item, key)
            elif isinstance(item, tuple):
                self.__getTupleValue(item, key)

    def value(self, obj, key, index: int = 1):
        """
        返回传入对象中指定键对应的值
        :param obj: 需要解析的对象
        :param key: 指定的键
        :param index: 若有多个键，指定返回第index个键对应的值
        :return: 返回指定键对应的值
        """
        # 将传入的对象转换成字符串，替换掉true/false/null为True/False/None,在进行反序列化
        if isinstance(obj, dict) or isinstance(obj, list) or isinstance(obj, tuple):
            obj = json.dumps(obj, ensure_ascii=False)
        else:
            pass
        if "false" in obj or "true" in obj or "null" in obj:
            obj = obj.replace("true", "True")
            obj = obj.replace("false", "False")
            obj = obj.replace("null", "None")
        try:
            obj = json.loads(obj, encoding='utf-8')
            # obj = json.loads(obj)
        except Exception:
            raise Exception("Enter parameter type is error! Parameter type is list or dict or tuple,please check parameter !")
        self.logger.info("After loads object: {0}".format(obj))
        # 根据obj的数据类型，调相应的方法
        if isinstance(obj, dict):
            self.__getDictValue(obj, key)
        elif isinstance(obj, list):
            self.__getListValue(obj, key)
        elif isinstance(obj, tuple):
            self.__getTupleValue(obj, key)
        # 返回查询指定索引的值
        try:
            result = self.valueList[index - 1]
            # result = self.valueList
        except IndexError:
            raise Exception("Found {0} key-value pairs! please check enter index!".format(len(self.valueList)))
        return result


if __name__ == '__main__':
    # listStr = {"case1":{
    #                     "name":"小红",
    #                     "project":[]
    #                     }
    #            }
    # print("返回值： ", MyJson().value(listStr, "name", index=2))

    # print(json.loads('{"isOn": t  rue}'))
    dictTest = {'id': 140393851939712, 'enterprise_id': 133, 'template_name': '颜色大小模板', 'tag_id': 140393851896064, 'created_at': 1614823685, 'updated_at': 1614823685, 'deleted_at': 0, 'attributes': [{'id': 140393851971712, 'attribute_name': '大小', 'enterprise_id': 133, 'attribute_template_id': 140393851939712, 'created_at': 1614823685, 'updated_at': 1614823685, 'deleted_at': 0, 'attribute_items': [{'id': 140393852041088, 'attribute_item_value': '大', 'goods_attribute_id': 140393851971712, 'enterprise_id': 133, 'created_at': 1614823685, 'updated_at': 1614823685, 'deleted_at': 0}, {'id': 140393852069632, 'attribute_item_value': '中', 'goods_attribute_id': 140393851971712, 'enterprise_id': 133, 'created_at': 1614823685, 'updated_at': 1614823685, 'deleted_at': 0}, {'id': 140393852088384, 'attribute_item_value': '小', 'goods_attribute_id': 140393851971712, 'enterprise_id': 133, 'created_at': 1614823685, 'updated_at': 1614823685, 'deleted_at': 0}]}, {'id': 140393851992896, 'attribute_name': '颜色', 'enterprise_id': 133, 'attribute_template_id': 140393851939712, 'created_at': 1614823685, 'updated_at': 1614823685, 'deleted_at': 0, 'attribute_items': [{'id': 140393852109824, 'attribute_item_value': '黄', 'goods_attribute_id': 140393851992896, 'enterprise_id': 133, 'created_at': 1614823685, 'updated_at': 1614823685, 'deleted_at': 0}, {'id': 140393852134912, 'attribute_item_value': '绿', 'goods_attribute_id': 140393851992896, 'enterprise_id': 133, 'created_at': 1614823685, 'updated_at': 1614823685, 'deleted_at': 0}, {'id': 140393852157248, 'attribute_item_value': '蓝', 'goods_attribute_id': 140393851992896, 'enterprise_id': 133, 'created_at': 1614823685, 'updated_at': 1614823685, 'deleted_at': 0}]}], 'tag': {'id': 140393851896064, 'tag_name': '颜色大小模板', 'enterprise_id': 133, 'created_at': 1614823685, 'updated_at': 1614823685, 'deleted_at': 0}}
    # strTest = json.dumps(dictTest)
    # dictTest = json.loads(strTest)

    ids = MyJson().value(obj=dictTest, key="id", index=3)
    print(ids)
