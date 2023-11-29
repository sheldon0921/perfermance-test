from utils.readerIniFile import ReaderIniFile
import json
from log.log import Logger


class ReaderFile(object):

    logger = Logger.Logger()

    @classmethod
    def readerJson(cls, fileName) -> dict:
        """
        读取json文件的内容
        :param fileName: 文件名称
        :return: 返  回Json格式内容
        """
        filePath = ReaderIniFile.getConfigFilePath("data", fileName)
        cls.logger.info("params json file: {0}".format(filePath))
        with open(filePath, "r", encoding="utf-8") as jf:
            contents = jf.read()
            contents = json.loads(contents)
            return contents


if __name__ == '__main__':
    print(ReaderFile.readerJson("addPostage.json"))
    print(type(ReaderFile.readerJson("addPostage.json")))
