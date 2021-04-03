import pytest

from academy.models import Student, Lecturer, Group


@pytest.mark.django_db
def test_successful_student_creation():
    Student.objects.create(first_name='Some name', last_name='Some name', email='somemail@gmail.com')
    assert Student.objects.count() == 1


@pytest.mark.django_db
def test_failure_due_to_student_long_first_name():
    long_name = 'a' * 31
    student = Student.objects.create(first_name=long_name, last_name='Some name', email='somemail@gmail.com')
    assert len(student.first_name) <= 30


# @pytest.mark.django_db
# def test_failure_due_to_student_mail_is_none():
#     student = Student.objects.create(first_name='Some name', last_name='Some name', email=None)
#     assert student.full_clean() is False


@pytest.mark.django_db
def test_successful_lecturer_creation():
    Lecturer.objects.create(first_name='Some name', last_name='Some name', email='somemail@gmail.com')
    assert Lecturer.objects.count() == 1


@pytest.mark.django_db
def test_failure_due_to_lecturer_long_first_name():
    long_name = 'a' * 31
    lecturer = Lecturer.objects.create(first_name=long_name, last_name='Some name', email='somemail@gmail.com')
    assert len(lecturer.first_name) <= 30


# @pytest.mark.django_db
# def test_failure_due_to_lecturer_mail_is_none():
#     lecturer = Lecturer.objects.create(first_name='Some name', last_name='Some name', email=None)


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
    assert len(group.course) <= 30


@pytest.mark.django_db
def test_to_dict_equals_to_short_representation():
    lecturer = Lecturer.objects.create(first_name='Some name', last_name='Some name', email='somemail@gmail.com')
    student = Student.objects.create(first_name='Some name', last_name='Some name', email='somemail@gmail.com')
    group = Group.objects.create(course='Some name', teacher=lecturer)
    group.students.add(student)
    expected = {'course': 'Some name', 'teacher': lecturer}
    assert group.to_dict() == expected
