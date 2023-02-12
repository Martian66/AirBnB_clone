#!/usr/bin/python3
"""City class"""

from models.base_model import BaseModel


class City(BaseModel):
    """City deriving its attributes from Basemodel"""

    state_id = ""
    name = ""
