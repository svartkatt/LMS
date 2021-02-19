from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()


class Lecturer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()


class Group(models.Model):
    course = models.CharField(max_length=30)
    students = models.ManyToManyField(Student)
    teacher = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
