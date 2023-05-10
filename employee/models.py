from django.db import models
from datetime import date

from django.core.validators import MaxValueValidator

# Create your models here.
class Employee(models.Model):
     id = models.AutoField(primary_key=True)
     name = models.CharField(max_length=255)
     department = models.CharField(max_length=255)
     dateOfBirth = models.DateField(validators=[MaxValueValidator(limit_value=date.today)])
     dateOfJoin = models.DateField(validators=[MaxValueValidator(limit_value=date.today)])
     post = models.CharField(max_length=255)
     address = models.CharField(max_length=255)
     city = models.CharField(max_length=255)
     country = models.CharField(max_length=255)
     zipCode = models.IntegerField()
     state = models.CharField(max_length=255)
     is_active = models.BooleanField(default=True)
     leaveCount = models.IntegerField(default=0,blank=True)
     on_leave = models.BooleanField(default=False)


     

     def __str__(self):
          return self.name




