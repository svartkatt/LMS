from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from exchanger.models import ExchangeRate
from .models import Student, Lecturer, Group
from .forms import StudentForm, LecturerForm, GroupForm, ContactForm

from django.views.decorators.cache import cache_page


def students(request):
    students = Student.objects.all()
    exchange_rates = ExchangeRate.objects.all()
    context = {
        k: v for ex_rate in exchange_rates
        for k, v in ex_rate.to_dict().items()
    }
    context['students'] = students
    return render(request, 'academy/students.html', context)


class StudentsCreateView(LoginRequiredMixin, CreateView):
    model = Student
    template_name = 'academy/create_students.html'
    fields = ['first_name', 'last_name', 'email']


class StudentsEditView(LoginRequiredMixin, CreateView):
    model = Student
    template_name = 'academy/edit_students.html'
    fields = ['first_name', 'last_name', 'email']


class StudentsDeleteView(DeleteView):
    model = Student
    template_name = 'academy/delete_students.html'
    success_url = reverse_lazy('students')


def lecturers(request):
    lecturers = Lecturer.objects.all()
    return render(request, 'academy/lecturers.html', {'lecturers': lecturers})


class LecturersCreateView(LoginRequiredMixin, CreateView):
    model = Lecturer
    template_name = 'academy/create_lecturers.html'
    fields = ['first_name', 'last_name', 'email']


class LecturersEditView(LoginRequiredMixin, UpdateView):
    model = Lecturer
    template_name = 'academy/edit_lecturers.html'
    fields = ['first_name', 'last_name', 'email']


class LecturersDeleteView(DeleteView):
    model = Lecturer
    template_name = 'academy/delete_lecturers.html'
    success_url = reverse_lazy('lecturers')


def groups(request):
    groups = Group.objects.all()
    return render(request, 'academy/groups.html', {'groups': groups})


class GroupsCreateView(LoginRequiredMixin, CreateView):
    model = Group
    template_name = 'academy/create_groups.html'
    fields = ['course', 'students', 'teacher']


class GroupsEditView(LoginRequiredMixin, UpdateView):
    model = Group
    template_name = 'academy/create_groups.html'
    fields = ['course', 'students', 'teacher']


class GroupsDeleteView(DeleteView):
    model = Group
    template_name = 'academy/delete_groups.html'
    success_url = reverse_lazy('groups')


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            request.session.set_expiry(300)
            request.session['paused'] = True

    form = ContactForm()

    data = {
        'contact_us': contact_us,
        'form': form
    }
    return render(request, 'academy/contact_us.html', data)
