from django.urls import path, include
from rest_framework.routers import DefaultRouter

from authors.views import AuthorViewSet

# app_name = 'authors'

router = DefaultRouter()
router.register('authors', AuthorViewSet)
#
# urlpatterns = [
#    path('',  include(router.urls)),
# ]