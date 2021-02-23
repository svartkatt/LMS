from django.contrib import admin
from .models import Student, Lecturer, Group, Contact

admin.site.register(Student)
admin.site.register(Lecturer)
admin.site.register(Group)
admin.site.register(Contact)
