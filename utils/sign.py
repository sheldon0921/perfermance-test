import hashlib
import json
import operator


class Sign(object):

    @staticmethod
    def generateSign(params,secret):
        """
        :param params:需要加密的参数
        :return: 加密后的sign
        """
        # md = hashlib.md5()
        # crsAuthSecret = "8aff1f0d37662d1274d219d2e9db81b6"
        #
        # # params=zip(params.keys(),params.values())
        # # paramsAsc = sorted(params)
        #
        # paramsAsc = params
        # print("\nparamsAsc: {0}".format(json.dumps(paramsAsc)))
        # signStr = crsAuthSecret+json.dumps(paramsAsc)+crsAuthSecret
        # # signStr = json.dumps(paramsAsc)
        # print(signStr)
        # md.update(signStr.encode(encoding='utf-8'))
        # sign = md.hexdigest()
        # print("sign: {0}".format(sign))
        # return sign

        md = hashlib.md5()
        # crsAuthSecret = "8aff1f0d37662d1274d219d2e9db81b6"
        # 对key为data对应的value(类型为dict)进行排序
        params["data"] = Sign.dictSort(params["data"])
        # 对外部字典进行排序
        paramsAsc = Sign.dictSort(params)
        # 将所有的空格全部取掉
        param = json.dumps(paramsAsc).replace(" ", "")
        print("\nparamsAsc: {0}".format(param))
        # 按照加密规则开始加密
        signStr = secret+param+secret
        # signStr = json.dumps(paramsAsc)
        print(signStr)
        md.update(signStr.encode(encoding='utf-8'))
        sign = md.hexdigest()
        print("sign: {0}".format(sign))
        return sign

    @staticmethod
    def dictSort(params):
        """
        对字典的key按照ascii码升序进行排序
        :param params: 需要排序的字典
        :return:
        """
        # print("before sort: {0}".format(params))
        keyAsc = sorted(params.items(), key=lambda item:item[0], reverse=False)
        sortedDict = dict(keyAsc)
        # print("after sort:  {0}".format(sortedDict))
        return sortedDict

    # @staticmethod
    # def ASCparams(params):
    #     if isinstance(params,str):
    #         pass
    #     else:
    #         param=Sign.dictSort(params)
    #         print(param)
    #         for key in param.keys():
    #             # print(key)
    #             if isinstance(param[key],dict):
    #                 print(param[key])
    #                 Sign.ASCparams(param[key])
    #             elif isinstance(param[key],list):
    #                 for i in param[key]:
    #                     Sign.ASCparams(i)
    #             else:
    #                 continue






if __name__ == '__main__':
    body = {
        "method": "goods.base",
        "platform": "crs",
        "data": {
            "spu_id": 1002982,
            "spu_name": "帽子",
            "source_id": 100000,
            "spu_sn": "spu编号10086",
            "short_title": "帽子短标题",
            "sell_point": "帽子售卖热点",
            "sales": 1000,
            "status": 1,
            "category_id": 0,
            "category_name": "",
            "sku": {
                "list": [
                    {
                        "id": 1000000,
                        "sku_name": "成人帽子",
                        "material_id": 1000222,
                        "source_id": 1000988,
                        "card_title": "帽子分享卡片标题",
                        "poster_title": "帽子分享海报标题",
                        "short_title": "帽子短标题",
                        "sign_price": 20000,
                        "sell_price": 1000,
                        "goods_weight": 100,
                        "goods_volume": 200,
                        "sell_point": "售卖热点",
                        "qrcode_url": "二维码地址",
                        "sale_type": 1,
                        "status": 2,
                        "sales": 6,
                        "stock": 100,
                        "created_at": 1982981927,
                        "attributes": [
                            {
                                "attribute_id": 9999,
                                "attribute_value_id": 11111,
                                "attribute_value_name": "绿色"
                            },
                            {
                                "attribute_id": 8888,
                                "attribute_value_id": 22222,
                                "attribute_value_name": "XXL"
                            }
                        ],
                        "pictures": {
                            "image": "https://img-crs.vchangyi.com/2020/07/28/eb8785e99ac7fc09f6851e5551bea114.png",
                            "main": [
                                "https://img-crs.vchangyi.com/2020/08/04/8930651b01a906478ae1eafb044c7f1e.jpg",
                                "https://img-crs.vchangyi.com/2020/08/04/22947b96afcb81d4cbbe3e9c159270a7.jpg",
                                "https://img-crs.vchangyi.com/2020/08/04/e7f0749c9f2cb30f53155ab9ed7c7fec.jpg"
                            ],
                            "main_video": [
                                {
                                    "is_radio": 1,
                                    "is_auto": 2,
                                    "is_foreach": 1,
                                    "width": 100,
                                    "height": 200,
                                    "time": 30,
                                    "cover_url": "https://img-crs.vchangyi.com/2020/07/28/bed32a4137e55c1b5084fe1c497a399a.jpg"
                                }
                            ],
                            "poster": [
                                "https://img-crs.vchangyi.com/2020/07/28/bed32a4137e55c1b5084fe1c497a399a.jpg",
                                "https://img-crs.vchangyi.com/2020/07/28/e9664853198271c3a2ac54ee397011a4.png"
                            ],
                            "card": [
                                "https://img-crs.vchangyi.com/2020/07/28/bed32a4137e55c1b5084fe1c497a399a.jpg",
                                "https://img-crs.vchangyi.com/2020/07/28/e9664853198271c3a2ac54ee397011a4.png"
                            ],
                            "content": [
                                "https://img-crs.vchangyi.com/2020/07/28/bed32a4137e55c1b5084fe1c497a399a.jpg",
                                "https://img-crs.vchangyi.com/2020/07/28/e9664853198271c3a2ac54ee397011a4.png"
                            ]
                        }
                    }
                ],
                "attributes": [
                    {
                        "id": 9999,
                        "name": "颜色",
                        "option": [
                            {
                                "id": 11111,
                                "name": "绿色"
                            },
                            {
                                "id": 33333,
                                "name": "红色"
                            }
                        ]
                    },
                    {
                        "id": 8888,
                        "name": "规格",
                        "option": [
                            {
                                "id": 22222,
                                "name": "XXL"
                            },
                            {
                                "id": 44444,
                                "name": "XXXL"
                            }
                        ]
                    }
                ],
                "default_attribute": {
                    "sku_id": 10086,
                    "attributes": [
                        {
                            "attribute_id": 9999,
                            "attribute_value_id": 11111,
                            "attribute_value_name": "绿色"
                        },
                        {
                            "attribute_id": 8888,
                            "attribute_value_id": 22222,
                            "attribute_value_name": "XXL"
                        }
                    ]
                }
            }
        }
    }
    print(Sign().dictSort(body))
    print()
    print(Sign().ASCparams(body))