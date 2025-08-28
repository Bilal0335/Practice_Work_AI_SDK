

# !custom_handoff_data.py
from pydantic import BaseModel

class MathReasoning(BaseModel):
    reasoning:str
    question:str