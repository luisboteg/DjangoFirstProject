from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions
from testbridgeforbillions.mentors.serializers import MentorSerializer
from testbridgeforbillions.mentors.models import Mentor
from rest_framework import generics


class GroupMentorSet(viewsets.ModelViewSet):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
    permission_classes = [permissions.IsAuthenticated]

class MentorList(generics.ListCreateAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer

class MentorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer