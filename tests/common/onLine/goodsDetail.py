import json
from tests.login.login import Login
from tests.login.singletonHttpClient import SingletonHttpClient
from utils.readerIniFile import ReaderIniFile
from utils.myTime import Mytime
from utils.myRandom import MyRandom



class GoodsDetail:

    def __init__(self):
        self.httpClient = SingletonHttpClient.get_instance(flag="onLine")
        self.shopBaseUrl = ReaderIniFile.value(key="shopBaseUrl")

    def get_goods_detail(self, datas, enterpriseHash, enterpriseID):
        # 发送登录请求，获取token
        res = Login.loginNew(enterpriseID=enterpriseID)
        token = res["data"]["token"]
        timeStamp = Mytime.getCurrTimeStamp()
        randomStr = MyRandom.getRandomStr(2)
        xRequestId = 'autoTest-7b9d-4091-b4af-{0}{1}'.format(randomStr, timeStamp)
        headers = {
                   'token': token,
                   'Enterprise-Hash': enterpriseHash,
                   'App-Version': 'V1.7.2',
                   'X-Request-ID': xRequestId
        }
        url = "{0}/gw-shop/app/v1/goods/detail".format(self.shopBaseUrl)
        # res = requests.post(url=url, json=datas, headers=headers)
        res = self.httpClient.Post(url=url, json=datas, headers=headers)
        if res.status_code == 200:
            # return res.json()
            return res
        else:
            raise Exception("Call /gw-shop/app/v1/goods/detail interface failed !", res.text)

