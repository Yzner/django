# academic_records_app/models.py
from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Course(BaseModel):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)

    def __str__(self):
        return self.course_name
    
class Student(BaseModel):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    profile_image = models.ImageField(upload_to='student_images/', blank=True, null=True)
    course = models.ManyToManyField(Course, related_name='students')  # Many-to-Many relationship

    def __str__(self):
        return f"{self.profile_image} {self.first_name} {self.last_name}"

class Activity(BaseModel):
    activity_id = models.AutoField(primary_key=True)
    activity_name = models.CharField(max_length=255)
    deadline = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Add this line
    students = models.ManyToManyField(Student, related_name='activities')

    def __str__(self):
        return self.activity_name

class Assignment(BaseModel):
    assignment_id = models.AutoField(primary_key=True)
    assignment_name = models.CharField(max_length=255)
    deadline = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Add this line
    students = models.ManyToManyField(Student, related_name='assignments')

    def __str__(self):
        return self.assignment_name

class Exam(BaseModel):
    exam_id = models.AutoField(primary_key=True)
    exam_name = models.CharField(max_length=255)
    date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True) 
    students = models.ManyToManyField(Student, related_name='exams')

    def __str__(self):
        return self.exam_name

class StudentScore(BaseModel):
    student_score_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, null=True, blank=True)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, null=True, blank=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, null=True, blank=True)
    
    def total_score(self):
        activity_score = self.activity.score if self.activity and self.activity.score else 0
        assignment_score = self.assignment.score if self.assignment and self.assignment.score else 0
        exam_score = self.exam.score if self.exam and self.exam.score else 0
        
        return activity_score + assignment_score + exam_score

    def __str__(self):
        return f"Total score for {self.student} - {self.course}: {self.total_score()}"

class Grade(BaseModel):
    grade_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student_score = models.ForeignKey(StudentScore, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)

    def is_pass(self, threshold=60):  # Change the threshold as needed
        return self.score >= threshold

    def __str__(self):
        pass_status = "Pass" if self.is_pass() else "Fail"
        return f"Grade for {self.student} - {self.course}: {self.score} ({pass_status})"
