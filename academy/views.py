from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect

from .models import Student, Lecturer, Group
from .forms import StudentForm, LecturerForm, GroupForm


def students(request):
    students = Student.objects.all()
    return render(request, 'academy/students.html', {'students': students})


def create_students(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    form = StudentForm()

    data = {
        'students': students,
        'form': form
    }
    return render(request, 'academy/create_students.html', data)


def edit_students(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect('edit_students', id=id)

    form = StudentForm(instance=student)
    return render(request, 'academy/edit_students.html', {'form': form})


def delete_student(request, id):
    try:
        student = Student.objects.get(id=id)
        student.delete()
        return HttpResponseRedirect("/students")
    except Student.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


def lecturers(request):
    lecturers = Lecturer.objects.all()
    return render(request, 'academy/lecturers.html', {'lecturers': lecturers})


def create_lecturers(request):
    if request.method == 'POST':
        form = LecturerForm(request.POST)
        if form.is_valid():
            form.save()
    form = LecturerForm()

    data = {
        'lecturers': lecturers,
        'form': form
    }
    return render(request, 'academy/create_lecturers.html', data)


def edit_lecturers(request, id):
    lecturer = get_object_or_404(Lecturer, id=id)
    if request.method == 'POST':
        form = LecturerForm(request.POST, instance=lecturer)
        if form.is_valid():
            lecturer = form.save(commit=False)
            lecturer.save()
            return redirect('edit_lecturers', id=id)

    form = LecturerForm(instance=lecturer)
    return render(request, 'academy/edit_lecturers.html', {'form': form})


def delete_lecturer(request, id):
    try:
        lecturer = Lecturer.objects.get(id=id)
        lecturer.delete()
        return HttpResponseRedirect("/lecturers")
    except Student.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


# def groups(request):
#     groups = Group.objects.all()
#     if request.method == 'POST':
#         form = GroupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/groups')
#     form = GroupForm()
#
#     data = {
#         'groups': groups,
#         'form': form
#     }
#     return render(request, 'academy/groups.html', data)

def groups(request):
    groups = Group.objects.all()
    return render(request, 'academy/groups.html', {'groups': groups})


def create_groups(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
    form = GroupForm()

    data = {
        'groups': groups,
        'form': form
    }
    return render(request, 'academy/create_groups.html', data)


def edit_groups(request, id):
    group = get_object_or_404(Group, id=id)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            group = form.save(commit=False)
            group.save()
            return redirect('edit_groups', id=id)

    form = GroupForm(instance=group)
    return render(request, 'academy/edit_groups.html', {'form': form})


def delete_groups(request, id):
    try:
        group = Group.objects.get(id=id)
        group.delete()
        return HttpResponseRedirect("/groups")
    except Student.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")