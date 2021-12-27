import logging

from main.pagination import BasePageNumberPagination
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from . import serializers
from .services import ActionsService

logger = logging.getLogger(__name__)


class LikeDislikeView(GenericAPIView):
    serializer_class = serializers.LikeDislikeSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        return Response(data, status.HTTP_200_OK)


class FollowViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    pagination_class = BasePageNumberPagination

    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.FollowSerializer
        elif self.action == 'list_followers':
            return serializers.UserFollowSerializer
        elif self.action == 'list_following':
            return serializers.UserFollowSerializer

    def get_queryset(self):
        if self.action == 'list_followers':
            return ActionsService.get_followers(self.request.user)
        elif self.action == 'list_following':
            return ActionsService.get_followings(self.request.user)

    def list_followers(self, request):
        return self.list(request)

    def list_following(self, request):
        return self.list(request)


class FollowView(GenericAPIView):
    serializer_class = serializers.FollowSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response_data: dict = serializer.save()

        return Response(response_data, status.HTTP_200_OK)
