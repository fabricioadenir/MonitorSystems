import psycopg2
from .baseconnection import BaseConnection
import logging

logger = logging.getLogger(__name__)


class Postgres(BaseConnection):
    def __init__(self, **kwargs):
        super(Postgres, self).__init__(**kwargs)

        db_config = {'dbname': self.db_or_index, 'host': self.ip,
                     'password': self.pwd, 'port': self.port, 'user': self.user}

        try:
            logger.info('connecting to PostgreSQL database...')
            self.connection = psycopg2.connect(**db_config)
            self.cursor = self.connection.cursor()

        except Exception as error:
            logger.error('Error: connection not established {}'.format(error))
            return None
        else:
            logger.info('connection established')

    def query(self, query):
        try:
            result = self.cursor.execute(query)
            return result
        except Exception as error:
            logger.error(f"Error executing command {error}")
            return None

    def close(self):
        self.connection.close()
        self.cursor.close()
