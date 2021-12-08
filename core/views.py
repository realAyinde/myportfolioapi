# from django.contrib.auth.models import User, Group
from core.models import User, Article
from rest_framework import viewsets
from rest_framework import permissions
from core.serializers import UserSerializer, ArticleSerializer #GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all() #.order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Article.objects.all() #.order_by('-date_joined')
    serializer_class = ArticleSerializer
    # permission_classes = [permissions.IsAuthenticated]

# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]