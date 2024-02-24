from django.db import models
from rest_framework import serializers
from django.core.validators import MinLengthValidator , RegexValidator
from datetime import datetime

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    
    def __str__(self):
        return self.name
    
class Email(models.Model):
    Email = models.EmailField()
    
    def __str__(self):
        return self.Email
    
class Student(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=15 , validators=[MinLengthValidator(10,message="The number must be at least 10 digit long"),RegexValidator('^9\d{9}$',message='The number must be start with 9 and 10 dight long')])
    age = models.IntegerField()
    date = models.DateField()
    school = models.ForeignKey(School , on_delete=models.CASCADE)
    email = models.ManyToManyField(Email)
    

class StudentSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
