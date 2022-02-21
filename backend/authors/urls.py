from django.urls import path, include
from rest_framework.routers import DefaultRouter

from authors.views import AuthorViewSet

app_name = 'authors'


urlpatterns = [
    path('',  AuthorViewSet.as_view({'get': 'list'})),
]