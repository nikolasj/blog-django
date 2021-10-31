from rest_framework import serializers

from user_profile.serializers import UserSerializer
from .models import Category, Article, Comment


class CommentChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        read_only_fields = ('user',)
        fields = ('id', 'user', 'author', 'content', 'updated')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.EmailField(required=False)
    child = CommentChildSerializer(source='children', many=True, read_only=True)
    parent_id = serializers.IntegerField(default=None, write_only=True)

    def validate(self, attrs: dict) -> dict:
        user = self.context['request'].user
        if not user.is_authenticated and not attrs.get('author'):
            raise serializers.ValidationError({"author": "type your email or login."})

        return attrs

    def create(self, validated_data: dict):
        user = self.context['request'].user
        if user.is_authenticated:
            validated_data['user'] = user
            validated_data['author'] = user.email
        return super().create(validated_data)

    class Meta:
        model = Comment
        read_only_fields = ('user',)
        fields = ('id', 'article', 'user', 'author', 'content', 'updated', 'parent_id', 'child')


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True, allow_unicode=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')


class ArticleSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url')
    author = UserSerializer()
    category = CategorySerializer()
    comments_count = serializers.IntegerField()

    class Meta:
        model = Article
        fields = ('id', 'title', 'url', 'author', 'image', 'category', 'created', 'updated', 'comments_count', 'likes',
                  'dislikes')


class FullArticleSerializer(ArticleSerializer):
    # comments = CommentSerializer(source='comment_set', many=True)
    comments = serializers.SerializerMethodField(method_name='get_parent_comments')

    def get_parent_comments(self, obj):
        queryset = obj.comment_set.filter(parent_id__isnull=True)
        serializer = CommentSerializer(queryset, source='comment_set', many=True)

        return serializer.data

    class Meta(ArticleSerializer.Meta):
        fields = ArticleSerializer.Meta.fields + ('content', 'comments',)
