from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .permissions import *
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import OutstandingToken, BlacklistedToken
from rest_framework import status

class StudentSignup(generics.GenericAPIView):
    permission_classes=[IsSuperUser]
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
    permission_classes=[IsSuperUser]
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
    permission_classes=[IsSuperUser]
    serializer_class = CareerSerializer
    queryset = Career.objects.all()
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
    permission_classes=[IsSuperUser]
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
    
class StudentView(APIView):
    permission_classes=[IsSuperUser]
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
                        
class SubjectView(generics.GenericAPIView):
    permission_classes=[IsSuperUser]
    queryset = Subject.objects.all()
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
        

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)

        return Response(status=status.HTTP_205_RESET_CONTENT)