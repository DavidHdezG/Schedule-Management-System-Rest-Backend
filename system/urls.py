from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    
)

urlpatterns = [
    path('student/register/', StudentSignup.as_view(),name='student'),
    path('teacher/register/', TeacherSignup.as_view(),name='teacher'),
    path('career/', CareerView.as_view(),name='career'),
    path('teacher/', TeacherView.as_view(),name='teacher'),
    path('student/', StudentView.as_view(),name='student'),
    path('subject/', SubjectView.as_view(),name='subject'),
    path('classroom/', ClassroomView.as_view(),name='classroom'),
    path('classroom/<str:pk>/', ClassroomDetailView.as_view(),name='classroom'),
    path('enrollment/', EnrollmentView.as_view(),name='enrollment'),
    path('course/', CourseView.as_view(),name='course'),
    
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),

]