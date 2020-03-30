import cx_Oracle

class Oracle:
    def __init__(self, server, user, pwd, db):
        self.server = server
        self.user = user
        self.pwd = pwd
        self.db = db
    
        db_config = (self.user + '/' + self.pwd + '@' + self.server + '/' + self.db)

        try:
            print('connecting to Oracle database...')
            self.connection = cx_Oracle.connect(db_config)
            self.cursor = self.connection.cursor()

        except Exception as error:
            print('Error: connection not established {}'.format(error))

        else:
            print('connection established') 
    
    def query(self, query):
        try:
            result = self.cursor.execute(query)
            return result.fetchall()
        except:
            print("Erro ao executar comando")
            return None
    
    def close(self):
        self.connection.close()
        self.cursor.close()
