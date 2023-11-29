import time


class Mytime(object):

    @staticmethod
    def getCurrTimeStamp():
        """获取当前时间戳"""
        return int(time.time())

    @staticmethod
    def getCurrTime():
        return time.strftime("%m%d%H%M%S", time.localtime())


if __name__ == '__main__':
    print(Mytime.getCurrTime())
