from django.db import models

class Course(models.Model):
    course_id = models.CharField(max_length=5)
    title = models.CharField(max_length=100)
    description = models.TextField()
    instructor = models.CharField(max_length=100)
    number_Class_Days = models.CharField(max_le ngth=80)
    extra_Assign = models.CharField(max_length=80)

class StudentSign(models.Model):
    student_id = models.CharField(max_length=7)
    first_Name = models.CharField(max_length=30)
    last_Name = models.CharField(max_length= 50)
