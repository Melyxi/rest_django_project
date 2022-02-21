import click
from django.core.management.base import BaseCommand
from django.contrib.auth.password_validation import validate_password

from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import getpass
from authors.models import MyUserModel
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from authors.forms import CustomUserCreateForm
from authors.serializers import UserSerializer
from django.contrib.auth import get_user_model
User = get_user_model()


def validateEmail(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False


class Command(BaseCommand):
    help = 'Create new user'

    def handle(self, *args, **kwargs):
        while True:
            username = input('Введите username: ')
            if username:
                break
        firstname = input('Введите имя: ')
        lastname = input('Введите фамилию: ')

        while True:
            email = input('Введите email: ')
            if validateEmail(email):
                break
        while True:
            password = getpass.getpass('Введите пароль: ')
            try:
                validate_password(password)
                break
            except ValidationError as e:
                for i in e:
                    print(i)

        while True:
            password1 = getpass.getpass('Повторите пароль: ')
            if password == password1:
                break
            else:
                print('Пароли не совпадают')
        
        try:
            login_form = UserSerializer()
            login_form.create({'username': username, 'email': email,
                                        'firstname': firstname, 'lastname': lastname,
                                        'password': password,
                                        'is_staff': False,
                          })
            print('Пользоваетель создан')
        except BaseException as e:
            print('Пользователь не создан')
            print(e)
