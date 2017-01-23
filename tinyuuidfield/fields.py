from uuid import uuid4

from django.core import checks
from django.db.models import CharField


class TinyUUIDField(CharField):
    def __init__(self, length=10, *args, **kwargs):

        # Sets default values if they are not specified
        if not kwargs.get('editable'):
            kwargs['editable'] = False
            kwargs['blank'] = True
        if not kwargs.get('unique'):
            kwargs['unique'] = True

        # Sets the length of the tiny_uuid
        self.length = length
        kwargs['max_length'] = length

        super(TinyUUIDField, self).__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        """
        This pre_save sets the uuid when the model is created
        """

        super(TinyUUIDField, self).pre_save(model_instance, add)

        self.model_type = type(model_instance)
        tiny_uuid = self.generate_uuid()

        if add:
            setattr(model_instance, self.attname, tiny_uuid)
        return tiny_uuid

    def generate_uuid(self):
        """
        Generates an unique tiny_uuid for the given model.
        If the model already have an instance with the given tiny_uuid, then it will recursively call itself.
        """

        tiny_uuid = uuid4().hex[:self.length]
        args = {getattr(self, 'name'): tiny_uuid}

        try:
            self.model_type.objects.get(**args)
            return self.generate_uuid()
        except self.model_type.DoesNotExist:
            return tiny_uuid

    def check(self, **kwargs):
        errors = super(TinyUUIDField, self).check(**kwargs)
        errors.extend(self._check_length_attribute(**kwargs))
        return errors

    def _check_length_attribute(self, **kwargs):
        if not self.length or not isinstance(self.length, int):
            return [
                checks.Error(
                    "TinyUUIDField must define a 'length' attribute between 6 and 32",
                    obj=self,
                )
            ]

        if self.length < 6 or self.length > 32:
            return [
                checks.Error(
                    "TinyUUIDField must define a 'length' attribute between 6 and 32.",
                    obj=self,
                )
            ]
        return []

