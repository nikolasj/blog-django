from django.db.models import IntegerChoices, TextChoices


class LikeDislikeChoice(IntegerChoices):
    LIKE = (1, "Like")
    DISLIKE = (0, "Dislike")


class LikeObjectChoice(TextChoices):
    ARTICLE = ("article", "Article")
    COMMENT = ("comment", "Comment")
