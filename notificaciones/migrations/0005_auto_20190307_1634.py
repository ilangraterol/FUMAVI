# Generated by Django 2.0.6 on 2019-03-07 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notificaciones', '0004_auto_20190307_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificaciones',
            name='asunto',
            field=models.TextField(blank=True, max_length=250),
        ),
    ]
