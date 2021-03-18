import csv

from django.contrib import admin
from django.http import HttpResponse

from .models import Student, Lecturer, Group, Contact


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    actions = ['students_export']

    def students_export(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="articles.csv"'
        writer = csv.writer(response)
        header = ['First name', 'Last name', 'Email', 'Avatar']
        writer.writerow(header)
        for student in queryset:
            row = [student.first_name, student.last_name, student.email, student.cover]
            writer.writerow(row)
        return response

    students_export.short_description = 'Export students'


@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    actions = ['lecturers_export']

    def lecturers_export(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="articles.csv"'
        writer = csv.writer(response)
        header = ['First name', 'Last name', 'Email', 'Cover']
        writer.writerow(header)
        for lecturer in queryset:
            row = [lecturer.first_name, lecturer.last_name, lecturer.email, lecturer.cover]
            writer.writerow(row)
        return response

    lecturers_export.short_description = 'Export lecturers'


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    actions = ['groups_export']

    def groups_export(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="articles.csv"'
        writer = csv.writer(response)
        header = ['Course', 'Students', 'Teacher']
        writer.writerow(header)
        for group in queryset:
            row = [group.course, group.students, group.teacher]
            writer.writerow(row)
        return response

    groups_export.short_description = 'Export groups'


admin.site.register(Contact)
