from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from news.models import News
from rest_framework.permissions import IsAdminUser
from .permissions import IsSuperUser
from .serializers  import NewsSerializer, UserSerializer
from django.contrib.auth.models import User



class NewsList(ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsDetail(RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = 'slug'


     

class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser, )  


class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser, )   