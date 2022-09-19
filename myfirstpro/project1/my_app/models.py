from django.db import models

# Create your models here.
class My_app(models.Model):
        rollnumber=models.CharField(max_length=100)
        studentname=models.CharField(max_length=100)