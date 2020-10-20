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
        results = QueryResults.objects.filter(
            created_date__gte=time_threshold).order_by('created_date')

        list_dates = list(set([result.created_date.strftime("%d %b %y").title()
                               for result in results]))

        list_dates.sort(
            key=lambda dates: datetime.strptime(dates, "%d %b %y"))

        dicionario_de_rotinas = {}

        # Cria um dicionario de rotinas com suas datas e erros por dia
        for result in results:
            execution_date = result.created_date.strftime("%d %b %y").title()
            if dicionario_de_rotinas.get(result.query.name):
                dicionario_de_rotinas[result.query.name].update(
                    {execution_date: result.count_values}
                )
            else:
                dicionario_de_rotinas.update(
                    {
                        f"{result.query.name}": {execution_date: result.count_values}
                    }
                )

        for dia in list_dates:
            for chave, valores in dicionario_de_rotinas.items():
                if not valores.get(dia) and valores.get(dia) != 0:
                    dicionario_de_rotinas[chave].update({dia: False})

        for item in dicionario_de_rotinas:
            dicionario_de_rotinas[item] = dict(sorted(
                dicionario_de_rotinas[item].items(),
                key=lambda x:  datetime.strptime(x[0], "%d %b %y")
            ))

        for rotina in dicionario_de_rotinas:
            dicionario_de_rotinas[rotina] = list(
                dicionario_de_rotinas[rotina].values())

        for key, value in dicionario_de_rotinas.items():
            self.results['list_of_routines'].append(
                {key: value})

        self.results['days_of_the_month'] = list_dates

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
