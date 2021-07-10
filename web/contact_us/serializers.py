from rest_framework import serializers
from .models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)
    name = serializers.CharField(min_length=2, required=False)
    file = serializers.FileField(required=False)

    class Meta:
        model = Feedback
        fields = ('name', 'email', 'content', 'file')

    def validate(self, attrs: dict) -> dict:
        user = self.context['request'].user
        print(user.is_authenticated, attrs.get('name'), attrs.get('email'))
        if not user.is_authenticated and (not attrs.get('name') or not attrs.get('email')):
            raise serializers.ValidationError({"email": "this field is required", "name": "this field is required"})

        return attrs

    def create(self, validated_data):
        user = self.context['request'].user
        if user.is_authenticated:
            validated_data['name'] = user.full_name()
            validated_data['email'] = user.email
        return super().create(validated_data)

# class UploadSerializer(serializers.Serializer):
#     file_uploaded = serializers.FileField()
#
#     class Meta:
#         fields = ['file_uploaded']
