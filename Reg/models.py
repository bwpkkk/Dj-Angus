from django.db import models

import datetime
# Create your models here.
class User(models.Model):
    username = models.CharField("Username", max_length=30, unique=True)
    password = models.CharField("Password", max_length=32)
    created_time = models.DateTimeField('Created time', auto_now_add=True)
    updated_time = models.DateTimeField('Updated time', auto_now=True)
    DateofBirth = models.DateField("Date of Birth",auto_now_add=False,blank=True,null=True)
    isStudent=models.BooleanField(default=False)
    profile_picture=models.ImageField("Profile Picture",upload_to='media/profile_pictures',blank=True,null=True)
    personal_Bio=models.CharField("Bio", max_length=200,blank=True, null=True )

    class meta:
        abstract = True

    def __str__(self):
        return self.username



class Teacher(User):

    specialty=  models.CharField("Specialty", max_length=32)
    personal_rate=models.DecimalField("rate",default=0, decimal_places=2,max_digits=6)
    numberofSudents = models.IntegerField(default=0)

    def __str__(self):
       return self.username


class Course(models.Model):
    course_name = models.CharField("Course Name", max_length=30, unique=True)
    course_description = models.CharField("Course Description", max_length=100, blank=True)
    created_time = models.DateTimeField('Created time', auto_now_add=True)
    owner = models.ForeignKey(Teacher, on_delete=models.CASCADE, default=1)

    price = models.DecimalField("Price", default=0, decimal_places=2, max_digits=6)
    course_picture = models.ImageField("Course Picture", upload_to='media/course_pictures', blank=True, null=True)

    def __str__(self):
        return self.course_name


class Student(User):
    Courses_bought = models.IntegerField("Course bought",default=0)
    Quetions_asked=models.IntegerField("Quetions_asked",default=0)
    Maximum_questions=models.IntegerField("Maximum_questions",default=3)
    Teacher = models.ManyToManyField(Teacher,blank=True, null=True)
    Courses = models.ManyToManyField(verbose_name="Courses",to=Course)

    def __str__(self):
       #return 'Student %s'(self.username)
       return self.username





class Question(models.Model):

    question_Name=models.CharField("Question Name", max_length=30, unique=True)
    question_Description=models.CharField("Question Description", max_length=100)
    created_time = models.DateTimeField('Created time', auto_now_add=True)
    owner=models.ForeignKey(Student,on_delete=models.CASCADE,default=1)
    isSolved=models.BooleanField('isSolved',default=False)
    solvedby= models.ForeignKey(Teacher,on_delete=models.CASCADE,default=1)


    def __str__(self):
        return self.question_Name
