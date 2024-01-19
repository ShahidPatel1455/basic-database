from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=18)
    father_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    name = models.CharField(max_length=50,default="sanjay",null="True")
    age = models.IntegerField(null="True",default=155)
    designation = models.CharField(max_length=50,default="senior madarchod",null="True")

    