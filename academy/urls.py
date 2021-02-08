from django.urls import path
from . import views

urlpatterns = [
    path('students', views.students),
    path('lecturers', views.lecturers),
    path('groups', views.groups),
]
