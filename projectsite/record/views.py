from django.shortcuts import render

# Create your views here.
# myapp/views.py
from django.views.generic.list import ListView
from record.models import Student, Course, Activity, Assignment, Exam, StudentScore, Grade
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from record.forms import StudentForm, CourseForm, ActivityForm, AssignmentForm, ExamForm, GradeForm, StudentScoreForm
from django.urls import reverse_lazy

class HomePageView(ListView):
    model = Student
    context_object_name = 'home'
    template_name = "base.html"
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       return context

class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'student'
    paginate_by = 5

    def get_queryset(self):
        return Student.objects.all()
    
class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_add.html'
    success_url = reverse_lazy('student-list')
    
class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_edit.html'
    success_url = reverse_lazy('student-list')
    
class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_del.html'
    success_url = reverse_lazy('student-list')  

class CourseListView(ListView):
    model = Course
    template_name = 'course_list.html'
    context_object_name = 'courses'
    paginate_by = 2

    def get_queryset(self):
        return Course.objects.all()
    
class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'course_add.html'
    success_url = reverse_lazy('course-list')
    
class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'course_edit.html'
    success_url = reverse_lazy('course-list')
    
class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'course_del.html'
    success_url = reverse_lazy('course-list')
    
class ActivityListView(ListView):
    model = Activity
    template_name = 'activity_list.html'
    context_object_name = 'activity'
    paginate_by = 5

    def get_queryset(self):
        return Activity.objects.all()
    
class ActivityCreateView(CreateView):
    model = Activity
    form_class = ActivityForm
    template_name = 'activity_add.html'
    success_url = reverse_lazy('activity-list')
    
class ActivityUpdateView(UpdateView):
    model = Activity
    form_class = ActivityForm
    template_name = 'activity_edit.html'
    success_url = reverse_lazy('activity-list')
    
class ActivityDeleteView(DeleteView):
    model = Activity
    template_name = 'activity_del.html'
    success_url = reverse_lazy('activity-list')
    
class AssignmentListView(ListView):
    model = Assignment
    template_name = 'assignment_list.html'
    context_object_name = 'assignment'
    paginate_by = 5

    def get_queryset(self):
        return Assignment.objects.all()
    
class AssignmentCreateView(CreateView):
    model = Assignment
    form_class = AssignmentForm
    template_name = 'assignment_add.html'
    success_url = reverse_lazy('assignment-list')
    
class AssignmentUpdateView(UpdateView):
    model = Assignment
    form_class = AssignmentForm
    template_name = 'assignment_edit.html'
    success_url = reverse_lazy('assignment-list')
    
class AssignmentDeleteView(DeleteView):
    model = Assignment
    template_name = 'assignment_del.html'
    success_url = reverse_lazy('assignment-list')
    
class ExamListView(ListView):
    model = Exam
    template_name = 'exam_list.html'
    context_object_name = 'exam'
    paginate_by = 5

    def get_queryset(self):
        return Exam.objects.all()
    
class ExamCreateView(CreateView):
    model = Exam
    form_class = ExamForm
    template_name = 'exam_add.html'
    success_url = reverse_lazy('exam-list')
    
class ExamUpdateView(UpdateView):
    model = Exam
    form_class = ExamForm
    template_name = 'exam_edit.html'
    success_url = reverse_lazy('exam-list')
    
class ExamDeleteView(DeleteView):
    model = Exam
    template_name = 'exam_del.html'
    success_url = reverse_lazy('exam-list')

class StudentScoreListView(ListView):
    model = StudentScore
    template_name = 'score_list.html'
    context_object_name = 'student_score'
    paginate_by = 5

    def get_queryset(self):
        return StudentScore.objects.all()
    
class StudentScoreCreateView(CreateView):
    model = StudentScore
    form_class = StudentScoreForm
    template_name = 'record_add.html'
    success_url = reverse_lazy('score-list')
    
class StudentScoreUpdateView(UpdateView):
    model = StudentScore
    form_class = StudentScoreForm
    template_name = 'record_edit.html'
    success_url = reverse_lazy('score-list')
    
class StudentScoreDeleteView(DeleteView):
    model = StudentScore
    template_name = 'record_del.html'
    success_url = reverse_lazy('score-list') 
    
class GradeListView(ListView):
    model = Grade
    template_name = 'grade_list.html'
    context_object_name = 'grade'
    paginate_by = 5

    def get_queryset(self):
        return Grade.objects.all()
    
class GradeCreateView(CreateView):
    model = Grade
    form_class = GradeForm
    template_name = 'grade_add.html'
    success_url = reverse_lazy('grade-list')
    
class GradeUpdateView(UpdateView):
    model = Grade
    form_class = GradeForm
    template_name = 'grade_edit.html'
    success_url = reverse_lazy('grade-list')
    
class GradeDeleteView(DeleteView):
    model = Grade
    template_name = 'grade_del.html'
    success_url = reverse_lazy('grade-list') 