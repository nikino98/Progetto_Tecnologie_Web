# Generated by Django 3.1.2 on 2020-11-09 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20201109_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drink',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='food',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
