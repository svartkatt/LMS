from django.db.models.signals import pre_save
from django.dispatch import receiver

from academy.models import Student, Lecturer, Group


@receiver(pre_save, sender=Student)
@receiver(pre_save, sender=Lecturer)
def capitalize_names(sender, instance, **kwargs):
    instance.first_name = instance.first_name.capitalize()
    instance.last_name = instance.last_name.capitalize()


@receiver(pre_save, sender=Group)
def capitalize_name(sender, instance, **kwargs):
    instance.course = instance.course.capitalize()
