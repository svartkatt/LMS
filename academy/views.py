import jwt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT, HTTP_200_OK, \
    HTTP_403_FORBIDDEN, HTTP_404_NOT_FOUND, HTTP_409_CONFLICT
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_payload_handler

from LMS.settings import ARTICLES_PER_PAGE, SECRET_KEY
from exchanger.models import ExchangeRate
from .models import Student, Lecturer, Group
from .forms import ContactForm

from django.views.decorators.cache import cache_page

from .serializers import StudentSerializer, LecturerSerializer, GroupSerializer


def students(request):
    students = Student.objects.all()
    exchange_rates = ExchangeRate.objects.all()
    paginator = Paginator(students, ARTICLES_PER_PAGE)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)
    context = {
        k: v for ex_rate in exchange_rates
        for k, v in ex_rate.to_dict().items()
    }
    context['students'] = students
    context['page'] = page
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
    paginator = Paginator(lecturers, ARTICLES_PER_PAGE)
    page = request.GET.get('page')
    try:
        lecturers = paginator.page(page)
    except PageNotAnInteger:
        lecturers = paginator.page(1)
    except EmptyPage:
        lecturers = paginator.page(paginator.num_pages)
    return render(request, 'academy/lecturers.html', {'lecturers': lecturers, 'page': page})


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
    paginator = Paginator(groups, ARTICLES_PER_PAGE)
    page = request.GET.get('page')
    try:
        groups = paginator.page(page)
    except PageNotAnInteger:
        groups = paginator.page(1)
    except EmptyPage:
        groups = paginator.page(paginator.num_pages)
    return render(request, 'academy/groups.html', {'groups': groups, 'page': page})


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


@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def student(request):
    if request.method == 'GET':
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        rdata = request.data
        data = {
            'first_name': rdata.get('first_name'),
            'last_name': rdata.get('last_name'),
            'email': rdata.get('email'),
        }
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def the_student(request, id):
    try:
        student = Student.objects.get(pk=id)
    except Student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    if request.method == 'DELETE':
        student.delete()
        return Response(status=HTTP_204_NO_CONTENT)

    if request.method == 'PUT':
        first_name = request.data.get('first_name')
        if first_name:
            student.first_name = first_name
        last_name = request.data.get('last_name')
        if last_name:
            student.last_name = last_name
        email = request.data.get('email')
        if email:
            student.email = email
        the_student.save()
        return Response(status=HTTP_200_OK)


@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def lecturer(request):
    if request.method == 'GET':
        lecturer = Lecturer.objects.all()
        serializer = LecturerSerializer(lecturer, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        rdata = request.data
        data = {
            'first_name': rdata.get('first_name'),
            'last_name': rdata.get('last_name'),
            'email': rdata.get('email'),
        }
        serializer = LecturerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def the_lecturer(request, id):
    try:
        the_lecturer = Lecturer.objects.get(pk=id)
    except Lecturer.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LecturerSerializer(the_lecturer)
        return Response(serializer.data)

    if request.method == 'DELETE':
        the_lecturer.delete()
        return Response(status=HTTP_204_NO_CONTENT)

    if request.method == 'PUT':
        first_name = request.data.get('first_name')
        if first_name:
            the_lecturer.first_name = first_name
        last_name = request.data.get('last_name')
        if last_name:
            the_lecturer.last_name = last_name
        email = request.data.get('email')
        if email:
            the_lecturer.email = email
        the_lecturer.save()
        return Response(status=HTTP_200_OK)


@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def group(request):
    if request.method == 'GET':
        group = Group.objects.all()
        serializer = GroupSerializer(group, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        rdata = request.data
        data = {
            'course': rdata.get('course'),
            'students': rdata.get('students'),
            'teacher': rdata.get('teacher'),
        }
        serializer = GroupSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def the_group(request, id):
    try:
        the_group = Group.objects.get(pk=id)
    except Group.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = GroupSerializer(the_group)
        return Response(serializer.data)

    if request.method == 'DELETE':
        the_group.delete()
        return Response(status=HTTP_204_NO_CONTENT)

    if request.method == 'PUT':
        course = request.data.get('course')
        if course:
            the_group.course = course
        students = request.data.get('students')
        if students:
            the_group.students = students
        teacher = request.data.get('teacher')
        if teacher:
            the_group.teacher = teacher
        the_group.save()
        return Response(status=HTTP_200_OK)

@api_view(['POST'])
@permission_classes([AllowAny])
def authenticate_user(request):
    email = request.data.get('email')
    password = request.data.get('password')
    if not email or not password:
        res = {'error': 'Please provide an email and a password'}
        return Response(res, status=HTTP_409_CONFLICT)

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        message = 'Cannot find user with specified email'
        res = {'error': message}
        return Response(res, status=HTTP_404_NOT_FOUND)
    if not user.check_password(password):
        message = "Can't authenticate with the given credentials or the account has " \
                  "been deactivated"
        res = {'error': message}
        return Response(res, status=HTTP_403_FORBIDDEN)

    payload = jwt_payload_handler(user)
    token = jwt.encode(payload, SECRET_KEY)
    user_details = {
        'name': f'{user.first_name} {user.last_name}',
        'token': token
    }
    return Response(user_details, status=HTTP_200_OK)
