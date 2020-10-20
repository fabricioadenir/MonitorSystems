from .databases.postgres import Postgres
from .databases.oracle import Oracle
from .databases.sqlserver import SqlServer
from .databases.mysql import MySql
from .databases.mongodb import MongoDB
from .databases._elasticsearch import MyElasticSearch
import logging

logger = logging.getLogger(__name__)


class GetResults:

    def get_results(self, query, data):
        connector = self.__get_cursor(data.get('type'))
        try:
            if connector:
                cursor = connector(**data)
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
            'postgresql': Postgres,
            'mongodb': MongoDB,
            'elasticsearch': MyElasticSearch
        }
        cursor = connectios.get(_type)
        return cursor
