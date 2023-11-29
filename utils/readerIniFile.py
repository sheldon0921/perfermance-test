import configparser
import os
import sys


class ReaderIniFile(object):
    @staticmethod
    def getConfigFilePath(fileDir, fileName):
        return os.path.join(os.path.dirname(os.path.dirname(__file__)), fileDir, fileName)

    @staticmethod
    def value(section="shop_sys_info", key=""):
        if key == "":
            raise Exception("Key is empty!")
        path = ReaderIniFile.getConfigFilePath("config", "enviroment.ini")
        config = configparser.ConfigParser()
        config.read(path,encoding="utf-8-sig")
        return config.get(section=section, option=key)



if __name__ == '__main__':
    print(ReaderIniFile.value(section="console_sys_info", key="consoleBaseUrl"))
    print(ReaderIniFile.value(key="shopBaseUrl"))
    print(ReaderIniFile.value(key="enterpriseId"))
    print(ReaderIniFile.value(key="enterpriseName"))
    print(ReaderIniFile.value(key="enterpriseHash"))
    # print(Config.value(key=""))

