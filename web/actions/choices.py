from django.db.models import IntegerChoices, TextChoices
from django.utils.translation import gettext_lazy as _


class LikeDislikeChoice(IntegerChoices):
    LIKE = (1, "Like")
    DISLIKE = (0, "Dislike")


class LikeObjectChoice(TextChoices):
    ARTICLE = ("article", "Article")
    COMMENT = ("comment", "Comment")


class FollowIconStatus(TextChoices):
    FOLLOW = ('Follow', _('Follow'))
    UNFOLLOW = ('Unfollow', _('Unfollow'))


class LikeIconStatus(TextChoices):
    LIKED = ('liked', _('Liked'))
    DISLIKED = ('disliked', _('Disliked'))
    UNDONE = ('undone', _('Undone'))


class LikeStatus(IntegerChoices):
    LIKE = (1, _('Like'))
    DISLIKE = (-1, _('Dislike'))
