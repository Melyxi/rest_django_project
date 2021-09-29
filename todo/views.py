from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .models import ToDo, Project
from .serializers import ToDoSerializer, ProjectSerializer


class ToDoViewSet(ModelViewSet):
   queryset = ToDo.objects.all()
   serializer_class = ToDoSerializer

class ProjectViewSet(ModelViewSet):
   queryset = Project.objects.all()
   serializer_class = ProjectSerializer