# Generated by Django 3.1.2 on 2020-11-04 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offerdrink',
            name='code',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='offerfood',
            name='code',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]