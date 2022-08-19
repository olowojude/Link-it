from django.forms import ModelForm
from .models import Home, User
from django.contrib.auth.forms import UserCreationForm


class AddLinkForm(ModelForm):
    class Meta:
        model = Home
        fields = '__all__'


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# FOR UPDATE USER FORM
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["image", "bio", "username", "email", ]
