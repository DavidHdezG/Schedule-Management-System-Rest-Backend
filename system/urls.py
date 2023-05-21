from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,

)

urlpatterns = [
    path('student/register/', StudentSignup.as_view(), name='student'),
    path('teacher/register/', TeacherSignup.as_view(), name='teacher'),
    path('career/', CareerView.as_view(), name='career'),
    path('career/<str:pk>/', CareerDetailView.as_view(), name='career'),
    path('teacher/', TeacherView.as_view(), name='teacher'),
    path('teacher/<str:pk>/', TeacherDetailView.as_view(), name='teacher'),
    path('student/', StudentView.as_view(), name='student'),
    path('student/<str:pk>/', StudentDetailView.as_view(), name='student'),
    path('subject/', SubjectView.as_view(), name='subject'),
    path('subject/<str:pk>/', SubjectDetailView.as_view(), name='subject'),
    path('classroom/', ClassroomView.as_view(), name='classroom'),
    path('classroom/<str:pk>/', ClassroomDetailView.as_view(), name='classroom'),
    path('enrollment/', EnrollmentView.as_view(), name='enrollment'),
    path('enrollment/<str:pk>/', EnrollmentDetailView.as_view(), name='enrollment'),
    path('course/', CourseView.as_view(), name='course'),
    path('course/<str:pk>/', CourseDetailView.as_view(), name='course'),
    path('schedule/', ScheduleView.as_view(), name='schedule'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
