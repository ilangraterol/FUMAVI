# Generated by Django 2.0.6 on 2019-03-04 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notificaciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificaciones',
            name='mensaje_cobro',
            field=models.TextField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='notificaciones',
            name='mensaje_saludo',
            field=models.TextField(blank=True, max_length=250),
        ),
    ]
