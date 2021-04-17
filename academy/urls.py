from django.urls import path
from . import views

urlpatterns = [
    path('', views.students, name='students'),
    path('students', views.students, name='students'),
    path('students/create_students', views.create_students, name='create_students'),
    path('students/edit/<int:id>', views.edit_students, name='edit_students'),
    path('students/delete/<int:id>', views.delete_student, name='delete_student'),
    path('lecturers', views.lecturers, name='lecturers'),
    path('lecturers/create_lecturers', views.create_lecturers, name='create_lecturers'),
    path('lecturers/edit/<int:id>', views.edit_lecturers, name='edit_lecturers'),
    path('lecturers/delete/<int:id>', views.delete_lecturer, name='delete_lecturer'),
    path('groups', views.groups, name='groups'),
    path('groups/create_groups', views.create_groups, name='create_groups'),
    path('groups/edit/<int:id>', views.edit_groups, name='edit_groups'),
    path('groups/delete/<int:id>', views.delete_groups, name='delete_groups'),
    path('contact_us', views.contact_us, name='contact_us'),
]
