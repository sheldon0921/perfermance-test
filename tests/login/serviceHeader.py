from utils.myTime import Mytime
import hashlib


class ServiceHeader(object):
    """
    构造服务(Service)接口的请求头
    """
    @staticmethod
    def getServiceHeader(authClient, enterpriseHash):
        hl = hashlib.md5()
        timeStamp = str(Mytime.getCurrTimeStamp())
        string = authClient + "7719f7e743c7e8b294dc50567ce23b57" + timeStamp
        hl.update(string.encode(encoding='utf-8'))
        encryptionStr = hl.hexdigest()
        header = {
            "Auth-Client": authClient,
            "Auth-Sign": encryptionStr,
            "Auth-Timestamp": timeStamp,
            "ep-version": "5",
            "enterprise-hash": enterpriseHash
        }
        return header


