from django.shortcuts import render
from Reg.models import User,Teacher,Student

def index_view(request):
    try:
        user = User.objects.get(username=request.session['username'])
        teachers = Teacher.objects.all()
        img = user.profile_picture

        print(user. profile_picture)

        return render(request, 'index/index.html', {'img': img, 'teachers': teachers})
    except Exception as e:
        print('--login user error 2 %s' % (e))
        return render(request, 'index/index.html')




# Create your views here.
