from django.db import models
from core.models import Monitoring


class Routines(models.Model):
    query = models.ForeignKey(Monitoring, on_delete=models.CASCADE, verbose_name='Query ')
    active_query = models.BooleanField(verbose_name='Ativar consulta ')
    initial_date = models.DateField('Inicio das consultas ')
    and_date = models.DateField('Válido até ')
    created_date = models.DateTimeField(
        verbose_name='Data criação ', editable=False, auto_now_add=True)
    modified_date = models.DateTimeField(
        verbose_name='Data modificação ', editable=False, auto_now=True)

    class Meta:
        verbose_name_plural = "Rotina"
