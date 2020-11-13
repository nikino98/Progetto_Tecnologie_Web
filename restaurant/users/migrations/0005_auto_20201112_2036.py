# Generated by Django 3.1.2 on 2020-11-12 19:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20201112_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cap',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='CAP'),
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Città'),
        ),
        migrations.AlterField(
            model_name='user',
            name='house_number',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Numero civico'),
        ),
        migrations.AlterField(
            model_name='user',
            name='province',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Provincia'),
        ),
        migrations.AlterField(
            model_name='user',
            name='region',
            field=models.CharField(blank=True, max_length=35, null=True, verbose_name='Regione'),
        ),
        migrations.AlterField(
            model_name='user',
            name='tel',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator(message='Numero di telefono errato!', regex='^\\+?1?\\d{10,10}$')], verbose_name='Telefono'),
        ),
        migrations.AlterField(
            model_name='user',
            name='via',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Via'),
        ),
    ]