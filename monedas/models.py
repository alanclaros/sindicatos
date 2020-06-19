from django.db import models
from status.models import Status


class TiposMonedas(models.Model):
    tipo_moneda_id = models.IntegerField(primary_key=True, blank=False)
    tipo_moneda = models.CharField(max_length=50, blank=False)
    codigo = models.CharField(max_length=50, blank=False)

    class Meta:
        db_table = 'tipos_monedas'


class Monedas(models.Model):
    moneda_id = models.IntegerField(primary_key=True, blank=False)
    tipo_moneda_id = models.ForeignKey(TiposMonedas, to_field='tipo_moneda_id', db_column='tipo_moneda_id', on_delete=models.PROTECT)
    monto = models.DecimalField(max_digits=5, decimal_places=2, blank=False, default=0)
    status_id = models.ForeignKey(Status, to_field='status_id', db_column='status_id', on_delete=models.PROTECT)

    class Meta:
        db_table = 'monedas'
