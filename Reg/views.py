from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from .models import User, Teacher, Course,Question,Student
from.forms import UserFrom


def UserRegister(request):

    if request.method=='GET':

        return render(request, 'Reg.html')
    elif request.method=='POST':

        username=request.POST['username']
        pswd=request.POST['password']
        pswd2=request.POST['password2']



        try:
             IsStudent=request.POST['IsStudent']
             if IsStudent=='':
                 return HttpResponse("Empty identity")

        except Exception as e:
            print('--error1 ' )

            return HttpResponse("Please choose your identity")



        if pswd!=pswd2:
            return HttpResponse("Two passwords don't match")

        old_users=User.objects.filter(username=username)
        if old_users:
            return  HttpResponse("User already exists.")

        if IsStudent=='student':
            ret=True
        else:
            ret =False

        try:
            User.objects.create(username=username, password=pswd,isStudent=ret)
        except Exception as e:
            print('-- error2 %s' %(e) )

        teachers = Teacher.objects.all()
        img = User.profile_picture
        Courses = Course.objects.all()
       # request.session['username'] = username  # store them into the session dictionary
       # request.session['uid'] = User.id
        return render(request, 'index/index.html',{'img': img, 'teachers': teachers,'courses': Courses})

def UserLogin(request):

    if request.method=='GET':
            if request.session.get('username') and request.session.get('uid'):
            #if  request.session['username']:
                return render(request, 'index/index.html')
            return render(request, 'Login.html')


    elif request.method=='POST':

        username=request.POST['username']                    #store username from the form into variables
        pswd=request.POST['password']

        try:
            student=User.objects.get(username=username)      #try getting qualifed username
        except Exception as e:
            print('--login user error %s'%(e))
            return HttpResponse("Incorrect username or password ")      #if there is exception, return error page

        try:
            user=User.objects.get(username=username,password=pswd)
        except Exception as e:
            print('--login user error 2 %s' % (e))
            return HttpResponse("Incorrect username or password ")

        request.session['username']=username                               #store them into the session dictionary
        request.session['uid']=user.id

        img=user.profile_picture
        teachers = Teacher.objects.all()          #fetch all the teacher obects, courses objects, and the profile image of current user.
        Courses = Course.objects.all()

        # If the user is a student:
        if user.isStudent==True:
            return render(request, 'index/index.html', {'img': img, 'teachers': teachers, 'courses': Courses})
        # If the user is a teacher ( modify indexforteacher.html so that it returns a page for teachers):
        else:
            return HttpResponse("Teacher Page")


# Create your views here.

def UserLogout(request):
        request.session['username']=0                               #Clear both username and password in session
        request.session['uid'] =0;
        return HttpResponseRedirect('/index/')      #return index page






def UpdateProfile(request):
    if request.method == 'GET':
            user = User.objects.get(username=request.session['username'])
            form1 = UserFrom()
            img = user.profile_picture
            return render(request, 'UpdateProfile.html',{'user': user,'form1':form1,'img':img} ) # Redirect to the user's profile page
    else:

        #image=request.FILES.get('profile_picture')
      #  dob=request.POST['DateofBirth']

        #print(image)
        #print( dob)
        user=User.objects.get(username= request.session['username'])
        #user.profile_picture=image
       # user.DateofBirth=dob
        img = user.profile_picture

        form1 = UserFrom(request.POST,request.FILES)
        if form1.is_valid():
            user.profile_picture=request.FILES.get('profile_picture')
            user.DateofBirth = request.POST['DateofBirth']
            user.personal_Bio=request.POST['personal_Bio']
            user.save()
        else:
            print(form1.errors)




    return render(request, 'index/index.html', {'img':img})