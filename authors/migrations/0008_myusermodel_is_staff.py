# Generated by Django 3.2.7 on 2021-09-15 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0007_auto_20210915_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='myusermodel',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
