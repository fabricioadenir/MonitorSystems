from django.contrib import admin
from django.shortcuts import redirect
from .models import Client, System, Module, Functionality, Functionality, DataBases, Monitoring, QueryResults, Routines, User
from .forms import BaseDeDadosForm, UserForm


class UserAdmin(admin.ModelAdmin):
    form = UserForm
    list_display = ['name', 'photo', 'id_user', 'positon', 'email', 'team', 'detail', 'created_date', 'modified_date']

    list_filter = ['name', 'id_user', 'positon', 'email', 'team', 'detail', 'created_date', 'modified_date']

    search_fields = ['name', 'id_user']


admin.site.register(User, UserAdmin)


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
                    'system', 'last_execution', 'functionality', 'timeout', 'is_enabled', 'created_date', 'modified_date']

    list_filter = ['name', 'source', 'description_source', 'client',
                   'system', 'functionality', 'database',
                   'timeout', 'last_execution', 'is_enabled', 'created_date', 'modified_date']

    search_fields = ['name', 'is_enabled', 'source', 'description_source', 'client__id_client', 'system__id',
                     'functionality__description', 'database__database', 'sql_qtd_consulta', 'sql_valores_consulta']


admin.site.register(Monitoring, MonitoringAdmin)


class QueryResultsAdmin(admin.ModelAdmin):
    model = QueryResults

    list_display = ['query', 'created_date', 'count_values', 'values']

    list_filter = ['query', 'created_date', 'count_values']

    search_fields = ['query', 'created_date', 'count_values', 'values']


admin.site.register(QueryResults, QueryResultsAdmin)


class RoutineAdmin(admin.ModelAdmin):
    model = Routines
    list_display = ['query', 'active_query', 'initial_date',
                    'and_date', 'created_date', 'modified_date']

    list_filter = ['query', 'active_query', 'initial_date',
                   'and_date', 'created_date', 'modified_date']

    search_fields = ['query']


admin.site.register(Routines, RoutineAdmin)
