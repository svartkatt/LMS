from sqlite3.dbapi2 import IntegrityError

import pytest
from django.core.exceptions import ValidationError

from academy.models import Student, Lecturer, Group, Contact


@pytest.mark.django_db
def test_successful_student_creation():
    Student.objects.create(first_name='Some name', last_name='Some name', email='somemail@gmail.com')
    assert Student.objects.count() == 1


@pytest.mark.django_db
def test_failure_due_to_student_long_first_name():
    long_name = 'a' * 31
    student = Student.objects.create(first_name=long_name, last_name='Some name', email='somemail@gmail.com')
    with pytest.raises(ValidationError):
        assert student.full_clean()


@pytest.mark.django_db
def test_failure_due_to_student_mail_is_wrong():
    student = Student.objects.create(first_name='Some name', last_name='Some name', email='wrong mail')
    with pytest.raises(ValidationError):
        assert student.full_clean()


@pytest.mark.django_db
def test_successful_lecturer_creation():
    Lecturer.objects.create(first_name='Some name', last_name='Some name', email='somemail@gmail.com')
    assert Lecturer.objects.count() == 1


@pytest.mark.django_db
def test_failure_due_to_lecturer_long_first_name():
    long_name = 'a' * 31
    lecturer = Lecturer.objects.create(first_name=long_name, last_name='Some name', email='somemail@gmail.com')
    with pytest.raises(ValidationError):
        lecturer.full_clean()


@pytest.mark.django_db
def test_failure_due_to_lecturer_mail_is_wrong():
    lecturer = Lecturer.objects.create(first_name='Some name', last_name='Some name', email='wrong mail')
    with pytest.raises(ValidationError):
        assert lecturer.full_clean()


@pytest.mark.django_db
def test_successful_group_creation():
    lecturer = Lecturer.objects.create(first_name='Some name', last_name='Some name', email='somemail@gmail.com')
    student = Student.objects.create(first_name='Some name', last_name='Some name', email='somemail@gmail.com')
    group = Group.objects.create(course='Some name', teacher=lecturer)
    group.students.add(student)
    assert Lecturer.objects.count() == 1


@pytest.mark.django_db
def test_failure_due_to_group_long_name():
    long_name = 'a' * 31
    lecturer = Lecturer.objects.create(first_name='Some name', last_name='Some name', email='somemail@gmail.com')
    student = Student.objects.create(first_name='Some name', last_name='Some name', email='somemail@gmail.com')
    group = Group.objects.create(course=long_name, teacher=lecturer)
    group.students.add(student)
    with pytest.raises(ValidationError):
        assert group.full_clean()


@pytest.mark.django_db
def test_group_to_dict_equals_to_short_representation():
    lecturer = Lecturer.objects.create(first_name='Some name', last_name='Some name', email='somemail@gmail.com')
    student = Student.objects.create(first_name='Some name', last_name='Some name', email='somemail@gmail.com')
    group = Group.objects.create(course='Some name', teacher=lecturer)
    group.students.add(student)
    expected = {'course': 'Some name', 'teacher': lecturer}
    assert group.to_dict() == expected


@pytest.mark.django_db
def test_failure_due_to_contact_name():
    long_name = 'a' * 31
    contact = Contact.objects.create(name=long_name, email='somemail@gmail.com', text='some text')
    with pytest.raises(ValidationError):
        assert contact.full_clean()


@pytest.mark.django_db
def test_contact_to_dict_equals_to_short_representation():
    contact = Contact.objects.create(name='Some Name', email='somemail@gmail.com', text='some text')
    expected = {'name': 'Some Name', 'email': 'somemail@gmail.com', 'text': 'some text'}
    assert contact.to_dict() == expected
