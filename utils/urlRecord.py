from utils.readerIniFile import ReaderIniFile
import time, threading


class UrlRecord:
    consoleUrl = ReaderIniFile.value(section="console_sys_info", key="consoleLoginUrl")
    shopUrl = ReaderIniFile.value(key="shopBaseUrl")
    lock = threading.RLock()

    def writeUrl(self, url, fileName):
        if fileName.startswith("urlRecord.json"):
            fileName = "urlRecord.json"
        elif fileName.startswith("slowUrlRecord.json"):
            fileName = "slowUrlRecord.json"
        if self.lock.acquire():
            with open(ReaderIniFile.getConfigFilePath("data", fileName), "a+") as f:
                f.write("{0},\n".format(url))
            self.lock.release()
