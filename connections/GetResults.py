from .DataBases.PostGres import Postgres
from .DataBases.Oracle import Oracle
from .DataBases.SqlServer import SqlServer
from .DataBases.MySql import MySql

class GetResults:

    def __init__(self, query, _type, data):
        self.query = query
        self._type = _type
        self.data= data
    
    def get_results(self):
        cursor = self.__get_cursor(self._type, self.data)
        results = cursor.query(self.query)
        cursor.close()
        return results


    def __get_cursor(self, _type: str, data):
        if _type.upper() == 'SQL SERVER':
            cursor = SqlServer(data['server'], data['user'], data['pwd'], data['database'])
            return cursor
        elif _type.upper() == 'ORACLE':
            cursor = Oracle(data['server'], data['user'], data['pdw'], data['database'])
            return cursor
        elif _type.upper() == 'MYSQL':
            cursor = MySql(data['host'], data['user'], data['pwd'], data['database'])
        elif _type.upper() == 'POSTGRES':
            cursor = Postgres(data['host'], data['port'], data['user'], data['pwd'], data['database'])
            return cursor

