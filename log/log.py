import logging
from utils.readerIniFile import ReaderIniFile


class Logger(object):

    @staticmethod
    def Logger():
        logging.basicConfig(format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
        logger = logging.getLogger()
        logger.setLevel(ReaderIniFile.value(section="log_level", key="logLevel"))
        return logger
