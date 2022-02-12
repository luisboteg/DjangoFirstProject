from django.urls import path
from testbridgeforbillions.mentorships import views

urlpatterns = [
    path('mentorships/', views.MentorshipList.as_view()),
    path('mentorships/<int:pk>/', views.MentorshipDetail.as_view),
]