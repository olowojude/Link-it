from django.forms import ModelForm
from .models import Home, Description
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AddLinkForm(ModelForm):
    class Meta:       
       model = Home
       fields = '__all__'
              
######
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

        
                        
#####
class DescriptionForm(ModelForm):
    class Meta:
        model = Description
        fields = "__all__"       