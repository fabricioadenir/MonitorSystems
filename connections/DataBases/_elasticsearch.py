from elasticsearch import Elasticsearch
from .baseconnection import BaseConnection
import logging

logger = logging.getLogger(__name__)


class MyElasticSearch(BaseConnection):
    def __init__(self, **kwargs):
        super(MyElasticSearch, self).__init__(**kwargs)
        self.host = kwargs.get('server')
        self.uri = kwargs.get('uri')

        try:
            logger.info("connecting to ElasticSearch...")

            if self.uri:
                self._elastic_search = Elasticsearch(hosts=self.uri)

            elif self.user and self.pwd:
                self._elastic_search = Elasticsearch(
                    {'host': self.ip, 'port': self.port}, http_auth=(self.user, self.pwd))

            logger.info("connection established")

        except Exception as err:
            logger.error(f"Error: connection not established {err}")

    def query(self, query: dict):
        try:
            result = self._elastic_search.search(
                index=self.db_or_index,
                body=query
            )
            return result
        except Exception as error:
            logger.error(f"Error executing command {error}")
            return None

    def close(self):
        pass
