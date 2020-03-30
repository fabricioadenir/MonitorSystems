from django.contrib import admin
from routine.models import Routines

class RoutineAdmin(admin.ModelAdmin):
    model = Routines
    list_display = ['query', 'active_query', 'initial_date', 'and_date', 'created_date', 'modified_date']

    list_filter = ['query', 'active_query', 'initial_date', 'and_date', 'created_date', 'modified_date']

    search_fields = ['query']


admin.site.register(Routines, RoutineAdmin)
