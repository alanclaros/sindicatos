from django.db import models
from django.conf import settings


class Perfiles(models.Model):
    perfil_id = models.IntegerField(primary_key=True)
    perfil = models.CharField(max_length=50)

    class Meta:
        db_table = "perfiles"


class UsersPerfiles(models.Model):
    user_perfil_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, to_field='id', on_delete=models.PROTECT, db_column='user_id')
    perfil_id = models.ForeignKey(Perfiles, to_field='perfil_id', on_delete=models.PROTECT, db_column='perfil_id')

    class Meta:
        db_table = "users_perfiles"


class Modulos(models.Model):
    modulo_id = models.IntegerField(primary_key=True)
    modulo = models.CharField(max_length=150, blank=False)
    modulo_txt = models.CharField(max_length=150, blank=False)
    enabled = models.BooleanField(blank=False, default=True)
    position = models.IntegerField(blank=False, default=0)
    grupo = models.IntegerField(blank=False, default=0)

    class Meta:
        db_table = "modulos"


class UsersModulos(models.Model):
    user_modulo_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, to_field='id', on_delete=models.PROTECT, db_column='user_id')
    modulo_id = models.ForeignKey('Modulos', to_field='modulo_id', on_delete=models.PROTECT, db_column='modulo_id')
    enabled = models.BooleanField(blank=False, default=False)
    adicionar = models.BooleanField(blank=False, default=False)
    modificar = models.BooleanField(blank=False, default=False)
    eliminar = models.BooleanField(blank=False, default=False)
    anular = models.BooleanField(blank=False, default=False)
    imprimir = models.BooleanField(blank=False, default=False)
    permiso = models.BooleanField(blank=False, default=False)

    class Meta:
        db_table = "users_modulos"
