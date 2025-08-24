
# ! context_data.py

from pydantic import BaseModel


class userData(BaseModel):
    name:str
    age:int
    role:str