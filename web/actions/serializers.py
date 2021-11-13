from rest_framework import serializers

from blog.models import Article, Comment
from .choices import LikeDislikeChoice, LikeObjectChoice
from blog.services import BlogService
from .services import ActionsService


# Create your serializers here.

class LikeDislikeSerializer(serializers.Serializer):
    vote = serializers.ChoiceField(choices=LikeDislikeChoice.choices)
    model = serializers.ChoiceField(choices=LikeObjectChoice.choices)
    object_id = serializers.IntegerField(min_value=1)

    def save(self):
        vote = self.validated_data.get('vote')
        model = self.validated_data.get('model')
        object_id = self.validated_data.get('object_id')
        user = self.context['request'].user

        if model == LikeObjectChoice.ARTICLE:
            obj: Article = BlogService.get_article_by_id(object_id)
        elif model == LikeObjectChoice.COMMENT:
            obj: Comment = BlogService.get_comment_by_id(object_id)

        like_obj = ActionsService.get_like_object(user=user, model_obj=obj, object_id=object_id)
        if not like_obj:
            obj.votes.create(user=user, vote=vote)
        else:
            if like_obj.vote == vote:
                like_obj.delete()
            else:
                like_obj.vote = vote
                like_obj.save(update_fields=['vote'])

        return self.response_data(obj)

    def response_data(self, obj):
        return {
            'count_like': obj.likes(),
            'count_dislike': obj.dislikes()
        }


class FollowSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(min_value=1)

    def save(self):
        subscriber = self.context['request'].user
        user_id = self.validated_data['user_id']
        if ActionsService.is_user_subscribed(subscriber, user_id):
            ActionsService.unfollow(subscriber, user_id)
        else:
            ActionsService.follow(subscriber, user_id)

