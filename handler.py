import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'serverless_micro_django.settings')
django.setup()

from utils.helper_models import EventModel, Response
from pydantic import ValidationError
from utils.controller import ModelController


def lambda_handler(event: dict, context):
    try:
        parsed_event = EventModel(**event)
        model_name = parsed_event.model_name
        operation = parsed_event.operation.value
        payload = parsed_event.payload

        model_controller = ModelController(model_name=model_name)

        response_obj: Response = model_controller.execute(operation, payload)
        return response_obj.json()
    except ValidationError as exc:
        print(f'validation error, error={exc}')
