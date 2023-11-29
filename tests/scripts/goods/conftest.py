import pytest,allure,json
from utils.readerIniFile import ReaderIniFile
from filelock import FileLock
from log.log import Logger
from tests.common.stock.console.stock import Stock


def pytest_sessionstart(session):
    with FileLock("session.lock"):
        param = {"page":1,"size":100,"first_value":"","first_type":"all","second_type":"all","min_value":"","max_value":"","source_id":0,"time_type":"create","start_time":"","end_time":""}
        res = Stock().queryStockList(param)
        Logger.Logger().info("queryStockList:{0}".format(res))
        for i in res['data']['list']:
            if i['material_no'] == 'xttt001':
                id = i['material_id']
                repalce_data(id)
                break
            else:
                id = Stock().queryWarehouseId()
                file = {
                    "warehouse_id": (None, id),
                    "operate_type": (None, 1),
                    "excel": ('物料导入模版.xlsx', open(ReaderIniFile.getConfigFilePath("data", '物料导入模版.xlsx'), 'rb'),
                              'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
                    "filename": '物料导入模版.xlsx'
                }
                print(ReaderIniFile.getConfigFilePath("data", '物料导入模版.xlsx'))
                Res = Stock().matterInport(file)
                Logger.Logger().info('matterInport:{0}'.format(Res))
                with allure.step(f"导入物料"):
                    assert Res['code'] == 200 and Res['message'] == 'success'

                param = {"page": 1, "size": 100, "first_value": "", "first_type": "all", "second_type": "all",
                         "min_value": "", "max_value": "", "source_id": 0, "time_type": "create", "start_time": "",
                         "end_time": ""}
                res = Stock().queryStockList(param)
                Logger.Logger().info("queryStockList1:{0}".format(res))
                for i in res['data']['list']:
                    if i['material_no'] == 'xttt001':
                        id = i['material_id']
                        repalce_data(id)
                        break
                    # else:
                    #     raise Exception("未找到该物料")
def repalce_data(id):
    """
    替换addGoods.json中的数据
    """
    with open(ReaderIniFile.getConfigFilePath("data", 'addGoods.json'), 'r', encoding='utf-8') as f:
        param = f.read()
        f.close()
        data = json.loads(param)
        data['sku'][0]['material_id'] = id
        data['sku'][0]['material_no'] = 'xttt001'
        print(data)
    with open(ReaderIniFile.getConfigFilePath("data", 'addGoods.json'), 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False))
        f.close()


if __name__ == '__main__':
    # with open(ReaderIniFile.getConfigFilePath("data", 'addGoods.json'),'r',encoding='utf-8') as f:
    #     param = f.read()
    #     data = json.loads(param)
    #     print(data)
    param = {"page": 1, "size": 10, "first_value": "", "first_type": "all", "second_type": "all", "min_value": "",
             "max_value": "", "source_id": 0, "time_type": "create", "start_time": "", "end_time": ""}
    res = Stock().queryStockList(param)
    for i in res['data']['list']:
        print(i)
        if i['material_no'] == 'xttt001':

            print(i['material_id'])
            # with open(ReaderIniFile.getConfigFilePath("data", 'addGoods.json'), 'r', encoding='utf-8') as f:
            #     param = f.read()
            #     f.close()
            #     data = json.loads(param)
            #     data['sku'][0]['material_id'] = i['material_id']
            #     data['sku'][0]['material_no'] = 'xttt001'
            # with open(ReaderIniFile.getConfigFilePath("data", 'addGoods.json'),'w',encoding='utf-8') as f:
            #     f.write(json.dumps(data,ensure_ascii=False))
            #     f.close()
