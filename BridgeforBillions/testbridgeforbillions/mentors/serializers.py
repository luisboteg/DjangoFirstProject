from rest_framework import serializers
from testbridgeforbillions.mentors.models import Mentor



class MentorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mentor
        fields = ['url','email', 'name', 'gender']
        

