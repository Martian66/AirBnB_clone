#!/usr/bin/python3
"""State class """
from models.base_model import BaseModel


class State(BaseModel):
    """State deriving its attributes from Basemodel """
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes attributes for the State class """
        super().__init__(*args, **kwargs)
