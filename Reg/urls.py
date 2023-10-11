from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[

    path('register',views.UserRegister),
    path('login',views.UserLogin),
    path('logout',views.UserLogout),
    path('UpdateProfile',views.UpdateProfile),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)