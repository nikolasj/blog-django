import pytz
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class SetTimeZoneSerializer(serializers.Serializer):
    timezone = serializers.ChoiceField(choices=pytz.common_timezones)
