from rest_framework import serializers 
from .models import *

def newId(user_role):
    if user_role == 1:
        lastId = User.objects.all().filter(is_student=True).order_by('username').last()
        if lastId is not None:
            lastId = int(lastId.username[2:])
            newId = str(lastId + 1).zfill(8)
        else:
            newId = "00000001"
        return "al" + newId
    else:
        lastId = User.objects.all().filter(is_teacher=True).order_by('username').last()
        if lastId is not None:
            lastId = int(lastId.username[2:])
            newId = str(lastId + 1).zfill(8)
        else:
            newId = "00000001"
        return "nm" + newId


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','first_name','last_name')
        
class StudentSignupSerializer(UserSerializer):
    first_name=serializers.CharField(required=False)
    last_name=serializers.CharField(required=False)
    password = serializers.CharField(required=False)
    def __init__(self,*args,**kwargs):
        super(StudentSignupSerializer,self).__init__(*args,**kwargs)
        
    class Meta:
        model = Student
        fields=('first_name','last_name','password','status','career')
        
    def save(self, **kwargs):
        user=User(
            username=newId(1),
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name']
        )
        user.is_student=True
        user.set_password(self.validated_data['password'])
        
        student=Student(
            user=user,
            career=self.validated_data['career'],
            status=self.validated_data['status']
        )
        
        student.save()
        return student

class TeacherSignupSerializer(UserSerializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
    def __init__(self, *args, **kwargs):
        super(TeacherSignupSerializer,self).__init__(*args, **kwargs)
    
    class Meta:
        model = Teacher
        fields = ('first_name','last_name','password')
    
    def save(self, **kwargs):
        user = User(
            username=newId(2),
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
        )
        user.is_teacher = True
        user.set_password(self.validated_data['password'])
        user.save()
        teacher = Teacher(
            user=user,
        )
        teacher.save()
        return teacher
    
class StudentSerializer(serializers.ModelSerializer):
    username=serializers.ReadOnlyField(source='user.username', read_only=True)
    first_name = serializers.ReadOnlyField(source='user.first_name', read_only=True)
    last_name = serializers.ReadOnlyField(source='user.last_name', read_only=True)
    password = serializers.ReadOnlyField(source='user.password', read_only=True)
    class Meta:
        model = Student
        fields = ('__all__')
        
class TeacherSerializer(serializers.ModelSerializer):
    username=serializers.ReadOnlyField(source='user.username', read_only=True)
    first_name = serializers.ReadOnlyField(source='user.first_name', read_only=True)
    last_name = serializers.ReadOnlyField(source='user.last_name', read_only=True)
    password = serializers.ReadOnlyField(source='user.password', read_only=True)
    
    class Meta:
        model =Teacher
        fields = ('__all__')

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'name','credits','dependency')
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
        
        
        