from django.contrib import admin
from .models import LikeDislike


@admin.register(LikeDislike)
class LikeDislikeAdmin(admin.ModelAdmin):
    list_display = ("user", "vote", "date", "content_object")
    list_select_related = ("user", "content_type")
