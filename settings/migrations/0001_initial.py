# Generated by Django 3.0.7 on 2020-06-25 21:31

from django.db import migrations, models
import django.db.models.deletion
import utils.custome_dbtypes


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('monedas', '0002_monedas_init_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('setting_id', models.IntegerField(primary_key=True, serialize=False)),
                ('empresa', models.CharField(max_length=250)),
                ('direccion', models.CharField(max_length=250)),
                ('ciudad', models.CharField(max_length=250)),
                ('telefonos', models.CharField(max_length=250)),
                ('actividad', models.CharField(max_length=250)),
                ('usar_fecha_servidor', models.CharField(max_length=50)),
                ('fecha_sistema', utils.custome_dbtypes.DateFieldCustome(blank=True, null=True)),
                ('cant_per_page', models.IntegerField(default=30)),
                ('cantidad_lista', models.IntegerField(default=10)),
                ('perfiles_admin_listado_cajas', models.CharField(max_length=50)),
                ('costo_m3', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('costo_minimo', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('unidad_minima_m3', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('periodo_ini', models.CharField(default='202001', max_length=50)),
                ('periodo_fin', models.CharField(default='202005', max_length=50)),
                ('multa_pasivo', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('cant_lista_cobranza', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'settings',
            },
        ),
        migrations.CreateModel(
            name='Zonas',
            fields=[
                ('zona_id', models.IntegerField(primary_key=True, serialize=False)),
                ('zona', models.CharField(max_length=150)),
                ('created_at', utils.custome_dbtypes.DateTimeFieldCustome(blank=True, null=True)),
                ('updated_at', utils.custome_dbtypes.DateTimeFieldCustome(blank=True, null=True)),
                ('deleted_at', utils.custome_dbtypes.DateTimeFieldCustome(blank=True, null=True)),
                ('status_id', models.ForeignKey(db_column='status_id', on_delete=django.db.models.deletion.PROTECT, to='status.Status')),
            ],
            options={
                'db_table': 'zonas',
            },
        ),
        migrations.CreateModel(
            name='Puntos',
            fields=[
                ('punto_id', models.IntegerField(primary_key=True, serialize=False)),
                ('caja_id', models.IntegerField(default=0)),
                ('punto', models.CharField(max_length=50)),
                ('codigo', models.CharField(max_length=50)),
                ('impresora_reportes', models.CharField(max_length=250)),
                ('created_at', utils.custome_dbtypes.DateTimeFieldCustome(blank=True, null=True)),
                ('updated_at', utils.custome_dbtypes.DateTimeFieldCustome(blank=True, null=True)),
                ('deleted_at', utils.custome_dbtypes.DateTimeFieldCustome(blank=True, null=True)),
                ('status_id', models.ForeignKey(db_column='status_id', on_delete=django.db.models.deletion.PROTECT, to='status.Status')),
            ],
            options={
                'db_table': 'puntos',
            },
        ),
        migrations.CreateModel(
            name='CobrosMensuales',
            fields=[
                ('cobro_mensual_id', models.IntegerField(primary_key=True, serialize=False)),
                ('cobro_mensual', models.CharField(max_length=150)),
                ('monto_bs', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('created_at', utils.custome_dbtypes.DateTimeFieldCustome(blank=True, null=True)),
                ('updated_at', utils.custome_dbtypes.DateTimeFieldCustome(blank=True, null=True)),
                ('deleted_at', utils.custome_dbtypes.DateTimeFieldCustome(blank=True, null=True)),
                ('status_id', models.ForeignKey(db_column='status_id', on_delete=django.db.models.deletion.PROTECT, to='status.Status')),
            ],
            options={
                'db_table': 'cobros_mensuales',
            },
        ),
        migrations.CreateModel(
            name='CobrosManuales',
            fields=[
                ('cobro_manual_id', models.IntegerField(primary_key=True, serialize=False)),
                ('cobro_manual', models.CharField(max_length=150)),
                ('monto_bs', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('created_at', utils.custome_dbtypes.DateTimeFieldCustome(blank=True, null=True)),
                ('updated_at', utils.custome_dbtypes.DateTimeFieldCustome(blank=True, null=True)),
                ('deleted_at', utils.custome_dbtypes.DateTimeFieldCustome(blank=True, null=True)),
                ('status_id', models.ForeignKey(db_column='status_id', on_delete=django.db.models.deletion.PROTECT, to='status.Status')),
            ],
            options={
                'db_table': 'cobros_manuales',
            },
        ),
        migrations.CreateModel(
            name='Cajas',
            fields=[
                ('caja_id', models.IntegerField(primary_key=True, serialize=False)),
                ('caja', models.CharField(max_length=50)),
                ('codigo', models.CharField(max_length=50)),
                ('created_at', utils.custome_dbtypes.DateTimeFieldCustome(blank=True, null=True)),
                ('updated_at', utils.custome_dbtypes.DateTimeFieldCustome(blank=True, null=True)),
                ('deleted_at', utils.custome_dbtypes.DateTimeFieldCustome(blank=True, null=True)),
                ('punto_id', models.ForeignKey(db_column='punto_id', on_delete=django.db.models.deletion.PROTECT, to='settings.Puntos')),
                ('status_id', models.ForeignKey(db_column='status_id', on_delete=django.db.models.deletion.PROTECT, to='status.Status')),
            ],
            options={
                'db_table': 'cajas',
            },
        ),
    ]
