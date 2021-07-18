from django.core.validators import FileExtensionValidator
from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import Feedback


def file_size(value):  # add this to some file where you can import it from
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 MiB.')


class FeedbackSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)
    name = serializers.CharField(min_length=2, required=False)
    file = serializers.FileField(required=False,
                                 validators=[
                                     FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png', 'gif', 'bmp']),
                                     file_size],
                                 )

    class Meta:
        model = Feedback
        fields = ('name', 'email', 'content', 'file')

    # def validate_file(self):
    #     file = self.validated_data['file']
    #     print(file)
    #     content_type = file.content_type.split('/')[0]
    #     if content_type in settings.CONTENT_TYPES:
    #         if content._size > settings.MAX_UPLOAD_SIZE:
    #             raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (
    #             filesizeformat(settings.MAX_UPLOAD_SIZE), filesizeformat(content._size)))
    #     else:
    #         raise forms.ValidationError(_('File type is not supported'))
    #     return content

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
