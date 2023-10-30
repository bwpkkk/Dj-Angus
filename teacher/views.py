from django.shortcuts import render
from django.http import HttpResponse
from Reg.models import Course,Teacher,Question,Student,User
# Create your views here.

def viewCourses(request):

        Courses = Course.objects.all()
        print(Courses)
        return render(request, 'viewCourses.html', {'Courses': Courses})

import random
def viewProfile(request):

        nid=request.GET.get('nid')
        teacher = Teacher.objects.get(pk=nid)

        count=Teacher.objects.exclude(pk=nid).count()

        teachers=Teacher.objects.exclude(pk=nid)

        newqs=[]

        i = 0
        while i < 3:
           newqs.append(teachers[i])
           i += 1

        print (newqs)
        print(teachers)


        return render(request, 'viewProfile.html', {'Teacher': teacher,'Teachers': newqs})



