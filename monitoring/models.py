from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from datetime import datetime


class Profile(AbstractUser):
    positon = models.CharField(
        max_length=250, verbose_name='Cargo ', null=True, blank=True)
    team = models.CharField(
        max_length=40, verbose_name='Time ', null=True, blank=True)
    detail = models.CharField(
        max_length=500, verbose_name='Detalhes ', null=True, blank=True)
    photo = models.ImageField("Foto", null=True, blank=True,
                              upload_to='static/img')
    created_date = models.DateTimeField(
        verbose_name='Data criação ', editable=False, auto_now_add=True)
    modified_date = models.DateTimeField(
        verbose_name='Data modificação ', editable=False, auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "0-User"


class Client(models.Model):
    name = models.CharField(max_length=250, verbose_name='Cliente ')
    slug = models.SlugField(
        unique=True, editable=False, verbose_name='Slug')
    created_date = models.DateTimeField(
        verbose_name='Data criação ', editable=False, auto_now_add=True)
    modified_date = models.DateTimeField(
        verbose_name='Data modificação ', editable=False, auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Client, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "1-Cliente"


class System(models.Model):
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, verbose_name='Cliente ')
    name = models.CharField(max_length=250, verbose_name='Sistema ')
    slug = models.SlugField(
        unique=True, editable=False, verbose_name='Slug')
    created_date = models.DateTimeField(
        verbose_name='Data criação ', editable=False, auto_now_add=True)
    modified_date = models.DateTimeField(
        verbose_name='Data modificação ', editable=False, auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(System, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "2-Sistema"


class Module(models.Model):
    system = models.ForeignKey(
        System, on_delete=models.CASCADE, verbose_name='Sistema ')
    name = models.CharField(max_length=250, verbose_name='Modulo ')
    slug = models.SlugField(
        unique=True, editable=False, verbose_name='Slug')
    description = models.CharField(
        max_length=250, verbose_name='Descrição do modulo ')
    created_date = models.DateTimeField(
        verbose_name='Data criação ', editable=False, auto_now_add=True)
    modified_date = models.DateTimeField(
        verbose_name='Data modificação ', editable=False, auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Module, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "3-Modulo"


class Functionality(models.Model):
    module = models.ForeignKey(
        Module, on_delete=models.CASCADE, verbose_name='Modulo')
    name = models.CharField(max_length=250, verbose_name='Funcionalidade ')
    slug = models.SlugField(
        unique=True, editable=False, verbose_name='Slug')
    description = models.CharField(
        max_length=250, verbose_name='Descrição da funcionalidade ')
    created_date = models.DateTimeField(
        verbose_name='Data criação ', editable=False, auto_now_add=True)
    modified_date = models.DateTimeField(
        verbose_name='Data modificação ', editable=False, auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Functionality, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "4-Funcionalidade"


class DataBases(models.Model):
    DRIVE_CHOICES = (
        (u'sql_server', u'SQL Server'),
        (u'oracle', u'Oracle'),
        (u'mongodb', u'MongoDB'),
        (u'postgresql', u'PostgreSQL'),
        (u'mysql', u'MySQL'),
        (u'elasticsearch', u'ElascticSearch'),
        (u'rabbitmq', u'RabbitMQ'),
    )
    name = models.CharField(max_length=250, verbose_name='Repositório ')
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, verbose_name='Cliente ')
    system = models.ForeignKey(
        System, on_delete=models.CASCADE, verbose_name='Sistema ')
    _type = models.CharField(
        max_length=200, choices=DRIVE_CHOICES, verbose_name='Tipo de repositório ')
    server_instancia = models.CharField(
        null=True, default=None, blank=True, max_length=50,
        verbose_name='Server Instancia ')
    ip = models.CharField(
        null=True, default=None, blank=True, max_length=50, verbose_name='IP ')
    port = models.CharField(
        null=True, default=None, blank=True, max_length=50,
        verbose_name='PORT ')
    uri = models.CharField(
        null=True, default=None, blank=True, max_length=200,
        verbose_name='URI ')
    index = models.CharField(
        null=True, default=None, blank=True, max_length=200,
        verbose_name='Index ')
    database = models.CharField(
        max_length=100, verbose_name='DataBase ', null=True, blank=True)
    collection = models.CharField(
        max_length=100, verbose_name='Coleção Mongo  ', null=True, blank=True)
    queue = models.CharField(
        max_length=100, verbose_name='Fila  ', null=True, blank=True)
    user = models.CharField(
        null=True, default=None, blank=True, max_length=100,
        verbose_name='Usuário ')
    password = models.CharField(
        null=True, default=None, blank=True, max_length=50,
        verbose_name='Senha ')
    created_date = models.DateTimeField(
        verbose_name='Data criação ', editable=False, auto_now_add=True)
    modified_date = models.DateTimeField(
        verbose_name='Data modificação ', editable=False, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "5-DataBases"


class Monitoring(models.Model):
    ORIGEM_CHOICES = (
        (u'rtc', u'RTC'),
        (u'sac', u'SAC'),
        (u'sccd', u'SCCD'),
        (u'interno', u'INTERNO'),
        (u'jira', u'Jira'),
        (u'monitoramento', u'Monitoramento'),
        (u'outro', u'Outro'),

    )
    name = models.CharField(
        unique=True, verbose_name='Nome ', max_length=250)
    source = models.CharField(
        max_length=20, choices=ORIGEM_CHOICES, verbose_name='Origem ')
    description_source = models.TextField(
        verbose_name='Descição ', blank=True, null=True)
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, verbose_name='Cliente ')
    system = models.ForeignKey(
        System, on_delete=models.CASCADE, verbose_name='Sistema ')
    module = models.ForeignKey(
        Module, on_delete=models.CASCADE,
        verbose_name='Modulo ')
    functionality = models.ForeignKey(
        Functionality, on_delete=models.CASCADE,
        verbose_name='Funcionalidade ', null=True, blank=True)
    database = models.ForeignKey(
        DataBases, on_delete=models.CASCADE, verbose_name='Repositório')
    timeout = models.PositiveIntegerField(
        verbose_name='TimeOut em segundos ',
        help_text="Tempo de espera pela execução da query.")
    query = models.TextField(
        verbose_name='Query ')
    last_execution = models.DateField(verbose_name="Ultima execução",
                                      null=True, blank=True)
    is_enabled = models.BooleanField(
        verbose_name="Está Cadastrada ", default=False, editable=False)
    created_date = models.DateTimeField(
        verbose_name='Data criação ', editable=False, auto_now_add=True)
    modified_date = models.DateTimeField(
        verbose_name='Data modificação ', editable=False, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "6-Cadastrar Monitoramento"


def increment_invoice_number():
    pass


class QueryResults(models.Model):
    query = models.ForeignKey(
        Monitoring, on_delete=models.CASCADE, verbose_name='Monitoramento',
        editable=True)
    count_values = models.IntegerField(
        verbose_name='Quantidade de resultados ', editable=True)
    values = models.TextField(
        null=True, verbose_name='Resultados ', editable=True)
    note = models.TextField(
        null=True, verbose_name='Observação ', editable=True)
    created_date = models.DateTimeField(
        verbose_name='Data criação ', editable=True, auto_now_add=True)

    def __str__(self):
        return self.query.name

    class Meta:
        verbose_name_plural = "8-Resultados de Moniramento"


class Routines(models.Model):
    query = models.ForeignKey(
        Monitoring, on_delete=models.CASCADE, verbose_name='Monitoramento ')
    active_query = models.BooleanField(verbose_name='Ativado? ')
    initial_date = models.DateField('Início ')
    and_date = models.DateField('Fim ')
    created_date = models.DateTimeField(
        verbose_name='Data criação ', editable=False, auto_now_add=True)
    modified_date = models.DateTimeField(
        verbose_name='Data modificação ', editable=False, auto_now=True)

    date = datetime.now().strftime("%Y-%m-%d")

    def save(self, *args, **kwargs):
        date_inicital = self.initial_date.strftime("%Y-%m-%d")
        and_date = self.and_date.strftime("%Y-%m-%d")

        if (date_inicital <= self.date) and (and_date >= self.date) and (self.active_query):
            self.query.is_enabled = True
            self.query.save(update_fields=['is_enabled'])
        else:
            self.query.is_enabled = False
        self.query.save(update_fields=['is_enabled'])
        super(Routines, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "7-Rotina"
