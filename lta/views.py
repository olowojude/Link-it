from django.shortcuts import render, redirect

from .models import Home, Description

from .forms import AddLinkForm, RegisterForm, DescriptionForm

from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required


# Create your views here.


    


######## HOME PAGE

@login_required(login_url="loginpage")
def home(request):
    links = Home.objects.all()
    bio = Description.objects.all()

    
    context = {"links": links, "bio": bio}
    return render(request, "lta/home.html", context)
    
    
    
    

#########   TO ADD LINK PAGE
@login_required(login_url="loginpage")
def addlink(request):
    addlinkform = AddLinkForm()
    if request.method == "POST":
        addlinkform = AddLinkForm(request.POST)
        if addlinkform.is_valid():
            addlinkform.save()
            return redirect('home')       
    
    context = {"addlinkform": addlinkform}
    return render(request, "lta/addlink.html", context)
    
    
    
    
    
    
###### TO UPDATE LINK PAGE

@login_required(login_url="loginpage")
def updatelink(request, pk):
    updatelink = Home.objects.get(id=pk)
    updatelinkform = AddLinkForm(instance=updatelink)
    
    if request.method == "POST":
        updatelinkform = AddLinkForm(request.POST, instance=updatelink)
        if updatelinkform.is_valid():
            updatelinkform.save()
            return redirect('home')
        
    
    context = {"updatelinkform": updatelinkform}
    return render(request, "lta/updatelink.html", context)
    
    
    
    
    
    
########### TO DELETE LINK PAGE

@login_required(login_url="loginpage")
def deletelink(request, pk):
    deletelink = Home.objects.get(id=pk) 
    if request.method == 'POST':
        deletelink.delete()
        return redirect("home")
     
    context = {"deletelink": deletelink}        
    return render(request, "lta/deletelink.html", context)  
    

    
        
            
                    
########## REGISTER PAGE

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:                
        registerform = RegisterForm()
    
    
        if request.method == "POST":        
            registerform = RegisterForm (request.POST)
            if registerform.is_valid():
                registerform.save()
                messages.success(request, "Account was created successfully")
                return redirect("loginpage")
            
        context = {"registerform": registerform}
        return render(request, "lta/register.html", context)
        
                
                
                
######### LOGIN PAGE

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
        
        
            user = authenticate(request, username=username, password= password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, "Username or Password is incorrect")    
        
    
        context = {}
        return render(request, "lta/login.html", context)










######### LOGOUT PAGE

def logoutpage(request):
    logout(request)
    return redirect('loginpage')
    
    
    
    

                
    
#### NORMAL VIEW THAT APPEARS TO NONE USERS

#def normalview(request, username):
#    links = Home.objects.all()
 #   username = RegisterForm.objects.get(username=username)
    
#    context = {"links": links}
#    return render(request, "lta/normalview.html", context)  
    
    

    
        
                
##### FOR DESCRIPTION
def description(request):
    descriptionform = DescriptionForm()
    
    if request.method == "POST":
        descriptionform = DescriptionForm(request.POST)
        if descriptionform.is_valid():
            descriptionform.save()
            return redirect('home')
    
    #if request.method == "POST":
        #description =  request.POST.get("description")
        
     #   if description.is_valid():
     #       description.save()
    #        return redirect('home')
    
    context = {"descriptionform": descriptionform}
    return render(request, "lta/description.html", context)