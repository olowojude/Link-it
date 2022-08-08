from django.db import models


# Create your models here.

class Home(models.Model):
    name = models.CharField(max_length=15)
    url = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

       
class Description(models.Model):    
    description = models.TextField(null=True, blank=True)
        
    def __str__(self):        
        return self.description                  
    