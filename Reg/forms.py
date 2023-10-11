from django.forms import ModelForm
from .models import User
class UserFrom(ModelForm):
    class Meta:
        model=User
        fields=["DateofBirth","profile_picture"]
       # labels=['DateofBirth','profile_picture']
        error_messages = {
        " DateofBirth": {'required': '用户名不能为空'},
        " profile_picture": {'required': '用户名不能为空'},
    }