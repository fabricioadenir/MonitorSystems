import mysql.connector


class MySql:
    def __init__(self, host, user, pwd, db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db
    
        db_config = {'user': self.user, 'password': self.pwd,
                     'host': self.host, 'database': self.db}

        try:
            print('connecting to PostgreSQL database...')
            self.connection = mysql.connector.connect(**db_config)
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
