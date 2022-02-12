from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.parsers import JSONParser
from testbridgeforbillions.mentorships.serializers import MentorshipSerializer
from testbridgeforbillions.mentorships.models import Mentorship
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics

class GroupMentorshipSet(viewsets.ModelViewSet):
    queryset = Mentorship.objects.all()
    serializer_class = MentorshipSerializer
    permission_classes = [permissions.IsAuthenticated]

class MentorshipList(generics.ListCreateAPIView):
    queryset = Mentorship.objects.all()
    serializer_class = MentorshipSerializer

class MentorshipDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mentorship.objects.all()
    serializer_class = MentorshipSerializer