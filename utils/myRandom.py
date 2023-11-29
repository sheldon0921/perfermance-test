import rstr


class MyRandom:

    @staticmethod
    def getRandomStr(n: int) -> str:
        """
        :param n: 随机字符串长度
        :return: 生成的随机字符串
        """
        return "".join([rstr.xeger(r"\d|[a-z]|[A-Z]") for _i in range(n)])
