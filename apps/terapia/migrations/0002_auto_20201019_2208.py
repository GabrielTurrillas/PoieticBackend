# Generated by Django 3.1 on 2020-10-20 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terapia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sesion',
            name='fechaPago',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sesion',
            name='modalidad',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='sesion',
            name='notasSesion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sesion',
            name='pago',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='sesion',
            name='fechaSesion',
            field=models.DateField(auto_now_add=True),
        ),
    ]
