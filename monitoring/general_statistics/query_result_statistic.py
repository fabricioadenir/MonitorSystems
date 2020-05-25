from monitoring.models import QueryResults
from django.utils import timezone
from datetime import date, timedelta
import locale


class QueryResultsStatistic:
    '''
    Classe responsável por gerar estatisticas sobre
    os resultados dos monitoramentos.
    '''

    def __init__(self):
        self.today = date.today()
        self.quantity_of_results_with_success = 0
        self.quantity_of_results_with_errors = 0
        self.results = {
            "days_of_the_month": list(),
            "list_of_routines": list()
        }
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
        list_of_routines = {}
        for result in results:
            execution_date = result.created_date.strftime("%d %b %y").title()
            self.results["days_of_the_month"].append(execution_date)

            if list_of_routines.get(result.query.name):
                list_of_routines[result.query.name].append(
                    result.count_values)
            else:
                list_of_routines.update(
                    {
                        f"{result.query.name}": [result.count_values]
                    })

        for key, value in list_of_routines.items():
            self.results['list_of_routines'].append({key: value})

        self.results["days_of_the_month"] = list(
            set(self.results["days_of_the_month"]))

        return self.results

    def get_the_top_3_with_errors(self):
        self.the_top_3_with_errors = {}
        return 10
