from django.forms import ModelForm, TextInput

from .models import Student, Lecturer, Group


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email']


class LecturerForm(ModelForm):
    class Meta:
        model = Lecturer
        fields = ['first_name', 'last_name', 'email']


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['course', 'students', 'teacher']
