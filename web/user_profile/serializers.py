from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from rest_framework import serializers
from .models import Profile
from .choices import GenderChoice
from actions.choices import FollowIconStatus
from actions.services import ActionsService

User = get_user_model()


class ShortUserSerializer(serializers.ModelSerializer):
    avatar = serializers.CharField(source='profile.avatar')
    url = serializers.URLField(source='full_profile_url')

    class Meta:
        model = User
        fields = ('id', 'full_name', 'avatar', 'url')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('birthday', 'avatar', 'gender',)


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = (
            'id', 'full_name', 'first_name', 'last_name', 'email', 'profile', 'is_active', 'email_verified'
        )
        read_only_fields = ('full_name', 'email_verified', 'user_likes', 'user_posts')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep.update(rep.pop('profile'))
        return rep


class UserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('avatar',)

    def validate_avatar(self, avatar):
        if avatar.size > settings.USER_AVATAR_MAX_SIZE * 1024 * 1024:
            raise serializers.ValidationError(_("Max size is {size} MB".format(size=settings.USER_AVATAR_MAX_SIZE)))
        return avatar

    def save(self, *args, **kwargs):
        if self.instance.avatar and not self.instance.is_default_image():
            self.instance.set_image_to_default()
        self.instance.avatar = self.validated_data['avatar']
        return self.instance.save(update_fields=['avatar'])


class UpdateUserProfileSerializer(serializers.ModelSerializer):
    # birthday = serializers.DateField(source='profile.birthday')
    gender = serializers.ChoiceField(source='profile.gender', choices=GenderChoice.choices, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'gender')


class UserListSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(source='profile.avatar')
    follow = serializers.SerializerMethodField('get_follow_status')

    def get_follow_status(self, obj) -> str:
        user = self.context['request'].user
        is_follow = ActionsService.is_user_subscribed(user, obj.id)
        return FollowIconStatus.UNFOLLOW if is_follow else FollowIconStatus.FOLLOW

    class Meta:
        model = User
        fields = ('id', 'full_name', 'avatar', 'follow')


class UserShortInfoSerializer(serializers.ModelSerializer):
    avatar = serializers.URLField(source='avatar_url')
    url = serializers.URLField(source='get_absolute_url')

    class Meta:
        model = User
        fields = ('id', 'full_name', 'avatar', 'url')


class UserChatListSerializer(serializers.Serializer):
    user_ids = serializers.ListSerializer(child=serializers.IntegerField(min_value=1))
