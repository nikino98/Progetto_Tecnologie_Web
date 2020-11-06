# Generated by Django 3.1.2 on 2020-11-03 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='users.review'),
        ),
    ]