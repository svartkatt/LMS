# import pytest
# from django.urls import reverse
#
#
# @pytest.mark.django_db
# def test_view_students_url_exists_at_desired_location(client):
#     resp = client.get('/students')
#     assert resp.status_code, 200
#
#
# @pytest.mark.django_db
# def test_view_students_url_accessible_by_name(client):
#     resp = client.get(reverse('students'))
#     assert resp.status_code, 200
#
#
# @pytest.mark.django_db
# def test_view_uses_correct_students_template(client):
#     resp = client.get(reverse('students'))
#     assert resp.status_code, 200
#     assert resp, 'academy/students.html'
#
#
# @pytest.mark.django_db
# def test_view_lecturers_url_exists_at_desired_location(client):
#     resp = client.get('/lecturers')
#     assert resp.status_code, 200
#
#
# @pytest.mark.django_db
# def test_view_lecturers_url_accessible_by_name(client):
#     resp = client.get(reverse('lecturers'))
#     assert resp.status_code, 200
#
#
# @pytest.mark.django_db
# def test_view_uses_correct_lecturers_template(client):
#     resp = client.get(reverse('lecturers'))
#     assert resp.status_code, 200
#     assert resp, 'academy/lecturers.html'
#
#
# @pytest.mark.django_db
# def test_view_groups_url_exists_at_desired_location(client):
#     resp = client.get('/groups')
#     assert resp.status_code, 200
#
#
# @pytest.mark.django_db
# def test_view_groups_url_accessible_by_name(client):
#     resp = client.get(reverse('groups'))
#     assert resp.status_code, 200
#
#
# @pytest.mark.django_db
# def test_view_uses_correct_groups_template(client):
#     resp = client.get(reverse('groups'))
#     assert resp.status_code, 200
#     assert resp, 'academy/groups.html'
