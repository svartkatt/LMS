from django.urls import path
from . import views
from .views import StudentsCreateView, LecturersCreateView, GroupsCreateView, GroupsEditView, LecturersEditView, \
    StudentsEditView, StudentsDeleteView, GroupsDeleteView, LecturersDeleteView

urlpatterns = [
    path('', views.students, name='students'),
    path('students', views.students, name='students'),
    path('students/create_students', StudentsCreateView.as_view(), name='create_students'),
    path('students/edit/<int:pk>', StudentsEditView.as_view(), name='edit_students'),
    path('students/delete/<int:pk>', StudentsDeleteView.as_view(), name='delete_student'),
    path('lecturers', views.lecturers, name='lecturers'),
    path('lecturers/create_lecturers', LecturersCreateView.as_view(), name='create_lecturers'),
    path('lecturers/edit/<int:pk>', LecturersEditView.as_view(), name='edit_lecturers'),
    path('lecturers/delete/<int:pk>', LecturersDeleteView.as_view(), name='delete_lecturer'),
    path('groups', views.groups, name='groups'),
    path('groups/create_groups', GroupsCreateView.as_view(), name='create_groups'),
    path('groups/edit/<int:pk>', GroupsEditView.as_view(), name='edit_groups'),
    path('groups/delete/<int:pk>', GroupsDeleteView.as_view(), name='delete_groups'),
    path('contact_us', views.contact_us, name='contact_us'),
]
