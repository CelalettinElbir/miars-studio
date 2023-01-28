from django.db import models

# Create your models here.



class project(models.Model):
    title  = models.CharField(max_length=25)
    description = models.TextField()
     