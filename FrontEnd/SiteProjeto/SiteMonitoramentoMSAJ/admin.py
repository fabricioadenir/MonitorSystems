from django.contrib import admin
from SiteMonitoramentoMSAJ.models import Cliente, Sistema, Modulo, BaseDeDados, Consulta, ResultadoConsulta

class ClienteAdmin(admin.ModelAdmin):
    model=Cliente
    list_display = ['nome_cliente','data_criacao','data_modificacao']

    list_filter = ['nome_cliente','data_criacao','data_modificacao']

    search_fields = ['nome_cliente']

    save_on_top = True
admin.site.register(Cliente, ClienteAdmin)


class SistemaAdmin(admin.ModelAdmin):
    model = Sistema
    list_display = ['nome_sistema','data_criacao','data_modificacao']

    list_filter = ['nome_sistema','data_criacao','data_modificacao']

    search_fields = ['nome_sistema']

    save_on_top=True
admin.site.register(Sistema, SistemaAdmin)

class ModuloAdmin(admin.ModelAdmin):
    model = Modulo

    list_display = ['id_sistema','nome_modulo', 'descricao_modulo','data_criacao','data_modificacao']

    list_filter = ['id_sistema','nome_modulo', 'descricao_modulo','data_criacao','data_modificacao']

    search_fields =['id_sistema__chave_sistema','nome_modulo', 'descricao_modulo','data_criacao','data_modificacao']

    save_on_top=True
admin.site.register(Modulo, ModuloAdmin)

class BaseDeDadosAdmin(admin.ModelAdmin):
    model = BaseDeDados

    list_display = ['id_cliente','id_sistema','alias','data_criacao','data_modificacao']

    list_filter = ['id_cliente','id_sistema','alias','data_criacao','data_modificacao']

    search_fields = ['id_cliente__chave_cliente','id_sistema__chave_sistema','alias']

    save_on_top=True
admin.site.register(BaseDeDados, BaseDeDadosAdmin)

class ConsultaAdmin(admin.ModelAdmin):
    model = Consulta

    list_display = ['nome_consulta', 'descricao_consulta','origem_consulta','descricao_origem','nome_cliente',
    'nome_sistema','nome_modulo_consulta','consulta_ativa','data_inicio','data_fim',
    'max_consulta','data_criacao','data_modificacao']
    
    list_filter = ['nome_consulta', 'descricao_consulta','origem_consulta','descricao_origem','nome_cliente',
    'nome_sistema','nome_modulo_consulta','nome_base','consulta_ativa','data_inicio','data_fim',
    'max_consulta','data_criacao','data_modificacao']
    
    #search_fields = ['nome_consulta', 'descricao_consulta','descricao_origem','nome_cliente__chave_cliente',
    #'nome_sistema__chave_sistema','nome_modulo_consulta__chave_modulo','nome_base__chave_base','sql_qtd_consulta__sql',
    #'sql_valores_consulta__sql2']
    
    search_fields = ['nome_consulta','descricao_consulta','origem_consulta','descricao_origem','nome_cliente__chave_cliente','nome_sistema__chave_sistema',
    'nome_modulo_consulta__descricao_modulo','nome_base__chave_base','sql_qtd_consulta','sql_valores_consulta']
    save_on_top = True
admin.site.register(Consulta, ConsultaAdmin)

class ResultadoConsultaAdmin(admin.ModelAdmin):
    model = ResultadoConsulta

    list_display = ['chave_resultado','get_name','nuseqexecucao','dtexecucao','deversao','qtdvalores','valores_consulta'] 

    

    list_filter = ['chave_resultado','nuseqexecucao','dtexecucao','deversao','qtdvalores'] 

    search_fields = ['chave_resultado','nuseqexecucao','dtexecucao','deversao','qtdvalores','valores_consulta'] 
    #search_fields = ['valores_consulta'] 

    def get_name(self, obj):
        return obj.consulta_chave.nome_consulta
    get_name.admin_order_field = 'consulta_chave'
    get_name.short_description = 'Nome da Consulta'
    
    

    save_on_top = True
admin.site.register(ResultadoConsulta, ResultadoConsultaAdmin)

# Register your models here.