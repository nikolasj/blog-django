from django.contrib.auth import get_user_model
from rest_framework import serializers

from blog.models import Article, Comment
from .choices import LikeDislikeChoice, LikeObjectChoice, FollowIconStatus
from blog.services import BlogService
from .services import ActionsService

User = get_user_model()


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

    def validate(self, data: dict):
        if not ActionsService.is_user_exists(data['user_id']):
            raise serializers.ValidationError({'user_id': 'User does not exist.'})
        return data

    def validate_user_id(self, user_id: int):
        if not ActionsService.is_user_exists(user_id):
            raise serializers.ValidationError('User does not exist.')
        return user_id

    def save(self):
        subscriber = self.context['request'].user
        user_id = self.validated_data['user_id']

        if ActionsService.is_user_subscribed(subscriber, user_id):
            ActionsService.unfollow(subscriber, user_id)
            return {'status': 200, 'status_icon': FollowIconStatus.FOLLOW}
        else:
            ActionsService.follow(subscriber, user_id)
            return {'status': 201, 'status_icon': FollowIconStatus.UNFOLLOW}


class UserFollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'full_name')
