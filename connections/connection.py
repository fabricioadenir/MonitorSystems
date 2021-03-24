from .get_results import GetResults
import logging

logger = logging.getLogger(__name__)


class Connection():
    '''
    Classe responsável por conectar ao banco de dados

    Caso o banco de dados não se conecte via uri basta informar o tipo do banco ex: "MongoDB"
    **kwargs com os dados para conexão

    Caso o banco seja via uri informe os dados para conexão e o tipo do banco.
    *args = uma uri valida **kwargs com o type do database

    '''

    def __init__(self, *args, **kwargs):
        self.__timeout = kwargs.get('timeout')
        self.__type = kwargs.get('type')
        self.__uri = kwargs.get('uri')
        self.__ip = kwargs.get('ip')
        self.__port = kwargs.get('port')
        self.__user = kwargs.get('user')
        self.__pwd = kwargs.get('pwd')
        self.__database = kwargs.get('database')
        self.__index = kwargs.get('index')
        self.__collection = kwargs.get('collection')
        self.__server = kwargs.get('server')

    def __data_connect(self):
        data = {}
        if self.__uri:
            data['uri'] = self.__uri
            data['index'] = self.__index
            data['database'] = self.__database
            data['collection'] = self.__collection
            data['timeout'] = self.__timeout
            return data
        elif self.__server:
            data['server'] = self.__server
            data['user'] = self.__user
            data['pwd'] = self.__pwd
            data['database'] = self.__database
            data['timeout'] = self.__timeout
            return data

        data['ip'] = self.__ip
        data['port'] = self.__port
        data['user'] = self.__user
        data['pwd'] = self.__pwd
        data['database'] = self.__database
        data['index'] = self.__index
        data['collection'] = self.__collection
        data['timeout'] = self.__timeout
        return data

    def execute(self, query):
        try:
            result = GetResults().get_results(query, self.__type, self.__data_connect())
            return result
        except Exception as error:
            logger.error(f"Error in executing. Details: {error}")
            return None
