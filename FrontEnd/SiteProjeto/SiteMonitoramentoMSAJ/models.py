from django.db import models
from django import forms
from django.utils import timezone

# Create your models here.


class Cliente(models.Model):
    nome_cliente = models.CharField(max_length=250, verbose_name='Cliente ')
    chave_cliente = models.CharField(primary_key=True, max_length=10, verbose_name='Sigla do Cliente')
    data_criacao = models.DateTimeField(verbose_name='Data de Criação ',editable=False, auto_now_add=True)
    data_modificacao = models.DateTimeField(verbose_name='Data Modificação ', editable=False, auto_now=True)



class Sistema(models.Model):
    #cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Cliente ')
    nome_sistema = models.CharField(max_length=250, verbose_name='Sistema ')
    sigla_sistema = models.CharField(max_length=10, verbose_name='Sigla do Sistema ')
    chave_sistema = models.CharField(primary_key=True, max_length=10, verbose_name='ID do Sistema ')
    data_criacao = models.DateTimeField(verbose_name='Data de Criação ',editable=False, auto_now_add=True)
    data_modificacao = models.DateTimeField(verbose_name='Data Modificação ', editable=False, auto_now=True)

class Modulo(models.Model):
    id_sistema = models.ForeignKey(Sistema, on_delete=models.CASCADE, verbose_name='Sistema')
    #chave_modulo = models.CharField(primary_key=True, max_length=250, verbose_name='Sigla do Modulo ')
    nome_modulo = models.CharField(max_length=250, verbose_name='Modulo ')
    descricao_modulo = models.CharField(primary_key=True, max_length=250, verbose_name='Local do Sistema ')
    
    data_criacao = models.DateTimeField(verbose_name='Data de Criação ',editable=False, auto_now_add=True)
    data_modificacao = models.DateTimeField(verbose_name='Data Modificação ', editable=False, auto_now=True)



class BaseDeDados(models.Model):

    DRIVE_CHOICES = (
        (u'sql server', u'SQL Server'),
        (u'oracle', u'Oracle'),
    )

    #chave_base = models.CharField(primary_key=True, max_length=20, verbose_name='Sigla da Base ')
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Cliente ')
    id_sistema = models.ForeignKey(Sistema, on_delete=models.CASCADE, verbose_name='Sistema ')
    driver = models.CharField(max_length=200, choices= DRIVE_CHOICES, verbose_name='Driver da Base ')
    server_instancia = models.CharField(null=True, blank=True, max_length=50, verbose_name='Servidor \ Instância ')
    alias = models.CharField(primary_key=True, max_length=100, verbose_name='Nome da Base ')
    usuario = models.CharField(max_length=100, verbose_name='Usuário ')
    password = models.CharField(max_length= 50, verbose_name='Senha ')
    data_criacao = models.DateTimeField(verbose_name='Data de Criação ',editable=False, auto_now_add=True)
    data_modificacao = models.DateTimeField(verbose_name='Data Modificação ', editable=False, auto_now=True)


class Consulta(models.Model):
    
    ORIGEM_CHOICES = (
        (u'rtc', u'RTC'),
        (u'sac', u'SAC'),
        (u'sccd', u'SCCD'),
        (u'interno', u'INTERNO'),

    )

    chave_consulta = models.AutoField(primary_key=True)
    nome_consulta = models.CharField(unique=True, verbose_name='Nome da Consulta ', max_length=250)
    descricao_consulta = models.CharField(verbose_name='Descrição ', max_length=500)
    origem_consulta = models.CharField(max_length=20,choices = ORIGEM_CHOICES, verbose_name='Origem da Conulta ')
    descricao_origem = models.TextField(verbose_name='Descição da Origem ')
    nome_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Cliente ')
    nome_sistema = models.ForeignKey(Sistema,on_delete=models.CASCADE, verbose_name='Sistema ')
    nome_modulo_consulta = models.ForeignKey(Modulo, on_delete=models.CASCADE, verbose_name='Local do Sistema ')
    nome_base = models.ForeignKey(BaseDeDados, on_delete=models.CASCADE, verbose_name='Base ')
    consulta_ativa = models.BooleanField(verbose_name='Consulta Ativa ')
    data_inicio = models.DateTimeField('Data Inicio das Consultas ')
    data_fim = models.DateTimeField('Data Fim das Consultas ')
    #consulta_versao = models.BooleanField(verbose_name='Consultar Versão em Produção ')
    max_consulta = models.PositiveIntegerField(verbose_name='Só Rodar Consulta Com Valor Menor Que ')
    sql_qtd_consulta = models.TextField(verbose_name='SQL Que Retorna a Quantidade de Valores ')
    sql_valores_consulta = models.TextField(verbose_name='SQL Que Retorna Os Valores ')
    data_criacao = models.DateTimeField(verbose_name='Data de Criação ',editable=False, auto_now_add=True)
    data_modificacao = models.DateTimeField(verbose_name='Data Modificação ', editable=False, auto_now=True)

  
class ResultadoConsulta(models.Model):

    chave_resultado = models.AutoField(primary_key= True, verbose_name='ID do Resultado ')
    consulta_chave = models.ForeignKey(Consulta, on_delete=models.CASCADE, verbose_name='ID da Consulta')
    nuseqexecucao = models.IntegerField(default=0, verbose_name='Sequência de Execução ')
    dtexecucao = models.DateTimeField(verbose_name='Data da Execução')
    deversao = models.CharField(max_length=150, verbose_name='Versão do Cliente em Produção')
    qtdvalores = models.IntegerField(verbose_name='Quantidade Encontrada ')
    valores_consulta = models.TextField(null=True, verbose_name='Resultados ')
    observacao = models.TextField(null=True, verbose_name='Observação ')

# Verificar antes o tido de dados datetime ou datetime2 antes de rodar o migrate

