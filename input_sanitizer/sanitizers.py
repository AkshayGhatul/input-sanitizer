from .config import get_bleach_default_options
from bleach import clean

def sanitize_data(data, bleach_kwargs={}):
    default_kwargs = get_bleach_default_options()
    if bleach_kwargs.get("allowed_tags", None):
        default_kwargs["tags"] = bleach_kwargs["allowed_tags"]
    if bleach_kwargs.get("strip_comments", None):
        default_kwargs["strip_comments"] = bleach_kwargs["strip_comments"]
    if bleach_kwargs.get("strip_tags", None):
        default_kwargs["strip"] = bleach_kwargs["strip_tags"]
    if data is None:
        return data
    return clean(data, **default_kwargs)