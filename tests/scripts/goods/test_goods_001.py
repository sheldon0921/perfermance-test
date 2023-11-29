from tests.common.goods.shop.goods import Goods
import pytest
from log.log import Logger
from utils.readerFile import ReaderFile
from utils.myJson import MyJson
import json
import allure

# import allure

'''
前置条件：

测试步骤：

测试结果：
'''


@allure.feature('商品')
class Test_goods_add_001:

    @pytest.fixture()
    def ini(self):
        # 脚本前置操作
        yield

        # 脚本后置操作

    # @pytest.mark.skip(reason="脚本模板")
    @pytest.mark.smoke
    def test_goods_query_001(self):
        # 实际脚本内容
        assert 1 == 1

    @pytest.mark.smoke
    @allure.story('999999999999')
    def test_goods_002(self):
        assert 1 == 1.0
