from tests.common.goods.console.specTemplate import SpecTemplate
from tests.common.goods.console.postage import Postage
from log.log import Logger
from utils.readerFile import ReaderFile
from utils.myJson import MyJson
from tests.common.goods.console.postage import Postage
from utils.myTime import Mytime
from tests.common.goods.console.goods import Goods
import time
import pytest
import allure
"""
测试步骤：
1、添加部门，点击确定
"""

@allure.feature('基础')
class Test_department_add(object):

    def test_department_add(self, ini):
        # 新增商品，点击确定
        self.code= "autobm"
        self.title= "auto001"
        self.type= 16
        self.f_id= 8
        self.service= 1
        self.service_id= 15
        










