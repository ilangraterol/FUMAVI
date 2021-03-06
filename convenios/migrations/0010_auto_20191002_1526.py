# Generated by Django 2.0.6 on 2019-10-02 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('convenios', '0009_asesor_correo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Procedimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True, verbose_name='Nombre del procedimiento')),
                ('precio1', models.FloatField(blank=True, null=True, verbose_name='precio1')),
                ('precio2', models.FloatField(blank=True, null=True, verbose_name='precio2')),
                ('precio3', models.FloatField(blank=True, null=True, verbose_name='precio3')),
            ],
        ),
        migrations.AlterField(
            model_name='contrato',
            name='centromedico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='convenios.CentroMedico', verbose_name='Centro Medico o Doctor'),
        ),
    ]
