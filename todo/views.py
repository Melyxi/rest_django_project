from django.shortcuts import render
from rest_framework.pagination import LimitOffsetPagination

from rest_framework.viewsets import ModelViewSet

from .filters import ProjectFilter
from .models import ToDo, Project
from .serializers import ToDoSerializer, ProjectSerializer


class ToDoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20

class ToDoViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    pagination_class = ToDoLimitOffsetPagination

class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = ProjectLimitOffsetPagination
    filterset_class = ProjectFilter