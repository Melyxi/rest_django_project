# Generated by Django 3.2.7 on 2021-09-15 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0005_remove_myusermodel_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='myusermodel',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
