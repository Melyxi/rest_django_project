# Generated by Django 3.2.7 on 2021-09-15 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='email')),
                ('firstname', models.CharField(max_length=50, verbose_name='Имя')),
                ('lasttname', models.CharField(max_length=50, verbose_name='Фамилия')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
