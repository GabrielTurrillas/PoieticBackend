# Generated by Django 3.1 on 2021-03-07 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0009_remove_paciente_ocupacionprofecion'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='valorSesion',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
