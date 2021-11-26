from django.conf import settings
from typing import Union
from django.contrib.contenttypes.models import ContentType
from blog.models import Article, Comment
from main.decorators import except_shell
from .models import LikeDislike, Follower
from user_profile.models import User


class ActionsService:

    @staticmethod
    @except_shell(LikeDislike.DoesNotExist)
    def get_like_object(user, model_obj: Union[Article, Comment], object_id: int):
        print(user, model_obj, object_id)
        content_type = ContentType.objects.get_for_model(model_obj)
        return LikeDislike.objects.get(user=user, content_type=content_type, object_id=object_id)

    @staticmethod
    def is_user_subscribed(subscriber, user_id: int) -> bool:
        return Follower.objects.filter(subscriber=subscriber, to_user_id=user_id).exists()

    @staticmethod
    def unfollow(subscriber, user_id: int):
        return Follower.objects.filter(subscriber=subscriber, to_user_id=user_id).delete()

    @staticmethod
    def follow(subscriber, user_id: int):
        return Follower.objects.create(subscriber=subscriber, to_user_id=user_id)

    @staticmethod
    def is_user_exists(user_id: int) -> bool:
        return User.objects.filter(id=user_id).exists()

    @staticmethod
    def get_followers(user):
        return user.followers.all()

    @staticmethod
    def get_followings(user):
        return user.following.all()
