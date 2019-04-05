# coding: utf-8
from django.db import models
from . validators import validate_weekday



class Master (models.Model):
    name = models.CharField(verbose_name='ФИО', max_length = 300) 
    specialization = models.CharField(verbose_name='Специализация', max_length=300)
    info = models.CharField(verbose_name='Инфо о мастере', max_length=10000)

    def __str__(self):
        return '%s ' % self.name

    class Meta:
        verbose_name_plural = "Мастера"
        verbose_name = "Мастер"


class Record (models.Model):
    date = models.DateField(verbose_name='Дата записи ', validators = [validate_weekday])
    time = models.TimeField(verbose_name='Время записи ')
    client_name = models.CharField(verbose_name='ФИО ', max_length=300)
    client_car = models.CharField(verbose_name='Инфо о автомобиле ', max_length=10000)
    master = models.ForeignKey( Master, verbose_name='Мастер ', on_delete=models.PROTECT)
 

    def __str__(self):
        return 'Запись № %s' % self.client_name

    class Meta:
        verbose_name_plural = "Записи"
        verbose_name = "Запись"



