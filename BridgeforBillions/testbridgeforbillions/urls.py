"""testbridgeforbillions URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from rest_framework import routers
from testbridgeforbillions.mentors import views as mentorViews
from testbridgeforbillions.projects import views as projectsViews
from testbridgeforbillions.mentorships import views as mentorshipsViews
from django.contrib import admin

from testbridgeforbillions.mentors import urls as mentorUrls
from testbridgeforbillions.projects import urls as projectUrls
from testbridgeforbillions.mentorships import urls as mentorshipUrls

from testbridgeforbillions.projects.admin import Project as adminProject
from testbridgeforbillions.mentors.admin import Mentor as mentorProject



router = routers.DefaultRouter()

router.register(r'mentors', mentorViews.GroupMentorSet)
router.register(r'project', projectsViews.GroupProjectSet)
router.register(r'mentorships', mentorshipsViews.GroupMentorshipSet)
admin.register(adminProject)
admin.register(mentorProject)



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(mentorUrls)),
    path('', include(projectUrls)),
    path('', include(mentorshipUrls)),
    path('admin/', admin.site.urls),

]