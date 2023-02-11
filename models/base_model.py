#!/usr/bin/python3
""" A Base class which provides attributes for other class """

import uuid
from datetime import datetime


class BaseModel:
    """ A class which defines attributes for other classes """

    def __init__(self, *args, **kwargs):
        """Initializes the databases"""

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.item():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        value = datetime.\
                                strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)

    def __str__(self):
        """returns a string repr of the class """

        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """updates the updated_at attribute """

        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dict representation of the instance"""
        my_dict = self.__dict__.copy()
        my_dict.update({
            "__class__": self.__class__.__name__,
            "updated_at": self.updated_at.isoformat(),
            "created_at": self.created_at.isoformat()
            })
        return my_dict
