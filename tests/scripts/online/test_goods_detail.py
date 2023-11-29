from tests.common.sendRequest.sendRequestForOnline import SendRequestForOnline
from tests.common.onLine.goodsDetail import GoodsDetail
from tests.common.onLine.getGoodsSpu import GetGoodsSpu
from utils.readerIniFile import ReaderIniFile
from utils.readerFile import ReaderFile
from utils.parseJson import ParseJson
import json, pytest, allure
from log.log import Logger



@allure.feature("商品")
class Test_Goods_Detail:

    @pytest.fixture()
    def ini(self):
        # 实例化对象
        self.logger = Logger.Logger()
        self.goods = GoodsDetail()
        self.getspu= GetGoodsSpu()
        self.parseJson = ParseJson()
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")
        yield self.logger, self.goods, self.shopBaseUrl, self.parseJson


    @allure.story("查询商品详情")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    def test_get_goods_detail(self, enterpriseInfo,ini):
        '''商品详情接口'''
        # print("unique enterprise info: {0}".format(enterpriseInfo))
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]

        Res=self.getspu.get_goods_spu(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        if len(Res['data']['list'])>0:
            spu_id=Res['data']['list'][0]['spu_id']
            sku_id=Res['data']['list'][0]['default_sku_id']
            goodsName = Res['data']['list'][0]['sku_name']
            
        else:
            self.logger.info('{0}商品上架中'.format(enterpriName))
            return
        # spu_id = enterpriseInfo["spu_id"]
        # sku_id = enterpriseInfo["sku_id"]
        # print("\nenterpriName: ",enterpriName,"enterpriseHash: ", enterpriseHash)
        datas = {"spu_id":spu_id,"sku_id":sku_id,"api_type":1}
        self.logger.info('spu{0}'.format(spu_id))
        self.logger.info('sku{0}'.format(sku_id))
        with allure.step(f"查询 {enterpriName} 的 {goodsName} 商品详情页面"):
            res = self.goods.get_goods_detail(datas=datas, enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        # print("goods detail interface response msg: ", res)
        assert res.status_code == 200

    @allure.story("商品详情页接口")
    @pytest.mark.parametrize("enterpriseInfo", ReaderFile.readerJson("onLineEnterpriseInfo.json"))
    @pytest.mark.onLineIndex
    def test_spu_list(self, enterpriseInfo, ini):
        '''商品详情接口'''
        self.logger.info("unique enterprise info: {0}".format(enterpriseInfo))
        enterpriName = enterpriseInfo["enterpriName"]
        enterpriseID = enterpriseInfo["enterpriseID"]
        enterpriseHash = enterpriseInfo["enterpriseHash"]

        Res = self.getspu.get_goods_spu(enterpriseHash=enterpriseHash, enterpriseID=enterpriseID)
        if len(Res['data']['list']) > 0:
            spu_id = Res['data']['list'][0]['spu_id']
            sku_id = Res['data']['list'][0]['default_sku_id']
            goodsName = Res['data']['list'][0]['sku_name']
        else:
            self.logger.info('{0}商品上架中'.format(enterpriName))
            return

        param = {"spu_id":spu_id,"type":1,"enterprise_id":"","sku_id":sku_id,"api_type":1}
        url = "{0}/gw-shop/app/v1/common/encrypt-short-link".format(self.shopBaseUrl)
        sendRequest = SendRequestForOnline(enterpriseInfo)
        spuListRes = sendRequest.sendRequest(url, param).json()
        print("spuListRes: {0}".format(spuListRes))
        with allure.step(f"查询 {enterpriName} 的 {goodsName} 商品详情页面的encrypt-short-link"):
            spuListRes["code"] == 200 and spuListRes["message"] == "success"


        param = {"spu_id":spu_id,"page":1,"size":5}
        url = "{0}/gw-shop/app/v1/goods/comment-list".format(self.shopBaseUrl)
        commonLstRes = sendRequest.sendRequest(url, param).json()
        print("commonLstRes: {0}".format(commonLstRes))
        with allure.step(f"查询 {enterpriName} 的 {goodsName} 商品详情页面的common-list"):
            commonLstRes["code"] == 200 and commonLstRes["message"] == "success"

        param = {"sku_id": sku_id, "activity_id": "", "module": "default",
         "wx_area": {"province": {"id": 27, "full_name": "陕西", "lat": "34.264860", "lng": "108.954240"},
                     "city": {"id": 423, "full_name": "西安", "lat": "34.341270", "lng": "108.939840"},
                     "district": {"id": 5072, "full_name": "雁塔区", "lat": "34.222590", "lng": "108.948780"},
                     "address": "西部国际广场(西安市雁塔区高新路2号)"}}
        url = "{0}/gw-shop/app/v1/goods/sku-postage".format(self.shopBaseUrl)
        skuPostageRes = sendRequest.sendRequest(url, param).json()
        print("skuPostageRes: {0}".format(skuPostageRes))
        with allure.step(f"查询 {enterpriName} 的 {goodsName} 商品详情页面的sku-postage接口"):
            skuPostageRes["code"] == 200 and skuPostageRes["message"] == "success"

        param = {"object_ids":[sku_id],"object_type":12}
        url = "{0}/gw-shop/app/v1/common/subscribe-status".format(self.shopBaseUrl)
        subscribeStatusRes = sendRequest.sendRequest(url, param).json()
        print("subscribeStatusRes: {0}".format(subscribeStatusRes))
        with allure.step(f"查询 {enterpriName} 的 {goodsName} 商品详情页面的subscribe-status接口"):
            subscribeStatusRes["code"] == 200 and subscribeStatusRes["message"] == "success"


        param = {"page":1,"size":10000, "coupon_type":3, "spu_id": spu_id, "sku_id": sku_id}
        url = "{0}/gw-shop/app/v1/coupon/list".format(self.shopBaseUrl)
        wxCouponRes = sendRequest.sendRequest(url, param, "Get").json()
        print("wxCouponRes: {0}".format(wxCouponRes))
        try:
            resList = self.parseJson.parseJson(wxCouponRes, *["data", "list[0]"])
        except StopIteration:
            return
        print("resList: {0}".format(resList))
        # if len(resList) == 0:
        #     return
        print("resList: {0}".format(resList))
        couponId = resList[0]["id"]
        couponType = resList[0]["coupon_type"]
        param = {"merchant_coupon_stock_id":"","out_request_no":"","coupon_id":couponId,"mem_uid":"","coupon_type":couponType}
        url = "{0}/gw-shop/app/v1/coupon_user/check".format(self.shopBaseUrl)
        couponUsrChkRes = sendRequest.sendRequest(url,param).json()
        with allure.step(f"查询 {enterpriName} 的 {goodsName} 商品详情页面的coupon_user/check接口"):
            couponUsrChkRes["code"] == 200 and couponUsrChkRes["message"] == "success"

        param = {"sku_id":sku_id,"number":1,"delivery_type":1}
        url = "{0}/gw-shop/app/v1/store-cart/add".format(self.shopBaseUrl)
        addCartRes = sendRequest.sendRequest(url, param).json()
        with allure.step(f"查询 {enterpriName} 的 {goodsName} 商品详情页面加入购物车"):
            addCartRes["code"] == 200 and addCartRes["message"] == "success"

