from rest_framework import serializers

from system.util import Util
from .models import *
from django.conf import settings

""" def email(request, password, id):
    subject = 'Thank you for registering to our site'
    message = ' Your password is: ' + password + ' fucking bitch'
    email_from = settings.EMAIL_HOST_USER
    email_to = str(id) + '@uach.mx'
    recipient_list = [email_to,]
    send_mail(subject, message, email_from, recipient_list)
     """
import random
import string


def generate_password():
    characters = string.ascii_letters+string.digits
    password = ''.join(random.choice(characters) for i in range(8))
    return password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')


class StudentSignupSerializer(UserSerializer):
    username = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    def __init__(self, *args, **kwargs):
        super(StudentSignupSerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = Student
        fields = ('username', 'first_name', 'last_name', 'status', 'career')

    def save(self, **kwargs):
        user = User(
            username=self.validated_data['username'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name']
        )
        user.is_student = True
        password = generate_password()
        Util.send_email(user.username, password)
        user.set_password(password)
        user.save()
        student = Student(
            user=user,
            career=self.validated_data['career'],
            status=self.validated_data['status']
        )

        student.save()
        return student


class TeacherSignupSerializer(UserSerializer):
    username = serializers.CharField(required=True)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super(TeacherSignupSerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = Teacher
        fields = ('username', 'first_name', 'last_name')

    def save(self, **kwargs):
        user = User(
            username=self.validated_data['username'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
        )
        user.is_teacher = True
        password = generate_password()
        Util.send_email(user.username, password)
        user.set_password(password)
        user.save()
        teacher = Teacher(
            user=user,
        )
        teacher.save()
        return teacher


class StudentSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(
        source='user.username', read_only=True)
    first_name = serializers.ReadOnlyField(
        source='user.first_name', read_only=True)
    last_name = serializers.ReadOnlyField(
        source='user.last_name', read_only=True)
    password = serializers.ReadOnlyField(
        source='user.password', read_only=True)

    class Meta:
        model = Student
        fields = ('__all__')


class TeacherSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(
        source='user.username', read_only=True)
    first_name = serializers.ReadOnlyField(
        source='user.first_name', read_only=True)
    last_name = serializers.ReadOnlyField(
        source='user.last_name', read_only=True)
    password = serializers.ReadOnlyField(
        source='user.password', read_only=True)

    class Meta:
        model = Teacher
        fields = ('__all__')


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'name', 'credits', 'dependency')
        extra_kwargs = {
            'id': {'required': True},
            'name': {'required': True},
            'credits': {'required': True},
            'dependency': {'required': False},
        }


class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = ('id', 'name')
        extra_kwargs = {
            'id': {'required': True},
            'name': {'required': True},
        }


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ('id', 'name', 'capacity')
        extra_kwargs = {
            'id': {'required': True},
            'name': {'required': True},
            'capacity': {'required': True},
        }


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ('id', 'student', 'course')
        extra_kwargs = {
            'id': {'read_only': True},
            'student': {'required': True},
            'course': {'required': True},
        }


class CourseSerializer(serializers.ModelSerializer):
    def save(self, **kwargs):
        super().save(**kwargs)
        return None

    def create(self, validated_data):
        print(type(validated_data))
        return super().create(validated_data)

    class Meta:
        model = Course
        fields = ("__all__")


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ("__all__")
