from .get_routines import GetRoutines
from connections.connection import Connection
from core.models import QueryResults

class ExecutingRoutines(object):
    
    def __init__(self):
        self.all_routines = GetRoutines().get_list_routines()
        self.query = ""

    def save_results(self, results, query, note=None):
        if results:
            query_result = QueryResults(
                count_values=0,
                values='results',
                note=note
            )
            query_result.query = query
            query_result.save(force_insert=True)

    def build_info_executer(self, routine):
        data_connection = {}
        query = routine.query.query
        data_connection['type'] = routine.query.database._type
        data_connection['server'] = routine.query.database.server_instancia
        data_connection['ip'] = routine.query.database.ip
        data_connection['port'] = routine.query.database.port
        data_connection['uri'] = routine.query.database.uri
        data_connection['user'] = routine.query.database.user
        data_connection['pwd'] = routine.query.database.password
        data_connection['database'] = routine.query.database.database
        
        return query, data_connection

    '''No futuro será permitido consultas no MongoDB e outros dbs não realcionais,
     então se fará necessário esta função'''
    def build_query_for_type(self, query, _type):
        return query

    #Essa função fará sentido quando for usado thread nas consultas
    def next_run(self, routine):
        query, data_connect = self.build_info_executer(routine)   
        query = self.build_query_for_type(query, data_connect['type']) 
        connection = Connection(**data_connect)
        results = connection.execute(query)
        self.save_results(results, routine.query)   

    def exectute(self):
        print("Solititado execução de rotina")
        for routine in self.all_routines:
            query, data_connect = self.build_info_executer(routine)   
            query = self.build_query_for_type(query, data_connect['type']) 
            connection = Connection(**data_connect)
            results = connection.execute(query)
            self.save_results(results, routine)
