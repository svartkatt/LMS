from celery import shared_task
from django.template.loader import render_to_string
from sendgrid import Mail, SendGridAPIClient

from LMS.settings import EMAIL_SENDER, SENDGRID_KEY


@shared_task
def send_email(data):
    context = {'name': data['name'],
               'text': data['text']
               }
    contact = render_to_string('emails/added_comment.html', context)
    message = Mail(
        from_email=EMAIL_SENDER,
        to_emails=data['email'],
        subject='Added new comment',
        html_content=contact
    )
    sg = SendGridAPIClient(SENDGRID_KEY)
    sg.send(message)
