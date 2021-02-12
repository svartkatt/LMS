from django.core.management.base import BaseCommand
from faker import Faker

from academy.models import Lecturer, Group, Student


class Command(BaseCommand):
    help = u'создание 2 новых групп, которые включают 10 новых студентов и 1 лектора'

    def handle(self, *args, **kwargs):
        for i in range(2):
            group = Group.objects.create(course='Group #' + str(i), teacher_id=1)
            name = Faker().name().split()
            lecturer = Lecturer.objects.create(first_name=name[0], last_name=name[1])
            group.teacher = lecturer
            for y in range(10):
                student_name = list(Faker().name().split())
                student = Student.objects.create(first_name=student_name[0], last_name=student_name[1])
                group.students.add(student)
