import pyodbc


class SqlServer:
    def __init__(self, server, user, pwd, db):
        self.server = server
        self.user = user
        self.pwd = pwd
        self.db = db
        self.driver = '{SQL Server}'

        db_config = ('DRIVER=' + self.driver + ';SERVER=' + self.server +
                     ';DATABASE=' + self.db + ';UID=' + self.user + ';PWD=' + self.pwd)

        try:
            print('connecting to SQL Server database...')
            self.connection = pyodbc.connect(db_config, autocommit=False)
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
