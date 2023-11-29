
class ShopForDDCApiAssert(object):


    def match_class(self ,dict1 ,dict2):
        '''
        循环遍历返回数据，并与预期数据格式进行比较
        :param dict1: 预期数据格式 字典
        :param dict2: 实际数据格式 字典
        :return:返回对比的key
        '''
        for k1 ,k2 in zip(dict1.keys() ,dict2.keys()):
            assert k1 == k2
            print(k1 ,k2)
            if isinstance(dict1[k1] ,dict) and isinstance(dict2[k2],dict):
                self.match_class(dict1[k1] ,dict2[k2])
            elif isinstance(dict1[k1] ,list) and isinstance(dict2[k2],list):
                for i ,j in zip(dict1[k1] ,dict2[k2]):
                    if isinstance(i ,dict) and isinstance(j,dict):
                        self.match_class(i ,j)
            else:
                continue
        return True






