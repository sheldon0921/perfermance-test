# -*- coding:utf-8 -*-

import requests
from tests.login.login import Login
from utils.readerIniFile import ReaderIniFile
from log.log import Logger
# from log.log import Logger
import urllib3
from utils.urlRecord import UrlRecord


# 请求通用方法封装
class HttpClient(object):

    # 获取登录小程序/管理后台的header信息
    def __init__(self, flag="all"):
        """
        获取管理后台和小程序的Token信息
        """
        self.logger = Logger.Logger()
        # 禁用安全请求警告
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        # self.logger = Logger.Logger()
        self.session = requests.Session()
        self.urlRecord = UrlRecord()
        self.headerShop = Login.loginShop()
        self.headerConsole = Login.loginConsole()
        self.headerBoss = Login.loginBoss()
        # if flag is "all":
        #     pass
        # elif flag is "boss":
        #     self.headerBoss = Login.loginBoss()

    # 通过URL判断访问小程序还是管理后台
    def getHeader(self, url: str):
        """
        根据请求接口的域名判断请求的是管理后台还是小程序
        :param url: 请求接口的URL
        :return: 对应系统的请求Token信息
        """
        if url.startswith(ReaderIniFile.value(section="console_sys_info", key="consoleBaseUrl")):
            # if side.upper() == "CONSOLE" :
            return self.headerConsole
        elif url.startswith(ReaderIniFile.value(section="shop_sys_info", key="shopBaseUrl")):
            # elif side.upper() == "SHOP":
            return self.headerShop
        elif url.startswith(ReaderIniFile.value(section="boss_sys_info", key="consoleBossUrl")):
            return self.headerBoss
        else:
            raise Exception("URL Error , Please Check URL!", url)

    def Post(self, url, data=None, json=None, headers=None, **kwargs):
        if headers is None:
            self.logger.info("url: {0}, header: {1}, data: {2}".format(url, self.getHeader(url), json))
            return self._request('post', url, headers=self.getHeader(url), data=data, json=json, verify=False, **kwargs)
        else:
            self.logger.info("url: {0}, header: {1}, data: {2}".format(url, headers, json))
            return self._request('post', url, headers=headers, data=data, json=json, verify=False, **kwargs)

    def GET(self, url, params=None, headers=None, **kwargs):
        # self.logger.info("url: {0}, header: {1}, data: {2}".format(url, headers, params))
        kwargs.setdefault('allow_redirects', True)
        if headers is None:
            self.logger.info("url: {0}, header: {1}, data: {2}".format(url, self.getHeader(url), params))
            return self._request('get', url, headers=self.getHeader(url), params=params, verify=False, **kwargs)
        else:
            self.logger.info("url: {0}, header: {1}, data: {2}".format(url, headers, params))
            return self._request('get', url, headers=headers, params=params, verify=False, **kwargs)

    def DELETE(self, url, **kwargs):
        return self._request('delete', url, headers=self.getHeader(url), **kwargs)

    def PUT(self, url, data=None, **kwargs):
        return self._request('put', url, headers=self.getHeader(url), data=data, verify=False, **kwargs)

    def PATCH(self, url, data=None, **kwargs):
        return self._request('patch', url, headers=self.getHeader(url), data=data, verify=False, **kwargs)

    def close(self):
        self.session.close()

    def _request(self, method, url: str,
                 params=None, data=None, headers=None, cookies=None, files=None,
                 auth=None, timeout=None, allow_redirects=True, proxies=None,
                 hooks=None, stream=None, verify=None, cert=None, json=None
                 ):
        res = self.session.request(method, url,
                                   headers=headers,
                                   files=files,
                                   data=data or {},
                                   json=json,
                                   params=params or {},
                                   auth=auth,
                                   cookies=cookies,
                                   hooks=hooks,
                                   timeout=timeout,
                                   allow_redirects=allow_redirects,
                                   proxies=proxies,
                                   stream=stream,
                                   verify=verify,
                                   cert=cert,
                                   )
        if url.startswith(ReaderIniFile.value(section="shop_sys_info", key="shopBaseUrl")):
            duration = res.elapsed.microseconds / 1000
            self.urlRecord.writeUrl(url + " :duration {0}".format(duration), "urlRecord.json")
        return res
