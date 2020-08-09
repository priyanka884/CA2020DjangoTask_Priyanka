from django.db import models

# Create your models here.

class Employee(models.Model):
    Name = models.CharField(max_length=40)
    Emp_Id = models.IntegerField()
    Contact = models.IntegerField(max_length=10)
    Address = models.CharField(max_length=100)