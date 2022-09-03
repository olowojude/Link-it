from msilib.schema import File
from re import L

from django.shortcuts import render, redirect

from .models import Link, User

from .forms import AddLinkForm, RegisterForm, UserForm

from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required


# Create your views here.


# HOME PAGE

def home(request):
    return render(request, "lta/home.html")


@login_required(login_url="loginpage")
def admin(request):
    links = Link.objects.all()

    context = {"links": links, }
    return render(request, "lta/admin.html", context)

# preview


def preview(request, username):
    username = User.objects.get(username=username)
    print(username)

    # username = request.user.username
    links = Link.objects.all()

    context = {"links": links}
    return render(request, "lta/preview.html", context)


# TO ADD LINK PAGE
@login_required(login_url="loginpage")
def addlink(request):
    addlinkform = AddLinkForm()
    if request.method == "POST":
        addlinkform = AddLinkForm(request.POST)
        if addlinkform.is_valid():
            addlinkform.save()
            return redirect('admin')

    context = {"addlinkform": addlinkform}
    return render(request, "lta/addlink.html", context)


# TO UPDATE LINK PAGE

@login_required(login_url="loginpage")
def updatelink(request, pk):
    updatelink = Link.objects.get(id=pk)
    updatelinkform = AddLinkForm(instance=updatelink)

    if request.method == "POST":
        updatelinkform = AddLinkForm(request.POST, instance=updatelink)
        if updatelinkform.is_valid():
            updatelinkform.save()
            return redirect('admin')

    context = {"updatelinkform": updatelinkform}
    return render(request, "lta/updatelink.html", context)


# TO DELETE LINK PAGE

@login_required(login_url="loginpage")
def deletelink(request, pk):
    deletelink = Link.objects.get(id=pk)
    if request.method == 'POST':
        deletelink.delete()
        return redirect("admin")

    context = {"deletelink": deletelink}
    return render(request, "lta/deletelink.html", context)


# REGISTER PAGE

def register(request):
    if request.user.is_authenticated:
        return redirect('admin')
    else:
        registerform = RegisterForm()

        if request.method == "POST":
            registerform = RegisterForm(request.POST)
            if registerform.is_valid():
                registerform.save()
                messages.success(request, "Account was created successfully")
                return redirect("loginpage")

        context = {"registerform": registerform}
        return render(request, "lta/register.html", context)


# LOGIN PAGE

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('admin')
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admin')
            else:
                messages.info(request, "Username or Password is incorrect")

        context = {}
        return render(request, "lta/login.html", context)


# Update User profile
@login_required(login_url="loginpage")
def updateProfile(request):

    user = request.user
    form = UserForm(instance=user)

    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid:
            form.save()
            return redirect("admin")

    context = {"form": form}
    return render(request, "lta/updateprofile.html", context)


# LOGOUT PAGE

def logoutpage(request):
    logout(request)
    return redirect('loginpage')


def notFound(request):
    return render(request, "lta/not-found.html")
