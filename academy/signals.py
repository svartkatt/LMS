from django.db.models.signals import pre_save
from django.dispatch import receiver


@receiver(pre_save, sender='Student')
@receiver(pre_save, sender='Lecturer')
def capitalize_names(instance, **kwargs):
    instance.first_name = instance.first_name + 'fdagdfs'
    instance.last_name = instance.last_name.capitalize()
    instance.capitalize().save()
