# Generated by Django 2.0.6 on 2019-10-02 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('convenios', '0010_auto_20191002_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='procedimiento',
            name='contrato',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='convenios.Contrato', verbose_name='Contrato'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='asesor',
            name='telefonos1',
            field=models.CharField(blank=True, max_length=50, verbose_name='Telefono'),
        ),
        migrations.AlterField(
            model_name='procedimiento',
            name='precio1',
            field=models.FloatField(blank=True, null=True, verbose_name='Precio Fumavi'),
        ),
        migrations.AlterField(
            model_name='procedimiento',
            name='precio2',
            field=models.FloatField(blank=True, null=True, verbose_name='Precio Particular'),
        ),
        migrations.AlterField(
            model_name='procedimiento',
            name='precio3',
            field=models.FloatField(blank=True, null=True, verbose_name='Monto a Consignar'),
        ),
    ]
