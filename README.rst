A tool for removing malicious content from input data before saving data into database.
It takes input containing HTML with XSS scripts and returns valid HTML in the output.
It is a wrapper around Python's `bleach`_ library to easily integrate it with Django framework and it implements whitelist based approach to remove harmful content.


Setup
-----


1. Install ``input-sanitizer`` via ``pip``::
    
    pip install input-sanitizer

2. Add ``input-sanitizer`` to your ``INSTALLED_APPS``:

   .. code-block:: python

        INSTALLED_APPS = [
            # ...
            'input_sanitizer',
            # ...
        ]

3. Add default configurations for allowed tags, etc in ``settings.py``. These configurations are optional and will defaults to using the ``bleach`` defaults. Refer to `bleach`_ documentation for their use:

   .. code-block:: python

        # tags which are allowed
        BLEACH_ALLOWED_TAGS = ["div", "section", "a", "i"]

        # remove all tags from input
        BLEACH_STRIP_TAGS = True

        # remove comments, or leave them in
        BLEACH_STRIP_COMMENTS = True


Usage
-----

In Django Models
****************

``input-sanitizer`` provides two custom model fields ``SanitizedCharField`` and ``SanitizedTextField`` to *automatically* remove malicious content from input before saving data into database, but keep in mind that it won't work with **bulk update**, **bulk create**, etc as these operations are done at the database level. You can still manually sanitize input data to use for **bulk update**, **bulk create**, etc operations.

.. code-block:: python

    # in models.py
    from django import models
    from input_sanitizer import sanitized_models

    class User(models.Model):
        username = sanitized_models.SanitizedCharField()
        info = sanitized_models.SanitizedTextField()

``SanitizedCharField`` and ``SanitizedTextField`` may take following arguments to alter cleaning behaviour.
Please, refer to `bleach`_ documentation for their use:

* ``allowed_tags``: Tags which are allowed
* ``strip_comments``: Remove comments from data
* ``strip_tags``: Remove all tags from data

``SanitizedCharField`` is a extension of Django model's CharField and therefore, it will accept all normal CharField arguments.

``SanitizedTextField`` is a extension of Django model's TextField and therefore, it will accept all normal TextField arguments.

In Django Forms
***************

``SanitizedCharField`` and ``SanitizedTextField`` fields can be used to clean XSS content from form fields while validating and saving the form data.

.. code-block:: python

    # in forms.py
    from django import forms
    from input_sanitizer import sanitized_forms

    class User(forms.ModelForm):
        username = sanitized_forms.SanitizedCharField()
        info = sanitized_forms.SanitizedTextField()

``SanitizedCharField`` and ``SanitizedTextField`` may take following arguments to alter cleaning behaviour.
Please, refer to `bleach`_ documentation for their use:

* ``allowed_tags``: Tags which are allowed
* ``strip_comments``: Remove comments from data
* ``strip_tags``: Remove all tags from data

``SanitizedCharField`` and ``SanitizedTextField`` fields will return validation errors if these fields are required. You can provide following arguments to customize error messages. ``f_name`` takes precedence over ``f_name`` while returning error message.

* ``FIELD_ERROR``: Error message
* ``FIELD_NAME``: Field name

``SanitizedCharField`` is a extension of Django form's CharField. It will accept all normal CharField arguments.

``SanitizedTextField`` is a extension of Django form's TextField. It will accept all normal TextField arguments.

In DRF Serializers
******************

``SanitizedCharField`` and ``SanitizedTextField`` fields can be used to clean XSS content from serializer fields while validating and saving the serializer data.

.. code-block:: python

    # in serializers.py
    from rest_framework import serializers
    from input_sanitizer import sanitized_serializers

    class User(serializers.ModelSerializer):
        username = sanitized_serializers.SanitizedCharField()
        info = sanitized_serializers.SanitizedTextField()

``SanitizedCharField`` and ``SanitizedTextField`` may take following arguments to alter cleaning behaviour.
Please, refer to `bleach`_ documentation for their use:

* ``allowed_tags``: Tags which are allowed
* ``strip_comments``: Remove comments from data
* ``strip_tags``: Remove all tags from data

``SanitizedCharField`` and ``SanitizedTextField`` fields will return validation errors if these fields are required. You can provide following arguments to customize error messages. ``f_name`` takes precedence over ``f_name`` while returning error message.

* ``FIELD_ERROR``: Error message
* ``FIELD_NAME``: Field name

``SanitizedCharField`` is a extension of DRF serializer's CharField. It will accept all normal CharField arguments.

``SanitizedTextField`` is a extension of DRF serializer's TextField. It will accept all normal TextField arguments.

In Views
********

To manually sanitize data, you can use ``sanitize_data`` function.
It can be used to sanitize data to be used for **bulk update**, **bulk create**, etc.

.. code-block:: python

    from input_sanitizer import sanitizers 
    cleaned_data = sanitizers.sanitize_data(data, bleach_kwargs={})

``bleach_kwargs`` arguments are optional and will default to using the ``bleach`` defaults.
You may pass following arguments to alter cleaned output as per your requirement.

* ``allowed_tags``: Tags which are allowed
* ``strip_comments``: Remove comments from data
* ``strip_tags``: Remove all tags from data

.. _bleach: https://bleach.readthedocs.io/en/latest/clean.html
