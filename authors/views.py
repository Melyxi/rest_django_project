
from rest_framework.viewsets import ModelViewSet
from .models import MyUserModel
from .serializers import AuthorSerializer


class AuthorViewSet(ModelViewSet):
   queryset = MyUserModel.objects.all()
   serializer_class = AuthorSerializer