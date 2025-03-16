from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator


class User(AbstractUser):
    userType = models.CharField(max_length=10, choices=[('teacher', 'Teacher'), ('student', 'Student')])

class Student(User):
    student_id = models.CharField(max_length=20, unique=True)

class Teacher(User):
    classmethod
    pass
    
class Exam(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    question= models.TextField(max_length=10000)
    model_answer = models.TextField(max_length=10000)
    keywordsList = models.TextField(max_length=10000,null=True,blank=True)
    is_active = models.BooleanField(default=False)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    ocr_graded = models.BooleanField(default=False)

class ExamSubmission(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE,related_name='submissions') #related name is used to access the submissions of a particular exam
    student = models.ForeignKey(User, on_delete=models.CASCADE,related_name='submissions') #related name is used to access the submissions of a particular student
    student_answer = models.TextField(max_length=10000)
    score = models.DecimalField(max_digits=5, decimal_places=3, validators=[MaxValueValidator(10.000)])
    time_submitted = models.DateTimeField(auto_now_add=True)
    is_graded = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False) #If the teacher approves the grade , this will be set to true and then the student can see the grade

class ExamSubmissionOCR(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='ocr_submissions')
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ocr_submissions')
    student_id = models.CharField(max_length=20)
    student_name= models.CharField(max_length=100,default='Anonymous')
    image = models.ImageField(upload_to='ocr_images/')
    extracted_text = models.TextField(blank=True, null=True)
    score = models.DecimalField(max_digits=5, decimal_places=3, validators=[MaxValueValidator(10.000)])
    is_graded = models.BooleanField(default=False)
    time_created = models.DateTimeField(auto_now_add=True)

# from django.db import models
# from django.conf import settings

# class MCQExam(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField(blank=True, null=True)
#     created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title

# class Question(models.Model):
#     exam = models.ForeignKey(MCQExam, on_delete=models.CASCADE, related_name="questions")
#     text = models.CharField(max_length=500)

#     def __str__(self):
#         return self.text

# class Option(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="options")
#     text = models.CharField(max_length=300)
#     is_correct = models.BooleanField(default=False)

#     def __str__(self):
#         return self.text

# class ExamResult(models.Model):
#     exam = models.ForeignKey(MCQExam, on_delete=models.CASCADE)
#     student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     score = models.IntegerField()
#     submitted_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.student} - {self.exam} score: {self.score}"

# models.py
# models.py
from django.conf import settings
from django.db import models

class MCQExam(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='mcq_exams')
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False) 

    def __str__(self):
        return self.title

class Question(models.Model):
    exam = models.ForeignKey(MCQExam, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=300)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class ExamResult(models.Model):
    exam = models.ForeignKey(MCQExam, on_delete=models.CASCADE)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.IntegerField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.exam}: {self.score}"


