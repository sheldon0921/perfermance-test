import requests
import pytest
from utils.readerIniFile import ReaderIniFile
from log.log import Logger


class SingleInterfaceLoginConsole():

    # 登录小程序
    @staticmethod
    def loginShop():
        """
        登录小程序
        :return: 登录成功返回Token
        """
        # 从配置文件获取登录小程序的参数,获取Token
        logger = Logger.Logger()
        baseUrl = ReaderIniFile.value(key="shopBaseUrl")
        enterpriseID = ReaderIniFile.value(key="enterpriseId")
        enterpriseHash = ReaderIniFile.value(key="enterpriseHash")
        userId = ReaderIniFile.value(key="userId")
        params = {
            "user_id": userId,
            "enterprise_id": enterpriseID,
            "sign": 2121
        }
        loginHeader = {
            "enterprise-hash":  enterpriseHash
        }
        loginUrl = "{0}/gw-shop/get_user_token".format(baseUrl)
        res = requests.get(url=loginUrl, params=params, headers=loginHeader)
        logger.info("request url: {0}".format(res.url))
        # 拼接访问接口需要的header信息并返回
        if res.status_code == 200:
            try:
                token = res.json()["data"]["token"]
                headers = {
                    'token': token,
                    'Enterprise-Hash': enterpriseHash,
                    'App-Version': 'V1.7.2'
                }
                # logger.info("headers: {0}".format(headers))
                # print("headers: {0}".format(headers))
                logger.info("Login shop Success!")
                return headers
            except Exception:
                raise Exception("Login shop fail, get token fail!", res.text)
        else:
            raise Exception("Login shop fail! return code is {0}".format(res.status_code), res.text)

    # 登录管理后台
    @staticmethod
    def loginConsole():
        """
        登录管理后台
        :return: 登录成功，返回Token信息
        """
        logger = Logger.Logger()
        auth_headers = dict()
        # 从配置文件读取
        consoleUrl = ReaderIniFile.value(section="console_sys_info_baize", key="consoleLoginUrl")
        account = ReaderIniFile.value(section="console_sys_info_baize", key="consoleAccount")
        password = ReaderIniFile.value(section="console_sys_info_baize", key="consolePassword")
        loginType = ReaderIniFile.value(section="console_sys_info_baize", key="loginType")
        enterpriseHash = ReaderIniFile.value(section="console_sys_info_baize",key="enterpriseHash")
        # 登录接口参数拼接
        data = {"login_type": int(loginType), "account": account,"password": password}
        loginURL = '{0}/gw-scrm/login'.format(consoleUrl)
        logger.info('console login url: {0}'.format(loginURL))
        response = requests.post(url=loginURL, json=data)
        logger.info(response.text)
        # 登录成功返回token
        if response.status_code == 200:
            try:
                loginData = response.json()
                enterPriseList = loginData["data"]["enterprise_list"]
                for enterPrise in enterPriseList:
                    if enterPrise["hash"] == enterpriseHash:
                        adminId = enterPrise["admin_id"]
                        getTokenParam = {"admin_id": adminId}
                        getTokenUrl = '{0}/gw-scrm/get-token'.format(consoleUrl)
                        getTokenRes = requests.post(url=getTokenUrl, json=getTokenParam)
                        token = getTokenRes.json()["data"]["token"]
                        break
                # auth_headers['Auth-Token'] = loginData['data']['token']
                # auth_headers['Enterprise-Hash'] = loginData['data']['hash']
                auth_headers['Auth-Token'] = token
                auth_headers['Enterprise-Hash'] = enterpriseHash
                logger.info("Login Console Success!")
                return auth_headers
            except Exception:
                raise Exception("Login console fail!", response.text)
        else:
            raise Exception("Login console fail!", response.text)

    @staticmethod
    def loginNew(enterpriseID):
        """
        登录线上环境小程序
        :param enterpriseID: 企业ID
        :return: 登录成功返回用户信息
        """
        jumpServerIp = ReaderIniFile.value(key="jumpServerIp")
        params = {
            "enterprise_id": enterpriseID,
            "size": 1,
            "sign": 2121
        }
        res = requests.get(url="{0}/internal-api/auto-test/get-temp-token".format(jumpServerIp), params=params)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("Login fail!", res.text)

    @staticmethod
    def loginBoss():
        log = Logger.Logger()
        host = ReaderIniFile.value(section="boss_sys_info", key="host")
        consoleUrl = ReaderIniFile.value(section="boss_sys_info", key="consoleBossUrl")
        account = ReaderIniFile.value(section="boss_sys_info", key="consoleBossAccount")
        password = ReaderIniFile.value(section="boss_sys_info", key="consoleBossPassword")
        header = {
            "Content-Type": "application/json",
            "Content-Length": "50",
            "HOST":host
        }
        data = {"account":account,"password":password}
        url = '{0}/micro-boss/app/v1/admin/login'.format(consoleUrl)
        res = requests.post(url=url,headers=header,json=data)
        log.info("response :{0}".format(res.json()))
        Token = res.json()['data']['Token']
        header['Token'] = Token
        header['authorization'] = 'Bearer'+' '+Token
        if res.status_code == 200:
            return header
        else:
            raise Exception("login Boss fail!",res.text)








if __name__ == '__main__':
    # print("header", Login.loginConsole())
    # Login.loginConsole()
    # print(Login.loginNew("134034389742592"))
    # res = Login.loginBoss()
    # print(res)
    print("login console Res: {0}".format(SingleInterfaceLoginConsole.loginConsole()))