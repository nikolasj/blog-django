import logging
from django.utils.translation import gettext_lazy as _
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import CreateModelMixin

from . import services
from . import serializers

logger = logging.getLogger(__name__)


class LikeDislikeView(GenericAPIView):
    serializer_class = serializers.LikeDislikeSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        return Response(data, status.HTTP_200_OK)


class FollowViewSet(CreateModelMixin, GenericViewSet):

    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.FollowSerializer
