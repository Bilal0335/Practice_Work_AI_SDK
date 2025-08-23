
# ! output_data.py
from pydantic import BaseModel,Field

class OutPutData(BaseModel):
    n1: int
    n2: int
    result: str

