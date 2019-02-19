# Generated by Django 2.0.6 on 2019-02-19 00:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('afiliados', '0011_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='PagoEmpresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pago', models.DateField(blank=True, null=True)),
                ('monto', models.FloatField(blank=True, null=True)),
                ('recibo', models.IntegerField(blank=True, null=True)),
                ('observacion', models.CharField(blank=True, max_length=50, verbose_name='Concepto de pago')),
                ('foto', models.ImageField(default='Foto recibo de Pago', upload_to='Consignaciones/')),
                ('empresaafiliada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afiliados.EmpresaAfiliada', verbose_name='Quién realizó el Pago?')),
            ],
        ),
    ]
