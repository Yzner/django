"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from record import views
from record.views import (
    HomePageView, StudentListView, StudentCreateView, StudentDeleteView, StudentUpdateView, 
    CourseListView, CourseCreateView, CourseDeleteView, CourseUpdateView, 
    ActivityListView, ActivityCreateView, ActivityDeleteView, ActivityUpdateView, 
    AssignmentListView, AssignmentCreateView, AssignmentDeleteView, AssignmentUpdateView,
    ExamListView, ExamCreateView, ExamDeleteView, ExamUpdateView,
    StudentScoreListView, StudentScoreCreateView, StudentScoreDeleteView, StudentScoreUpdateView,
    GradeListView, GradeCreateView, GradeDeleteView, GradeUpdateView
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Include the admin URLs here
    path('', views.HomePageView.as_view(), name='home'),
    path('students/', StudentListView.as_view(), name='student-list'),
    path('student_list/add', StudentCreateView.as_view(), name='student-add'),
    path('student_list/<int:pk>/', StudentUpdateView.as_view(), name='student-update'),
    path('student_list/<int:pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),

    path('courses/', CourseListView.as_view(), name='course-list'),
    path('course_list/add', CourseCreateView.as_view(), name='course-add'),
    path('course_list/<int:pk>/', CourseUpdateView.as_view(), name='course-update'),
    path('course_list/<int:pk>/delete/', CourseDeleteView.as_view(), name='course-delete'),

    path('activity/', ActivityListView.as_view(), name='activity-list'),
    path('activity_list/add', ActivityCreateView.as_view(), name='activity-add'),
    path('activity_list/<int:pk>/', ActivityUpdateView.as_view(), name='activity-update'),
    path('activity_list/<int:pk>/delete/', ActivityDeleteView.as_view(), name='activity-delete'),

    path('assignment/', AssignmentListView.as_view(), name='assignment-list'),
    path('assignment_list/add', AssignmentCreateView.as_view(), name='assignment-add'),
    path('assignment_list/<int:pk>/', AssignmentUpdateView.as_view(), name='assignment-update'),
    path('assignment_list/<int:pk>/delete/', AssignmentDeleteView.as_view(), name='assignment-delete'),

    path('exam/', ExamListView.as_view(), name='exam-list'),
    path('exam_list/add', ExamCreateView.as_view(), name='exam-add'),
    path('exam_list/<int:pk>/', ExamUpdateView.as_view(), name='exam-update'),
    path('exam_list/<int:pk>/delete/', ExamDeleteView.as_view(), name='exam-delete'),

    path('student_score/', StudentScoreListView.as_view(), name='score-list'),
    path('StudentScore_list/add', StudentScoreCreateView.as_view(), name='StudentScore-add'),
    path('StudentScore_list/<int:pk>/', StudentScoreUpdateView.as_view(), name='StudentScore-update'),
    path('StudentScore_list/<int:pk>/delete/', StudentScoreDeleteView.as_view(), name='StudentScore-delete'),


    path('grade/', GradeListView.as_view(), name='grade-list'),
    path('grade_list/add', GradeCreateView.as_view(), name='grade-add'),
    path('grade_list/<int:pk>/', GradeUpdateView.as_view(), name='grade-update'),
    path('grade_list/<int:pk>/delete/', GradeDeleteView.as_view(), name='grade-delete'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

