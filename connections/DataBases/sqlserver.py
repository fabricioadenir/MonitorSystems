import pyodbc
from .baseconnection import BaseConnection
import logging

logger = logging.getLogger(__name__)


class SqlServer(BaseConnection):
    def __init__(self, **kwargs):
        super(SqlServer, self).__init__(**kwargs)
        self.server = kwargs.get('server')
        self.driver = '{SQL Server}'

        db_config = ('DRIVER=' + self.driver + ';SERVER=' + self.server +
                     ';DATABASE=' + self.db_or_index + ';UID=' + self.user + ';PWD=' + self.pwd)

        try:
            logger.info('connecting to SQL Server database...')
            self.connection = pyodbc.connect(db_config, autocommit=False)
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
        try:
            self.connection.close()
            self.cursor.close()
        except Exception as error:
            logger.error(f"Error close connection {error}")
