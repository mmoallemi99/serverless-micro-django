from functools import cached_property
from django.contrib.contenttypes.models import ContentType
from utils.helper_models import Response


class ModelController:

    OPERATIONS = {
        'create': 'get_obj',
        'retrieve': 'create_obj',
        'update': 'update_obj',
        'delete': 'delete_obj',
        'list': 'list_objs',
    }

    def __init__(self, model_name):
        self.model = ContentType.objects.filter(model__iexact=model_name).first().model_class()

    @cached_property
    def model_manager(self):
        return self.model.objects

    def get_operation(self, operation):
        method_name = self.OPERATIONS[operation]
        return getattr(self, method_name)

    def execute(self, operation, payload):
        method = self.get_operation(operation)
        return method(**payload)

    def get_obj(self, **kwargs):
        model_obj = self.model_manager.filter(**kwargs).first()
        return Response(
            success=True,
            message='Object retrieved successfully!',
            data=model_obj,
        )

    def create_obj(self, **kwargs):
        model_obj = self.model_manager.create(**kwargs)
        return Response(
            success=True,
            message='Object created successfully!',
            data=model_obj,
        )

    def update_obj(self, search_obj_by: dict, new_data: dict):
        model_obj = self.model_manager.update(**search_obj_by, defaults=new_data)
        return Response(
            success=True,
            message='Object updated successfully!',
            data=model_obj,
        )

    def delete_obj(self, **kwargs):
        model_obj = self.model_manager.filter(**kwargs).first()
        if not model_obj:
            return Response(
                success=False,
                message='Object not found!',
            )
        model_obj.delete()
        return Response(
            success=True,
            message='Object deleted successfully!',
        )

    def list_objs(self, **kwargs):
        queryset = self.model_manager.filter(**kwargs)
        return Response(
            success=True,
            message='Object retrieved successfully!',
            data=queryset,
        )
