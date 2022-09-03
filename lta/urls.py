from cgitb import handler
from re import template
from django.urls import path, re_path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views

urlpatterns = [

    path("", views.home, name="home"),

    path("admin-page/", views.admin, name="admin"),

    path("add-link/", views.addlink, name="addlink"),

    path("update-link/<str:pk>/", views.updatelink, name="updatelink"),

    path("delete-link/<str:pk>/", views.deletelink, name="deletelink"),

    path("login/", views.loginpage, name="loginpage"),

    path("logout/", views.logoutpage, name="logoutpage"),

    path("register/", views.register, name="register"),

    path("error/", views.notFound, name="notfound"),

    path("update-profile/", views.updateProfile, name="updateprofile"),

    #     path("<username>/", views.preview, name="preview"),
    re_path(r'^(?P<username>\w+)/$', views.preview, name="preview"),

    path('reset-password/', auth_views.PasswordResetView.as_view(template_name="lta/password-reset.html"),
         name="reset_password"),

    path('reset-password-sent/', auth_views.PasswordResetDoneView.as_view(template_name="lta/password-reset-sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="lta/password-reset-form.html"),
         name="password_reset_confirm"),

    path('reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name="lta/password-reset-complete.html"),
         name="password_reset_complete")
]

# handler404 = "lta.views.notFound"
urlpatterns += staticfiles_urlpatterns()
