# Generated by Django 3.2.7 on 2021-09-29 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_todo_date_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
