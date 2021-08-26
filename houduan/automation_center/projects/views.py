from .models import Project
from .serializer import ProjectSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# 如果你的类只需要get和post方法你继承generics.ListCreateAPIView就可以了
class ProjectList(generics.ListCreateAPIView):
    '''
    OK
    '''
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


# class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
class ProjectDetail(generics.RetrieveUpdateAPIView):
    '''
    OK
    '''
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer