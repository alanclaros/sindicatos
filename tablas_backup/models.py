from django.db import models


class TablasBackup(models.Model):
    tabla = models.CharField(max_length=150, primary_key=True)
    posicion = models.IntegerField(blank=False)

    class Meta:
        db_table = 'tablas_backup'
