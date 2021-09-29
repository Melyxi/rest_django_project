from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet
from .models import MyUserModel
from .serializers import AuthorSerializer
from rest_framework import mixins, viewsets


class AuthorViewSet(mixins.ListModelMixin,
                          mixins.RetrieveModelMixin, viewsets.GenericViewSet, mixins.UpdateModelMixin):
   queryset = MyUserModel.objects.all()
   serializer_class = AuthorSerializer



