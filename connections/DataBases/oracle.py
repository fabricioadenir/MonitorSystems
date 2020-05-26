import cx_Oracle
from .baseconnection import BaseConnection
import logging

logger = logging.getLogger(__name__)


class Oracle(BaseConnection):
    def __init__(self, **kwargs):
        super(Oracle, self).__init__(**kwargs)
        self.server = kwargs.get('server')

        db_config = (self.user + '/' + self.pwd +
                     '@' + self.server + '/' + self.db_or_index)

        try:
            logger.info('connecting to Oracle database...')
            self.connection = cx_Oracle.connect(db_config)
            self.cursor = self.connection.cursor()

        except Exception as error:
            logger.error('Error: connection not established {}'.format(error))
            return None

        else:
            logger.info('connection established')

    def query(self, query):
        try:
            result = self.cursor.execute(query)
            return result.fetchall()
        except Exception as error:
            logger.error(f"Error executing command {error}")
            return None

    def close(self):
        self.connection.close()
        self.cursor.close()
