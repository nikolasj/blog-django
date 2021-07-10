from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.reverse import reverse_lazy

from auth_app.tasks import send_information_email
from .models import Feedback
from django.conf import settings


@receiver(post_save, sender=Feedback)
def email_contact(sender, created: bool, instance, **kwargs):
    print(sender, created, instance)
    if created:
        send_information_email.delay(**get_admin_data(instance))
        send_information_email.delay(**get_user_data(instance))


def get_admin_data(instance):
    app_name = instance._meta.app_label
    print(instance._meta.app_label)
    url = reverse_lazy(f'admin:{app_name}_feedback_change', args=(instance.id,))
    return {
        'to_email': settings.ADMIN_EMAILS,
        'subject': 'Feedback!',
        'html_email_template_name': 'emails/admin_email.html',
        'context': {
            'user': 'name_admin',
            'feedback_url': url,
        }
    }


def get_user_data(instance):
    print("email", instance.email)
    return {
        'to_email': instance.email,
        'subject': 'Thank You for your feedback',
        'html_email_template_name': 'emails/user_email.html',
        'context': {
            'user': instance.name,
        },
    }
