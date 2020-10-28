# Generated by Django 3.1.2 on 2020-10-28 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=60, unique=True)),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('region', models.CharField(max_length=35)),
                ('province', models.CharField(max_length=30)),
                ('cap', models.CharField(max_length=5)),
                ('city', models.CharField(max_length=50)),
                ('via', models.CharField(max_length=50)),
                ('house_number', models.CharField(max_length=10)),
                ('piano', models.CharField(blank=True, max_length=30)),
                ('note', models.TextField(blank=True)),
                ('tel', models.CharField(max_length=20)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_restaurateur', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Restaurant user',
                'verbose_name_plural': 'Restaurant users',
            },
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_people', models.DecimalField(decimal_places=0, max_digits=2)),
                ('reservation_name', models.CharField(default=None, max_length=50)),
                ('reservation_last_name', models.CharField(default=None, max_length=50)),
                ('date', models.DateTimeField(default=None)),
            ],
        ),
    ]
