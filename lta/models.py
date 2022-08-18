from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Home(models.Model):
    name = models.CharField(max_length=15)
    url = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    image = models.ImageField(
        null=True, default="default.png", upload_to="media/images/")

    USERNAME_FIELDS = "email"
    REQUIRED_FIELDS = []
