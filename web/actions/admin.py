from django.contrib import admin
from .models import LikeDislike, Follower


@admin.register(LikeDislike)
class LikeDislikeAdmin(admin.ModelAdmin):
    list_display = ("user", "vote", "date", "content_object")
    list_select_related = ("user", "content_type")


@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    list_display = ("subscriber", "to_user", "created")
    date_hierarchy = "created"
