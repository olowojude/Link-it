from django.urls import path
from . import views

urlpatterns = [

    path("", views.home, name = "home"),

    path("add-link/", views.addlink, name = "addlink"),
    
    path("update-link/<str:pk>/", views.updatelink, name = "updatelink"),
    
    path("delete-link/<str:pk>/", views.deletelink, name = "deletelink"),
    
    path("login/", views.loginpage, name = "loginpage"),
    
    path("logout/", views.logoutpage, name = "logoutpage"),
    
    
    path("register/", views.register, name = "register"),
    
   # path("lta/<str:username>/", views.normalview, name = "normalview"),
    
   path("description/", views.description, name = "description"),
]
#url(r'^profile_view/(?P<username>\w+)/$', 
                       #profile_view,
                     #  name='profile_view'),