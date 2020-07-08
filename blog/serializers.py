from rest_framework import serializers
from blog.models import Client
from blog.models import  Project


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id','Project']


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ['id','client_name','created_by','created_at','Project','Project']





