from django.contrib import admin
from .models import Client, System, Module, Functionality, Functionality, DataBases, Monitoring, QueryResults
from .forms import BaseDeDadosForm


class ClientAdmin(admin.ModelAdmin):
    model = Client
    list_display = ['name', 'created_date', 'modified_date']

    list_filter = ['name', 'created_date', 'modified_date']

    search_fields = ['name']


admin.site.register(Client, ClientAdmin)


class SystemAdmin(admin.ModelAdmin):
    model = System
    list_display = ['name', 'created_date', 'modified_date']

    list_filter = ['name', 'created_date', 'modified_date']

    search_fields = ['name']


admin.site.register(System, SystemAdmin)


class ModuleAdmin(admin.ModelAdmin):
    model = Module

    list_display = ['system', 'name', 'description',
                    'created_date', 'modified_date']

    list_filter = ['system', 'name', 'description',
                   'created_date', 'modified_date']

    search_fields = ['system', 'name', 'description',
                     'created_date', 'modified_date']


admin.site.register(Module, ModuleAdmin)


class FunctionalityAdmin(admin.ModelAdmin):
    model = Functionality

    list_display = ['module', 'name', 'description',
                    'created_date', 'modified_date']

    list_filter = ['module', 'name', 'description',
                   'created_date', 'modified_date']

    search_fields = ['module', 'name', 'description',
                     'created_date', 'modified_date']


admin.site.register(Functionality, FunctionalityAdmin)


class DataBasesAdmin(admin.ModelAdmin):
    form = BaseDeDadosForm

    list_display = ['database',
                    'created_date', 'modified_date']

    list_filter = ['database',
                   'created_date', 'modified_date']

    list_display = ['client', 'system', 'database',
                    'created_date', 'modified_date']

    list_filter = ['client', 'system', 'database',
                   'created_date', 'modified_date']

    search_fields = ['client__id_client', 'system__id', 'database']


admin.site.register(DataBases, DataBasesAdmin)


class MonitoringAdmin(admin.ModelAdmin):
    model = Monitoring

    list_display = ['name', 'source', 'description_source', 'client',
                    'system', 'functionality', 'max_count_query', 'created_date', 'modified_date']

    list_filter = ['name', 'source', 'description_source', 'client',
                   'system', 'functionality', 'database',
                   'max_count_query', 'created_date', 'modified_date']

    search_fields = ['name', 'source', 'description_source', 'client__id_client', 'system__id',
                     'functionality__description', 'database__database', 'sql_qtd_consulta', 'sql_valores_consulta']


admin.site.register(Monitoring, MonitoringAdmin)


class QueryResultsAdmin(admin.ModelAdmin):
    model = QueryResults

    list_display = ['query', 'get_name', 'execution_number',
                    'date_query', 'count_values', 'values']

    list_filter = ['query', 'execution_number', 'date_query', 'count_values']

    search_fields = ['query', 'execution_number',
                     'date_query', 'count_values', 'values']

    def get_name(self, obj):
        return obj.id.query
    get_name.admin_order_field = 'query'
    get_name.short_description = 'Nome da Consulta'


admin.site.register(QueryResults, QueryResultsAdmin)
