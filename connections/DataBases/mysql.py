import mysql.connector


class MySql:
    def __init__(self, **kwargs):
        self.server = kwargs.get('server')
        self.user = kwargs.get('user')
        self.pwd = kwargs.get('pwd')
        self.db = kwargs.get('database')
        self.timeout = kwargs.get('timeout')
    
        db_config = {'user': self.user, 'password': self.pwd,
                     'host': self.server, 'database': self.db}

        try:
            print('connecting to MySql database...')
            self.connection = mysql.connector.connect(**db_config)
            self.cursor = self.connection.cursor()

        except Exception as error:
            print('Error: connection not established {}'.format(error))
            return None
        else:
            print('connection established') 
    
    def query(self, query):
        try:
            result = self.cursor.execute(query)
            return result
        except Exception as error:
            print(f"Error executing command {error}")
            return None
    
    def close(self):
        self.connection.close()
        self.cursor.close()
