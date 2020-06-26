from django.db import models


class TmpListadoMes(models.Model):
    tmp_listado_mes_id = models.IntegerField(primary_key=True)
    fecha = models.CharField(max_length=50, blank=False)
    operacion = models.CharField(max_length=250, blank=False)
    monto = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    mes = models.CharField(max_length=50, blank=False)

    class Meta:
        db_table = 'tmp_listado_mes'
