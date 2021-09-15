from rest_framework.serializers import HyperlinkedModelSerializer
from .models import MyUserModel

class AuthorSerializer(HyperlinkedModelSerializer):
   class Meta:
       model = MyUserModel
       fields = ('username', 'firstname', 'lastname', 'email')