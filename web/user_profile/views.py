import logging
from django.utils.translation import gettext_lazy as _
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Profile

from . import services
from . import serializers

logger = logging.getLogger(__name__)


class ProfileView(GenericViewSet):
    template_name = 'user_profile/profile.html'

    def get_serializer_class(self):
        return serializers.UserSerializer

    def get_object(self):
        return self.request.user

    def retrieve(self, request):
        serializer = self.get_serializer(self.get_object())
        return Response(serializer.data, status=status.HTTP_200_OK, template_name=self.template_name)
