from django.shortcuts import render
from Reg.models import User,Teacher,Student,Course,Question

def index_view(request):
    try:
        user = User.objects.get(username=request.session['username'])
        teachers = Teacher.objects.all()
        img = user.profile_picture
        numofCourses= Course.objects.all().count()

        Courses= Course.objects.all()
        course=Course.objects.get(course_name="Fancy gun")
        students=course.student_set.all()
        #student=Student.objects.filter(username="Mad Max").first()


        print(numofCourses)
        return render(request, 'index/index.html', {'img': img, 'teachers': teachers,'courses': Courses})
    except Exception as e:
        print('--login user error 2 %s' % (e))
        return render(request, 'index/index.html')




# Create your views here.
