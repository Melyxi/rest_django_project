from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import MyUserModel
from .serializers import AuthorSerializer, AuthorSerializerV2, UserRegistrSerializer
from rest_framework import mixins, viewsets, status


class AuthorViewSet(mixins.ListModelMixin,
                          mixins.RetrieveModelMixin, viewsets.GenericViewSet, mixins.UpdateModelMixin, mixins.CreateModelMixin):
   queryset = MyUserModel.objects.all()


   def get_serializer_class(self):
       if self.request.version == 'v2':
           return AuthorSerializerV2
       return AuthorSerializer


class RegistrUserView(CreateAPIView):
    # Добавляем в queryset
    queryset = MyUserModel.objects.all()
    # Добавляем serializer UserRegistrSerializer
    serializer_class = UserRegistrSerializer
    # Добавляем права доступа
    permission_classes = [AllowAny]

    # Создаём метод для создания нового пользователя
    def post(self, request, *args, **kwargs):
        # Добавляем UserRegistrSerializer
        serializer = UserRegistrSerializer(data=request.data)
        # Создаём список data
        data = {}
        # Проверка данных на валидность
        if serializer.is_valid():
            # Сохраняем нового пользователя
            serializer.save()
            # Добавляем в список значение ответа True
            data['response'] = True
            # Возвращаем что всё в порядке
            return Response(data, status=status.HTTP_200_OK)
        else:  # Иначе
            # Присваиваем data ошибку
            data = serializer.errors
            # Возвращаем ошибку
            return Response(data)