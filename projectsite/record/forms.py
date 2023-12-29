# myapp/forms.py
from django.forms import ModelForm
from django import forms
from .models import Student, Course, Assignment, Activity, Exam, Grade, StudentScore


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = "__all__"

class ActivityForm(ModelForm):
    class Meta:
        Deadline = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
        model = Activity
        fields = "__all__"

class AssignmentForm(ModelForm):
    class Meta:
        Deadline = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
        model = Assignment
        fields = "__all__"

class ExamForm(ModelForm):
    class Meta:
        Deadline = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
        model = Exam
        fields = "__all__"

class GradeForm(ModelForm):
    class Meta:
        model = Grade
        fields = "__all__"

class StudentScoreForm(ModelForm):
    class Meta:
        model = StudentScore
        fields = "__all__"

