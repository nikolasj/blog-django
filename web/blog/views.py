import logging
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from main.pagination import BasePageNumberPagination
from rest_framework.mixins import CreateModelMixin

from .services import BlogService
from .filters import ArticleFilter

from . import serializers

logger = logging.getLogger(__name__)


class ViewSet(ModelViewSet):
    http_method_names = ('get', 'post', 'put', 'delete')
    lookup_field = 'slug'
    permission_classes = (AllowAny,)
    pagination_class = BasePageNumberPagination


class CategoryViewSet(ViewSet):
    serializer_class = serializers.CategorySerializer

    def get_queryset(self):
        return BlogService.category_queryset()


class ArticleViewSet(ViewSet):
    filterset_class = ArticleFilter
    pagination_class = BasePageNumberPagination

    def get_template_name(self):
        if self.action == 'list':
            return 'blog/post_list.html'
        elif self.action == 'retrieve':
            return 'blog/post_detail.html'

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ArticleSerializer
        return serializers.FullArticleSerializer

    def get_queryset(self):
        return BlogService.get_active_articles()

    def list(self, request, **kwargs):
        response = super().list(request, **kwargs)
        response.template_name = self.get_template_name()
        return response

    def retrieve(self, request, **kwargs):
        response = super().retrieve(request, **kwargs)
        response.template_name = self.get_template_name()
        return response


class CommentViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = serializers.CommentSerializer
    permission_classes = (AllowAny,)

    # def get_queryset(self):
    #     comments =
    #     return
