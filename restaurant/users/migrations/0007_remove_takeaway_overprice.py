# Generated by Django 3.1.2 on 2020-10-30 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_takeaway'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='takeaway',
            name='overprice',
        ),
    ]