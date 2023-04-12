from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
# Create your views here.
from rest_framework import permissions
class StudentSignup(generics.GenericAPIView):
    serializer_class = StudentSignupSerializer
    #permission_classes=[permissions.IsAuthenticated]
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        user = user.user
        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "Student Created Successfully.  Now perform Login to get your token"
        })
        
class TeacherSignup(generics.GenericAPIView):
    serializer_class = TeacherSignupSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        user = user.user
        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "Teacher Created Successfully.  Now perform Login to get your token"
        })
        
        
class CareerView(generics.GenericAPIView):
    serializer_class = CareerSerializer
    def get(self, request):
        careers = Career.objects.all()
        serializer = CareerSerializer(careers, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializers = self.get_serializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        career = serializers.save()
        return Response({
            "career": CareerSerializer(career, context=self.get_serializer_context()).data,
            "message": "Career Created Successfully."
        })


class TeacherView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
    
class StudentView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
                        
class SubjectView(generics.GenericAPIView):
    serializer_class = SubjectSerializer
    def get(self, request):
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializers = self.get_serializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        subject = serializers.save()
        return Response({
            "subject": SubjectSerializer(subject, context=self.get_serializer_context()).data,
            "message": "Subject Created Successfully."
        })          