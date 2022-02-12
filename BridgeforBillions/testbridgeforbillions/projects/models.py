from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


class Project(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.TextField()

    class Meta:
        ordering = ['created']
