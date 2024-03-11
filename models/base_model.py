#!/usr/bin/python3
"""BaseModel Module"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """BaseModel class is the base class for other classes in the project."""

    def save(self):
        """Updates 'updated_at with the current datetime."""

        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def __init__(self, *args, **kwargs):
        """Initializes an instance of the BaseModel class."""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(
                        self,
                        key,
                        datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"),
                    )
                else:
                    self.__dict__[key] = value
        if not kwargs:
            storage.new(self)

    def __str__(self):
        """String representation of the BaseModel instance."""

        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates 'updated_at with the current datetime."""

        self.updated_at = datetime.now()

    def to_dict(self):
        """Dictionary representation of the BaseModel instance."""

        dict_instance = self.__dict__.copy()
        dict_instance["__class__"] = type(self).__name__
        dict_instance["created_at"] = self.created_at.isoformat()
        dict_instance["updated_at"] = self.updated_at.isoformat()
        return dict_instance
