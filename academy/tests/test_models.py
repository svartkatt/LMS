import contextlib

from django.core.exceptions import ValidationError
from django.test import TestCase

from academy.models import Student, Lecturer, Group


class AcademyModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.text = 'Some text'
        cls.mail = 'somemail@gmail.com'
        cls.student = Student.objects.create(
            first_name='some_name',
            last_name='some_name',
            email='somemail@gmail.com'
        )

        cls.lecturer = Lecturer.objects.create(
            first_name='some_name',
            last_name='some_name',
            email='somemail@gmail.com'
        )

    def setUp(self) -> None:
        print('setup')

    def tearDown(self) -> None:
        print('teardown')

    def test_successful_student_creation(self):
        student = Student(first_name=self.text, last_name=self.text, email=self.mail)
        student.full_clean()

    def test_failure_due_to_student_long_first_name(self):
        long_name = 'a' * 31
        student = Student(first_name=long_name, last_name=self.text, email=self.mail)
        expected_message = 'Ensure this value has at most 30 characters (it has 31).'
        with self.assertRaisesMessage(ValidationError, expected_message):
            student.full_clean()

    def test_failure_due_to_student_mail_is_none(self):
        student = Student(first_name=self.text, last_name=self.text, email=None)
        expected_message = 'This field cannot be null.'
        with self.assertRaisesMessage(ValidationError, expected_message):
            student.full_clean()

    def test_successful_lecturer_creation(self):
        lecturer = Lecturer(first_name=self.text, last_name=self.text, email=self.mail)
        lecturer.full_clean()

    def test_failure_due_to_lecturer_long_second_name(self):
        long_name = 'a' * 31
        lecturer = Lecturer(first_name=self.text, last_name=long_name, email=self.mail)
        expected_message = 'Ensure this value has at most 30 characters (it has 31).'
        with self.assertRaisesMessage(ValidationError, expected_message):
            lecturer.full_clean()

    def test_failure_due_to_lecturer_mail_is_none(self):
        lecturer = Lecturer(first_name=self.text, last_name=self.text, email=None)
        expected_message = 'This field cannot be null.'
        with self.assertRaisesMessage(ValidationError, expected_message):
            lecturer.full_clean()

    def test_successful_group_creation(self):
        group = Group.objects.create(course=self.text, teacher=self.lecturer)
        group.students.add(self.student)
        group.full_clean()

    def test_failure_due_to_group_long_name(self):
        long_name = 'a' * 31
        group = Group.objects.create(course=long_name, teacher=self.lecturer)
        group.students.add(self.student)
        expected_message = 'Ensure this value has at most 30 characters (it has 31).'
        with self.assertRaisesMessage(ValidationError, expected_message):
            group.full_clean()

    @contextlib.contextmanager
    def test_to_dict_equals_to_short_representation(self):
        group = Group.objects.create(course=self.text, teacher=self.lecturer)
        group.students.add(self.student)
        expected = {'course': self.text, 'teacher': self.lecturer}
        self.assertEquals(group.to_dict(), expected)
