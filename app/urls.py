from django.urls import path
from .views import *


urlpatterns = [
    path('university/list', UniversityListAPIView.as_view()), 
    path('university/retrieve/<pk>', UniversityRestrieveAPIView.as_view()), 
    path('faculty/list', FacultyListAPIView.as_view()), 
    path('faculty/retrieve/<pk>', FacultytyRestrieveAPIView.as_view()), 
    path('group/list', GroupListAPIView.as_view()), 
    path('group/retrieve/<pk>', GroupRestrieveAPIView.as_view()), 
    path('teacher/list', TeacherListAPIView.as_view()), 
    path('teacher/retrieve/<pk>', TeacherRestrieveAPIView.as_view()),
    path('subject/list', SubjectListAPIView.as_view()), 
    path('subject/retrieve/<pk>', SubjectRestrieveAPIView.as_view()), 
    path('student/list', StudentListAPIView.as_view()), 
    path('student/retrieve/<pk>', StudentRestrieveAPIView.as_view()),  
]
