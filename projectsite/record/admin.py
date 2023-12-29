# academic_records_app/admin.py
from django.contrib import admin
from .models import Student, Course, Activity, Assignment, Exam, Grade, StudentScore

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "created_at", "updated_at")
    search_fields = ("first_name", "last_name", "email")

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("course_name", "department", "created_at", "updated_at")
    search_fields = ("course_name", "department")
    def get_students(self, obj):
        return ", ".join([student.first_name + " " + student.last_name for student in obj.students.all()])
    get_students.short_description = "Students"
    
@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ("activity_name", "deadline", "course", "score", "created_at", "updated_at")
    search_fields = ("activity_name", "course__course_name")

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ("assignment_name", "deadline", "course", "score", "created_at", "updated_at")
    search_fields = ("assignment_name", "course__course_name")

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ("exam_name", "date", "course", "score", "created_at", "updated_at")
    search_fields = ("exam_name", "course__course_name")

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ("student", "course", "get_assignment_name", "get_activity_name", "get_exam_name", "score", "created_at", "updated_at")

    def get_assignment_name(self, obj):
        return obj.student_score.assignment.assignment_name if obj.student_score.assignment else None

    def get_activity_name(self, obj):
        return obj.student_score.activity.activity_name if obj.student_score.activity else None

    def get_exam_name(self, obj):
        return obj.student_score.exam.exam_name if obj.student_score.exam else None

@admin.register(StudentScore)
class StudentScoreAdmin(admin.ModelAdmin):
    list_display = ("student", "course", "activity", "assignment", "exam", "total_score", "created_at", "updated_at")
    search_fields = ("student__first_name", "student__last_name", "course__course_name", "activity__activity_name", "assignment__assignment_name", "exam__exam_name")
