from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import Computer
from .serializer import ComputerSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework import filters

class ComputerAmount(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request):
        count = {"count":Computer.objects.count()}
        return Response(count,status=status.HTTP_200_OK)

class ComputerList(generics.ListCreateAPIView):

    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Computer.objects.all().order_by('id')
    serializer_class = ComputerSerializer

class ComputerDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer

class ComputerFilterInUrl(generics.ListAPIView):
    serializer_class = ComputerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_queryset(self):

        """
        This view return all computers based on url parameter
        """
        type_name = self.kwargs['type_name']
        return Computer.objects.filter(computer_type=type_name)

class ComputerFilterInRequest(generics.ListAPIView):
    serializer_class = ComputerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """
        This view return all computers based on request parameter
        """
        return Computer.objects.filter(computer_type=self.request.data["type_name"])

class ComputerList(generics.ListAPIView):
    """
        get:
            Return all projects or based on search condition.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Computer.objects.all().order_by("id")
    serializer_class = ComputerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "=computer_type"]