from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import MyUserModel


class CustomUserCreateForm(UserCreationForm):
    class Meta:
        model = MyUserModel
        fields = ('username',)

