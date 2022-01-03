from django.db import models
from .config import get_bleach_default_options
from bleach import clean

class SanitizedCharField(models.CharField):
    def __init__(self, allowed_tags=None, strip_comments=None,
            strip_tags=None, *args, **kwargs,
        ):
        self.bleach_kwargs = get_bleach_default_options()
        if allowed_tags:
            self.bleach_kwargs["tags"] = allowed_tags
        if strip_comments:
            self.bleach_kwargs["strip_comments"] = strip_comments
        if strip_tags:
            self.bleach_kwargs["strip"] = strip_tags
        super(SanitizedCharField,self).__init__(*args, **kwargs)
        
    def pre_save(self, instance, add):
        data = getattr(instance, self.attname)
        if data is None:
            return data
        clean_value = clean(data, **self.bleach_kwargs)
        setattr(instance, self.attname, clean_value)
        return clean_value

class SanitizedTextField(models.TextField):
    def __init__(self, allowed_tags=None, strip_comments=None,
            strip_tags=None, *args, **kwargs,
        ):
        self.bleach_kwargs = get_bleach_default_options()
        if allowed_tags:
            self.bleach_kwargs["tags"] = allowed_tags
        if strip_comments:
            self.bleach_kwargs["strip_comments"] = strip_comments
        if strip_tags:
            self.bleach_kwargs["strip"] = strip_tags
        super(SanitizedCharField,self).__init__(*args, **kwargs)
        
    def pre_save(self, instance, add):
        data = getattr(instance, self.attname)
        if data is None:
            return data
        clean_value = clean(data, **self.bleach_kwargs)
        setattr(instance, self.attname, clean_value)
        return clean_value