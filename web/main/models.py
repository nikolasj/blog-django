from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from rest_framework.reverse import reverse

from .managers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(_('Email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    following = models.ManyToManyField('self', through='actions.Follower', symmetrical=False, related_name='followers')
    objects = UserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.email

    def full_name(self):
        return super().get_full_name()

    def email_verified(self):
        print(self.emailaddress_set.all())
        print(self.id)
        return self.emailaddress_set.get(primary=True).verified

    def get_absolute_url(self) -> str:
        return reverse('user_profile:user_by_id', args=[self.pk])

    def followers_count(self) -> int:
        return self.followers.count()

    def following_count(self) -> int:
        return self.following.count()

    email_verified.boolean = True
