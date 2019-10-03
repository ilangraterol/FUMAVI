# Generated by Django 2.0.6 on 2019-10-02 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('convenios', '0006_asesor_cargo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Espe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True, verbose_name='Nombre de la Especialidad')),
            ],
        ),
        migrations.AlterField(
            model_name='especialidad',
            name='nombre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='convenios.Espe', verbose_name='Contrato'),
        ),
    ]
