from .models import Project
from projects.serializer import ProjectSerializer
from rest_framework import generics


class ProjectList(generics.ListCreateAPIView):
    '''
    OK
    '''
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


# class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
class ProjectDetail(generics.RetrieveUpdateAPIView):
    '''
    OK
    '''
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer