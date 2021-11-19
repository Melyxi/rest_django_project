from rest_framework.serializers import HyperlinkedModelSerializer
from .models import MyUserModel
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = MyUserModel
        fields = ('id', 'username', 'firstname', 'lastname', 'email', 'password')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class AuthorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = MyUserModel
        fields = ('id', 'username', 'firstname', 'lastname', 'email')


class AuthorSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = MyUserModel
        fields = ('id', 'username', 'firstname', 'lastname', 'email', 'is_superuser', 'is_staff')


class UserRegistrSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    class Meta:
        model = MyUserModel
        fields = ['email', 'username', 'password', 'password2', ]

    def save(self, *args, **kwargs):
        user = MyUserModel(
            email=self.validated_data['email'],
            username=self.validated_data['username'],  # Назначаем Логин
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({password: "Пароль не совпадает"})

        user.set_password(password)
        user.save()
        return user
