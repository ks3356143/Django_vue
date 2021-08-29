from django.urls import path
from . import views

urlpatterns = [
    path('', views.ComputerList.as_view(), name='computer_list'),
    path(r'<int:pk>/', views.ComputerDetail.as_view(), name='computer_detail'),
    path(r'amount/', views.ComputerAmount.as_view(), name='computer_amount'),
    path(r'in_url/<str:type_name>/', views.ComputerFilterInUrl.as_view(), name='computer_filter_in_url'),
    path(r'in_request/', views.ComputerFilterInRequest.as_view(), name='computer_filter_in_request'),
]