from django.shortcuts import render
from django.http import HttpResponse
from Reg.models import Course,Teacher,Question,Student,User
# Create your views here.

def viewCourses(request):

        Courses = Course.objects.all()
        print(Courses)
        return render(request, 'viewCourses.html', {'Courses': Courses})





