from tests.login.singletonHttpClient import SingletonHttpClient
from utils.readerIniFile import ReaderIniFile
import pytest


class Boss():
    def __init__(self):
        self.httpclient = SingletonHttpClient().get_instance()
        self.consoleBoss = ReaderIniFile.value(section="boss_sys_info", key="consoleBossUrl")

    def new_edit(self,param):
        """
        boss后台编辑
        """
        url = '{0}/micro-boss/app/v1/enterprise-new/edit'.format(self.consoleBoss)
        res = self.httpclient.Post(url=url,json=param)
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("enterprise new edit fail!",res.text)