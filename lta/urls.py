from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

    path("", views.home, name="home"),

    path("add-link/", views.addlink, name="addlink"),

    path("update-link/<str:pk>/", views.updatelink, name="updatelink"),

    path("delete-link/<str:pk>/", views.deletelink, name="deletelink"),

    path("login/", views.loginpage, name="loginpage"),

    path("logout/", views.logoutpage, name="logoutpage"),


    path("register/", views.register, name="register"),

    path("update-profile/", views.updateProfile, name="updateprofile"),

    path("preview/", views.preview, name="preview")
]

urlpatterns += staticfiles_urlpatterns()
