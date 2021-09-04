from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from . import managers
from .choices import LikeDislikeChoice

User = get_user_model()


def like_limit():
    return (
        models.Q(app_label='blog', model='article') | models.Q(app_label='blog', model='comment')
    )


class LikeDislike(models.Model):
    vote = models.PositiveSmallIntegerField(choices=LikeDislikeChoice.choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    date = models.DateTimeField(auto_now=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to=like_limit)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    objects = models.Manager()
