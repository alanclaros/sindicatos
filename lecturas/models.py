from django.db import models

from status.models import Status
from settings.models import Puntos, Cajas, CobrosManuales, CobrosMensuales
from monedas.models import Monedas
from socios.models import Socios

from utils.custome_dbtypes import DateTimeFieldCustome, DateFieldCustome
from django.conf import settings


class Lecturas(models.Model):
    lectura_id = models.IntegerField(primary_key=True)
    socio_id = models.ForeignKey(Socios, to_field='socio_id', on_delete=models.PROTECT, db_column='socio_id')
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, to_field='id', on_delete=models.PROTECT, db_column='user_id')
    status_id = models.ForeignKey(Status, to_field='status_id', on_delete=models.PROTECT, db_column='status_id')
    periodo = models.CharField(max_length=20, blank=False)
    lectura = models.IntegerField(blank=False)
    costo_m3 = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    consumo = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    suma_cobros_manuales = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    fecha_cobro = DateTimeFieldCustome(null=True, blank=True)
    punto_id = models.IntegerField(blank=False)
    caja_id = models.IntegerField(blank=False)
    user_id_cobro = models.IntegerField(blank=False)
    observacion = models.CharField(max_length=250, blank=False)
    created_at = DateTimeFieldCustome(null=True, blank=True)
    updated_at = DateTimeFieldCustome(null=True, blank=True)
    deleted_at = DateTimeFieldCustome(null=True, blank=True)

    class Meta:
        db_table = 'lecturas'


class LecturasAnulados(models.Model):
    lectura_anulado_id = models.IntegerField(primary_key=True)
    lectura_id = models.IntegerField(blank=False)
    socio_id = models.ForeignKey(Socios, to_field='socio_id', on_delete=models.PROTECT, db_column='socio_id')
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, to_field='id', on_delete=models.PROTECT, db_column='user_id')
    status_id = models.ForeignKey(Status, to_field='status_id', on_delete=models.PROTECT, db_column='status_id')
    periodo = models.CharField(max_length=20, blank=False)
    lectura = models.IntegerField(blank=False)
    costo_m3 = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    consumo = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    suma_cobros_manuales = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    fecha_cobro = DateTimeFieldCustome(null=True, blank=True)
    punto_id = models.IntegerField(blank=False)
    caja_id = models.IntegerField(blank=False)
    user_id_cobro = models.IntegerField(blank=False)
    observacion = models.CharField(max_length=250, blank=False)
    created_at = DateTimeFieldCustome(null=True, blank=True)
    updated_at = DateTimeFieldCustome(null=True, blank=True)
    deleted_at = DateTimeFieldCustome(null=True, blank=True)

    class Meta:
        db_table = 'lecturas_anulados'


class SociosCobrosManuales(models.Model):
    socio_cobro_manual_id = models.IntegerField(primary_key=True)
    socio_id = models.ForeignKey(Socios, to_field='socio_id', on_delete=models.PROTECT, db_column='socio_id')
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, to_field='id', on_delete=models.PROTECT, db_column='user_id')
    cobro_manual_id = models.ForeignKey(CobrosManuales, to_field='cobro_manual_id', on_delete=models.PROTECT, db_column='cobro_manual_id')
    status_id = models.ForeignKey(Status, to_field='status_id', on_delete=models.PROTECT, db_column='status_id')
    periodo = models.CharField(max_length=20, blank=False)
    monto_bs = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    fecha_cobro = DateTimeFieldCustome(null=True, blank=True)
    punto_id = models.IntegerField(blank=False)
    caja_id = models.IntegerField(blank=False)
    user_id_cobro = models.IntegerField(blank=False)
    observacion = models.CharField(max_length=250, blank=False)
    created_at = DateTimeFieldCustome(null=True, blank=True)
    updated_at = DateTimeFieldCustome(null=True, blank=True)
    deleted_at = DateTimeFieldCustome(null=True, blank=True)

    class Meta:
        db_table = 'socios_cobros_manuales'


class SociosCobrosManualesAnulados(models.Model):
    socio_cobro_manual_anulado_id = models.IntegerField(primary_key=True)
    socio_cobro_manual_id = models.IntegerField(blank=False)
    socio_id = models.ForeignKey(Socios, to_field='socio_id', on_delete=models.PROTECT, db_column='socio_id')
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, to_field='id', on_delete=models.PROTECT, db_column='user_id')
    cobro_manual_id = models.ForeignKey(CobrosManuales, to_field='cobro_manual_id', on_delete=models.PROTECT, db_column='cobro_manual_id')
    status_id = models.ForeignKey(Status, to_field='status_id', on_delete=models.PROTECT, db_column='status_id')
    periodo = models.CharField(max_length=20, blank=False)
    monto_bs = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    fecha_cobro = DateTimeFieldCustome(null=True, blank=True)
    punto_id = models.IntegerField(blank=False)
    caja_id = models.IntegerField(blank=False)
    user_id_cobro = models.IntegerField(blank=False)
    observacion = models.CharField(max_length=250, blank=False)
    created_at = DateTimeFieldCustome(null=True, blank=True)
    updated_at = DateTimeFieldCustome(null=True, blank=True)
    deleted_at = DateTimeFieldCustome(null=True, blank=True)

    class Meta:
        db_table = 'socios_cobros_manuales_anulados'


class SociosCobrosMensuales(models.Model):
    socio_cobro_mensual_id = models.IntegerField(primary_key=True)
    socio_id = models.ForeignKey(Socios, to_field='socio_id', on_delete=models.PROTECT, db_column='socio_id')
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, to_field='id', on_delete=models.PROTECT, db_column='user_id')
    cobro_mensual_id = models.ForeignKey(CobrosMensuales, to_field='cobro_mensual_id', on_delete=models.PROTECT, db_column='cobro_mensual_id')
    status_id = models.ForeignKey(Status, to_field='status_id', on_delete=models.PROTECT, db_column='status_id')
    periodo = models.CharField(max_length=20, blank=False)
    monto_bs = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    fecha_cobro = DateTimeFieldCustome(null=True, blank=True)
    punto_id = models.IntegerField(blank=False)
    caja_id = models.IntegerField(blank=False)
    user_id_cobro = models.IntegerField(blank=False)
    observacion = models.CharField(max_length=250, blank=False)
    created_at = DateTimeFieldCustome(null=True, blank=True)
    updated_at = DateTimeFieldCustome(null=True, blank=True)
    deleted_at = DateTimeFieldCustome(null=True, blank=True)

    class Meta:
        db_table = 'socios_cobros_mensuales'


class SociosCobrosMensualesAnulados(models.Model):
    socio_cobro_mensual_anulado_id = models.IntegerField(primary_key=True)
    socio_cobro_mensual_id = models.IntegerField(blank=False)
    socio_id = models.ForeignKey(Socios, to_field='socio_id', on_delete=models.PROTECT, db_column='socio_id')
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, to_field='id', on_delete=models.PROTECT, db_column='user_id')
    cobro_mensual_id = models.ForeignKey(CobrosMensuales, to_field='cobro_mensual_id', on_delete=models.PROTECT, db_column='cobro_mensual_id')
    status_id = models.ForeignKey(Status, to_field='status_id', on_delete=models.PROTECT, db_column='status_id')
    periodo = models.CharField(max_length=20, blank=False)
    monto_bs = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    fecha_cobro = DateTimeFieldCustome(null=True, blank=True)
    punto_id = models.IntegerField(blank=False)
    caja_id = models.IntegerField(blank=False)
    user_id_cobro = models.IntegerField(blank=False)
    observacion = models.CharField(max_length=250, blank=False)
    created_at = DateTimeFieldCustome(null=True, blank=True)
    updated_at = DateTimeFieldCustome(null=True, blank=True)
    deleted_at = DateTimeFieldCustome(null=True, blank=True)

    class Meta:
        db_table = 'socios_cobros_mensuales_anulados'


class SociosCobros(models.Model):
    socio_cobro_id = models.IntegerField(primary_key=True)
    socio_id = models.ForeignKey(Socios, to_field='socio_id', on_delete=models.PROTECT, db_column='socio_id')
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, to_field='id', on_delete=models.PROTECT, db_column='user_id')
    punto_id = models.IntegerField(blank=False)
    caja_id = models.IntegerField(blank=False)
    user_id_cobro = models.IntegerField(blank=False)
    status_id = models.ForeignKey(Status, to_field='status_id', on_delete=models.PROTECT, db_column='status_id')
    fecha_cobro = DateTimeFieldCustome(null=True, blank=True)
    monto_bs = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    periodo = models.CharField(max_length=20, blank=False)
    observacion = models.CharField(max_length=250, blank=False)
    user_id_anula = models.IntegerField(null=True, blank=True)
    motivo_anula = models.CharField(max_length=250, blank=False)
    created_at = DateTimeFieldCustome(null=True, blank=True)
    updated_at = DateTimeFieldCustome(null=True, blank=True)
    deleted_at = DateTimeFieldCustome(null=True, blank=True)

    class Meta:
        db_table = 'socios_cobros'


class SociosCobrosAnulados(models.Model):
    socio_cobro_anulado_id = models.IntegerField(primary_key=True)
    socio_cobro_id = models.IntegerField(blank=False)
    socio_id = models.ForeignKey(Socios, to_field='socio_id', on_delete=models.PROTECT, db_column='socio_id')
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, to_field='id', on_delete=models.PROTECT, db_column='user_id')
    punto_id = models.IntegerField(blank=False)
    caja_id = models.IntegerField(blank=False)
    user_id_cobro = models.IntegerField(blank=False)
    status_id = models.ForeignKey(Status, to_field='status_id', on_delete=models.PROTECT, db_column='status_id')
    fecha_cobro = DateTimeFieldCustome(null=True, blank=True)
    monto_bs = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    periodo = models.CharField(max_length=20, blank=False)
    observacion = models.CharField(max_length=250, blank=False)
    user_id_anula = models.IntegerField(null=True, blank=True)
    motivo_anula = models.CharField(max_length=250, blank=False)
    created_at = DateTimeFieldCustome(null=True, blank=True)
    updated_at = DateTimeFieldCustome(null=True, blank=True)
    deleted_at = DateTimeFieldCustome(null=True, blank=True)

    class Meta:
        db_table = 'socios_cobros_anulados'


class SociosCobrosDetalles(models.Model):
    socio_cobro_detalle_id = models.IntegerField(primary_key=True)
    socio_cobro_id = models.ForeignKey(SociosCobros, to_field='socio_cobro_id', on_delete=models.PROTECT, db_column='socio_cobro_id')
    lectura_id = models.IntegerField(blank=False)
    socio_cobro_mensual_id = models.IntegerField(blank=False)
    socio_cobro_manual_id = models.IntegerField(blank=False)
    monto_bs = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    detalle = models.CharField(max_length=250, blank=False)
    observacion = models.CharField(max_length=250, blank=False)
    created_at = DateTimeFieldCustome(null=True, blank=True)
    updated_at = DateTimeFieldCustome(null=True, blank=True)
    deleted_at = DateTimeFieldCustome(null=True, blank=True)

    class Meta:
        db_table = 'socios_cobros_detalles'


class SociosCobrosDetallesAnulados(models.Model):
    socio_cobro_detalle_anulado_id = models.IntegerField(primary_key=True)
    socio_cobro_detalle_id = models.IntegerField(blank=False)
    socio_cobro_id = models.ForeignKey(SociosCobros, to_field='socio_cobro_id', on_delete=models.PROTECT, db_column='socio_cobro_id')
    lectura_id = models.IntegerField(blank=False)
    socio_cobro_mensual_id = models.IntegerField(blank=False)
    socio_cobro_manual_id = models.IntegerField(blank=False)
    monto_bs = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    detalle = models.CharField(max_length=250, blank=False)
    observacion = models.CharField(max_length=250, blank=False)
    created_at = DateTimeFieldCustome(null=True, blank=True)
    updated_at = DateTimeFieldCustome(null=True, blank=True)
    deleted_at = DateTimeFieldCustome(null=True, blank=True)

    class Meta:
        db_table = 'socios_cobros_detalles_anulados'
