from pymongo import MongoClient
from .baseconnection import BaseConnection
import logging

logger = logging.getLogger(__name__)


class MongoDB(BaseConnection):

    def __init__(self, **kwargs):
        super(MongoDB, self).__init__(**kwargs)
        self.uri = kwargs.get("uri")
        self.collection = kwargs.get("collection")

        try:
            logger.info("connecting to PostgreSQL database...")
            if self.uri:
                self.client = MongoClient(self.uri)
            elif self.user and self.pwd:
                self.client = MongoClient(
                    f"mongodb://{self.user}:{self.pwd}@{self.ip}:{self.port}")
            else:
                self.client = MongoClient(self.ip, self.port)
            logger.info("connection established")
        except Exception as err:
            logger.error(f"Error: connection not established {err}")

    def query(self, query):
        try:
            db = self.client[self.db_or_index]
            collection = db[self.collection]
            result = collection.find(query)
            return result
        except Exception as err:
            logger(f"Error executing command {err}")
            return None

    def close(self):
        pass
