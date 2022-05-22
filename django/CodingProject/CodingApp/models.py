from django.db import models

class Student(models.Model):
  name = models.CharField(max_length=40)
  last_name = models.CharField(max_length=40)
  email = models.EmailField()

class Professor(models.Model):
  name = models.CharField(max_length=40)
  last_name = models.CharField(max_length=40)
  email = models.EmailField()
  field = models.CharField(max_length=40)

class Task(models.Model):
  name= models.CharField(max_length=30)
  delivery_date = models.DateField()  
  delivered = models.BooleanField()

class Course(models.Model):
  name = models.CharField(max_length=40)
  course_id = models.IntegerField()
