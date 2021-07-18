from django.db import models
from django.contrib.auth import get_user_model
from .choices import GenderChoice

User = get_user_model()


def upload_to(obj, filename: str):
    return f'avatar/{obj.user_id}/{filename}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    gender = models.IntegerField(choices=GenderChoice.choices, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    website = models.URLField(default="", blank=True)
    avatar = models.ImageField(upload_to=upload_to, default='avatar/no_avatar.png', blank=True)

    objects = models.Manager()
