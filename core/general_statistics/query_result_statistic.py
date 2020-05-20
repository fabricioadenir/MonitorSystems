from core.models import QueryResults
from django.db.models import Count
from django.utils import timezone
from datetime import date, timedelta
import locale
import json


class QueryResultsStatistic:
    '''
    Classe responsável por gerar estatisticas sobre
    os resultados dos monitoramentos.
    '''

    def __init__(self):
        self.today = date.today()
        self.quantity_of_results_with_success = 0
        self.quantity_of_results_with_errors = 0
        self.results = {}
        self.the_top_3_with_errors = {}

    def get_quantity_of_results_with_success(self):
        self.quantity_of_results_with_success = len(QueryResults.objects.filter(
            count_values=0, created_date__gte=self.today).distinct())
        return self.quantity_of_results_with_success

    def get_quantity_of_results_with_errors(self):
        self.quantity_of_results_with_errors = len(QueryResults.objects.filter(
            created_date__gte=self.today).exclude(count_values=0).distinct())
        return self.quantity_of_results_with_errors

    def get_results(self):
        locale.setlocale(locale.LC_ALL, 'pt_pt.UTF-8')
        how_many_days = 30  # Disponibilizar configuração
        time_threshold = timezone.now() - timedelta(days=how_many_days)
        results = QueryResults.objects.filter(created_date__gte=time_threshold)
        self.results = {
            "dias_do_mes": [],
            "lista_de_rotinas": {}
        }
        for result in results:
            execution_date = result.created_date.strftime("%d %b %y").title()
            self.results["dias_do_mes"].append(execution_date)

            if not self.results["lista_de_rotinas"].get(result.query.id):
                self.results["lista_de_rotinas"].update(
                    {
                        f"{result.query.id}": {
                            "name": result.query.name,
                            "values": [result.count_values]
                        }
                    })
            
            else:
                self.results["lista_de_rotinas"][result.query.id]["values"].append(
                    result.count_values)

        self.results["dias_do_mes"] = list(set(self.results["dias_do_mes"]))

        return self.results

    def get_the_top_3_with_errors(self):
        self.the_top_3_with_errors = {}
        return 10


# exemplo do retorno do resultado
# teste = {
#     'dias_do_mes': [
#         '17 Mai 20', 
#         '18 Mai 20', 
#         '16 Mai 20'
#         ], 
#     'lista_de_rotinas': {
#         'Atualizar Documento': [0, 1, 15], 
#         'Fluxo de Trabalho': [0, 1, 20], 
#         'Monitorar cadastro de usuários': [0, 1, 35]
#         }
#     }
