import graphene
from graphene_django import DjangoObjectType
from authors.models import MyUserModel
from todo.models import Project, ToDo





class ProgectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'

class AuthorsType(DjangoObjectType):
    class Meta:
        model = MyUserModel
        fields = '__all__'

class TodoType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'

class Query(graphene.ObjectType):
    all_authors = graphene.List(AuthorsType)
    all_projects = graphene.List(ProgectType)
    all_todo = graphene.List(TodoType)

    project_by_authors = graphene.List(ProgectType, id_authors=graphene.List(of_type=graphene.Int, required=True))

    author_by_id = graphene.Field(AuthorsType, id=graphene.Int(required=True))

    def resolve_project_by_authors(self, info, id_authors):
        obj = Project.objects.filter(users__in=id_authors)
        return obj

    def resolve_author_by_id(self, info, id):
        try:
            return MyUserModel.objects.get(id=id)
        except MyUserModel.DoesNotExist:
            return None

    def resolve_all_authors(root, info):
        return MyUserModel.objects.all()

    def resolve_all_projects(root, info):
        return Project.objects.all()

    def resolve_all_todo(root, info):
        return ToDo.objects.all()




class ProjectMutation(graphene.Mutation):
    print('mutate1')
    class Arguments:
        name = graphene.String()
        id = graphene.ID()

    project = graphene.Field(ProgectType)

    @classmethod
    def mutate(cls, root, info, id, name=None):
        projects = Project.objects.get(pk=id)
        if name is not None:
            projects.name = name
            projects.save()
        return ProjectMutation(project=projects)

class Mutation(graphene.ObjectType):
    update_project = ProjectMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)