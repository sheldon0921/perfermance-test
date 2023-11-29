from tests.login.singletonHttpClient import SingletonHttpClient
from utils.readerIniFile import ReaderIniFile
from tests.common.boss.console.boss import Boss
from log.log import Logger
import pytest, allure


@allure.feature('BOSS后台')
class Test_boss():
    @pytest.fixture()
    def ini(self):
        self.boss = Boss()
        self.log = Logger.Logger()
        # self.httpclient = SingletonHttpClient().get_instance()
        self.consoleBoss = ReaderIniFile.value(section="boss_sys_info", key="consoleBossUrl")

    @allure.story('是否删除侧边栏')
    @pytest.mark.smoke
    def test_new_edit(self, ini):
        """
        is_delete_work_plugin_exec 为False时，说明未修改侧边栏
                                   为True时，说明修改侧边栏，脚本报错
        """
        param = {
            "industry": "电子产品",
            "permission_list": [
                150,
                155,
                480,
                159,
                218,
                223,
                257,
                228
            ],
            "warehouse_type": 1,
            "show_changyi_logo": 1,
            "available_system": [
                1
            ],
            "admin_available_system": [
                1
            ],
            "id": 174067958256320,
            "hash": "b6d50280a47964487f64feff50f0a887",
            "name": "白泽信息科技",
            "contact": "白喆",
            "mobile": "12345678810",
            "address": "陕西省西安市雁塔区",
            "logo": "",
            "corp_id": "123456",
            "domain": "CBC908537F00000131937ADB436A2F5D",
            "separate_switch": 1,
            "industry_id": 3,
            "lock_time": 0,
            "proportion": 0,
            "start_fee": None,
            "crs_status": 1,
            "store_status": 1,
            "contact_status": 2,
            "external_secret": "",
            "status": 1,
            "business_source": 0,
            "version": 3,
            "version_tag": "正式版",
            "erp_status": 1,
            "crm_status": 1,
            "return_address": "",
            "service_merchant_id": 6,
            "stop_at": 0,
            "open_platform_id": 0,
            "account_limit": 10,
            "account_start_at": 1631203200,
            "account_expire_at": 1815062399,
            "is_split_flow": 0,
            "edit_at": 1631266120,
            "is_chain_split": 2,
            "brand_name": "",
            "created_at": 1631266120,
            "updated_at": 1631266120,
            "deleted_at": 0,
            "username": "mujunqiang@vchangyi.com",
            "account": "mujunqiang@vchangyi.com",
            "global_roaming": "",
            "email": "mujunqiang@vchangyi.com",
            "admin_mobile": "12345678810",
            "range_type": 1,
            "enterprise_id": 174067958256320
        }
        res = self.boss.new_edit(param)
        self.log.info("new edit :{0}".format(res))
        assert res['code'] == 200 and res['message'] == 'success'
        isDelWorkPluginExec = res['data']['is_delete_work_plugin_exec']
        assert not isDelWorkPluginExec
