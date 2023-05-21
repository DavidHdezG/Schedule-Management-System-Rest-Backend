from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# Create your models here.


class Subject(models.Model):
    id = models.CharField(max_length=5, primary_key=True, unique=True)
    name = models.CharField(max_length=50)
    credits = models.IntegerField()
    dependency = models.ForeignKey(
        'Subject', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.name)


class Career(models.Model):
    id = models.CharField(max_length=5, primary_key=True, unique=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have an id')
        user = self.model(
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return str(self.username)

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return True


class Student(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    status = models.CharField(max_length=50)
    career = models.ForeignKey(Career, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.user.username)


class Teacher(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return str(self.user.first_name) + ' ' + str(self.user.last_name)


class Admin(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.username


class Classroom(models.Model):
    id = models.CharField(max_length=5, primary_key=True, unique=True)
    name = models.CharField(max_length=50)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.course.id) + ' - ' + str(self.student.user.username)


class Course(models.Model):
    id = models.CharField(max_length=5, primary_key=True, unique=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    schedule = models.ManyToManyField('Schedule', through='ScheduleCourse')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    semester = models.IntegerField()
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    min_students = models.IntegerField()
    student = models.ManyToManyField(Student, through='Enrollment')

    def __str__(self):
        return str(self.id)


class Schedule(models.Model):
    id = models.CharField(max_length=5, primary_key=True, unique=True)
    day = models.CharField(max_length=50)
    hour = models.CharField(max_length=50)

    def __str__(self):
        return str(self.course.id) + ' - ' + str(self.day) + ' - ' + str(self.start_time) + ' - ' + str(self.end_time)


class ScheduleCourse(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.schedule.id) + ' - ' + str(self.course.id)
