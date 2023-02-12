#!/usr/bin/python3
"""Review class """
from models.base_model import BaseModel


class Review(BaseModel):
    """Review deriving its attributes from Basemodel """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initializes attributes for the review class """
        super().__init__(*args, **kwargs)
