from django.db import models
from django.contrib.auth import get_user_model
from .choices import GenderChoice
from django.utils.translation import gettext_lazy as _

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

    class Meta:
        verbose_name = _('Profile')

    def set_image_to_default(self):
        self.avatar.delete(save=False)  # delete old image file

    def is_default_image(self):
        return True if self.avatar.url.find("no-avatar.png") != -1 else False

    def __str__(self):
        return f"{self.user.full_name()} profile"
