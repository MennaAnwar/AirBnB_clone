import uuid
from datetime import datetime

""" BaseModel class """
class BaseModel:
  def __init__(self,name="",my_number=0):
    self.my_number = my_number
    self.name = name
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
