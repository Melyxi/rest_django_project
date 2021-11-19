from rest_framework.serializers import HyperlinkedModelSerializer

from authors.serializers import AuthorSerializer
from .models import ToDo, Project
from rest_framework import serializers


class ToDoSerializer(serializers.ModelSerializer):
    create_user = AuthorSerializer()
    class Meta:
        model = ToDo
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'



class AddTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('text', 'project', 'create_user')