# Generated by Django 3.1.2 on 2020-10-19 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20201018_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='image',
            field=models.ImageField(default='dishes/no-imaage-1771002-1505134.png', upload_to='dishes/'),
        ),
    ]
