from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    prevHash = models.CharField(max_length=100,default=0)
    prevHash = models.CharField(max_length=500,default=0)
    data = models.CharField(max_length=100,default=0)
    student_id = models.CharField(max_length=300,default=0)
    first_name= models.CharField(max_length=300,default=0)
    last_name= models.CharField(max_length=300,default=0)
