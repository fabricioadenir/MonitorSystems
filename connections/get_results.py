from .databases.postgres import Postgres
from .databases.oracle import Oracle
from .databases.sqlserver import SqlServer
from .databases.mysql import MySql
import logging

logger = logging.getLogger(__name__)


class GetResults:

    def get_results(self, query, _type, data):
        connector = self.__get_cursor(_type)
        cursor = connector(**data)
        try:
            if cursor:
                results = cursor.query(query)
                cursor.close()
                return results
            return None
        except Exception as e:
            logger.error(f"Erro detalhes: {e}")

    def __get_cursor(self, _type):
        connectios = {
            'sql_server': SqlServer,
            'oracle': Oracle,
            'mysql': MySql,
            'postgresql': Postgres
        }
        cursor = connectios.get(_type)
        return cursor
