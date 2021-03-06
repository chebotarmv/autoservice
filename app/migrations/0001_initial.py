# Generated by Django 2.2 on 2019-04-05 11:15

import app.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300, verbose_name='ФИО')),
                ('specialization', models.CharField(max_length=300, verbose_name='Специализация')),
                ('info', models.CharField(max_length=10000, verbose_name='Инфо о мастере')),
            ],
            options={
                'verbose_name': 'Мастер',
                'verbose_name_plural': 'Мастера',
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField(validators=[app.validators.validate_weekday], verbose_name='Дата записи ')),
                ('time', models.TimeField(verbose_name='Время записи ')),
                ('client_name', models.CharField(max_length=300, verbose_name='ФИО ')),
                ('client_car', models.CharField(max_length=10000, verbose_name='Инфо о автомобиле ')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Master', verbose_name='Мастер ')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Записи',
            },
        ),
    ]
