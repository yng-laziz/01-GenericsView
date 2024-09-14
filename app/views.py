from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.


class UniversityListAPIView(generics.ListAPIView):
    queryset = UniversityModel.objects.all()
    serializer_class = UniversitySerializer

class UniversityRestrieveAPIView(generics.RetrieveAPIView):
    queryset = UniversityModel.objects.all()
    serializer_class = UniversitySerializer

class FacultyListAPIView(generics.ListAPIView):
    queryset = FacultyModel.objects.all()
    serializer_class = FacultySerializer

class FacultytyRestrieveAPIView(generics.RetrieveAPIView):
    queryset = FacultyModel.objects.all()
    serializer_class = FacultySerializer

class GroupListAPIView(generics.ListAPIView):
    queryset = GroupModel.objects.all()
    serializer_class = GroupSerializer

class GroupRestrieveAPIView(generics.RetrieveAPIView):
    queryset = GroupModel.objects.all()
    serializer_class = GroupSerializer

class TeacherListAPIView(generics.ListAPIView):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializer

class TeacherRestrieveAPIView(generics.RetrieveAPIView):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializer

class SubjectListAPIView(generics.ListAPIView):
    queryset = SubjectModel.objects.all()
    serializer_class = SubjectSerializer

class SubjectRestrieveAPIView(generics.RetrieveAPIView):
    queryset = SubjectModel.objects.all()
    serializer_class = SubjectSerializer

class StudentListAPIView(generics.ListAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer

class StudentRestrieveAPIView(generics.RetrieveAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer