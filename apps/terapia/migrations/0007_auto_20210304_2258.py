# Generated by Django 3.1 on 2021-03-04 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terapia', '0006_auto_20201118_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='terapia',
            name='captacion',
        ),
        migrations.RemoveField(
            model_name='terapia',
            name='motivoConsulta',
        ),
    ]
