from django.db import models
from status.models import Status
from settings.models import Zonas
from utils.custome_dbtypes import DateTimeFieldCustome


class CiExtensiones(models.Model):
    ci_extension_id = models.IntegerField(primary_key=True)
    ci_extension = models.CharField(max_length=50, blank=False)
    orden = models.IntegerField(blank=False)

    class Meta:
        db_table = 'ci_extensiones'


class Socios(models.Model):
    socio_id = models.IntegerField(primary_key=True)
    ci_extension_id = models.ForeignKey(CiExtensiones, to_field='ci_extension_id', on_delete=models.PROTECT, db_column='ci_extension_id')
    zona_id = models.ForeignKey(Zonas, to_field='zona_id', on_delete=models.PROTECT, db_column='zona_id')
    ci_nit = models.CharField(max_length=50, blank=False)
    nombres = models.CharField(max_length=150, blank=False)
    apellidos = models.CharField(max_length=150, blank=False)
    direccion = models.CharField(max_length=250, blank=False)
    telefonos = models.CharField(max_length=250, blank=False)
    numero_cuenta = models.IntegerField(blank=False)
    status_id = models.ForeignKey(Status, to_field='status_id', on_delete=models.PROTECT, db_column='status_id')
    created_at = DateTimeFieldCustome(null=True, blank=True)
    updated_at = DateTimeFieldCustome(null=True, blank=True)
    deleted_at = DateTimeFieldCustome(null=True, blank=True)

    class Meta:
        db_table = 'socios'


class SociosCambiosEstados(models.Model):
    socio_cambio_estado_id = models.IntegerField(primary_key=True)
    socio_id = models.ForeignKey(Socios, to_field='socio_id', on_delete=models.PROTECT, db_column='socio_id')
    status_id_1 = models.IntegerField(blank=False)
    status_id_2 = models.IntegerField(blank=False)
    motivo_cambio = models.CharField(max_length=250, blank=False)
    fecha_operacion = DateTimeFieldCustome(null=True, blank=True)
    monto_bs = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    punto_id = models.IntegerField(blank=False)
    caja_id = models.IntegerField(blank=False)
    user_id_cobra = models.IntegerField(blank=False)
    status_id = models.ForeignKey(Status, to_field='status_id', on_delete=models.PROTECT, db_column='status_id')
    created_at = DateTimeFieldCustome(null=True, blank=True)
    updated_at = DateTimeFieldCustome(null=True, blank=True)
    deleted_at = DateTimeFieldCustome(null=True, blank=True)

    class Meta:
        db_table = 'socios_cambios_estados'
