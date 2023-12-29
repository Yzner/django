# academic_records_app/scripts/create_initial_data.py
import random
from faker import Faker
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils import timezone
from record.models import Student, Course, Activity, Assignment, Exam, Grade, StudentScore

fake = Faker()

class Command(BaseCommand):
    help = 'Create initial data for the academic_records_app models'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Creating initial data...'))

        # Create students

        # Create courses and enroll students
        courses = []
        for _ in range(10):
            course = Course(
                course_name=fake.sentence(),
                department=fake.sentence(),
            )
            course.save()
            courses.append(course)
            
        students = []
        for _ in range(20):
            student = Student(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email()
            )
            student.save()
            students.append(student)
            

            for _ in range(random.randint(5, 15)):
                course = random.choice(courses)
                student.courses.add(course)

        # Create activities, assignments, exams, and scores
        for course in courses:
            for _ in range(random.randint(3, 5)):
                activity = Activity(
                    activity_name=fake.sentence(),
                    deadline=fake.future_date(),
                    course=course
                )
                activity.save()
            
            for _ in range(random.randint(5, 15)):
                student = random.choice(students)
                activity.students.add(student)
            
            for _ in range(random.randint(5, 15)):
                student = random.choice(students)
                assignment.students.add(student)
            
            for _ in range(random.randint(5, 15)):
                student = random.choice(students)
                exam.students.add(student)
                

            for _ in range(random.randint(2, 5)):
                assignment = Assignment(
                    assignment_name=fake.sentence(),
                    deadline=fake.future_date(),
                    course=course
                )
                assignment.save()

            for _ in range(random.randint(2, 5)):
                exam = Exam(
                    exam_name=fake.sentence(),
                    date=fake.future_date(),
                    course=course
                )
                exam.save()

            for student in course.students.all():
                student_score = StudentScore(
                    student=student,
                    course=course,
                    activity=random.choice(course.activity_set.all()),
                    assignment=random.choice(course.assignment_set.all()),
                    exam=random.choice(course.exam_set.all())
                )
                student_score.save()

                # Set random scores for student scores
                student_score.activity.score = random.uniform(0, 100)
                student_score.assignment.score = random.uniform(0, 100)
                student_score.exam.score = random.uniform(0, 100)
                student_score.save()

                # Create grades
                grade = Grade(
                    student=student,
                    course=course,
                    student_score=student_score,
                    score=student_score.total_score()
                )
                grade.save()

        self.stdout.write(self.style.SUCCESS('Initial data created successfully.'))
