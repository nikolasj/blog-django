from django.conf import settings
from typing import Union
from django.contrib.contenttypes.models import ContentType
from blog.models import Article, Comment
from main.decorators import except_shell
from .models import LikeDislike


class ActionsService:

    @staticmethod
    @except_shell(LikeDislike.DoesNotExist)
    def get_like_object(user, model_obj: Union[Article, Comment], object_id: int):
        print(user, model_obj, object_id)
        content_type = ContentType.objects.get_for_model(model_obj)
        return LikeDislike.objects.get(user=user, content_type=content_type, object_id=object_id)
