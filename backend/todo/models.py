from django.db import models
from django.utils import timezone
from django.utils.datetime_safe import datetime


class Project(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Название проекта', unique=True)
    data_at = models.DateTimeField(default=timezone.now, verbose_name='Время создания')
    users = models.ManyToManyField('authors.MyUserModel')

    def __str__(self):
        return self.name


class ToDo(models.Model):
    id = models.BigAutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date_at = models.DateTimeField(default=timezone.now, verbose_name="Время создания")
    date_update = models.DateTimeField(verbose_name="Время обновления", auto_now=True)
    text = models.TextField(verbose_name="Текст заметки")
    create_user = models.ForeignKey('authors.MyUserModel', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def delete(self, using=None, keep_parents=False):
        self.is_active = False
        self.save()

    def __str__(self):
        return self.text
