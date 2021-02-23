from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from sendgrid import Mail, SendGridAPIClient

from LMS.settings import EMAIL_SENDER, SENDGRID_KEY
from academy.models import Student, Lecturer, Group, Contact

from .tasks import send_email


@receiver(pre_save, sender=Student)
@receiver(pre_save, sender=Lecturer)
def capitalize_names(sender, instance, **kwargs):
    instance.first_name = instance.first_name.capitalize()
    instance.last_name = instance.last_name.capitalize()


@receiver(pre_save, sender=Group)
def capitalize_name(sender, instance, **kwargs):
    instance.course = instance.course.capitalize()


@receiver(post_save, sender=Contact)
def send_notification(sender, instance, **kwargs):
    send_email.delay(instance.to_dict())

