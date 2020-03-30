import psycopg2


class Postgres:
    def __init__(self, host, port, user, pwd, db):
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.db = db
    
        db_config = {'dbname': self.db, 'host': self.host,
                     'password': self.pwd, 'port': self.port, 'user': self.user}

        try:
            print('connecting to PostgreSQL database...')
            self.connection = psycopg2.connect(**db_config)
            self.cursor = self.connection.cursor()

        except Exception as error:
            print('Error: connection not established {}'.format(error))
        else:
            print('connection established') 
    
    def query(self, query):
        try:
            result = self.cursor.execute(query)
            return result
        except:
            print("Erro ao executar comando")
            return None
    
    def close(self):
        self.connection.close()
        self.cursor.close()
