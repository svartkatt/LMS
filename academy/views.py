from django.shortcuts import render
from .models import Student, Lecturer, Group


def students(request):
    students = Student.objects.all()
    return render(request, 'academy/students.html', {'students': students})


def lecturers(request):
    lecturers = Lecturer.objects.all()
    return render(request, 'academy/lecturers.html', {'lecturers': lecturers})


def groups(request):
    groups = Group.objects.all()
    return render(request, 'academy/groups.html', {'groups': groups})
