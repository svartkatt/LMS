import pytest

from academy.forms import StudentForm, ContactForm


@pytest.mark.django_db
def test_expected_student_fields():
    form = StudentForm()
    expected_fields = {'first_name', 'last_name', 'email'}
    assert set(form.fields.keys()) == expected_fields


@pytest.mark.django_db
def test_student_first_name_validation_failure():
    form_data = {'first_name': 'a' * 31, 'last_name': 'Some name', 'email': 'somemail@gmail.com'}
    form = StudentForm(data=form_data)
    with pytest.raises(AssertionError):
        assert form.is_valid()


@pytest.mark.django_db
def test_expected_contact_fields():
    form = ContactForm()
    expected_fields = {'name', 'email', 'text'}
    assert set(form.fields.keys()) == expected_fields


@pytest.mark.django_db
def test_contact_name_validation_failure():
    form_data = {'name': 'a' * 31, 'email': 'somemail@gmail.com', 'text': 'Some text'}
    form = ContactForm(data=form_data)
    with pytest.raises(AssertionError):
        assert form.is_valid()
