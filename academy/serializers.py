from rest_framework.serializers import ModelSerializer

from academy.models import Student, Lecturer, Group


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'email')


class LecturerSerializer(ModelSerializer):
    class Meta:
        model = Lecturer
        fields = ('first_name', 'last_name', 'email')


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ('course', 'students', )
