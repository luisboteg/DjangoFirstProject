from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.parsers import JSONParser
from testbridgeforbillions.projects.serializers import ProjectSerializer
from testbridgeforbillions.projects.models import Project
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics



class GroupProjectSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer