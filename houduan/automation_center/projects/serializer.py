from .models import Project
from rest_framework import serializers
from django.contrib.auth.models import User

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"



'''    
class BookSerializer(serializers.ModelSerializer):
  	class Meta:
      	model = 指定模型类
        fields = (指定验证字段)
        extra_kwargs = {"field_name":{"write_only":True}}
'''
