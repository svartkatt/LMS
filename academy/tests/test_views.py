# from django.test import TestCase
# from django.urls import reverse
#
#
# class ListViewTest(TestCase):
#
#     def test_view_students_url_exists_at_desired_location(self):
#         resp = self.client.get('/students')
#         self.assertEqual(resp.status_code, 200)
#
#     def test_view_students_url_accessible_by_name(self):
#         resp = self.client.get(reverse('students'))
#         self.assertEqual(resp.status_code, 200)
#
#     def test_view_uses_correct_students_template(self):
#         resp = self.client.get(reverse('students'))
#         self.assertEqual(resp.status_code, 200)
#         self.assertTemplateUsed(resp, 'academy/students.html')
#
#     def test_view_lecturers_url_exists_at_desired_location(self):
#         resp = self.client.get('/lecturers')
#         self.assertEqual(resp.status_code, 200)
#
#     def test_view_lecturers_url_accessible_by_name(self):
#         resp = self.client.get(reverse('lecturers'))
#         self.assertEqual(resp.status_code, 200)
#
#     def test_view_uses_correct_lecturers_template(self):
#         resp = self.client.get(reverse('lecturers'))
#         self.assertEqual(resp.status_code, 200)
#         self.assertTemplateUsed(resp, 'academy/lecturers.html')
#
#     def test_view_groups_url_exists_at_desired_location(self):
#         resp = self.client.get('/groups')
#         self.assertEqual(resp.status_code, 200)
#
#     def test_view_groups_url_accessible_by_name(self):
#         resp = self.client.get(reverse('groups'))
#         self.assertEqual(resp.status_code, 200)
#
#     def test_view_uses_correct_groups_template(self):
#         resp = self.client.get(reverse('groups'))
#         self.assertEqual(resp.status_code, 200)
#         self.assertTemplateUsed(resp, 'academy/groups.html')