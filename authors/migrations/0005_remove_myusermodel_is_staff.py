# Generated by Django 3.2.7 on 2021-09-15 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0004_myusermodel_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myusermodel',
            name='is_staff',
        ),
    ]
