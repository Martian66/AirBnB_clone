#!/usr/bin/python3
"""City class """
from models.base_model import BaseModel


class City(BaseModel):
    """Class deriving its attributes from BaseModel """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes attributes for the city class """
        super().__init__(*args, **kwargs)
