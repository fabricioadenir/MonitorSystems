import psycopg2


class Postgres:
    def __init__(self, **kwargs):
        self.ip = kwargs.get('ip')
        self.port = kwargs.get('port')
        self.user = kwargs.get('user')
        self.pwd = kwargs.get('pwd')
        self.db = kwargs.get('database')
        self.timeout = kwargs.get('timeout')
    
        db_config = {'dbname': self.db, 'host': self.ip,
                     'password': self.pwd, 'port': self.port, 'user': self.user}

        try:
            print('connecting to PostgreSQL database...')
            self.connection = psycopg2.connect(**db_config)
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
