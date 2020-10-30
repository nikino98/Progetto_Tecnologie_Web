# Generated by Django 3.1.2 on 2020-10-30 14:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20201030_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='discount',
            field=models.PositiveIntegerField(default=10, help_text="Inserire l'ammontare dello sconto percentuale", validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
