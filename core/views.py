from django.shortcuts import render
import json
from core.general_statistics.monitoring_statistic import MonitoringStatistic
from core.general_statistics.query_result_statistic import QueryResultsStatistic
from core.general_statistics.code_coverage_statistic import CodeCoverageStatistic
from core.general_statistics.routines_statistic import RoutineStatistic
# Create your views here.


def dashboard(request):
    monitoring = MonitoringStatistic()
    query_result = QueryResultsStatistic()
    code_coverage = CodeCoverageStatistic()
    routine = RoutineStatistic()

    data = {
        "registered_monitoring_count": monitoring.get_quantity_of_registered_monitoring(),
        "monitoring_count_running": routine.get_monitoring_count_running(),
        "count_sucess": query_result.get_quantity_of_results_with_success(),
        "count_error": query_result.get_quantity_of_results_with_errors(),
        "count_ag_ativation": monitoring.get_quantity_of_monitoring_waiting_for_activation(),
        "graphic_error": query_result.get_results(),
        "graphic_top_error": query_result.get_the_top_3_with_errors(),
        "graphic_coverage_level": code_coverage.exemplo()
    }

    return render(request, 'core/index.html', {'teste': data})


def login(request):
    return render(request, 'core/login.html')


def user(request):
    return render(request, 'core/user.html')
