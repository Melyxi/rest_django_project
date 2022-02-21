from django.contrib import admin

from .models import *

admin.site.register(ToDo)
admin.site.register(Project)