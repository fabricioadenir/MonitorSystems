from .GetResults import get_results

class Connection():
    '''
    Classe responsável por conectar ao banco de dados 
    
    Caso o bando de dados se conecte viu uri basta informar o tipo do bando ex: "MongoDB"

    Caso o banco não seja via uri informe os dados para conexão e o tipo do banco.
    '''
    def __init__(self, uri=None, **kwargs):
        self.__type = kwargs.get('typeDb')
        self.__uri = uri
        self.__ip = kwargs.get('ip')
        self.__port = kwargs.get('port')
        self.__user = kwargs.get('user')
        self.__pwd = kwargs.get('pwd')
        self.__database = kwargs.get('database')
        self.__server = kwargs.get('server')

    def __data_connect(self):
        data = {}
        data['type'] = self.__type
        if self.__uri:
            data['uri'] = self.__uri
            return data
        elif self.__server:
            data['user'] = self.__user
            data['pwd'] = self.__pwd
            data['database'] = self.__database
            return data

        data['ip'] = self.__ip
        data['port'] = self.__port
        data['user'] = self.__user
        data['pwd'] = self.__pwd
        data['database'] = self.__database
        return data

    def execute(self, query):
        result = get_results(
                query,
                self.__type,
                self.__data_connect)
        return result

