from django.db import models
from status.models import Status
from utils.custome_dbtypes import DateTimeFieldCustome, DateFieldCustome


class Zonas(models.Model):
    zona_id = models.IntegerField(primary_key=True)
    status_id = models.ForeignKey(Status, to_field='status_id', on_delete=models.PROTECT, db_column='status_id')
    zona = models.CharField(max_length=150, blank=False)
    created_at = DateTimeFieldCustome(null=True, blank=True)
    updated_at = DateTimeFieldCustome(null=True, blank=True)
    deleted_at = DateTimeFieldCustome(null=True, blank=True)

    class Meta:
        db_table = 'zonas'


class Settings(models.Model):
    setting_id = models.IntegerField(primary_key=True)
    empresa = models.CharField(max_length=250, blank=False)
    direccion = models.CharField(max_length=250, blank=False)
    ciudad = models.CharField(max_length=250, blank=False)
    telefonos = models.CharField(max_length=250, blank=False)
    actividad = models.CharField(max_length=250, blank=False)
    usar_fecha_servidor = models.CharField(max_length=50, blank=False)
    fecha_sistema = DateFieldCustome(null=True, blank=True)
    cant_per_page = models.IntegerField(blank=False, default=30)
    cantidad_lista = models.IntegerField(blank=False, default=10)
    perfiles_admin_listado_cajas = models.CharField(max_length=50, blank=False)
    costo_m3 = models.DecimalField(max_digits=5, decimal_places=2, blank=False, default=0)
    costo_minimo = models.DecimalField(max_digits=5, decimal_places=2, blank=False, default=0)
    unidad_minima_m3 = models.DecimalField(max_digits=5, decimal_places=2, blank=False, default=0)
    periodo_ini = models.CharField(max_length=50, default='202001', blank=False)
    periodo_fin = models.CharField(max_length=50, default='202005', blank=False)
    multa_pasivo = models.DecimalField(max_digits=5, decimal_places=2, default=0, blank=False)
    cant_lista_cobranza = models.IntegerField(blank=False, default=0)

    class Meta:
        db_table = 'settings'


class CobrosManuales(models.Model):
    cobro_manual_id = models.IntegerField(primary_key=True)
    cobro_manual = models.CharField(max_length=150, blank=False)
    monto_bs = models.DecimalField(max_digits=5, decimal_places=2, blank=False, default=0)
    status_id = models.ForeignKey(Status, to_field='status_id', on_delete=models.PROTECT, db_column='status_id')
    created_at = DateTimeFieldCustome(null=True, blank=True)
    updated_at = DateTimeFieldCustome(null=True, blank=True)
    deleted_at = DateTimeFieldCustome(null=True, blank=True)

    class Meta:
        db_table = 'cobros_manuales'


class CobrosMensuales(models.Model):
    cobro_mensual_id = models.IntegerField(primary_key=True)
    cobro_mensual = models.CharField(max_length=150, blank=False)
    monto_bs = models.DecimalField(max_digits=5, decimal_places=2, default=0, blank=False)
    status_id = models.ForeignKey(Status, to_field='status_id', on_delete=models.PROTECT, db_column='status_id')
    created_at = DateTimeFieldCustome(null=True, blank=True)
    updated_at = DateTimeFieldCustome(null=True, blank=True)
    deleted_at = DateTimeFieldCustome(null=True, blank=True)

    class Meta:
        db_table = 'cobros_mensuales'


class Puntos(models.Model):
    punto_id = models.IntegerField(primary_key=True)
    caja_id = models.IntegerField(default=0, blank=False)
    punto = models.CharField(max_length=50, blank=False)
    codigo = models.CharField(max_length=50, blank=False)
    status_id = models.ForeignKey(Status, to_field='status_id', on_delete=models.PROTECT, db_column='status_id')
    impresora_reportes = models.CharField(max_length=250, blank=False)
    created_at = DateTimeFieldCustome(null=True, blank=True)
    updated_at = DateTimeFieldCustome(null=True, blank=True)
    deleted_at = DateTimeFieldCustome(null=True, blank=True)

    class Meta:
        db_table = 'puntos'


class Cajas(models.Model):
    caja_id = models.IntegerField(primary_key=True)
    punto_id = models.ForeignKey(Puntos, to_field='punto_id', on_delete=models.PROTECT, db_column='punto_id')
    caja = models.CharField(max_length=50, blank=False)
    codigo = models.CharField(max_length=50, blank=False)
    status_id = models.ForeignKey(Status, to_field='status_id', on_delete=models.PROTECT, db_column='status_id')
    created_at = DateTimeFieldCustome(null=True, blank=True)
    updated_at = DateTimeFieldCustome(null=True, blank=True)
    deleted_at = DateTimeFieldCustome(null=True, blank=True)

    class Meta:
        db_table = 'cajas'
