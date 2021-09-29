

from django.db import models

# Create your models here.
from django.utils import timezone
from django.utils.datetime_safe import datetime


class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название проекта', unique=True)
    data_at = models.DateTimeField(default=timezone.now, verbose_name='Время создания')
    users = models.ManyToManyField('authors.MyUserModel')


class ToDo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date_at = models.DateTimeField(default=timezone.now, verbose_name="Время создания")
    date_update = models.DateTimeField(verbose_name="Время обновления", auto_now=True)
    text = models.TextField(verbose_name="Текст заметки")
    create_user = models.ForeignKey('authors.MyUserModel', on_delete=models.CASCADE)

