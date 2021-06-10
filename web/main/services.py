from django.contrib.auth import get_user_model

from auth_app.utils import get_activate_key
from main.decorators import except_shell
from auth_app.tasks import send_information_email

User = get_user_model()


class CeleryService:

    @staticmethod
    def send_password_reset(self, data: dict):
        pass

    @staticmethod
    def send_email_confirm(user):
        key = get_activate_key(user)
        kwargs = {
            'to_email': user.email,
            'context': {
                'user': user.get_full_name(),
                'activate_url': key,
            }
        }
        print(kwargs)
        subject = 'Confirm your email!'
        template_name = 'auth_app/emails/verify_email.html'
        send_information_email.delay(subject, template_name, **kwargs)


class UserService:

    @staticmethod
    @except_shell((User.DoesNotExist,))
    def get_user(email):
        return User.objects.get(email=email)
