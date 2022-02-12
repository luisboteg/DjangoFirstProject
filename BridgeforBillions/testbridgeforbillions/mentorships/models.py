from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from testbridgeforbillions.mentors.models import Mentor
from testbridgeforbillions.projects.models import Project


class Mentorship(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField()
    mentor_ids = models.ManyToManyField(Mentor)
    project_ids = models.ManyToManyField(Project)

    class Meta:
        ordering = ['created']
