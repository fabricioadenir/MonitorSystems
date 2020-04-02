import pyodbc


class SqlServer:
    def __init__(self, **kwargs):
        self.server = kwargs.get('server')
        self.user = kwargs.get('user')
        self.pwd = kwargs.get('pwd')
        self.db = kwargs.get('database')
        self.driver = '{SQL Server}'
        self.timeout = kwargs.get('timeout')

        db_config = ('DRIVER=' + self.driver + ';SERVER=' + self.server +
                     ';DATABASE=' + self.db + ';UID=' + self.user + ';PWD=' + self.pwd)

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
