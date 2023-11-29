from utils.myTime import Mytime
from utils.myRandom import MyRandom


class GetXRequestId(object):

    @staticmethod
    def retXRequestId():
        timeStamp = Mytime.getCurrTimeStamp()
        randomStr = MyRandom.getRandomStr(2)
        xRequestId = 'autoTest-7b9d-4091-b4af-{0}{1}'.format(randomStr, timeStamp)
        return xRequestId