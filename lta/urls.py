from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path("", views.home, name="home"),

    path("add-link/", views.addlink, name="addlink"),

    path("update-link/<str:pk>/", views.updatelink, name="updatelink"),

    path("delete-link/<str:pk>/", views.deletelink, name="deletelink"),

    path("login/", views.loginpage, name="loginpage"),

    path("logout/", views.logoutpage, name="logoutpage"),


    path("register/", views.register, name="register"),

    path("update-profile/", views.updateProfile, name="updateprofile"),
]

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
