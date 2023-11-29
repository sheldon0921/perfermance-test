from tests.common.sendRequest.sendRequest import SendRequest
from utils.readerIniFile import ReaderIniFile
from utils.parseJson import ParseJson
import time



class Activity(object):
    """
        封装了对自提门店的操作
    """

    def __init__(self):
        self.shopUrl = ReaderIniFile.value(key="shopBaseUrl")
        self.consoleUrl = ReaderIniFile.value(section="console_sys_info", key="consoleBaseUrl")
        self.send = SendRequest()

    def getActivityGoods(self,goodsType,activity):
        """
        goodstype:活动类型，limitTime为限时购 ，groupWork 为拼团
        activity：nostart限时购未开始  start为开始
        """
        url = '{0}/gw-shop/app/v1/activity-center/activity-goods-list'.format(self.shopUrl)
        params={"list_search":{"type":14,"activity_status":9},"method":"list"}
        if goodsType == "limitTime":
            params["list_search"]["type"] = 12
        elif goodsType == "groupWork":
            pass
        if activity == "nostart":
            params["list_search"]['activity_status'] = 2
        else:
            pass
        res = self.send.sendRequest(url=url, params=params, method="post")
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("call {0} interface is failed".format(url))

    def getActivityGoodsDetail(self,params:dict):
        url = '{0}/gw-shop/app/v1/goods/detail'.format(self.shopUrl)
        res = self.send.sendRequest(url=url,params=params,method="post")
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("call {0} interface is failed".format(url))

    def getActivityDetail(self,id,method,type):
        """
        method: list为活动列表  detail不传为活动详情
        type:
            拼团：Group
            限时购：flash-sale
            新人购：new-buy
            今日爆款：hot-goods
        """
        url = '{0}/gw-console/v1/activity-common/activity'.format(self.consoleUrl)
        if method == "list":
            params = {"search":{"search_type":"activity_id","search_value":id,"status":"","start_time":"","end_time":""},"type":"flash-sale","method":"list","page":1,"size":10}
        else:
            params = {"type":"flash-sale","method":"detail","id":id}
        if type == "Group":
            params["type"] = "Group"
        if type == "flash-sale":
            params["type"] = "flash-sale"
        if type == "new-buy":
            params["type"] = "new-buy"
        if type == "hot-goods":
            params["type"] = "hot-goods"
            # del params["search"]["start_time"]
            # del params["search"]["end_time"]
            print("hotGoods param: {0}".format(params))
        res = self.send.sendRequest(url=url, params=params ,method="post")
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("call {0} interface is failed".format(url))
    def getTemplateActivityList(self):
        """
        获取首页模板中的活动列表
        """
        param = {"page":1,"size":10,"type":"hot-goods","sku_enable":1,"method":"list","show_activity_sku":1,"search":{"selected_activity_ids":[],"search_value":"","search_type":"activity_name","status":[2,3],"sale_type":2}}
        url = '{0}/gw-console/v1/activity-common/activity'.format(self.consoleUrl)
        res = self.send.sendRequest(url=url, params=param, method="post")
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception("call {0} interface is failed".format(url))


    def getActivityTicket(self,param:dict):
        """
        获取活动票据
        """
        time.sleep(10)
        params = {
            "sku_list": [
                {
                    "spu_id": param['spu_id'],
                    "rule_id": param['rule_id'],
                    "init_id": 0,
                    "type": param['type'],
                    "price": param['price'],
                    "sku_id": param['sku_id'],
                    "buy_num": param['buy_num'],
                    "sale_type": 2,
                    "store_info": {
                        "extract_id": param['extract_id'],
                        "store_id": param['store_id']
                    }
                }
            ]
        }
        url = '{0}/gw-shop/app/v1/activity-center/ticket'.format(self.shopUrl)
        res = self.send.sendRequest(url=url,params=params,method="post")
        if res.status_code == 200:
            resJson = res.json()
            resJson['num'] = params['sku_list'][0]['buy_num']
            return resJson
        else:
            raise Exception("call {0} interface is failed".format(url))


if __name__ == '__main__':
    # id = 154019450159360
    # method = "detail"
    # type = "new-buy"

    id = 169062363552640
    method = "detail"
    type = "hot-goods"
    res=Activity().getActivityDetail(id,method,type)
    print(res)