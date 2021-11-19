from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APITestCase, APISimpleTestCase, APIRequestFactory, force_authenticate
from .models import Project, ToDo
from authors.models import MyUserModel
from django.contrib.auth.models import User, AbstractUser
from mixer.backend.django import mixer


# class CustomUser(AbstractUser):
#     pass
#
# class MixerTestCase(APITestCase):
#
#     def test_author_list(self):
#         # Author.objects.create(first_name='Александр', last_name='Пушкин', birthday_year=1799)
#         mixer.blend(Project, author__birthday_year=1799)
#         # author = Author.objects.get(id=bio.author.id)
#
#         print(bio)
from .views import ProjectViewSet


class AuthorTestCase(APITestCase):

    # первоначальные настройки
    def setUp(self):
        self.admin = MyUserModel.objects.create_superuser(username='igor', email='dasdad@dsfs.ru', password='dsntuhf')
        obj = MyUserModel.objects.all()
        print(obj)
        res = self.client.login(username='igor', password='dsntuhf')

    # список авторов
    def test_author_list(self):
        res = self.client.get('/api/authors/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        print(res.data)
        self.client.logout()
        res = self.client.get('/api/authors/')
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_todo_list(self):
        res = self.client.get('/api/todo/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        print(res.data)
        self.client.logout()
        res = self.client.get('/api/todo/')
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_project_list(self):
        res = self.client.get('/api/project/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        print(res.data)
        self.client.logout()
        res = self.client.get('/api/project/')
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

class TestAuthorViewSet(TestCase):
    def setUp(self):
        self.admin = MyUserModel.objects.create_superuser(username='igor', email='dasdad@dsfs.ru', password='dsntuhf')
        obj = MyUserModel.objects.all()
        print(obj)
        #res = self.client.login(username='igor', password='dsntuhf')

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.post('/api/authors/',
            {
                "username": "ewrewr",
                "firstname": "",
                "lastname": "rewrwe",
                "email": "rewrwe@dsfsdf.ru"
            }, format='json'
            )
        force_authenticate(request, self.admin)
        view = ProjectViewSet.as_view(actions={'post': 'create'})
        print(request.body)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


#     def test_author_post(self):
#         res = self.client.post('/api/authors/', {
#             'first_name': 'Александр',
#             'last_name': 'Пушкин',
#             'birthday_year': 1799})
#         self.assertEqual(res.status_code, status.HTTP_201_CREATED)
#         author = Author.objects.get(id=res.data['id'])
#         self.assertEqual(author.last_name, 'Пушкин')
#
#     def test_factory(self):
#         factory = APIRequestFactory()
#         view = AuthorViewSet.as_view({'get': 'list'})
#         request = factory.get('/api/authors/')
#         res = view(request)
#         self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
#
#         request = factory.get('/api/authors/')
#         force_authenticate(request, self.admin)
#         res = view(request)
#         self.assertEqual(res.status_code, status.HTTP_200_OK)
#
#
# class FuncTest(APISimpleTestCase):
#
#     def test_func(self):
#         self.assertTrue(True)
