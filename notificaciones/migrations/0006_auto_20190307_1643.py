# Generated by Django 2.0.6 on 2019-03-07 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notificaciones', '0005_auto_20190307_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificaciones',
            name='asunto2',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='notificaciones',
            name='despedida',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='notificaciones',
            name='asunto',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='notificaciones',
            name='saludo',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
