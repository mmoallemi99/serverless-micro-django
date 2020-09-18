from enum import Enum
from typing import Union, List, Dict

from pydantic import BaseModel
from utils import serializers


class Response(BaseModel):
    success: bool
    message: str
    data: Union[Dict, List, None] = None


class Operations(Enum):
    create = 'create'
    retrieve = 'retrieve'
    update = 'update'
    delete = 'delete'
    list = 'list'


class EventModel(BaseModel):
    model_name: str
    operation: Operations
    payload: dict
