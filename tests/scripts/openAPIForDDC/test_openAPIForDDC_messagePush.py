from utils.shopForDDCApiAssert import ShopForDDCApiAssert
from tests.common.openAPIForDDC.shopForDDCApi import ShopForDDCApi
import pytest
import allure


@allure.epic("DDC对接Shop接口")
@allure.feature("用户、商品、订单相关事件")
class Test_openAPIForDDC_messagePush(object):
    @pytest.fixture()
    def ini(self):
        self.shop=ShopForDDCApiAssert()

    @allure.story("商城用户新增(shop_user_add)")
    @pytest.mark.onLineIndex
    def test_messagePush_userAdd(self,ini):
        body = {
            "data": {
                "enterprise_id":140269187892096,
                "mobile":"13388888888",
                "user_id":147478118478720
            },
            "method":"user.shop_user_add",
            "platform":"crs"
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res=ShopForDDCApi.sendRequest(body)
        print(res)
        examples={
                    "code": 200,
                    "message": "success",
                    "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
                    "data": {
                        "msg_id": "19984723346456603"
                    }
                }
        Res=self.shop.match_class(examples,res)
        print(Res)

    @allure.story("商城用户更新(shop_user_update)")
    @pytest.mark.onLineIndex
    def test_messagePush_userUpdate(self,ini):
        body = {
            "data": {
                "enterprise_id":140269187892096,
                "mobile":"13388888888",
                "user_id":147478118478720
            },
            "method":"user.shop_user_update",
            "platform":"crs"
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res=ShopForDDCApi.sendRequest(body)
        print(res)
        examples={
                    "code": 200,
                    "message": "success",
                    "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
                    "data": {
                        "msg_id": "19984723346456603"
                    }
                }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("商城用户授权(shop_user_auth)")
    @pytest.mark.onLineIndex
    def test_messagePush_userAuth(self,ini):
        body = {
            "data": {
                "enterprise_id":140269187892096,
                "mobile":"13388888888",
                "user_id":147478118478720
            },
            "method":"user.shop_user_auth",
            "platform":"crs"
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res=ShopForDDCApi.sendRequest(body)
        print(res)
        examples={
                    "code": 200,
                    "message": "success",
                    "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
                    "data": {
                        "msg_id": "19984723346456603"
                    }
                }
        Res = self.shop.match_class(examples,res)
        print(Res)

    @allure.story("商城用户地址添加(user.user_address_add)")
    @pytest.mark.onLineIndex
    def test_messagePush_userAddress_add(self, ini):
        body = {
            "data": {
                "enterprise_id": 140269187892096,
                "union_id": "oRZwf5yN3L-0bMBSIdNhsqvGOEW8",
                "user_id": 147478118478720,
                "address_id":148595323817536
            },
            "method": "user.user_address_add",
            "platform": "crs"
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("商城用户地址更新(user.user_address_update)")
    @pytest.mark.onLineIndex
    def test_messagePush_userAddress_update(self,ini):
        body = {
            "data": {
                "enterprise_id": 140269187892096,
                "union_id": "oRZwf5yN3L-0bMBSIdNhsqvGOEW8",
                "user_id": 147478118478720,
                "address_id": 148595323817536
            },
            "method": "user.user_address_update",
            "platform": "crs"
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("商城用户地址删除(user.user_address_delete)")
    @pytest.mark.onLineIndex
    def test_messagePush_userAddress_delete(self, ini):
        body = {
            "data": {
                "enterprise_id": 140269187892096,
                "union_id": "oRZwf5yN3L-0bMBSIdNhsqvGOEW8",
                "user_id": 147478118478720,
                "address_id": 148595323817536
            },
            "method": "user.user_address_delete",
            "platform": "crs"
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("用户发起/参加活动(user.shop_user_join_activity)")
    @pytest.mark.onLineIndex
    def test_messagePush_userJoin_activity(self, ini):
        body = {
            "data": {
                "enterprise_id": 140269187892096,
                "union_id": "oRZwf5yN3L-0bMBSIdNhsqvGOEW8",
                "user_id": 147478118478720,
                "event": "user.shop_user_join_activity",
                "event_desc":'',
                "event_at":1618884738,
                "object_id":"12345",
                "extra":"[aaa]"
            },
            "method": "user.shop_user_join_activity",
            "platform": "crs"
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("导购认证事件(user.guide_bind_user)")
    @pytest.mark.onLineIndex
    def test_messagePush_guideBind_user(self, ini):
        body = {
            "data": {
                "enterprise_hash": "61fb72b508532bfa698f17b37be7ff9a",
                "source_type": 1,
                "source_user_id": 147478118478720,
                "mem_uid":"F75BCF3D7F000001669F7007802EC0AE"
            },
            "method": "user.guide_bind_user",
            "platform": "crs"
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("商品基础信息(goods.base)")
    @pytest.mark.onLineIndex
    def test_messagePush_Goods_base(self, ini):
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
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("商品基础信息变更(goods.change)")
    @pytest.mark.onLineIndex
    def test_messagePush_Goods_change(self, ini):
        body ={
                "method":"goods.change",
                "platform":"crs",
                "data":{
                    "list": [{
                      "spu_id": 91789260042944,
                      "spu_status": 1,
                      "sku": [{
                        "spu_id": 91789260042944,
                        "source_id": 136,
                        "id": 91789260114048,
                        "status": 2,
                        "stock": 9963,
                        "price": 11590,
                        "sign_price": 12590,
                        "material_id": 125
                        }]
                      }]
                }
            }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("商品邮费信息(goods.postage)")
    @pytest.mark.onLineIndex
    def test_messagePush_Goods_postage(self, ini):
        body = {
                "method":"goods.postage",
                "platform":"crs",
                "data":{
                    "list":[
                        {
                            "postage_id":107701011297152,
                            "sku_id":907701011297152,
                            "delivery_type":1,
                            "name":"默认模板",
                            "type":1,
                            "weight":0,
                            "settlement_type":1,
                            "delivery_region":1,
                            "range_type":3,
                            "store_id":16,
                            "enterprise_id":16,
                            "created_at":1598860384,
                            "updated_at":1598860384,
                            "deleted_at":0,
                            "rules":[
                                {
                                    "postage_id":107701011297152,
                                    "base_fee":100,
                                    "free_shipping_fee":0,
                                    "free_shipping_num":0,
                                    "increase_value":0,
                                    "increase_fee":0,
                                    "code_list":"[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34]",
                                    "enterprise_id":16,
                                    "created_at":1598860384,
                                    "updated_at":1598860384,
                                    "deleted_at":0,
                                    "tree":[
                                        {
                                            "id":1,
                                            "label":"北京市",
                                            "children":[

                                            ]
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("商品分类(goods.category)")
    @pytest.mark.onLineIndex
    def test_messagePush_Goods_category(self, ini):
        body = {
                "method":"goods.category",
                "platform":"crs",
                "data":{
                    "enterprise_id":2,
                    "list":[
                        {
                            "id":107701011297152,
                            "name":"默认模板",
                            "pid":1,
                            "level":1
                        }
                    ]
                }
            }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("商品邮费变更(goods.postage_change)")
    @pytest.mark.onLineIndex
    def test_messagePush_Goods_postage_change(self, ini):
        body = {
                  "method": "goods.postage_change",
                  "platform": "CRS",
                  "data": {
                    "postage": {
                      "created_at": 1617155459,
                      "deleted_at": 0,
                      "delivery_region": 2,
                      "enterprise_id": 133,
                      "id": 145169324209088,
                      "name": "阿树新增邮费模板",
                      "rules": [
                        {
                          "base_fee": 100,
                          "code_list": "[35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]",
                          "created_at": 1617155459,
                          "deleted_at": 0,
                          "enterprise_id": 133,
                          "free_shipping_fee": 0,
                          "free_shipping_num": 0,
                          "id": 145169324231744,
                          "increase_fee": 100,
                          "increase_init_value": 1,
                          "increase_value": 1,
                          "postage_id": 145169324209088,
                          "starting_price": 0,
                          "tree": [
                            {
                              "children": [
                                {
                                  "children": [
                                    {
                                      "children": [],
                                      "id": 35,
                                      "label": "东城区",
                                      "level": 3
                                    },
                                    {
                                      "children": [],
                                      "id": 36,
                                      "label": "西城区",
                                      "level": 3
                                    },
                                    {
                                      "children": [],
                                      "id": 37,
                                      "label": "朝阳区",
                                      "level": 3
                                    },
                                    {
                                      "children": [],
                                      "id": 38,
                                      "label": "丰台区",
                                      "level": 3
                                    },
                                    {
                                      "children": [],
                                      "id": 39,
                                      "label": "石景山区",
                                      "level": 3
                                    },
                                    {
                                      "children": [],
                                      "id": 40,
                                      "label": "海淀区",
                                      "level": 3
                                    },
                                    {
                                      "children": [],
                                      "id": 41,
                                      "label": "门头沟区",
                                      "level": 3
                                    },
                                    {
                                      "children": [],
                                      "id": 42,
                                      "label": "房山区",
                                      "level": 3
                                    },
                                    {
                                      "children": [],
                                      "id": 43,
                                      "label": "通州区",
                                      "level": 3
                                    },
                                    {
                                      "children": [],
                                      "id": 44,
                                      "label": "顺义区",
                                      "level": 3
                                    },
                                    {
                                      "children": [],
                                      "id": 45,
                                      "label": "昌平区",
                                      "level": 3
                                    },
                                    {
                                      "children": [],
                                      "id": 46,
                                      "label": "大兴区",
                                      "level": 3
                                    },
                                    {
                                      "children": [],
                                      "id": 47,
                                      "label": "怀柔区",
                                      "level": 3
                                    },
                                    {
                                      "children": [],
                                      "id": 48,
                                      "label": "平谷区",
                                      "level": 3
                                    },
                                    {
                                      "children": [],
                                      "id": 49,
                                      "label": "密云区",
                                      "level": 3
                                    },
                                    {
                                      "children": [],
                                      "id": 50,
                                      "label": "延庆区",
                                      "level": 3
                                    }
                                  ],
                                  "id": 5844,
                                  "label": "北京市",
                                  "level": 2
                                }
                              ],
                              "id": 1,
                              "label": "北京市",
                              "level": 1
                            }
                          ],
                          "updated_at": 1617155459
                        }
                      ],
                      "settlement_type": 2,
                      "store_id": 133,
                      "type": "[2,1,3,4]",
                      "updated_at": 1617155459
                    },
                    "postage_id": 145169324209088,
                    "sku_list": []
                  },
                  "hash": "61fb72b508532bfa698f17b37be7ff9a",
                  "enterprise_id": 140269187892096
                }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("获取sku列表(goods.sku_detail)")
    @pytest.mark.onLineIndex
    def test_messagePush_Goods_sku_detail(self, ini):
        body ={
                "method": "goods.sku_detail",
                "platform": "crs",
                "data": {
                    "show_hide": 0,
                    "sku_ids": [
                        148717492554560,148740929198784
                    ],
                    "page": 1,
                    "size": 20
                }
            }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
                    "code":200,
                    "message":"success",
                    "request_id":"2bb4d2ec-9cfc-402d-8e5f-5c548e9ca5d0",
                    "data":{
                        "list":[
                            {
                                "attribute":[
                                    {
                                        "id":148587652707648,
                                        "item_id":148587652738560,
                                        "item_value":"大",
                                        "name":"大小"
                                    },
                                    {
                                        "id":148587652721728,
                                        "item_id":148587652781696,
                                        "item_value":"黄",
                                        "name":"颜色"
                                    }
                                ],
                                "category_id":[

                                ],
                                "category_name":[

                                ],
                                "detail_img":[
                                    "https://img-crs.vchangyi.com/goods16188878890070.jpg"
                                ],
                                "enterprise_id":140269187892096,
                                "market_price":0,
                                "sales":0,
                                "sell_point":"小熊佩奇，给孩子一个完整的童年",
                                "sell_price":10000,
                                "sign_price":10,
                                "sku_id":148717492554560,
                                "sku_img":"https://img-crs.vchangyi.com/goods16188879451100.jpg",
                                "sku_name":"小熊佩奇",
                                "spu_id":148717492463680,
                                "spu_name":"小熊佩奇",
                                "status":1,
                                "stock":20
                            },
                            {
                                "attribute":[
                                    {
                                        "id":147694814395968,
                                        "item_id":147694814426624,
                                        "item_value":"大",
                                        "name":"大小"
                                    },
                                    {
                                        "id":147694814408832,
                                        "item_id":147694814466816,
                                        "item_value":"黄",
                                        "name":"颜色"
                                    }
                                ],
                                "category_id":[

                                ],
                                "category_name":[

                                ],
                                "detail_img":[
                                    "https://img-crs.vchangyi.com/goods16149152272710.jpg"
                                ],
                                "enterprise_id":140269187892096,
                                "market_price":0,
                                "sales":3,
                                "sell_point":"QWERTY",
                                "sell_price":1,
                                "sign_price":2000,
                                "sku_id":148740929198784,
                                "sku_img":"https://img-crs.vchangyi.com/goods16149152407290.jpg",
                                "sku_name":"监控专用",
                                "spu_id":148740929134848,
                                "spu_name":"监控专用",
                                "status":2,
                                "stock":48
                            }
                        ],
                        "page":1,
                        "size":20,
                        "total":2
                    }
                }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("订单支付成功(wx_pay_success_no_confirm)")
    @pytest.mark.onLineIndex
    def test_messagePush_wx_pay_success_no_confirm(self, ini):
        body = {
                "method":"order.wx_pay_success_no_confirm",
                "platform":"crs",
                "data":{
                    "meta":{
                        "source":"crs"
                    },
                    "orderInfo":{
                        "id":115481366469504,
                        "orderNo":"116026593857636",
                        "mainOrderNo":"416026593855388",
                        "enterpriseId":73,
                        "status":40,
                        "type":14,
                        "totalAmount":4290,
                        "preferentialPrice":0,
                        "activityDiscountAmount":0,
                        "finalAmount":4290,
                        "paymentChannel":1,
                        "payAt":1602659395,
                        "refundAt":0,
                        "createdAt":1602659385,
                        "deliveryName":"陶照辉",
                        "deliveryMobile":"18827080424",
                        "deliveryAddress":"华中科技大学接待中心3号楼",
                        "remarks":"",
                        "thirdNo":"0",
                        "sendAt":0,
                        "signAt":0,
                        "cashFee":4290,
                        "couponFee":0,
                        "otherFee":0,
                        "couponCount":0,
                        "discountFee":0,
                        "province":"湖北省",
                        "city":"武汉市",
                        "area":"洪山区",
                        "logisticIdentity":"",
                        "logisticNo":"",
                        "isLottery":0,
                        "logisticsPrice":0,
                        "lotteryId":0,
                        "storeId":73,
                        "storeStaffId":112616555512064,
                        "serviceStoreId":73,
                        "serviceStaffId":0,
                        "totalRefundFee":0,
                        "takeGoodsMobile":"",
                        "takeGoodsName":"",
                        "deliveryType":1,
                        "goodsCount":0
                    },
                    "orderGoods":[
                        {
                            "id":115481366482752,
                            "spuId":114768525179776,
                            "skuId":114768525306112,
                            "spuName":" 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                            "categoryName":"[]",
                            "skuPicture":"https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                            "type":14,
                            "goodsType":1,
                            "skuAttribute":"",
                            "quantity":1,
                            "originalPrice":9990,
                            "sellPrice":4290,
                            "singleDiscount":0,
                            "subPrice":4290,
                            "skuNo":"10800097",
                            "goodsPayPrice":4290
                        }
                    ],
                    "orderUser":{
                        "id":115478258620224,
                        "enterpriseId":73,
                        "avatar":"https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                        "unionId":"ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                        "openId":"ok1H25VEj_ujXKcm6eU4XVthbrYw",
                        "thirdMemberNo":"",
                        "nickName":"那个陶💕",
                        "realName":"",
                        "mobile":"",
                        "sex":2,
                        "authAt":1602658942,
                        "createdAt":1602657868,
                        "registerAt":0,
                        "country":"中国",
                        "province":"广东",
                        "city":"深圳",
                        "birthday":"",
                        "userAmount":0,
                        "isCrmUser":0
                    },
                    "orderStatusTrace":{
                        "id":115481388200640,
                        "event":"wx_pay_success_no_confirm",
                        "eventDesc":"微信支付成功(不需要确认)",
                        "from":20,
                        "to":40,
                        "createdAt":1602659396
                    },
                    "payInfo":{
                        "id":115481368679296,
                        "mainOrderNo":"416026593855388",
                        "thirdPaymentNo":"4200000741202010141515301763",
                        "amount":4290,
                        "comment":"",
                        "paymentChannel":1,
                        "status":2,
                        "payMoney":4290,
                        "callBackInfo":"",
                        "finishedAt":1602659396,
                        "createdAt":1602659387
                    },
                    "mainOrderInfo":{
                        "id":115481366464320,
                        "mainOrderNo":"416026593855388",
                        "status":40,
                        "type":14,
                        "enterpriseId":73,
                        "userId":115478258620224,
                        "totalAmount":4290,
                        "preferentialPrice":0,
                        "finalAmount":4290,
                        "paymentChannel":1,
                        "payAt":1602659395,
                        "quantity":1,
                        "refundAt":0,
                        "totalRefundFee":0,
                        "logisticsPrice":0,
                        "cashFee":4290,
                        "couponFee":0,
                        "otherFee":0,
                        "couponCount":0,
                        "preCouponFee":0,
                        "isSplitOrder":0
                    },
                    "mainOrderGoods":[
                        {
                            "spuId":114768525179776,
                            "skuId":114768525306112,
                            "spuName":" 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                            "categoryName":"[]",
                            "skuPicture":"https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                            "type":14,
                            "goodsType":1,
                            "skuAttribute":"",
                            "quantity":1,
                            "originalPrice":9990,
                            "sellPrice":4290,
                            "singleDiscount":0,
                            "subPrice":4290,
                            "skuNo":"10800097",
                            "goodsPayPrice":4290
                        }
                    ],
                    "orderLogistic":[

                    ],
                    "refundApply":[

                    ],
                    "payRefund":[

                    ],
                    "action":"send_message"
                }
            }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("ERP通知已发货(open_send_out_order)")
    @pytest.mark.onLineIndex
    def test_messagePush_open_send_out_order(self, ini):
        body = {
            "method": "order.open_send_out_order",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("导入发货信息成已发货(import_send_out_order)")
    @pytest.mark.onLineIndex
    def test_messagePush_import_send_out_order(self, ini):
        body = {
            "method": "order.import_send_out_order",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("人工处理成已发货(manual_send_out_order)")
    @pytest.mark.onLineIndex
    def test_messagePush_manual_send_out_order(self, ini):
        body = {
            "method": "order.manual_send_out_order",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("用户申请仅退款(customer_apply_refund_only_money)")
    @pytest.mark.onLineIndex
    def test_messagePush_customer_apply_refund_only_money(self, ini):
        body = {
            "method": "order.customer_apply_refund_only_money",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("用户申请退货退款(customer_apply_refund_goods_money)")
    @pytest.mark.onLineIndex
    def test_messagePush_customer_apply_refund_goods_money(self, ini):
        body = {
            "method": "order.customer_apply_refund_goods_money",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("人工拒绝(manual_refuse_apply_refund)")
    @pytest.mark.onLineIndex
    def test_messagePush_manual_refuse_apply_refund(self, ini):
        body = {
            "method": "order.manual_refuse_apply_refund",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("后台驳回(console_refuse_apply_refund)")
    @pytest.mark.onLineIndex
    def test_messagePush_console_refuse_apply_refund(self, ini):
        body = {
            "method": "order.console_refuse_apply_refund",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("ERP驳回(open_refuse_apply_refund)")
    @pytest.mark.onLineIndex
    def test_messagePush_open_refuse_apply_refund(self, ini):
        body = {
            "method": "order.open_refuse_apply_refund",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("ERP同意仅退款(open_agree_only_refund)")
    @pytest.mark.onLineIndex
    def test_messagePush_open_agree_only_refund(self, ini):
        body = {
            "method": "order.open_agree_only_refund",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("ERP同意退款退货(open_agree_refund)")
    @pytest.mark.onLineIndex
    def test_messagePush_open_agree_refund(self, ini):
        body = {
            "method": "order.open_agree_refund",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("人工同意退款(manual_agree_refund)")
    @pytest.mark.onLineIndex
    def test_messagePush_manual_agree_refund_001(self, ini):
        body = {
            "method": "order.manual_agree_refund",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("超期未寄回商品(auto_overdue_no_send_back)")
    @pytest.mark.onLineIndex
    def test_messagePush_auto_overdue_no_send_back(self, ini):
        body = {
            "method": "order.auto_overdue_no_send_back",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("用户签收(customer_sign)")
    @pytest.mark.onLineIndex
    def test_messagePush_customer_sign(self, ini):
        body = {
            "method": "order.customer_sign",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("超期自动签收(auto_sign)")
    @pytest.mark.onLineIndex
    def test_messagePush_auto_sign(self, ini):
        body = {
            "method": "order.auto_sign",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("已过售后期自动完成(auto_complete)")
    @pytest.mark.onLineIndex
    def test_messagePush_auto_complete_001(self, ini):
        body = {
            "method": "order.auto_complete",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("全部退款成功(all_refund_success)")
    @pytest.mark.onLineIndex
    def test_messagePush_all_refund_success_001(self, ini):
        body = {
            "method": "order.all_refund_success",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("部分退款成功(7天内)(partial_refund_success)")
    @pytest.mark.onLineIndex
    def test_messagePush_partial_refund_success(self, ini):
        body = {
            "method": "order.partial_refund_success",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("部分退款成功(超7天)(partial_refund_success_overdue_after_sale)")
    @pytest.mark.onLineIndex
    def test_messagePush_partial_refund_success_overdue_after_sale(self, ini):
        body = {
            "method": "order.partial_refund_success_overdue_after_sale",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("退款失败(refund_fail)")
    @pytest.mark.onLineIndex
    def test_messagePush_refund_fail(self, ini):
        body = {
            "method": "order.refund_fail",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("部分退款已过售后期(partial_refund_overdue_after_sale)")
    @pytest.mark.onLineIndex
    def test_messagePush_partial_refund_overdue_after_sale(self, ini):
        body = {
            "method": "order.partial_refund_overdue_after_sale",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("用户再次申请售后(customer_apply_return_again)")
    @pytest.mark.onLineIndex
    def test_messagePush_customer_apply_return_again(self, ini):
        body = {
            "method": "order.customer_apply_return_again",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("人工处理成已完成(manual_complete)")
    @pytest.mark.onLineIndex
    def test_messagePush_manual_complete(self, ini):
        body = {
            "method": "order.manual_complete",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("订单退款成功(all_refund_success)")
    @pytest.mark.onLineIndex
    def test_messagePush_all_refund_success(self, ini):
        body = {
            "method": "order.all_refund_success",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("订单完成(auto_complete)")
    @pytest.mark.onLineIndex
    def test_messagePush_auto_complete(self, ini):
        body = {
            "method": "order.auto_complete",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("用户申请售后(未发货，仅退款)(customer_apply_refund_of_not_send)")
    @pytest.mark.onLineIndex
    def test_messagePush_customer_apply_refund_of_not_send(self, ini):
        body = {
            "method": "order.customer_apply_refund_of_not_send",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("	用户申请售后(已签收，退货退款)(customer_apply_return_of_has_signed)")
    @pytest.mark.onLineIndex
    def test_messagePush_customer_apply_return_of_has_signed(self, ini):
        body = {
            "method": "order.customer_apply_return_of_has_signed",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("	用户取消(customer_cancel)")
    @pytest.mark.onLineIndex
    def test_messagePush_customer_cancel(self, ini):
        body = {
            "method": "order.customer_cancel",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("过期未寄回商品(customer_overdue_deliver)")
    @pytest.mark.onLineIndex
    def test_messagePush_customer_overdue_deliver(self, ini):
        body = {
            "method": "order.customer_overdue_deliver",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("	后台审核通过(console_agree)")
    @pytest.mark.onLineIndex
    def test_messagePush_console_agree(self, ini):
        body = {
            "method": "order.console_agree",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("后台驳回(console_reject)")
    @pytest.mark.onLineIndex
    def test_messagePush_console_reject(self, ini):
        body = {
            "method": "order.console_reject",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("OPEN同意退货(open_agree_return)")
    @pytest.mark.onLineIndex
    def test_messagePush_open_agree_return(self, ini):
        body = {
            "method": "order.open_agree_return",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("OPEN拒绝退货(open_reject_return)")
    @pytest.mark.onLineIndex
    def test_messagePush_open_reject_return(self, ini):
        body = {
            "method": "order.open_reject_return",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("用户寄回商品(customer_deliver)")
    @pytest.mark.onLineIndex
    def test_messagePush_customer_deliver(self, ini):
        body = {
            "method": "order.customer_deliver",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("OPEN同意退款(open_agree_refund)")
    @pytest.mark.onLineIndex
    def test_messagePush_open_agree_refund_001(self, ini):
        body = {
            "method": "order.open_agree_refund",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("OPEN拒绝退款(open_reject_refund)")
    @pytest.mark.onLineIndex
    def test_messagePush_open_reject_refund(self, ini):
        body = {
            "method": "order.open_reject_refund",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("人工同意退款(manual_agree_refund)")
    @pytest.mark.onLineIndex
    def test_messagePush_manual_agree_refund(self, ini):
        body = {
            "method": "order.manual_agree_refund",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("人工拒绝退款(manual_reject_refund)")
    @pytest.mark.onLineIndex
    def test_messagePush_manual_reject_refund(self, ini):
        body = {
            "method": "order.manual_reject_refund",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("OPEN 通知转人工(open_notice_to_manual)")
    @pytest.mark.onLineIndex
    def test_messagePush_open_notice_to_manual(self, ini):
        body = {
            "method": "order.open_notice_to_manual",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("OPEN 通知已发货(open_notice_send_out)")
    @pytest.mark.onLineIndex
    def test_messagePush_open_notice_send_out(self, ini):
        body = {
            "method": "order.open_notice_send_out",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("OPEN 通知仅退款(open_notice_refund)")
    @pytest.mark.onLineIndex
    def test_messagePush_open_notice_refund(self, ini):
        body = {
            "method": "order.open_notice_refund",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("人工处理为已发货(manual_send_out)")
    @pytest.mark.onLineIndex
    def test_messagePush_manual_send_out(self, ini):
        body = {
            "method": "order.manual_send_out",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("open通知人工中的售后单为已发货(open_notice_manual_send_out)")
    @pytest.mark.onLineIndex
    def test_messagePush_open_notice_manual_send_out(self, ini):
        body = {
            "method": "order.open_notice_manual_send_out",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("用户申请售后（未发货，仅退款）,特殊企业处理(customer_apply_refund_of_not_send_special)")
    @pytest.mark.onLineIndex
    def test_messagePush_customer_apply_refund_of_not_send_special(self, ini):
        body = {
            "method": "order.customer_apply_refund_of_not_send_special",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("已发货用户申请仅退款(send_out_apply_only_refund)")
    @pytest.mark.onLineIndex
    def test_messagePush_send_out_apply_only_refund(self, ini):
        body = {
            "method": "order.send_out_apply_only_refund",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("已发货用户申请退货退款(send_out_apply_return_goods)")
    @pytest.mark.onLineIndex
    def test_messagePush_send_out_apply_return_goods(self, ini):
        body = {
            "method": "order.send_out_apply_return_goods",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("客服一键转人工(customer_service_to_manual)")
    @pytest.mark.onLineIndex
    def test_messagePush_customer_service_to_manual(self, ini):
        body = {
            "method": "order.customer_service_to_manual",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("客服创建手工售后单(manual_apply_return_goods)")
    @pytest.mark.onLineIndex
    def test_messagePush_manual_apply_return_goods(self, ini):
        body = {
            "method": "order.manual_apply_return_goods",
            "platform": "crs",
            "data": {
                "meta": {
                    "source": "crs"
                },
                "orderInfo": {
                    "id": 115481366469504,
                    "orderNo": "116026593857636",
                    "mainOrderNo": "416026593855388",
                    "enterpriseId": 73,
                    "status": 40,
                    "type": 14,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "activityDiscountAmount": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "refundAt": 0,
                    "createdAt": 1602659385,
                    "deliveryName": "陶照辉",
                    "deliveryMobile": "18827080424",
                    "deliveryAddress": "华中科技大学接待中心3号楼",
                    "remarks": "",
                    "thirdNo": "0",
                    "sendAt": 0,
                    "signAt": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "discountFee": 0,
                    "province": "湖北省",
                    "city": "武汉市",
                    "area": "洪山区",
                    "logisticIdentity": "",
                    "logisticNo": "",
                    "isLottery": 0,
                    "logisticsPrice": 0,
                    "lotteryId": 0,
                    "storeId": 73,
                    "storeStaffId": 112616555512064,
                    "serviceStoreId": 73,
                    "serviceStaffId": 0,
                    "totalRefundFee": 0,
                    "takeGoodsMobile": "",
                    "takeGoodsName": "",
                    "deliveryType": 1,
                    "goodsCount": 0
                },
                "orderGoods": [
                    {
                        "id": 115481366482752,
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderUser": {
                    "id": 115478258620224,
                    "enterpriseId": 73,
                    "avatar": "https://img-crs.vchangyi.com/2020/10/14/7a8919b31e9213d0521bc5b69116219b.png",
                    "unionId": "ouQkJ5ytihwSdYbYAsJ32d19LgyE",
                    "openId": "ok1H25VEj_ujXKcm6eU4XVthbrYw",
                    "thirdMemberNo": "",
                    "nickName": "那个陶💕",
                    "realName": "",
                    "mobile": "",
                    "sex": 2,
                    "authAt": 1602658942,
                    "createdAt": 1602657868,
                    "registerAt": 0,
                    "country": "中国",
                    "province": "广东",
                    "city": "深圳",
                    "birthday": "",
                    "userAmount": 0,
                    "isCrmUser": 0
                },
                "orderStatusTrace": {
                    "id": 115481388200640,
                    "event": "wx_pay_success_no_confirm",
                    "eventDesc": "微信支付成功(不需要确认)",
                    "from": 20,
                    "to": 40,
                    "createdAt": 1602659396
                },
                "payInfo": {
                    "id": 115481368679296,
                    "mainOrderNo": "416026593855388",
                    "thirdPaymentNo": "4200000741202010141515301763",
                    "amount": 4290,
                    "comment": "",
                    "paymentChannel": 1,
                    "status": 2,
                    "payMoney": 4290,
                    "callBackInfo": "",
                    "finishedAt": 1602659396,
                    "createdAt": 1602659387
                },
                "mainOrderInfo": {
                    "id": 115481366464320,
                    "mainOrderNo": "416026593855388",
                    "status": 40,
                    "type": 14,
                    "enterpriseId": 73,
                    "userId": 115478258620224,
                    "totalAmount": 4290,
                    "preferentialPrice": 0,
                    "finalAmount": 4290,
                    "paymentChannel": 1,
                    "payAt": 1602659395,
                    "quantity": 1,
                    "refundAt": 0,
                    "totalRefundFee": 0,
                    "logisticsPrice": 0,
                    "cashFee": 4290,
                    "couponFee": 0,
                    "otherFee": 0,
                    "couponCount": 0,
                    "preCouponFee": 0,
                    "isSplitOrder": 0
                },
                "mainOrderGoods": [
                    {
                        "spuId": 114768525179776,
                        "skuId": 114768525306112,
                        "spuName": " 【社群专属】香飘飘奶茶全家福礼盒*15杯-拼团",
                        "categoryName": "[]",
                        "skuPicture": "https://img-crs.vchangyi.com/2020/09/22/a4397c07006743b28d54ea908cc20e55.jpg",
                        "type": 14,
                        "goodsType": 1,
                        "skuAttribute": "",
                        "quantity": 1,
                        "originalPrice": 9990,
                        "sellPrice": 4290,
                        "singleDiscount": 0,
                        "subPrice": 4290,
                        "skuNo": "10800097",
                        "goodsPayPrice": 4290
                    }
                ],
                "orderLogistic": [

                ],
                "refundApply": [

                ],
                "payRefund": [

                ],
                "action": "send_message"
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("添加微信优惠券信息(wx_coupon_add)")
    @pytest.mark.onLineIndex
    def test_messagePush_wx_coupon_add(self, ini):
        body = {
                "method":"coupon.wx_coupon_add",
                "platform":"crs",
                "data":{
                }
            }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print("####:{0}".format(res))
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "status": "OK"
            }
        }
        Res = self.shop.match_class(examples, res)
        print("@@@@@:{0}".format(Res))

    @allure.story("更新微信优惠券信息(wx_coupon_update)")
    @pytest.mark.onLineIndex
    def test_messagePush_wx_coupon_update(self, ini):
        body = {
            "method": "coupon.wx_coupon_update",
            "platform": "crs",
            "data": {
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("删除微信优惠券信息(wx_coupon_delete)")
    @pytest.mark.onLineIndex
    def test_messagePush_wx_coupon_delete(self, ini):
        body = {
            "method": "coupon.wx_coupon_delete",
            "platform": "crs",
            "data": {
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("添加用户优惠券信息(user_coupon_add)")
    @pytest.mark.onLineIndex
    def test_messagePush_user_coupon_add(self, ini):
        body = {
            "method": "coupon.user_coupon_add",
            "platform": "crs",
            "data": {
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("更新用户优惠券信息(核销,过期)(user_coupon_update)")
    @pytest.mark.onLineIndex
    def test_messagePush_user_coupon_update(self, ini):
        body = {
            "method": "coupon.user_coupon_update",
            "platform": "crs",
            "data": {
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("新增绑定导购(user_binding_add)")
    @pytest.mark.onLineIndex
    def test_messagePush_user_binding_add(self, ini):
        body = {
            "method": "guide.user_binding_add",
            "platform": "crs",
            "data": {
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("更新绑定导购(user_binding_update)")
    @pytest.mark.onLineIndex
    def test_messagePush_user_binding_update(self, ini):
        body = {
            "method": "guide.user_binding_update",
            "platform": "crs",
            "data": {
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("删除绑定导购(user_binding_delete)")
    @pytest.mark.onLineIndex
    def test_messagePush_user_binding_delete(self, ini):
        body = {
            "method": "guide.user_binding_delete",
            "platform": "crs",
            "data": {
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("分销商品链路查询(share_link_check)")
    @pytest.mark.onLineIndex
    def test_messagePush_share_link_check(self, ini):
        body = {
            "method": "guide.share_link_check",
            "platform": "crs",
            "data": {
                "enterprise_hash": "61fb72b508532bfa698f17b37be7ff9a",
                "user_id": 147478118478720
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "store_staff_id": 0
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("分销商品链路绑定(share_link_bind)")
    @pytest.mark.onLineIndex
    def test_messagePush_share_link_bind(self, ini):
        body = {
            "method": "guide.share_link_bind",
            "platform": "crs",
            "data": {
                "enterprise_hash": "61fb72b508532bfa698f17b37be7ff9a",
                "user_id": 147478118478720
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("查物流(logistics_query)")
    @pytest.mark.onLineIndex
    def test_messagePush_logistics_query(self, ini):
        body = {
                "method":"open.logistics_query",
                "platform":"crs",
                "data":{
                    "list":[
                        {
                            "logistic_key":"zto",
                            "logistic_no":"75392426128856",
                            "receiver_mobile":""
                        }
                    ]
                }
            }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
                    "code":200,
                    "message":"",
                    "request_id":"f8f0a10f-55b3-469b-b452-55122c999736",
                    "data":{
                        "fail_list":[

                        ],
                        "success_list":[
                            {
                                "created_at":1601370725,
                                "is_over":1,
                                "logistic_key":"zto",
                                "logistic_name":"中通",
                                "logistic_no":"75392426128856",
                                "query_num":2,
                                "response_desc":"查询成功",
                                "sign_at":1601449548,
                                "status_desc":"已签收",
                                "traces":[
                                    {
                                        "datetime":"2020-09-29 17:10:37",
                                        "desc":"【合肥蜀山四部】（0551-64936665） 的 洽洽（18815694451） 已揽收"
                                    },
                                    {
                                        "datetime":"2020-09-29 17:10:52",
                                        "desc":"快件离开 【合肥蜀山四部】 已发往 【合肥中转部】"
                                    },
                                    {
                                        "datetime":"2020-09-29 22:45:00",
                                        "desc":"快件已经到达 【合肥中转部】"
                                    },
                                    {
                                        "datetime":"2020-09-29 22:46:28",
                                        "desc":"快件离开 【合肥中转部】 已发往 【南通中转部】"
                                    },
                                    {
                                        "datetime":"2020-09-30 05:51:10",
                                        "desc":"快件已经到达 【南通中转部】"
                                    },
                                    {
                                        "datetime":"2020-09-30 05:53:20",
                                        "desc":"快件离开 【南通中转部】 已发往 【通州】"
                                    },
                                    {
                                        "datetime":"2020-09-30 07:41:36",
                                        "desc":"快件已经到达 【通州】"
                                    },
                                    {
                                        "datetime":"2020-09-30 07:43:19",
                                        "desc":"【通州】 的曹鹏鸣（15996574266） 正在第1次派件, 请保持电话畅通,并耐心等待（95720为中通快递员外呼专属号码，请放心接听）"
                                    },
                                    {
                                        "datetime":"2020-09-30 10:30:49",
                                        "desc":"您的快递已暂存至【快递超市的卡柏洗衣店】, 地址: 金沙镇碧桂园商业街, 请及时领取。如有问题请电联:（15996574266）, 投诉电话:（15996574266）, 感谢您使用中通快递, 期待再次为您服务!"
                                    },
                                    {
                                        "datetime":"2020-09-30 15:05:48",
                                        "desc":"您的快递已签收, 签收人在【快递超市的卡柏洗衣店】(金沙镇碧桂园商业街)领取。如有疑问请电联:（15996574266）, 投诉电话:（15996574266）, 您的快递已经妥投。风里来雨里去, 只为客官您满意。上有老下有小, 赏个好评好不好？【请在评价快递员处帮忙点亮五颗星星哦~】"
                                    }
                                ],
                                "updated_at":1601515020
                            }
                        ]
                    }
                }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("查支持的快递公司(logistics_key_list)")
    @pytest.mark.onLineIndex
    @pytest.mark.skip()
    def test_messagePush_logistics_key_list(self, ini):
        body = {
            "method": "open.logistics_key_list",
            "platform": "crs",
            "data": {
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
                    "code":200,
                    "message":"",
                    "request_id":"a94a0678-268f-481b-b292-1e5a2d8330b6",
                    "data":{
                        "aae":"AAE全球专递",
                        "aj":"安捷快递",
                        "anneng":"安能物流",
                        "auto":"自动匹配",
                        "axd":"安信达快递",
                        "bfdf":"百福东方",
                        "bsky":"百世快运",
                        "chengguang":"程光快递",
                        "coe":"东方快递",
                        "cs":"城市100",
                        "cszx":"城市之星物流",
                        "ctwl":"长通物流",
                        "cxwl":"传喜物流",
                        "danniao":"丹鸟物流",
                        "db":"德邦",
                        "dhl":"DHL",
                        "dpex":"DPEX国际快递",
                        "ds":"D速物流",
                        "dsf":"递四方快递",
                        "ems":"EMS",
                        "emsg":"EMS国际",
                        "fedex":"Fedex国际",
                        "fedexcn":"FEDEX国内快递",
                        "feibao":"飞豹快递",
                        "gt":"国通",
                        "ht":"汇通（百世快递）",
                        "jd":"京东快递",
                        "jiaji":"佳吉快运",
                        "jitu":"极兔快递",
                        "jiuye":"九曳",
                        "kuaijie":"快捷速递",
                        "malaysiaems":"马来西亚（大包EMS）",
                        "ocs":"OCS",
                        "other":"其他",
                        "pjbest":"品骏快递",
                        "qf":"全峰",
                        "rfd":"如风达",
                        "sf":"顺丰",
                        "shpost":"同城快寄",
                        "sto":"申通",
                        "suer":"速尔快递",
                        "suning":"苏宁快递",
                        "tdhy":"天地华宇",
                        "tnt":"TNT",
                        "tt":"天天",
                        "ups":"UPS国际快递",
                        "xfwl":"信丰物流",
                        "ycgky":"远成物流",
                        "ycky":"远成快运",
                        "yd":"韵达",
                        "ymdd":"壹米滴答",
                        "yousu":"优速快递",
                        "youzheng":"邮政快递",
                        "yt":"圆通",
                        "yzgn":"邮政国内（挂号信）",
                        "zhongyou":"中邮物流",
                        "zhongyouex":"众邮快递",
                        "zjs":"宅急送",
                        "ztky":"中铁快运",
                        "zto":"中通",
                        "ztoky":"中通快运",
                        "zuochuan":"佐川急便"
                    }
                }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("商品详情(goods.detail)")
    @pytest.mark.onLineIndex
    def test_messagePush_goods_detail(self, ini):
        body = {
                "method":"goods.detail",
                "platform":"crs",
                "data":{
                     "enterprise_id": 140269187892096,
                     "spu_id":148717492463680
                }
            }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
                    "code":200,
                    "message":"success",
                    "request_id":"6a8a6bb0-c76a-4502-a4ac-01008acee065",
                    "data":{
                        "sku":{
                            "attributes":[
                                {
                                    "id":148587652707648,
                                    "name":"大小",
                                    "option":[
                                        {
                                            "id":148587652738560,
                                            "name":"大"
                                        },
                                        {
                                            "id":148587652753088,
                                            "name":"中"
                                        },
                                        {
                                            "id":148587652767488,
                                            "name":"小"
                                        }
                                    ]
                                },
                                {
                                    "id":148587652721728,
                                    "name":"颜色",
                                    "option":[
                                        {
                                            "id":148587652781696,
                                            "name":"黄"
                                        },
                                        {
                                            "id":148587652794496,
                                            "name":"绿"
                                        },
                                        {
                                            "id":148587652807296,
                                            "name":"蓝"
                                        }
                                    ]
                                }
                            ],
                            "list":[
                                {
                                    "activity_id":0,
                                    "activity_type":0,
                                    "attributes":[
                                        {
                                            "attribute_id":148587652707648,
                                            "attribute_name":"大小",
                                            "attribute_value":"大",
                                            "attribute_value_id":148587652738560
                                        },
                                        {
                                            "attribute_id":148587652721728,
                                            "attribute_name":"颜色",
                                            "attribute_value":"黄",
                                            "attribute_value_id":148587652781696
                                        }
                                    ],
                                    "card_title":"小熊佩奇",
                                    "created_at":1618887963,
                                    "goods_volume":"0.00",
                                    "goods_weight":"1.00",
                                    "id":148717492554560,
                                    "market_price":0,
                                    "material_channel_id":148717493840896,
                                    "material_id":147702583668864,
                                    "off_line_price":10000,
                                    "off_line_stock":10,
                                    "on_line_price":10000,
                                    "on_line_stock":10,
                                    "pictures":{
                                        "card":[
                                            "https://img-crs.vchangyi.com/goods16188878973330.jpg"
                                        ],
                                        "content":[
                                            "https://img-crs.vchangyi.com/goods16188878890070.jpg"
                                        ],
                                        "image":"https://img-crs.vchangyi.com/goods16188879451100.jpg",
                                        "main":[
                                            "https://img-crs.vchangyi.com/goods16188878856150.jpg"
                                        ],
                                        "main_video":[

                                        ],
                                        "poster":[
                                            "https://img-crs.vchangyi.com/goods16188878947190.jpg"
                                        ]
                                    },
                                    "postage_fee_rule":"运费1元（每增加1件加1元）",
                                    "poster_title":"小熊佩奇",
                                    "qrcode_url":"https://img-crs.vchangyi.com/2021/04/20/5231673d6fc464200be9930c9705059b.png",
                                    "sale_type":3,
                                    "sales":0,
                                    "sell_point":"小熊佩奇，给孩子一个完整的童年",
                                    "sell_price":10000,
                                    "sendType":"self",
                                    "short_title":"小熊佩奇",
                                    "sign_price":10,
                                    "sku_name":"小熊佩奇",
                                    "source_id":140269187892096,
                                    "status":1,
                                    "stock":20,
                                    "type":1
                                }
                            ]
                        },
                        "spu":{
                            "card_title":"小熊佩奇",
                            "created_at":1618887963,
                            "id":148717492463680,
                            "poster_title":"小熊佩奇",
                            "qrcode_url":"",
                            "sales":0,
                            "sell_point":"小熊佩奇，给孩子一个完整的童年",
                            "short_title":"小熊佩奇",
                            "source_id":140269187892096,
                            "spu_name":"小熊佩奇",
                            "spu_sn":"",
                            "status":0,
                            "updated_at":1618888428
                        }
                    }
                }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("企业一口价活动列表(buy_out_price_one_price_list)")
    @pytest.mark.onLineIndex
    def test_messagePush_buy_out_price_one_price_list(self, ini):
        body = {
            "method": "activity.buy_out_price_one_price_list",
            "platform": "crs",
            "data": {
                "enterprise_id": 140269187892096,
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
                    "code":200,
                    "message":"success",
                    "request_id":"05c06d84-f7b2-42d8-ba03-b8a3b5bd887f",
                    "data":{
                        "list":[
                            {
                                "activity_status":2,
                                "activity_type":21,
                                "end_at":1622390400,
                                "enterprise_id":140269187892096,
                                "id":149249820691520,
                                "is_limit_buy":0,
                                "n_piece":3,
                                "n_price":1,
                                "name":"fvsfscc",
                                "post_sale_type":2,
                                "postage":149211058662720,
                                "postage_status":3,
                                "quota_num":0,
                                "quota_status":2,
                                "start_at":1619193600
                            }
                        ],
                        "page":1,
                        "size":10,
                        "total":1
                    }
                }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("活动页详情(buy_out_price_detail)")
    @pytest.mark.onLineIndex
    def test_messagePush_buy_out_price_detail(self, ini):
        body = {
                "method": "activity.buy_out_price_detail",
                "platform": "crs",
                "data": {
                    "activity_rule_id": 149254443583744,
                    "user_id": 147478118478720,
                    "enterprise_id": 140269187892096
                }
            }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "05ef900f-2038-4c7a-8e0f-11daba637fc8",
            "data": {
                "activity_cart": {
                    "merge_list": [],
                    "untuck_list": []
                },
                "activity_qrcode": "",
                "activity_rule_info": {
                    "activity_ids": "",
                    "activity_status": 2,
                    "activity_type": 14,
                    "auth_phone": 2,
                    "community_status": 2,
                    "coupon_id": None,
                    "cron_up_at": 0,
                    "deleted_at": 0,
                    "duration": 3600,
                    "end_at": 1622390400,
                    "enterprise_id": 140269187892096,
                    "extract_end_at": 0,
                    "extract_start_at": 0,
                    "extract_time_status": 0,
                    "goods_down_status": 1,
                    "id": 149254443583744,
                    "is_deal": 2,
                    "is_join_cart": 2,
                    "is_limit_buy": None,
                    "line_price_status": 1,
                    "n_piece": None,
                    "n_price": None,
                    "name": 123123,
                    "need_num": 5,
                    "need_switch": 2,
                    "post_sale_type": 2,
                    "postage": 0,
                    "postage_status": 2,
                    "quota_num": 0,
                    "quota_status": 2,
                    "sale_type": 1,
                    "server_time": 1619150204,
                    "show_zero_stock": 1,
                    "sort_spu_text": None,
                    "start_at": 1619193600,
                    "state_text": None,
                    "store_ids": [],
                    "termination_at": 1622394000,
                    "up_type": 1
                },
                "activity_spu_list": {
                    "alone_spu": [],
                    "double_spu": []
                },
                "app_info": {
                    "app_id": "wx33133af0bae30971",
                    "app_name": "白泽信息科技",
                    "logo": "https://wx.qlogo.cn/mmopen/HGAuVvdbccicgEBvjoSK5swXVSGab2IbcakdwKPbRMW2ibKtbZ3mTQaouiaGgAiauc7s7JmiaFxKToDV5yEicvDcZBEHG8LffBWnnU/0"
                },
                "coupon_info": [],
                "is_can_buy": 1,
                "is_show_bubble": 1
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("加购(buy_out_price_edit_cart)")
    @pytest.mark.onLineIndex
    @pytest.mark.skip("数据有误")
    def test_messagePush_buy_out_price_edit_cart(self, ini):
        body = {
                "method":"activity.buy_out_price_edit_cart",
                "platform":"crs",
                "data":{
                       "enterprise_id":140269187892096,
                       "user_id": 147478118478720,
                        "activity_rule_id":"149254443583744",
                        "sku_id":147694816208960,
                        "spu_id":147694816148160,
                        "sku_picture":"https:\/\/img-crs.vchangyi.com\/goods16149152407290.jpg",
                        "sku_name":"口红合集041416240028WY",
                        "attribute_arr":["21"],
                        "on_line_price":1,
                        "operate_type":"add",
                        "num":1
                    }
            }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "05ef900f-2038-4c7a-8e0f-11daba637fc8",
            "data": {
                "activity_cart": {
                    "merge_list": [],
                    "untuck_list": []
                },
                "activity_qrcode": "",
                "activity_rule_info": {
                    "activity_ids": "",
                    "activity_status": 2,
                    "activity_type": 14,
                    "auth_phone": 2,
                    "community_status": 2,
                    "coupon_id": None,
                    "cron_up_at": 0,
                    "deleted_at": 0,
                    "duration": 3600,
                    "end_at": 1622390400,
                    "enterprise_id": 140269187892096,
                    "extract_end_at": 0,
                    "extract_start_at": 0,
                    "extract_time_status": 0,
                    "goods_down_status": 1,
                    "id": 149254443583744,
                    "is_deal": 2,
                    "is_join_cart": 2,
                    "is_limit_buy": None,
                    "line_price_status": 1,
                    "n_piece": None,
                    "n_price": None,
                    "name": 123123,
                    "need_num": 5,
                    "need_switch": 2,
                    "post_sale_type": 2,
                    "postage": 0,
                    "postage_status": 2,
                    "quota_num": 0,
                    "quota_status": 2,
                    "sale_type": 1,
                    "server_time": 1619150204,
                    "show_zero_stock": 1,
                    "sort_spu_text": None,
                    "start_at": 1619193600,
                    "state_text": None,
                    "store_ids": [],
                    "termination_at": 1622394000,
                    "up_type": 1
                },
                "activity_spu_list": {
                    "alone_spu": [],
                    "double_spu": []
                },
                "app_info": {
                    "app_id": "wx33133af0bae30971",
                    "app_name": "白泽信息科技",
                    "logo": "https://wx.qlogo.cn/mmopen/HGAuVvdbccicgEBvjoSK5swXVSGab2IbcakdwKPbRMW2ibKtbZ3mTQaouiaGgAiauc7s7JmiaFxKToDV5yEicvDcZBEHG8LffBWnnU/0"
                },
                "coupon_info": [],
                "is_can_buy": 1,
                "is_show_bubble": 1
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("清除加购缓存(buy_out_price_del_cart)")
    @pytest.mark.onLineIndex
    @pytest.mark.skip("数据有误")
    def test_messagePush_buy_out_price_del_cart(self, ini):
        body = {
            "method": "activity.buy_out_price_del_cart",
            "platform": "crs",
            "data": {
                "enterprise_id": 140269187892096,
                "user_id": 147478118478720,
                "activity_rule_id": "149254443583744",
                "mark_id": 116865742399296
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "05ef900f-2038-4c7a-8e0f-11daba637fc8",
            "data": {
                "activity_cart": {
                    "merge_list": [],
                    "untuck_list": []
                },
                "activity_qrcode": "",
                "activity_rule_info": {
                    "activity_ids": "",
                    "activity_status": 2,
                    "activity_type": 14,
                    "auth_phone": 2,
                    "community_status": 2,
                    "coupon_id": None,
                    "cron_up_at": 0,
                    "deleted_at": 0,
                    "duration": 3600,
                    "end_at": 1622390400,
                    "enterprise_id": 140269187892096,
                    "extract_end_at": 0,
                    "extract_start_at": 0,
                    "extract_time_status": 0,
                    "goods_down_status": 1,
                    "id": 149254443583744,
                    "is_deal": 2,
                    "is_join_cart": 2,
                    "is_limit_buy": None,
                    "line_price_status": 1,
                    "n_piece": None,
                    "n_price": None,
                    "name": 123123,
                    "need_num": 5,
                    "need_switch": 2,
                    "post_sale_type": 2,
                    "postage": 0,
                    "postage_status": 2,
                    "quota_num": 0,
                    "quota_status": 2,
                    "sale_type": 1,
                    "server_time": 1619150204,
                    "show_zero_stock": 1,
                    "sort_spu_text": None,
                    "start_at": 1619193600,
                    "state_text": None,
                    "store_ids": [],
                    "termination_at": 1622394000,
                    "up_type": 1
                },
                "activity_spu_list": {
                    "alone_spu": [],
                    "double_spu": []
                },
                "app_info": {
                    "app_id": "wx33133af0bae30971",
                    "app_name": "白泽信息科技",
                    "logo": "https://wx.qlogo.cn/mmopen/HGAuVvdbccicgEBvjoSK5swXVSGab2IbcakdwKPbRMW2ibKtbZ3mTQaouiaGgAiauc7s7JmiaFxKToDV5yEicvDcZBEHG8LffBWnnU/0"
                },
                "coupon_info": [],
                "is_can_buy": 1,
                "is_show_bubble": 1
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("根据skuIDs获取活动信息(activity_by_sku)")
    @pytest.mark.onLineIndex
    def test_messagePush_activity_by_sku(self, ini):
        body = {
                "method": "activity.activity_by_sku",
                "platform": "crs",
                "data": {
                    "enterprise_id": 140269187892096,
                    "user_id": 147478118478720,
                    "sku_ids": [
                        147694816208960
                    ]
                }
            }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {'code': 200,
                    'message': 'success',
                    'request_id': '410efa59-7d82-42e0-bcd5-90a4acd1c12c',
                    'data': {
                        'list': [
                            {
                                'activity_price': 100,
                                'activity_rule_id': 149254443583744,
                                'activity_rule_status': 2,
                                'activity_status': 1,
                                'activity_stock': 11122,
                                'activity_stock_set': 11122,
                                'activity_stock_type': 1,
                                'created_at': 1619150146,
                                'deleted_at': 0,
                                'enterprise_id': 140269187892096,
                                'id': 149254444678272,
                                'is_activity': 1,
                                'material_id': 146774972228928,
                                'quota_enable': 2,
                                'rule': {
                                    'activity_ids': '',
                                    'activity_status': 2,
                                    'activity_type': 14,
                                    'auth_phone': 2,
                                    'community_status': 2,
                                    'coupon_id': 0,
                                    'cron_up_at': 0,
                                    'deleted_at': 0,
                                    'duration': 3600,
                                    'end_at': 1622390400,
                                    'enterprise_id': 140269187892096,
                                    'extract_end_at': 0,
                                    'extract_start_at': 0,
                                    'extract_time_status': 0,
                                    'goods_down_status': 1,
                                    'id': 149254443583744,
                                    'is_deal': 2,
                                    'is_join_cart': 2,
                                    'line_price_status': 1,
                                    'name': 123123,
                                    'need_num': 5,
                                    'need_switch': 2,
                                    'post_sale_type': 2,
                                    'postage': 0,
                                    'postage_status': 2,
                                    'quota_num': 0,
                                    'quota_status': 2,
                                    'robot_status': 2,
                                    'sale_type': 1,
                                    'start_at': 1619193600,
                                    'state_text': '{"share_content":"123","share_type":2,"share_img":"https://img-crs.vchangyi.com/public/2021/04/23/f6c96b22b042a9a271f447aea16fcc2f.png"}',
                                    'store_ids': [],
                                    'termination_at': 1622394000,
                                    'up_type': 1,
                                    'wait_list_status': 1
                                },
                                'sell_price': 100,
                                'sku_id': 147694816208960,
                                'sku_picture': '',
                                'spu_id': 147694816148160,
                                'type': 14,
                                'updated_at': 1619161524,
                                'user_activity_info': []
                            }
                        ]
                    }
                    }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("验证商品库存(vali_activity_stock)")
    @pytest.mark.onLineIndex
    def test_messagePush_vali_activity_stock(self, ini):
        body = {
                "method": "activity.vali_activity_stock",
                "platform": "crs",
                "data": {
                    "enterprise_id": 140269187892096,
                    "goods_list": [
                        {
                            "activity_id": '149254443583744',
                            "activity_type": 14,
                            "sku_id": 149254444678272,
                            "num": 11122
                        }
                    ]
                }
            }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
                    "code":200072,
                    "message":"业务端错误:抱歉，活动商品库存不足",
                    "request_id":"1334ab66-a706-4477-8cc7-681f10b8db3c",
                    "data":{
                        "activity_id":"149254443583744",
                        "activity_type":14,
                        "num":11122,
                        "sku_id":149254444678272
                    }
                }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("获取活动商品列表(goods_list_all)")
    @pytest.mark.onLineIndex
    def test_messagePush_goods_list_all(self, ini):
        body = {
                "method": "activity.goods_list_all",
                "platform": "crs",
                "data": {
                    "enterprise_id": 140269187892096,
                    "activity_rule_id": 149254443583744
                }
            }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
                    "code":200,
                    "message":"success",
                    "request_id":"7f89c81e-455b-4d75-aa61-4a97571958de",
                    "data":{
                        "list":[
                            {
                                "activity_price":100,
                                "activity_status":1,
                                "activity_stock":11122,
                                "activity_stock_set":11122,
                                "activity_stock_type":1,
                                "attribute_data":[
                                    {
                                        "attribute_item_value":"大",
                                        "attribute_name":"大小"
                                    },
                                    {
                                        "attribute_item_value":"黄",
                                        "attribute_name":"颜色"
                                    }
                                ],
                                "enterprise_id":140269187892096,
                                "goods_pic":"https://img-crs.vchangyi.com/goods16149152215180.jpg",
                                "id":149254444678272,
                                "is_activity":1,
                                "market_price":0,
                                "material_id":146774972228928,
                                "name":"口红合集041416240028WY",
                                "on_line_price":100,
                                "picture_url":"https://img-crs.vchangyi.com/goods16149152407290.jpg",
                                "sale_stock":0,
                                "sell_price":100,
                                "sign_price":2000,
                                "sku_id":147694816208960,
                                "sku_name":"口红合集041416240028WY",
                                "sku_no":"xtwl001",
                                "sku_picture":"https://img-crs.vchangyi.com/goods16149152407290.jpg",
                                "spu_id":147694816148160,
                                "spu_name":"口红合集041416240028WY",
                                "stock":99982997
                            }
                        ],
                        "page":1,
                        "size":10,
                        "total":1
                    }
                }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("门店新增(store_add)")
    @pytest.mark.onLineIndex
    def test_messagePush_store_add(self, ini):
        body = {
                "method":"store.store_add",
                "platform":"crs",
                "data":{
                }
            }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
                    "code": 200,
                    "message": "success",
                    "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
                    "data": {
                        "msg_id": "19984723346456603"
                    }
                }
        Res = self.shop.match_class(examples, res)
        print(Res)

    @allure.story("门店更新(store_update)")
    @pytest.mark.onLineIndexs
    def test_messagePush_store_update(self, ini):
        body = {
            "method": "store.store_update",
            "platform": "crs",
            "data": {
            }
        }
        # print("openAPI res: {0}".format(ShopForDDCApi.sendRequest(body)))
        res = ShopForDDCApi.sendRequest(body)
        print(res)
        examples = {
            "code": 200,
            "message": "success",
            "request_id": "8944e520-ac50-40d8-b643-f75d8dc736cd",
            "data": {
                "msg_id": "19984723346456603"
            }
        }
        Res = self.shop.match_class(examples, res)
        print(Res)


