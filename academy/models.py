from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(null=True)
    avatar = models.ImageField(upload_to='covers/', default='covers/default.png')


class Lecturer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    avatar = models.ImageField(upload_to='covers/', default='covers/default.png')


class Group(models.Model):
    course = models.CharField(max_length=30)
    students = models.ManyToManyField(Student)
    teacher = models.ForeignKey(Lecturer, on_delete=models.CASCADE)

    def to_dict(self):
        return {
            'course': self.course,
            'teacher': self.teacher,
        }


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    text = models.TextField()

    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'text': self.text,
        }
