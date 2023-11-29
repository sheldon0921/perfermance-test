import requests
import pytest
from utils.readerIniFile import ReaderIniFile
from log.log import Logger


class Login():

    # 登录管理后台
    @staticmethod
    def loginConsole():
        """
        登录管理后台
        :return: 登录成功，返回msg信息
        """
        logger = Logger.Logger()
        # 从配置文件读取
        consoleUrl = ReaderIniFile.value(section="console_cyy_info", key="consoleUrl")
        username = ReaderIniFile.value(section="console_cyy_info", key="username")
        password = ReaderIniFile.value(section="console_cyy_info", key="password")

        # 登录接口参数拼接
        data = { "username": username,"password": password}
        loginURL = '{0}/login/login'.format(consoleUrl)
        logger.info('console login url: {0}'.format(loginURL))
        response = requests.post(url=loginURL, json=data)
        logger.info(response.text)
        # 登录成功返回msg
        if response.status_code == 200:
            return response.json()["msg"]
        else:
            raise Exception("Login fail!", res.text)



if __name__ == '__main__':
    # print("header", Login.loginConsole())
    # Login.loginConsole()
    # print(Login.loginNew("134034389742592"))
    res = Login.loginConsole()
    print(res)