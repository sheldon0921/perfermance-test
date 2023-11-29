from tests.login.httpclient import HttpClient
import threading


class SingletonHttpClient(object):
    _instance_lock = threading.Lock()

    @classmethod
    def get_instance(cls, flag="all", *args, **kwargs):
        if not hasattr(SingletonHttpClient,'_instance'):
            with SingletonHttpClient._instance_lock:
                if not hasattr(SingletonHttpClient,'_instance'):
                    SingletonHttpClient._instance = HttpClient(flag)

        return SingletonHttpClient._instance