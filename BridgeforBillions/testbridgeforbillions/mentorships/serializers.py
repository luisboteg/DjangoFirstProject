from django.contrib.auth.models import User, Group
from rest_framework import serializers
from testbridgeforbillions.mentorships.models import Mentorship



class MentorshipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mentorship
        fields = ['url','status','mentor_ids','project_ids']
        
