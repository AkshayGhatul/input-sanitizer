from .config import get_bleach_default_options
from bleach import clean
from rest_framework import serializers

class SanitizedCharField(serializers.CharField):
    def __init__(self, FIELD_NAME=None, FIELD_ERROR = None,
                allowed_tags=None, strip_comments=None, strip_tags=None,
                *args, **kwargs,
            ):
        self.FIELD_NAME = FIELD_NAME
        self.FIELD_ERROR = FIELD_ERROR
        self.bleach_kwargs = get_bleach_default_options()
        if allowed_tags:
            self.bleach_kwargs["tags"] = allowed_tags
        if strip_comments:
            self.bleach_kwargs["strip_comments"] = strip_comments
        if strip_tags:
            self.bleach_kwargs["strip"] = strip_tags
        super(SanitizedCharField, self).__init__(*args, **kwargs)

    def get_error_message(self):
        if self.FIELD_ERROR:
            return self.FIELD_ERROR
        elif self.FIELD_NAME:
            return f"Please enter valid {' '.join(self.FIELD_NAME.split('_'))}."
        return "Please enter valid text for this field."

    def to_internal_value(self, data):
        if data is None:
            return data
        cleaned_data = clean(data, **self.bleach_kwargs)
        if not cleaned_data and self.required:
            raise serializers.ValidationError(self.get_error_message())
        return cleaned_data

class SanitizedTextField(serializers.CharField):
    def __init__(self, FIELD_NAME=None, FIELD_ERROR = None,
                allowed_tags=None, strip_comments=None, strip_tags=None,
                *args, **kwargs,
            ):
        self.FIELD_NAME = FIELD_NAME
        self.FIELD_ERROR = FIELD_ERROR
        self.bleach_kwargs = get_bleach_default_options()
        if allowed_tags:
            self.bleach_kwargs["tags"] = allowed_tags
        if strip_comments:
            self.bleach_kwargs["strip_comments"] = strip_comments
        if strip_tags:
            self.bleach_kwargs["strip"] = strip_tags
        super(SanitizedTextField, self).__init__(*args, **kwargs)

    def get_error_message(self):
        if self.FIELD_ERROR:
            return self.FIELD_ERROR
        elif self.FIELD_NAME:
            return f"Please enter valid {' '.join(self.FIELD_NAME.split('_'))}."
        return "Please enter valid text for this field."

    def to_internal_value(self, data):
        if data is None:
            return data
        cleaned_data = clean(data, **self.bleach_kwargs)
        if not cleaned_data and self.required:
            raise serializers.ValidationError(self.get_error_message())
        return cleaned_data