from tests.common.sendRequest.sendRequestForOnline import SendRequestForOnline
from tests.common.onLineForSupermarket.categoryForSm import CategoryForSm
from utils.readerIniFile import ReaderIniFile
from utils.parseJson import ParseJson
from utils.readerFile import ReaderFile
import json, pytest, allure
from log.log import Logger


@allure.feature("(商超)小程序分类页")
class Test_Category_Sm:

    @pytest.fixture()
    def ini(self):
        # 实例化对象
        self.logger = Logger.Logger()
        self.category = CategoryForSm()
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")
        yield self.logger, self.shopBaseUrl

    @allure.story("分类页数据是否正常")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo(supermarket).json"))
    @pytest.mark.onLineSupermarket
    def test_category_list_sm(self, enterpriseInfo, ini):
        """
        分类页商品数据正常
        """
        # 判断业务接口是否正常
        print("response message: {0}".format(self.category.categoryList(enterpriseInfo).json()))
        categoryList = self.category.categoryList(enterpriseInfo).json()
        assert categoryList["code"] == 200
        assert categoryList["message"] == "success"
        # 判断业务接口逻辑是否正常
        categoryData = ParseJson.parseJson(categoryList, *["data", "list"])[0]
        self.logger.info("categoryData: {0}".format(categoryData))
        if len(categoryData) != 0:
            # for category in categoryData:
            for i in range(0, len(categoryData)):
                if i != 0:
                    beforeSkuIdArray = skuIdArray
                resData = self.category.categoryData(enterpriseInfo, categoryData[i]["id"])
                skuIdArray = ParseJson.getAllValue(resData, "sku_id")
                # skuIdArray = ParseJson.parse_json_by_objectpath(resData, "$..sku_id")
                if i !=0 and len(beforeSkuIdArray) != 0 and beforeSkuIdArray.sort() != None:
                    assert len(beforeSkuIdArray) != len(skuIdArray) \
                        or beforeSkuIdArray.sort() != skuIdArray.sort()

                print(resData)






