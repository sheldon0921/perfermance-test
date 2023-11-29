# -*- coding:utf-8 -*-
from types import MethodType

'''
   header bean 
'''


class Header(object):

    def __init__(self):
        self.__token = ''
        self.__EnterpriseHash = ''
        self.__AppVersion = ''

    @property
    def token(self):
        return self.__token

    @token.setter
    def age(self, token):
        self.__token = token

    @property
    def EnterpriseHash(self):
        return self.__EnterpriseHash

    @EnterpriseHash.setter
    def EnterpriseHash(self, EnterpriseHash):
        self.__EnterpriseHash = EnterpriseHash

    @property
    def AppVersion(self):
        return self.__AppVersion

    @AppVersion.setter
    def AppVersion(self, AppVersion):
        self.__age = AppVersion


if __name__ == '__main__':
    header = Header()
    header.EnterpriseHash = 'str'
    print(header.EnterpriseHash)
