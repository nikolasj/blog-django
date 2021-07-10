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

    # def put(self, request, filename, format=None):
    #     up_file = request.FILES['file']
    #     destination = open('/Users/Username/' + up_file.name, 'wb+')
    #     for chunk in up_file.chunks():
    #         destination.write(chunk)
    #     destination.close()  # File should be closed only after all chuns are added
    #
    #     # ...
    #     # do some stuff with uploaded file
    #     # ...
    #     return Response(up_file.name, status.HTTP_201_CREATED)


# class UploadViewSet(ViewSet):
#     serializer_class = UploadSerializer
#
#     def list(self, request):
#         return Response("GET API")
#
#     def create(self, request):
#         file_uploaded = request.FILES.get('file_uploaded')
#         content_type = file_uploaded.content_type
#         response = "POST API and you have uploaded a {} file".format(content_type)
#         return Response(response)
