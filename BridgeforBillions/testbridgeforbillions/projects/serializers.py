from django.contrib.auth.models import User, Group
from rest_framework import serializers
from testbridgeforbillions.projects.models import Project



class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['url','name']
        
