from django.shortcuts import render
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.viewsets import ModelViewSet

from .filters import ProjectFilter
from .models import ToDo, Project
from .serializers import ToDoSerializer, ProjectSerializer, AddTodoSerializer


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

class TodoAddView(APIView):
    def get(self, request, **kwargs):
        todo = ToDo.objects.all()
        print('111')
        serializer = ToDoSerializer(todo, many=True)
        return Response(serializer.data)


    def post(self, request, **kwargs):
        id = kwargs['id']
        data_request = request.data
        user_id = request.user.id

        data = {'text': data_request.get('text'), 'project': int(id), 'create_user': user_id}
        print(data)
        serializer = AddTodoSerializer(data=data)
        if serializer.is_valid():
            print('yes')
            serializer.save()
            return Response(serializer.data)
        print('no')
        return Response(serializer.errors)

