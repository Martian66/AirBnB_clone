#!/usr/bin/python3
""" User class """

from models.base_model import BaseModel


class User(BaseModel):
    """User deriving its attributes from Basemodel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
