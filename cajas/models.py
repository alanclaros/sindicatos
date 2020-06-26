from django.db import models
from status.models import Status
from settings.models import Puntos, Cajas
from monedas.models import Monedas
from utils.custome_dbtypes import DateTimeFieldCustome, DateFieldCustome
from django.conf import settings


class CajasIngresos(models.Model):
    caja_ingreso_id = models.IntegerField(primary_key=True)
    caja_id = models.ForeignKey(Cajas, to_field='caja_id', on_delete=models.PROTECT, db_column='caja_id')
    punto_id = models.ForeignKey(Puntos, to_field='punto_id', on_delete=models.PROTECT, db_column='punto_id')
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, to_field='id', on_delete=models.PROTECT, db_column='user_id')
    socio_cambio_estado_id = models.IntegerField(blank=False, default=0)
    socio_cobro_id = models.IntegerField(blank=False, default=0)
    fecha = DateTimeFieldCustome(null=True, blank=True)
    concepto = models.CharField(max_length=250, blank=False)
    monto = models.DecimalField(max_digits=10, decimal_places=2, blank=False, default=0)
    user_id_anula = models.IntegerField(null=True)
    motivio_anula = models.CharField(max_length=250, null=True)
    status_id = models.ForeignKey(Status, to_field='status_id', on_delete=models.PROTECT, db_column='status_id')
    created_at = DateTimeFieldCustome(null=True, blank=True)
    updated_at = DateTimeFieldCustome(null=True, blank=True)
    deleted_at = DateTimeFieldCustome(null=True, blank=True)

    class Meta:
        db_table = 'cajas_ingresos'


class CajasEgresos(models.Model):
    caja_egreso_id = models.IntegerField(primary_key=True)
    caja_id = models.ForeignKey(Cajas, to_field='caja_id', on_delete=models.PROTECT, db_column='caja_id')
    punto_id = models.ForeignKey(Puntos, to_field='punto_id', on_delete=models.PROTECT, db_column='punto_id')
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, to_field='id', on_delete=models.PROTECT, db_column='user_id')
    socio_cambio_estado_id = models.IntegerField(blank=False, default=0)
    socio_cobro_id = models.IntegerField(blank=False, default=0)
    fecha = DateTimeFieldCustome(null=True, blank=True)
    concepto = models.CharField(max_length=250, blank=False)
    monto = models.DecimalField(max_digits=10, decimal_places=2, blank=False, default=0)
    user_id_anula = models.IntegerField(null=True)
    motivio_anula = models.CharField(max_length=250, null=True)
    status_id = models.ForeignKey(Status, to_field='status_id', on_delete=models.PROTECT, db_column='status_id')
    created_at = DateTimeFieldCustome(null=True, blank=True)
    updated_at = DateTimeFieldCustome(null=True, blank=True)
    deleted_at = DateTimeFieldCustome(null=True, blank=True)

    class Meta:
        db_table = 'cajas_egresos'


class CajasOperaciones(models.Model):
    caja_operacion_id = models.IntegerField(primary_key=True)
    caja_id = models.ForeignKey(Cajas, to_field='caja_id', on_delete=models.PROTECT, db_column='caja_id')
    fecha = DateFieldCustome(null=True, blank=True)
    aperturado = models.CharField(max_length=10, blank=False)
    monto_apertura = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    usuario_apertura_id = models.IntegerField(blank=False)
    usuario_apertura_r_id = models.IntegerField(blank=False)
    cerrado = models.CharField(max_length=10, blank=False)
    monto_cierre = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    usuario_cierre_id = models.IntegerField(blank=False)
    usuario_cierre_r_id = models.IntegerField(blank=False)
    status_id = models.ForeignKey(Status, to_field='status_id', on_delete=models.PROTECT, db_column='status_id')
    created_at = DateTimeFieldCustome(null=True, blank=True)
    updated_at = DateTimeFieldCustome(null=True, blank=True)
    deleted_at = DateTimeFieldCustome(null=True, blank=True)

    class Meta:
        db_table = 'cajas_operaciones'


class CajasOperacionesDetalles(models.Model):
    caja_operacion_detalle_id = models.IntegerField(primary_key=True)
    caja_operacion_id = models.ForeignKey(CajasOperaciones, to_field='caja_operacion_id', on_delete=models.PROTECT, db_column='caja_operacion_id')
    moneda_id = models.ForeignKey(Monedas, to_field='moneda_id', on_delete=models.PROTECT, db_column='moneda_id')
    cantidad_apertura = models.IntegerField(blank=False)
    cantidad_cierre = models.IntegerField(blank=False)

    class Meta:
        db_table = 'cajas_operaciones_detalles'
