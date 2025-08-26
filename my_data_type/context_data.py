
# ! context_data.py

from pydantic import BaseModel


class userData(BaseModel):
    name:str
    age:int
    role:str
    
    
class UserData(BaseModel):
    name: str
    age: int
    role: str
    favorite_subject: str
    study_hours: int