from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


class Mentor(models.Model):
    GENDERS = (
    (0,'Male'),
    (1,'Female'),
    (2,'Not binary')
    )
    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    name = models.TextField()
    gender = models.CharField(max_length=1,choices=GENDERS)
    class Meta:
        ordering = ['created']
