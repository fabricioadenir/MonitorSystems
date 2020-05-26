import logging

logger = logging.getLogger(__name__)


class BaseConnection:
    def __init__(self, **kwargs):
        self.ip = kwargs.get('ip')
        self.port = kwargs.get('port')
        self.user = kwargs.get('user')
        self.pwd = kwargs.get('pwd')
        self.db_or_index = kwargs.get('database')
        self.timeout = kwargs.get('timeout')

    def query(self, query):
        pass

    def close(self):
        pass
