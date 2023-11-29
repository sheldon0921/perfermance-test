import json
from tests.login.login import Login
from tests.login.singletonHttpClient import SingletonHttpClient
from utils.readerIniFile import ReaderIniFile
from utils.myTime import Mytime
from utils.myRandom import MyRandom


class User:
    def __init__(self):
        self.httpClient = SingletonHttpClient.get_instance(flag="onLine")
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")

    def get_user_detail(self, enterpriseHash, enterpriseID):
        # 发送登录请求，获取token
        res = Login.loginNew(enterpriseID=enterpriseID)
        token = res["data"]["token"]
        app_version = res['data']['app_version']
        timeStamp = Mytime.getCurrTimeStamp()
        randomStr = MyRandom.getRandomStr(2)
        xRequestId = 'autoTest-7b9d-4091-b4af-{0}{1}'.format(randomStr, timeStamp)
        headers = {
            'Token': token,
            'Enterprise-Hash': enterpriseHash,
            'App-Version': app_version,
            'Ep-Version': '5',
            'content-type': 'application/json',
            'X-Request-ID': xRequestId
        }
        url = "{0}/gw-shop/app/v1/user/detail".format(self.shopBaseUrl)
        res = self.httpClient.GET(url=url, headers=headers)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call /gw-shop/app/v1/user/detail interface failed !", res.text)


class LiveBroadCast:
    def __init__(self):
        self.httpClient = SingletonHttpClient.get_instance(flag="onLine")
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")

    # @params token 用户登录token
    # @params datas 请求数据
    # @response 将接口返回的数据直接返回给调用方进行处理
    def list_live_broadcast(self, datas, enterpriseID, enterpriseHash):
        res = Login.loginNew(enterpriseID=enterpriseID)
        token = res["data"]["token"]
        app_version = res['data']['app_version']
        timeStamp = Mytime.getCurrTimeStamp()
        randomStr = MyRandom.getRandomStr(2)
        xRequestId = 'autoTest-7b9d-4091-b4af-{0}{1}'.format(randomStr, timeStamp)
        headers = {
            'Token': token,
            'Enterprise-Hash': enterpriseHash,
            'App-Version': app_version,
            'Ep-Version': '5',
            'content-type': 'application/json',
            'X-Request-ID': xRequestId
        }
        url = "{0}/gw-shop/app/v1/app-center/live-broadcast/list".format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url, json=datas, headers=headers)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call /gw-shop/app/v1/app-center/live-broadcast/list interface failed !", res.text)


class TabRedHot:
    def __init__(self):
        self.httpClient = SingletonHttpClient.get_instance(flag="onLine")
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")

    def get_tab_red_dot(self, enterpriseHash, enterpriseID):
        res = Login.loginNew(enterpriseID=enterpriseID)
        token = res["data"]["token"]
        app_version = res['data']['app_version']
        timeStamp = Mytime.getCurrTimeStamp()
        randomStr = MyRandom.getRandomStr(2)
        xRequestId = 'autoTest-7b9d-4091-b4af-{0}{1}'.format(randomStr, timeStamp)
        headers = {
            'Token': token,
            'Enterprise-Hash': enterpriseHash,
            'App-Version': app_version,
            'Ep-Version': '5',
            'content-type': 'application/json',
            'X-Request-ID': xRequestId
        }
        url = "{0}/gw-shop/app/v1/content-manage/tab-red-dot".format(self.shopBaseUrl)
        res = self.httpClient.GET(url=url, headers=headers)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call /gw-shop/app/v1/content-manage/tab-red-dot interface failed !", res.text)


class PopContent:
    def __init__(self):
        self.httpClient = SingletonHttpClient.get_instance(flag="onLine")
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")

    def pop_content(self, datas, enterpriseHash, enterpriseID):
        res = Login.loginNew(enterpriseID=enterpriseID)
        token = res["data"]["token"]
        app_version = res['data']['app_version']
        timeStamp = Mytime.getCurrTimeStamp()
        randomStr = MyRandom.getRandomStr(2)
        xRequestId = 'autoTest-7b9d-4091-b4af-{0}{1}'.format(randomStr, timeStamp)
        headers = {
            'Token': token,
            'Enterprise-Hash': enterpriseHash,
            'App-Version': app_version,
            'Ep-Version': '5',
            'content-type': 'application/json',
            'X-Request-ID': xRequestId
        }
        url = "{0}/gw-shop/app/v1/page/pop-content".format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url, headers=headers)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call/gw-shop/app/v1/page/pop-content interface failed !", res.text)


class InitialSetting:
    def __init__(self):
        self.httpClient = SingletonHttpClient.get_instance(flag="onLine")
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")

    def initial_Setting(self, datas, enterpriseHash, enterpriseID):
        res = Login.loginNew(enterpriseID=enterpriseID)
        token = res["data"]["token"]
        app_version = res['data']['app_version']
        timeStamp = Mytime.getCurrTimeStamp()
        randomStr = MyRandom.getRandomStr(2)
        xRequestId = 'autoTest-7b9d-4091-b4af-{0}{1}'.format(randomStr, timeStamp)
        headers = {
            'Token': token,
            'Enterprise-Hash': enterpriseHash,
            'App-Version': app_version,
            'Ep-Version': '5',
            'content-type': 'application/json',
            'X-Request-ID': xRequestId
        }
        url = "{0}/gw-shop/app/v1/common/initial-setting".format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url, headers=headers)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call /gw-shop/app/v1/common/initial-setting failed !", res.text)


class ShopShareImage:
    def __init__(self):
        self.httpClient = SingletonHttpClient.get_instance(flag="onLine")
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")

    def shop_share_image(self, enterpriseHash, enterpriseID):
        res = Login.loginNew(enterpriseID=enterpriseID)
        token = res["data"]["token"]
        app_version = res['data']['app_version']
        timeStamp = Mytime.getCurrTimeStamp()
        randomStr = MyRandom.getRandomStr(2)
        xRequestId = 'autoTest-7b9d-4091-b4af-{0}{1}'.format(randomStr, timeStamp)
        headers = {
            'Token': token,
            'Enterprise-Hash': enterpriseHash,
            'App-Version': app_version,
            'Ep-Version': '5',
            'content-type': 'application/json',
            'X-Request-ID': xRequestId
        }
        url = "{0}/gw-shop/app/v1/shop/share-image".format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url, headers=headers)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call /gw-shop/app/v1/shop/share-image failed !", res.text)


class CommonConfig:
    def __init__(self):
        self.httpClient = SingletonHttpClient.get_instance(flag="onLine")
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")

    def common_config(self, enterpriseHash, enterpriseID):
        res = Login.loginNew(enterpriseID=enterpriseID)
        token = res["data"]["token"]
        app_version = res['data']['app_version']
        timeStamp = Mytime.getCurrTimeStamp()
        randomStr = MyRandom.getRandomStr(2)
        xRequestId = 'autoTest-7b9d-4091-b4af-{0}{1}'.format(randomStr, timeStamp)
        headers = {
            'Token': token,
            'Enterprise-Hash': enterpriseHash,
            'App-Version': app_version,
            'Ep-Version': '5',
            'content-type': 'application/json',
            'X-Request-ID': xRequestId
        }
        url = "{0}/gw-shop/app/v1/common/config".format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url, headers=headers)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call /gw-shop/app/v1/common/config !", res.text)


class PageConfig:
    def __init__(self):
        self.httpClient = SingletonHttpClient.get_instance(flag="onLine")
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")

    def page_config(self, datas, header):

        url = "{0}/gw-shop/app/v1/new-template/page-config".format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url, headers=header, json=datas)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call /gw-shop/app/v1/new-template/page-config !", res.text)


class UserExtractOrder:
    def __init__(self):
        self.httpClient = SingletonHttpClient.get_instance(flag="onLine")
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")

    def user_extract_order(self, enterpriseHash, enterpriseID):
        res = Login.loginNew(enterpriseID=enterpriseID)
        token = res["data"]["token"]
        app_version = res['data']['app_version']
        timeStamp = Mytime.getCurrTimeStamp()
        randomStr = MyRandom.getRandomStr(2)
        xRequestId = 'autoTest-7b9d-4091-b4af-{0}{1}'.format(randomStr, timeStamp)
        headers = {
            'Token': token,
            'Enterprise-Hash': enterpriseHash,
            'App-Version': app_version,
            'Ep-Version': '5',
            'content-type': 'application/json',
            'X-Request-ID': xRequestId
        }
        url = "{0}/gw-shop/app/v1/user/user-extract-order".format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url, headers=headers)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call /gw-shop/app/v1/user/user-extract-order !", res.text)


class WriteTrace:
    def __init__(self):
        self.httpClient = SingletonHttpClient.get_instance(flag="onLine")
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")
        self.consoleBaseUrl = ReaderIniFile.value(section="console_sys_info",key="consoleBaseUrl")

    def write_trace(self, enterpriseHash, enterpriseID, params):
        res = Login.loginNew(enterpriseID=enterpriseID)
        token = res["data"]["token"]
        app_version = res['data']['app_version']
        timeStamp = Mytime.getCurrTimeStamp()
        randomStr = MyRandom.getRandomStr(2)
        xRequestId = 'autoTest-7b9d-4091-b4af-{0}{1}'.format(randomStr, timeStamp)
        headers = {
            'Token': token,
            'Enterprise-Hash': enterpriseHash,
            'App-Version': app_version,
            'Ep-Version': '5',
            'content-type': 'application/json',
            'X-Request-ID': xRequestId
        }
        url = "{0}/gw-shop/app/v1/trace/write-trace".format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url, headers=headers, json=params)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call /gw-shop/app/v1/trace/write-trace !", res.text)

    def getAgreements(self,header):
        location = "/gw-shop/app/v1/user/get-agreements"
        url = "{0}{1}".format(self.shopBaseUrl,location)
        res = self.httpClient.GET(url=url, headers=header,json={})
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call {0} !".format(location), res.text)


    def newTemplateIndex(self,header,param):
        location = "/gw-shop/app/v1/user/get-agreements"
        url = "{0}{1}".format(self.consoleBaseUrl,location)
        res = self.httpClient.GET(url=url, headers=header,json=param)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call {0} !".format(location), res.text)


    def categoryList(self,header,param):
        location = "/gw-shop/app/v1/category/category-list"
        url = "{0}{1}".format(self.shopBaseUrl,location)
        res = self.httpClient.Post(url=url, headers=header,json=param)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call {0} !".format(location), res.text)

    def cleanGoodsFoot(self,header,param):
        location = "/gw-shop/app/v1/goods-footprint/clear"
        url = "{0}{1}".format(self.shopBaseUrl,location)
        res = self.httpClient.Post(url=url, headers=header,json=param)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call {0} !".format(location), res.text)


    def scoreLog(self,header,param):
        location = "/gw-shop/app/v1/score/log"
        url = "{0}{1}".format(self.shopBaseUrl,location)
        res = self.httpClient.GET(url=url, headers=header,params=param)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call {0} !".format(location), res.text)


    def userCenterEdit(self,header,param):
        location = "/gw-shop/app/v1/user-center/edit"
        url = "{0}{1}".format(self.shopBaseUrl,location)
        res = self.httpClient.Post(url=url, headers=header,json=param)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call {0} !".format(location), res.text)


    def mentionCode(self,header,param):
        location = "/gw-shop/app/v1/store-order/mention-code"
        url = "{0}{1}".format(self.shopBaseUrl,location)
        res = self.httpClient.Post(url=url, headers=header,json=param)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call {0} !".format(location), res.text)


    def initialSetting(self,header,param):
        location = "/gw-shop/app/v1/common/initial-setting"
        url = "{0}{1}".format(self.shopBaseUrl,location)
        res = self.httpClient.Post(url=url, headers=header,json=param)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call {0} !".format(location), res.text)


    def addressByKeywords(self,header,param):
        location = "/gw-shop/app/v1/map/address-by-keywords"
        url = "{0}{1}".format(self.shopBaseUrl,location)
        res = self.httpClient.Post(url=url, headers=header,json=param)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call {0} !".format(location), res.text)


    def addressAnalysis(self,header,param):
        location = "/gw-shop/app/v1/map/address-analysis"
        url = "{0}{1}".format(self.shopBaseUrl,location)
        res = self.httpClient.Post(url=url, headers=header,json=param)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call {0} !".format(location), res.text)



class Hotgoods:
    def __init__(self):
        self.httpClient = SingletonHttpClient.get_instance(flag="onLine")
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")

    def hot_sku_list(self, params,header):

        url = "{0}/gw-shop/app/v1/goods/hot-sku-list".format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url, headers=header, json=params)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call /gw-shop/app/v1/goods/hot-sku-list !", res.text)

    def skuDiscountPrice(self,header,params):
        location = "/gw-shop/app/v1/goods/sku-discount-price"
        url = "{0}{1}".format(self.shopBaseUrl,location)
        res = self.httpClient.Post(url=url, headers=header, json=params)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call {0} !".format(location), res.text)

    def goodsDetailQRCode(self,header,params):
        location = "/gw-shop/app/v1/app-code/goods-detail-qrcode"
        url = "{0}{1}".format(self.shopBaseUrl,location)
        res = self.httpClient.Post(url=url, headers=header, json=params)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call {0} !".format(location), res.text)

    def userExtractInfoSave(self,header,params):
        location = "/gw-shop/app/v1/user/user-extract-address-save"
        url = "{0}{1}".format(self.shopBaseUrl,location)
        res = self.httpClient.Post(url=url, headers=header, json=params)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call {0} !".format(location), res.text)

    def joinActivityData(self, header, params):
        location = "/gw-shop/app/v1/collect-bills/join-activity-data"
        url = "{0}{1}".format(self.shopBaseUrl, location)
        res = self.httpClient.Post(url=url, headers=header, json=params)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call {0} !".format(location), res.text)

class VisitExtract:
    def __init__(self):
        self.httpClient = SingletonHttpClient.get_instance(flag="onLine")
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")

    def visit_extract(self, params,header):

        url = "{0}/gw-shop/app/v1/user/visit-extract".format(self.shopBaseUrl)
        res = self.httpClient.Post(url=url, headers=header, json=params)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Call /gw-shop/app/v1/user/visit-extract !", res.text)





if __name__ == '__main__':
    pageconfig = PageConfig()
    enterpriseHash = "284e1ab0778bf2dcce0dee9354918df0"
    enterpriseID = "96900000000000"
    res = pageconfig.page_config(enterpriseID=enterpriseID, enterpriseHash=enterpriseHash)
