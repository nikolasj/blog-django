import logging

from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser, JSONParser
from .serializers import FeedbackSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet

logger = logging.getLogger(__name__)


class FeedbackView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = FeedbackSerializer
    parser_classes = (MultiPartParser, JSONParser)
    template_name = 'contact_us/index.html'
