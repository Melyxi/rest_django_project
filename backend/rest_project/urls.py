from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from drf_yasg import openapi
from graphene_django.views import GraphQLView

from authors.views import AuthorViewSet
from todo.views import ToDoViewSet, ProjectViewSet, TodoAddView

from authors.views import RegistrUserView

router = DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('project', ProjectViewSet)
router.register('todo', ToDoViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Library",
      default_version='0.1',
      description="Documentation to out project",
      contact=openapi.Contact(email="admin@admin.local"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api-auth/', include('rest_framework.urls')),
   path('api/projects/<int:id>/create/', TodoAddView.as_view()),
   #path('api/', include('authors.urls', namespace="api")),
   path('api/registration', RegistrUserView.as_view()),
   # версионность api namespace
   path('api/v1/authors/', include('authors.urls', namespace='v1')),
   path('api/v2/authors/', include('authors.urls', namespace='v2')),

   path('api/', include(router.urls)),
   path('api-token-auth/', obtain_jwt_token),
   path('api-token-refresh/', refresh_jwt_token),
   path('api-token-verify/', verify_jwt_token),

   path('', TemplateView.as_view(template_name='index.html')),


   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

   path("graphql/", GraphQLView.as_view(graphiql=True)),
]
