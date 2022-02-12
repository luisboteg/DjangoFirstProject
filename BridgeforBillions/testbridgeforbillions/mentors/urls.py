from django.urls import path
from testbridgeforbillions.mentors import views

urlpatterns = [
    path('mentors/', views.MentorList.as_view()),
    path('mentors/<int:pk>/', views.MentorDetail.as_view),
]