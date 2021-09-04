from django.db.models import IntegerChoices


class LikeDislikeChoice(IntegerChoices):
    LIKE = (1, "Like")
    DISLIKE = (0, "Dislike")
