from django.conf import settings
from django.db.models import Count

from main.decorators import except_shell
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

    @staticmethod
    @except_shell(Article.DoesNotExist)
    def get_article_by_id(article_id: int) -> Article:
        return Article.objects.get(id=article_id)

    @staticmethod
    @except_shell(Comment.DoesNotExist)
    def get_comment_by_id(comment_id: int) -> Comment:
        return Comment.objects.get(id=comment_id)
