from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Создает и сохраняет пользователя с введенным им email и паролем.
        """
        if not email:
            raise ValueError('email должен быть указан')
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        #extra_fields.setdefault('is_superuser', True)
        user = self._create_user(email, password, **extra_fields)
        print(extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user



class MyUserModel(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=50, verbose_name="username")
    email = models.EmailField(unique=True, max_length=50, verbose_name="email")
    firstname = models.CharField(max_length=50, verbose_name="Имя", blank=True)
    lastname = models.CharField(max_length=50, verbose_name="Фамилия", blank=True)
    is_staff = models.BooleanField(default=False)
    # is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['firstname', 'lastname', 'email']

    objects = UserManager()
        
    def __str__(self):
        return self.username

    def get_full_name(self):
        return f"{self.firstname} {self.lastname}"

    def get_short_name(self):
        return self.firstname


