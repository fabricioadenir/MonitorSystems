import pyodbc
from .baseconnection import BaseConnection


class SqlServer(BaseConnection):
    def __init__(self, **kwargs):
        super(SqlServer, self).__init__(**kwargs)
        self.server = kwargs.get('server')
        self.driver = '{SQL Server}'

        db_config = ('DRIVER=' + self.driver + ';SERVER=' + self.server +
                     ';DATABASE=' + self.db_or_index + ';UID=' + self.user + ';PWD=' + self.pwd)

        try:
            print('connecting to SQL Server database...')
            self.connection = pyodbc.connect(db_config, autocommit=False)
            self.cursor = self.connection.cursor()

        except Exception as error:
            print('Error: connection not established {}'.format(error))
            return None
        else:
            print('connection established')

    def query(self, query):
        try:
            result = self.cursor.execute(query)
            return result.fetchall()
        except Exception as error:
            print(f"Error executing command {error}")
            return None

    def close(self):
        try:
            self.connection.close()
            self.cursor.close()
        except Exception as error:
            print(f"Error close connection {error}")
