from .models import Project
from .serializer import ProjectSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .utils import IsStaffUserReadOnly
from .permission import IsSpecifiedProjectOrReadOnly
from rest_framework.response import Response

# 如果你的类只需要get和post方法你继承generics.ListCreateAPIView就可以了
class ProjectList(generics.ListCreateAPIView):
    '''
    OK
    '''
    permission_classes = [IsStaffUserReadOnly]
    queryset = Project.objects.all().order_by('id')
    serializer_class = ProjectSerializer


# class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
class ProjectDetail(generics.RetrieveUpdateAPIView):
    '''
    OK
    '''
    permission_classes = [IsSpecifiedProjectOrReadOnly]  # here
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

'''viewSet的写法，只有超级用户才可以更新用户数据'''
from rest_framework import viewsets
from .utils import IsSuperUserOrReadOnly
from django.contrib.auth.models import User # 导入user模块
from .serializer import UserSerializer
from rest_framework.views import APIView


class UserViewSet(viewsets.ModelViewSet):
    """
        get:
            返回所有用户数据
        post:
            增加用户数据
        put:
            更新一个用户数据
        patch:
            更新用户一个或者多个信息
        delete:
            删除现有用户数据
    """
    #这里只允许超级用户，若设定IsAuthticatedOrReadOnly则是登录后都可以修改
    permission_classes = [IsSuperUserOrReadOnly]
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    #目前还是User的数据结构还未找到

