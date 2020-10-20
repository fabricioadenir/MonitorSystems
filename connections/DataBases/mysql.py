import mysql.connector
from .baseconnection import BaseConnection
import logging

logger = logging.getLogger(__name__)


class MySql(BaseConnection):
    def __init__(self, **kwargs):
        super(MySql, self).__init__(**kwargs)
        self.server = kwargs.get('server')

        db_config = {'user': self.user, 'password': self.pwd,
                     'host': self.server, 'database': self.db_or_index}

        try:
            logger.info('connecting to MySql database...')
            self.connection = mysql.connector.connect(**db_config)
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
