from django.conf import settings
from django.db.models import Count

from .choices import ArticleStatus
from .models import Category, Article, Comment


class BlogService:

    @staticmethod
    def category_queryset():
        return Category.objects.all()

    @staticmethod
    def get_active_articles():
        return Article.objects.filter(status=ArticleStatus.ACTIVE).annotate(
            comments_count=Count('comment_set')).prefetch_related('comment_set')

    @staticmethod
    def get_parent_comments():
        return Comment.objects.filter()
