from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from authors.views import AuthorViewSet
from todo.views import ToDoViewSet, ProjectViewSet

router = DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('project', ProjectViewSet)
router.register('todo', ToDoViewSet)


urlpatterns = [
   path('admin/', admin.site.urls),
   path('api-auth/', include('rest_framework.urls')),
   #path('api/', include('authors.urls', namespace="api")),
   path('api/', include(router.urls)),
]
