from monitoring.models import QueryResults
from django.utils import timezone
from datetime import date, timedelta, datetime
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
        self.the_top_3_with_errors = dict()

    def get_quantity_of_results_with_success(self):
        self.quantity_of_results_with_success = len(QueryResults.objects.filter(
            count_values=0, created_date__gte=self.today).values('query').distinct())
        return self.quantity_of_results_with_success

    def get_quantity_of_results_with_errors(self):
        self.quantity_of_results_with_errors = len(QueryResults.objects.filter(
            created_date__gte=self.today).values('query').distinct().exclude(count_values=0))
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
                list_of_routines[result.query.name].update(
                    {execution_date: result.count_values})
            else:
                list_of_routines.update(
                    {
                        f"{result.query.name}": {execution_date: result.count_values}
                    })

        self.results["days_of_the_month"] = list(
            set(self.results["days_of_the_month"]))

        for dia in self.results['days_of_the_month']:
            for chave, valores in list_of_routines.items():
                if not valores.get(dia) and valores.get(dia) != 0:
                    list_of_routines[chave].update({dia: False})

        self.results["days_of_the_month"].sort(
            key=lambda dates: datetime.strptime(dates, "%d %b %y"))

        for key, value in list_of_routines.items():
            aqui = dict(sorted(value.items()))
            self.results['list_of_routines'].append(
                {key: list(aqui.values())})

        return self.results

    def get_the_top_3_with_errors(self):
        results = QueryResults.objects.filter(
            created_date__gte=self.today).exclude(count_values=0).distinct()

        list_of_items_with_error = {
            item.query.name: item.count_values for item in results}

        self.the_top_3_with_errors = {key: rank for rank, key in enumerate(
            sorted(list_of_items_with_error, key=list_of_items_with_error.get, reverse=True))}

        for chave, valor in list_of_items_with_error.items():
            self.the_top_3_with_errors[chave] = valor

        self.the_top_3_with_errors = [
            {chave: valor} for chave, valor in self.the_top_3_with_errors.items()]
        return self.the_top_3_with_errors[:3]
