from utils.readerIniFile import ReaderIniFile
from tests.login.login import Login
from utils.myTime import Mytime
from utils.myRandom import MyRandom



class ShopForHWJLogin(object):



    @staticmethod
    def loginHWJShop(loginShop="shop"):
        if loginShop is "HWJ":
            enterpriName = "好物集福利社"
            enterpriseID = "78"
            enterpriseHash = "4b3c85a218426cf3fe5ba7e9f093f106"

            loginRes = Login.loginNew(enterpriseID)
            token = loginRes["data"]["token"]
            # token = "eyJpdiI6IjFJM3J3ZTNSVnlib2NmeHE2cXpSR1E9PSIsInZhbHVlIjoiczMwMTdCa1pMQURXMmFrbjRLQ2tJZXBDdEMyWGlVTHNBbFM2enA4NFNFMGZ0M1RRXC9CbGNrSHFEUzFBelNWM2pSRXdzRHlaQXZvZFwvdVpxc0Vwc0FKbDJpVzR1U1M5XC9NNDN2RFhQeHBqY1d1alJjNUc0a3l3XC8wdkJVbTJTSk9tVlRsUGVURVZyRHFubVNMK1wvZGFJc2dzeUgrVE9vNVlHODRtbWxUbHMwYTVlamV3aUJRRjZHdDkwNTBoQVVZNHdUT0tCZFo5VVYrOU9wV3lcL1piT2NzNkJldndKTzZVeDdYZlNYSWRRNit0Yz0iLCJtYWMiOiI1NDRhNzNmOWNjMTNmZGEzZDQ1Y2U0ZjRmMGQwODM5MGQyYmQxMDYxNTYzYWRkMGZhZGMyN2VkMTIzZGFkNGUyIn0="
            xRequestId = 'autoTest-7b9d-4091-b4af-{0}{1}'.format(MyRandom.getRandomStr(2), Mytime.getCurrTimeStamp())
            headers = {
                'X-Adserver-Token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzaWQiOjgwMDI3MjY2NjMzMTUwNDIsInZ0cyI6MTYxMjU3OTU5OH0.1NVLSTgduymtwlTNq4JGhrQf7USQaivnes-mSna_v1c',
                'X-Launch-Option': token,
                'token': token,
                'X-App-Version': 'v02070201',
                'X-Request-ID': xRequestId,
                'X-Wechat-Appid': 'wxde69093658ce8aa8',
                'Content-Type': 'application/json',
                'Enterprise-Hash': enterpriseHash

            }
        elif loginShop == "wd":
            enterpriName = "维达官方商城"
            enterpriseID = "102"
            enterpriseHash = "b83dc24a0d30e9ed38424dd3e62838a7"

            loginRes = Login.loginNew(enterpriseID)
            token = loginRes["data"]["token"]
            # token = "eyJpdiI6IjFJM3J3ZTNSVnlib2NmeHE2cXpSR1E9PSIsInZhbHVlIjoiczMwMTdCa1pMQURXMmFrbjRLQ2tJZXBDdEMyWGlVTHNBbFM2enA4NFNFMGZ0M1RRXC9CbGNrSHFEUzFBelNWM2pSRXdzRHlaQXZvZFwvdVpxc0Vwc0FKbDJpVzR1U1M5XC9NNDN2RFhQeHBqY1d1alJjNUc0a3l3XC8wdkJVbTJTSk9tVlRsUGVURVZyRHFubVNMK1wvZGFJc2dzeUgrVE9vNVlHODRtbWxUbHMwYTVlamV3aUJRRjZHdDkwNTBoQVVZNHdUT0tCZFo5VVYrOU9wV3lcL1piT2NzNkJldndKTzZVeDdYZlNYSWRRNit0Yz0iLCJtYWMiOiI1NDRhNzNmOWNjMTNmZGEzZDQ1Y2U0ZjRmMGQwODM5MGQyYmQxMDYxNTYzYWRkMGZhZGMyN2VkMTIzZGFkNGUyIn0="
            timeStamp = Mytime.getCurrTimeStamp()
            randomStr = MyRandom.getRandomStr(2)
            xRequestId = 'autoTest-7b9d-4091-b4af-{0}{1}'.format(randomStr, timeStamp)
            headers = {
                       'token': token,
                       'Enterprise-Hash': enterpriseHash,
                       # 'App-Version': 'V1.7.2',
                       'X-Request-ID': xRequestId,
                       # 'Content-Type': 'application/json',
                       'User-Id': '131822439329728'
            }
        else:
            enterpriName = "小洽优选商城"
            enterpriseID = "108241811457856"
            enterpriseHash = "2e60aa03beb3493d4baf393a129ce7a6"

            # enterpriName = "百草味官方商城"
            # enterpriseID = "120"
            # enterpriseHash = "49858c7c7be3ed21bb8320445c87da62"

            loginRes = Login.loginNew(enterpriseID)
            token = loginRes["data"]["token"]
            # token = "eyJpdiI6IjFJM3J3ZTNSVnlib2NmeHE2cXpSR1E9PSIsInZhbHVlIjoiczMwMTdCa1pMQURXMmFrbjRLQ2tJZXBDdEMyWGlVTHNBbFM2enA4NFNFMGZ0M1RRXC9CbGNrSHFEUzFBelNWM2pSRXdzRHlaQXZvZFwvdVpxc0Vwc0FKbDJpVzR1U1M5XC9NNDN2RFhQeHBqY1d1alJjNUc0a3l3XC8wdkJVbTJTSk9tVlRsUGVURVZyRHFubVNMK1wvZGFJc2dzeUgrVE9vNVlHODRtbWxUbHMwYTVlamV3aUJRRjZHdDkwNTBoQVVZNHdUT0tCZFo5VVYrOU9wV3lcL1piT2NzNkJldndKTzZVeDdYZlNYSWRRNit0Yz0iLCJtYWMiOiI1NDRhNzNmOWNjMTNmZGEzZDQ1Y2U0ZjRmMGQwODM5MGQyYmQxMDYxNTYzYWRkMGZhZGMyN2VkMTIzZGFkNGUyIn0="
            timeStamp = Mytime.getCurrTimeStamp()
            randomStr = MyRandom.getRandomStr(2)
            xRequestId = 'autoTest-7b9d-4091-b4af-{0}{1}'.format(randomStr, timeStamp)
            headers = {
                       'token': token,
                       'Enterprise-Hash': enterpriseHash,
                       # 'App-Version': 'V1.7.2',
                       'X-Request-ID': xRequestId,
                       # 'Content-Type': 'application/json',
                       'User-Id': '131822439329728'
            }

        return headers



if __name__ == '__main__':
    print(ShopForHWJLogin.loginHWJShop())