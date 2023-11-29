from tests.login.singletonHttpClient import SingletonHttpClient
from utils.readerIniFile import ReaderIniFile
from utils.myTime import Mytime
from utils.sign import Sign


class ShopForDDCApi(object):

    @staticmethod
    def sendRequest(requestParams):
        # 构造请求Url
        baseUrl = ReaderIniFile.value(section="console_sys_info", key="consoleBaseUrl")
        url = f"{baseUrl}/micro-ddc/message/push"
        # 对请求体进行加密
        sign = Sign.generateSign(params=requestParams,secret=ReaderIniFile.value(section="open-api", key="crsAuthSecret"))
        # 构造header头
        headers = {
            "appKey": ReaderIniFile.value(section="open-api", key="crsAuthKey"),
            # "sign": sign,
            "sign":"CRS.micro",
            # "debug": "CRS.micro",
            "timestamp": str(Mytime.getCurrTimeStamp())
        }
        print("headers: {0}".format(headers))
        # 获取发送请求的实例，并发送请求
        httpClient = SingletonHttpClient.get_instance("openApi")
        res = httpClient.Post(url=url, headers=headers, json=requestParams)
        return res.json()
