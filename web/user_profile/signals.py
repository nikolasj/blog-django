from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_profile_after_create_user(sender, created: bool, instance, **kwargs):
    if created:
        print("Create profile after create user")
        Profile.objects.create(user=instance)
