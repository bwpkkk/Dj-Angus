from django.forms import ModelForm
from .models import User
from django import forms
class UserFrom(ModelForm):
    class Meta:
        model=User
        fields=["DateofBirth","profile_picture","personal_Bio"]
       # labels=['DateofBirth','profile_picture']
        error_messages = {
        " DateofBirth": {'required': "Date of Birth can't be empty"},
        " profile_picture": {'required': "profile picture can't be empty"},
    }
        widgets={
            "DateofBirth":forms.DateInput(attrs={"class":"form-control",}),
            "profile_picture":forms.FileInput(attrs={"class":"form-control"}),
            "personal_Bio":forms.Textarea(attrs={"class":"form-control", })
            #"placeholder":
        }


        def __init___(self,*args,**kwargs):
            super().__init__(*args,**kwargs)

            for name,field in self.fields.items():
                print (name,field)