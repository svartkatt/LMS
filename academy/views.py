from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .models import Student, Lecturer, Group
from .forms import StudentForm, LecturerForm, GroupForm


def students(request):
    students = Student.objects.all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    form = StudentForm()

    data = {
        'students': students,
        'form': form
    }
    return render(request, 'academy/students.html', data)


def lecturers(request):
    lecturers = Lecturer.objects.all()
    if request.method == 'POST':
        form = LecturerForm(request.POST)
        if form.is_valid():
            form.save()
    form = LecturerForm()

    data = {
        'lecturers': lecturers,
        'form': form
    }
    return render(request, 'academy/lecturers.html', data)


def groups(request):
    groups = Group.objects.all()
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups')
    form = GroupForm()

    data = {
        'groups': groups,
        'form': form
    }
    return render(request, 'academy/groups.html', data)
