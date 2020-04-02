from .databases.postgres import Postgres
from .databases.oracle import Oracle
from .databases.sqlserver import SqlServer
from .databases.mysql import MySql

class GetResults:

    def get_results(self, query, _type, data):
        cursor = self.__get_cursor(_type, data)
        if cursor:
            results = cursor.query(query)
            cursor.close()
            return results
        return None


    def __get_cursor(self, _type, data):
        connectios = {
            'sql_server': SqlServer,
            'oracle': Oracle,
            'mysql': MySql,
            'postgresql': Postgres
        }
        cursor = connectios.get(_type)
        cursor(**data)
        return cursor


