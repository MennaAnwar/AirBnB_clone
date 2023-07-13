#!/usr/bin/python3
import uuid
from datetime import datetime

""" BaseModel class """
class BaseModel:
  def __init__(self, *args, **kwargs):
    if kwargs:
      for key, value in kwargs.items():
        if key == "created_at" or key == "updated_at":
          setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
        elif key != "__class__":
          setattr(self, key, value)
      if "id" not in kwargs.keys():
        self.id = str(uuid.uuid4())
      if "created_at" not in kwargs.keys():
        self.created_at = datetime.now()
      if "updated_at" not in kwargs.keys():
        self.updated_at = datetime.now()
    else:
      self.id = str(uuid.uuid4())
      self.created_at = datetime.now()
      self.updated_at = datetime.now()
    
  def __str__(self):
    return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
  
  def save(self):
    self.updated_at = datetime.now()
    
  def to_dict(self):
    my_dict = self.__dict__.copy()
    my_dict["created_at"] = self.created_at.isoformat()
    my_dict["updated_at"] = self.updated_at.isoformat()
    my_dict["__class__"] = self.__class__.__name__
    return my_dict
