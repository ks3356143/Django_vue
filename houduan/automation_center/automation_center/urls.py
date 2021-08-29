from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()

urlpatterns = [
    path('api/computers/', include('computer.urls')),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/projects/', include('projects.urls')),
    path('docs/',include_docs_urls(title="接口测试平台API文档",description="这个是接口平台的文档")),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
